import os
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger()


def command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", "-n", help="How many times script will be executed", required=True,
                        type=int, dest="variable_name", default=2)
    parser.add_argument("--command", "-c", help="Command to execute in bash/terminal", default="ls")
    return parser.parse_args()


def main(**kwargs):
    if kwargs:
        # Use os.system to use terminal - One way communication:
        os.system(f"echo Call {kwargs['command']} {kwargs['variable_name']} times.")
        for _ in range(kwargs["variable_name"]):
            os.system(kwargs["command"])

        # Bidirectional communication
        # Use subprocess to use terminal and fetch back resulted prints
        import subprocess
        cmd = [kwargs["command"]]  # Run command in terminal
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]  # Get results of command
        logger.info(output.decode('UTF-8'))


if __name__ == "__main__":
    args = command_line_arguments()
    # print(args)
    # print(vars(args))
    main(**vars(args))
