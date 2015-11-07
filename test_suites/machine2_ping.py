import os

import zopkio.runtime as runtime
import zopkio.test_utils as testutilities

#  Set the sequency of the test.
test_phase = 5


def test_ping_host2():
    print "==> ping example.com (machine2)"
    pyhk_deployer = runtime.get_deployer("pyhk")

    pyhk_deployer.start(
        "machine2",
        configs={
            "start_command": runtime.get_active_config('ping_cmd'),
            "sync": True
            })


def validate_ping_host2():
    '''
    Send 10 icmp to example.com.
    '''

    hostname2_log_file = os.path.join(perf.LOGS_DIRECTORY, "machine2-ping-output.csv")
    hostname2_logs = testutilities.get_log_for_test(
        "test_ping_host2", hostname2_log_file, "12:00:00")

    #  Number of icmp packages
    size_p = len(hostname2_logs.split(',')) / 2

    assert size_p == 10, "Less than 10 packages received on host2"
