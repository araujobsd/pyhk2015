import os

#  Set where the logs will be stored after tests.
LOGS_DIRECTORY = "/tmp/pyhk/collected_logs/"
OUTPUT_DIRECTORY = "/tmp/pyhk/results/"


#  Path to collect the logs in the target machine.
def machine_logs():
    return {
        "client1": [os.path.join("/tmp/pyhk/", "connection.log")],
        "machine1": [os.path.join("/tmp/pyhk/", "run.log")],
        "machine2": [os.path.join("/tmp/pyhk/", "run.log")],
    }


#  Path to collect the csv logs for naarad in the target machine.
def naarad_logs():
    return {
        "machine1": [os.path.join("/tmp/pyhk/", "run.csv")],
        "machine2": [os.path.join("/tmp/pyhk/", "run.csv")],
        "machine1": [os.path.join("/tmp/pyhk/", "ping-output.csv")],
        "machine2": [os.path.join("/tmp/pyhk/", "ping-output.csv")],
    }


#  Path to naarad configuration.
def naarad_config():
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "naarad.cfg")
