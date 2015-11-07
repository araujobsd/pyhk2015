import os

import zopkio.runtime as runtime
import zopkio.test_utils as testutilities

#  Set the sequency of the test.
test_phase = 3


def test_ping_host1():
    print "==> ping example.com (machine1)"
    pyhk_deployer = runtime.get_deployer("pyhk")

    pyhk_deployer.start(
        "machine1",
        configs={
            "start_command": runtime.get_active_config('ping_cmd'),
            "sync": True
            })


def validate_ping_host1():
    '''
    Send 10 icmp to example.com.
    '''
    hostname1_log_file = os.path.join(
        perf.LOGS_DIRECTORY, "machine1-ping-output.csv")
    hostname1_logs = testutilities.get_log_for_test(
        "test_ping_host1", hostname1_log_file, "12:00:00")

    #  Number of icmp packages
    size_p = len(hostname1_logs.split(',')) / 2

    assert size_p == 10, "Less than 10 icmp replyes received on host1"
