"""Main module for ansible-deploy"""

import sys
import os
import argparse
import logging
import datetime
import subprocess
import pwd
import grp
import errno
from logging import handlers as log_han
import yaml
from cerberus import Validator


APP_CONF = "/etc/ansible-deploy/ansible-deploy.yaml"


def verify_subcommand(command: str):
    """Function to check the first arguments for a valid subcommand"""
    if command not in ("run", "list", "lock", "unlock"):
        print("Unknown subcommand :%s", (command), file=sys.stderr)
        sys.exit("55")

def set_logging(log_dir: str, timestamp: str, options: dict):
    """Function to create logging objects"""
    logger = logging.getLogger("ansible-deployer_log")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
    console_formatter = logging.Formatter("\n%(asctime)s [%(levelname)s]: %(message)s\n")

    if options["syslog"]:
        rsys_handler = log_han.SysLogHandler(address="/dev/log")
        rsys_handler.setFormatter(formatter)
        rsys_handler.setLevel(logging.WARNING)
        logger.addHandler(rsys_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.DEBUG if options["debug"] else logging.INFO)
    logger.addHandler(console_handler)

    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir,
                                conf["file_naming"]["log_file_name_frmt"].format(timestamp))
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
    return logger

def parse_options(argv):
    """Generic function to parse options for all commands, we validate if the option was allowed for
    specific subcommand outside"""
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument("subcommand", nargs=1, default=[None], metavar="SUBCOMMAND",
                        help='Specify command to run. Available commands: run, list, lock, unlock.')
    parser.add_argument("--infrastructure", "-i", nargs=1, default=[None], metavar="INFRASTRUCTURE",
                        help='Specify infrastructure for deploy.')
    parser.add_argument("--stage", "-s", nargs=1, default=[None], metavar="STAGE",
                        help='Specify stage type. Available types are: "testing" and "prod".')
    parser.add_argument("--commit", "-c", nargs=1, default=[None], metavar="COMMIT",
                        help='Provide commit ID.')
    parser.add_argument("--task", "-t", nargs=1, default=[None], metavar='TASK_NAME',
                        help='Provide task_name.')
    parser.add_argument("--dry", "-C", default=False, action='store_true', help='Perform dry run.')
    parser.add_argument("--debug", "-d", default=False, action="store_true",
                        help='Print debug output.')
    parser.add_argument("--syslog", "-v", default=False, action="store_true", help='Log warnings '
                        'and errors to syslog. --debug doesn\'t affect this option!')
    parser.add_argument("--limit", "-l", nargs=1, default=[None], metavar="[LIMIT]",
                        help='Limit task execution to specified host.')

    arguments = parser.parse_args(argv)

    options = {}
    options["subcommand"] = arguments.subcommand[0]
    verify_subcommand(options["subcommand"])

    options["infra"] = arguments.infrastructure[0]
    options["stage"] = arguments.stage[0]
    options["commit"] = arguments.commit[0]
    options["task"] = arguments.task[0]
    options["dry"] = arguments.dry
    options["debug"] = arguments.debug
    options["syslog"] = arguments.syslog
    options["limit"] = arguments.limit[0]

    return options

def create_workdir(timestamp: str):
    """
    Function to create working directory on file system, we expect it to change
    the cwd to newly created workdir at the end.
    """
    short_ts = timestamp.split("_")[0]
    date_dir = os.path.join(conf["global_paths"]["work_dir"], short_ts)

    #
    #TODO: Add locking of the directory

    if short_ts not in os.listdir(conf["global_paths"]["work_dir"]):
        seq_path = os.path.join(date_dir, f"{conf['file_naming']['sequence_prefix']}0000")
    else:
        sequence_list = os.listdir(date_dir)
        sequence_list.sort()
        new_sequence = int(sequence_list[-1].split(conf['file_naming']['sequence_prefix'])[1]) + 1
        seq_path = os.path.join(date_dir, f"{conf['file_naming']['sequence_prefix']}"
                                          f"{new_sequence:04d}")

    try:
        os.makedirs(seq_path)
        os.chdir(seq_path)
    except Exception as e:
        print("Failed to create work dir:%s error was:%s", seq_path, e, file=sys.stderr)
        sys.exit(90)
    print("Successfully created workdir: %s", seq_path)
    return seq_path

def validate_options(options: dict):
    """Function checking if the options set are allowed in this subcommand"""
    logger.debug("validate_options running for subcommand: %s", options["subcommand"])
    required = []
    notsupported = []

    if options["subcommand"] == "run":
        required = ["task", "infra", "stage"]
    elif options["subcommand"] in ("lock", "unlock"):
        required = ["infra", "stage"]
        notsupported = ["task", "commit", "limit"]
    elif options["subcommand"] == "list":
        notsupported = ["commit", "limit"]

    failed = False
    for req in required:
        if options[req] is None:
            logger.error("%s is required for %s", req, options["subcommand"])
            failed = True

    for notsup in notsupported:
        if options[notsup] is not None:
            logger.error("%s is not supported by %s", notsup, options["subcommand"])
            failed = True

    if failed:
        logger.error("Failed to validate options")
        sys.exit(55)

def load_configuration_file(config_file: str):
    """Function responsible for single file loading and validation"""
    #TODO: Add verification of owner/group/persmissions
    logger.debug("Loading :%s", config_file)

    with open(os.path.join(conf["global_paths"]["config_dir"], config_file), "r", encoding="utf8") \
            as config_stream:
        try:
            config = yaml.safe_load(config_stream)
        except yaml.YAMLError as e:
            logger.error(e)
            sys.exit(51)

    with open(os.path.join(conf["global_paths"]["config_dir"], "schema", config_file), "r",
              encoding="utf8") as schema_stream:
        try:
            schema = yaml.safe_load(schema_stream)
        except yaml.YAMLError as e:
            logger.error(e)
            sys.exit(52)

    validator = Validator(schema)
    if not validator.validate(config, schema):
        logger.error(validator.errors)
        sys.exit(53)

    logger.debug("Loaded:\n%s", str(config))
    return config

def load_configuration():
    """Function responsible for reading configuration files and running a schema validator against
    it
    """
    logger.debug("load_configuration called")
    #TODO: validate files/directories permissions - should be own end editable only by special user

    infra = load_configuration_file("infra.yaml")
    tasks = load_configuration_file("tasks.yaml")

    config = {}
    config["infra"] = infra["infrastructures"]
    config["tasks"] = tasks

    return config

def validate_option_by_dict_with_name(optval: str, conf: dict):
    """
    Validate if given dictionary contains element with name equal to optval
    """
    elem = None
    if optval:
        for elem in conf:
            if elem["name"] == optval:
                break
        else:
            logger.error("%s not found in configuration file.", optval)
            sys.exit(54)

    return elem

def validate_user_infra_stage():
    """Function checking if user has rights to execute command on selected infrastructure
    Required for: run, lock and unlock operations
    Exit on failure, return inventory on success
    """
    inventory = ""

    return inventory

def validate_user_task():
    """Function checking if user has rights to execute the task
    Rquired for: run"""

def validate_option_values_against_config(config: dict, options: dict):
    """
    Function responsible for checking if option values match configuration
    """
    selected_items = {}
    for option in options.keys():
        if options[option]:
            if option == "infra":
                selected_items["infra"] = validate_option_by_dict_with_name(options["infra"],
                                                                            config["infra"])
            elif option == "task":
                selected_items["task"] = validate_option_by_dict_with_name(options["task"],
                                                                           config["tasks"]["tasks"])
            elif option == "stage":
                for item in config["infra"]:
                    if item["name"] == options["infra"]:
                        index = config["infra"].index(item)
                selected_items["stage"] = validate_option_by_dict_with_name(options["stage"],\
                                                                config["infra"][index]["stages"])
            elif option == "limit":
                for item in config["tasks"]["tasks"]:
                    if item["name"] == options["task"]:
                        if item["allow_limit"]:
                            selected_items["limit"] = options["limit"]
                            break
                else:
                    logger.error("Limit %s is not available for task %s.", options["limit"],
                                 options["task"])
                    sys.exit(54)
            #TODO: validate if user is allowed to use --commit
            #TODO: validate if user is allowed to execute the task on infra/stag pair
            #(validate_user_infra_stage(), validate_usr_task())
            logger.debug("Completed validate_option_values_with_config")

    return selected_items

def lock_inventory(lockdir: str, lockpath: str):
    """
    Function responsible for locking inventory file.
    The goal is to prevent two parallel ansible-deploy's running on the same inventory
    This needs to be done by the use of additional directory under PARNT_WORKDIR,, for instance:
    PARENT_WORKDIR/locks.
    We shouldn't check if file exists, but rather attempt to open it for writing, until we're
    done every other process should be rejected this access.
    The file should match inventory file name.
    """

    logger.debug("Started lock_inventory for lockdir: %s and lockpath %s.", lockdir, lockpath)
    os.makedirs(lockdir, exist_ok=True)

    try:
        with open(lockpath, "x", encoding="utf8") as fh:
            fh.write(str(os.getpid()))
            fh.write(str("\n"))
            fh.write(str(pwd.getpwuid(os.getuid()).pw_name))
        logger.info("Infra locked.")
    except FileExistsError:
        with open(lockpath, "r", encoding="utf8") as fh:
            proc_pid, proc_user = fh.readlines()
        logger.error("Another process (PID: %s) started by user %s is using this infrastructure, "
                     "please try again later.", proc_pid.strip(), proc_user.strip())
        logger.error("Program will exit now.")
        sys.exit(61)
    except Exception as exc:
        logger.error(exc)
        logger.error("Program will exit now.")
        sys.exit(62)

def unlock_inventory(lockpath: str):
    """
    Function responsible for unlocking inventory file, See also lock_inventory
    """

    logger.debug("Started unlock_inventory for lockpath %s.", lockpath)

    try:
        os.remove(lockpath)
        logger.info("Lock %s has been removed.", lockpath)
    except FileNotFoundError:
        logger.error("Requested lock %s was not found. Nothing to do.", lockpath)
        logger.error("Program will exit now.")
        sys.exit(63)
    except Exception as exc:
        logger.error(exc)
        logger.error("Program will exit now.")
        sys.exit(64)

def setup_ansible(setup_hooks: list, commit: str, workdir: str):
    """
    Function responsible for execution of setup_hooks
    It passes the "commit" to the hook if one given, if not the hook should
    checkout the default repo.
    """
    failed = False

    if not commit:
        commit = ""
    for hook in setup_hooks:
        if hook["module"] == "script":
            try:
                hook_env = os.environ.copy()
                hook_env["ANSIBLE_DEPLOY_WORKDIR"] = workdir
                with subprocess.Popen([hook["opts"]["file"], commit],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      stdin=subprocess.PIPE,
                                      env=hook_env) as proc:
                    hook_out = proc.communicate()
                    if proc.returncode != 0:
                        failed = True
            except Exception as e:
                logger.error("Failed executing %s: %s", hook["opts"]["file"], e)
                sys.exit(41)
            else:
                if hook_out != ("", ""):
                    logger.info("setup_hook(%s),\nstdout:\n%s\nstdrr:\n%s", hook["name"],
                                hook_out[0].decode(), hook_out[1].decode())
                    logger.info(hook_out)
                if proc.returncode:
                    logger.error("Setup hook %s failed, cannot continue", hook["name"])
                    sys.exit(40)
                else:
                    logger.info("Setup completed in %s", os.getcwd())

        else:
            logger.error("Not supported")
        if failed:
            sys.exit(69)

def get_playbooks(config: dict, options: dict):
    """
    Function obtaining play items for specified task.
    :param config:
    :param task_name:
    :return:
    """
    playbooks = []

    for item in config["tasks"]["tasks"]:
        if item["name"] == options["task"]:
            play_names = item["play_items"]

    for play in play_names:
        for item in config["tasks"]["play_items"]:
            if item["name"] == play:
                if item["skip"]:
                    for elem in item["skip"]:
                        if elem["infra"] == options["infra"] and elem["stage"] == options["stage"]:
                            logger.info("Skipping playbook %s on %s and %s stage.", play,
                                        options["infra"], options["stage"])
                            break
                    else:
                        playbooks.append(item["file"])
                else:
                    playbooks.append(item["file"])

    # TODO add check if everything was skipped
    return playbooks

def run_task(config: dict, options: dict, inventory: str):
    """
    Function implementing actual execution of ansible-playbook
    """
    playbooks = get_playbooks(config, options)
    tags = get_tags_for_task(config, options)
    if len(playbooks) < 1:
        logger.error("No playbooks found for requested task %s. Nothing to do.", options['task'])
        logger.error("Program will exit now.")
        sys.exit(70)
    else:
        for playbook in playbooks:
            command = ["ansible-playbook", "-i", inventory, playbook]
            if options["limit"]:
                command.append("-l")
                command.append(options["limit"])
            if tags:
                tag_string = ",".join(tags)
                command.append("-t")
                command.append(tag_string)
            logger.debug("Running '%s'.", command)
            try:
                with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as \
                        proc:
                    std_o, std_e = proc.communicate()
                    for line in std_o.split(b"\n\n"):
                        logger.info(line.decode("utf-8"))
                if proc.returncode == 0:
                    logger.info("'%s' ran succesfully", command)
                else:
                    logger.error("'%s' failed due to:", command)
                    for line in std_e.split(b"\n\n"):
                        logger.error(line.decode("utf-8"))
                    logger.error("Program will exit now.")
                    sys.exit(71)
            except Exception as exc:
                logger.error("'%s' failed due to:")
                logger.error(exc)
                logger.error("Program will exit now.")
                sys.exit(72)

def verify_task_permissions(selected_items, user_groups):
    """
    Function verifies if the running user is allowed to run the task
    """
    s_task = selected_items["task"]
    s_infra = selected_items["infra"]
    o_stage = selected_items["stage"]
    logger.debug("Running verify_task_permissions, for s_task:%s, s_infra:%s, o_stage:%s and user"
                 "groups: %s", s_task, s_infra, o_stage, user_groups)

    for allow_group in s_task["allowed_for"]:
        logger.debug("\tChecking group: %s, for user_groups:%s", allow_group, user_groups)
        if allow_group["group"] in user_groups:
            for infra in allow_group["infra"]:
                logger.debug("\t\tChecking infra: %s for infra:%s", infra,
                             selected_items["infra"]["name"])
                if infra["name"] == selected_items["infra"]["name"]:
                    for stage in infra["stages"]:
                        logger.debug("\t\t\tChecking stage:%s for stage:%s", stage, o_stage["name"])
                        if stage == o_stage["name"]:
                            logger.debug("Task allowed, based on %s", allow_group)
                            return True
    logger.debug("Task forbidden")
    return False

def list_tasks(config: dict, options: dict):
    """
    Function listing tasks available to the user limited to given infra/stage/task
    """
    task_list = []
    for item in config["tasks"]["tasks"]:
        task_list.append(item["name"])

    logger.info("  ".join(task_list))

# TODO: At least infra level should be returned from validate options since we do similar check
# (existence) there.
def get_inventory_file(config: dict, options: dict):
    """
    Function returning relativ path to inventory file.
    :param config:
    :param options:
    :return:
    """

    inv_file = None

    for item in config["infra"]:
        if item["name"] == options["infra"]:
            for elem in item["stages"]:
                if elem["name"] == options["stage"]:
                    inv_file = os.path.basename(elem["inventory"])

    return inv_file

def get_all_user_groups():
    """
    Function returning all user groups in form of their names
    """
    user_groups = [grp.getgrgid(g).gr_name for g in os.getgroups()]
    logger.debug("User groups:%s %s", user_groups, grp.getgrgid(os.getgid()).gr_name)
    user_groups.append(str(grp.getgrgid(os.getgid()).gr_name))


    return user_groups

def load_global_configuration():
    """Function responsible for single file loading and validation"""
    with open(APP_CONF, "r", encoding="utf8") as config_stream:
        try:
            config = yaml.safe_load(config_stream)
            return config
        except yaml.YAMLError as e:
            print(e, file=sys.stderr)
            sys.exit(51)

def get_tags_for_task(config: dict, options: dict):
    """Function to get task's tags"""
    tags = []
    for task in config["tasks"]["tasks"]:
        if task["name"] == options["task"]:
            tags = task["tags"]

    return tags

def main():
    """ansible-deploy endpoint function"""
    global logger, conf

    start_ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    if len(sys.argv) < 2:
        print("Too few arguments", file=sys.stderr)
        sys.exit(2)
    options = parse_options(sys.argv[1:])

    conf = load_global_configuration()
    if options["subcommand"] == "run":
        workdir = create_workdir(start_ts)
    else:
        workdir = None

    logger = set_logging(workdir, start_ts, options)

    validate_options(options)
    config = load_configuration()
    selected_items = validate_option_values_against_config(config, options)

    user_groups = get_all_user_groups()

    if options["dry"]:
        logger.info("Skipping execution because of --dry-run option")
        sys.exit(0)

    if options["subcommand"] == "list":
        list_tasks(config, options)
    else:
        lockdir = os.path.join(conf["global_paths"]["work_dir"], "locks")
        inv_file = get_inventory_file(config, options)
        lockpath = os.path.join(lockdir, inv_file.replace(os.sep, "_"))
        if options["subcommand"] == "run":
            if not verify_task_permissions(selected_items, user_groups):
                logger.error("Task forbidden")
                sys.exit(errno.EPERM)
            setup_ansible(config["tasks"]["setup_hooks"], options["commit"], workdir)
            lock_inventory(lockdir, lockpath)
            run_task(config, options, inv_file)
            unlock_inventory(lockpath)
        elif options["subcommand"] == "lock":
            lock_inventory(lockdir, lockpath)
        elif options["subcommand"] == "unlock":
            unlock_inventory(lockpath)

    sys.exit(0)
