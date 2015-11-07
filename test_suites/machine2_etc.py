import os

import zopkio.runtime as runtime
import zopkio.test_utils as testutilities

#  Set the sequency of the test.
test_phase = 4

def test_files_on_etc_host2():
    print "==> Check how many files on /etc/ (machine2)"
    pyhk_deployer = runtime.get_deployer("pyhk")
    pyhk_deployer.start("machine2", configs={
        "start_command": runtime.get_active_config('pyhk_cmd'),
        "sync": True})


def validate_files_on_etc_host2():
    '''
    Must return the number of files >= 112.
    '''

    hostname2_log_file = os.path.join(perf.LOGS_DIRECTORY, "machine2-run.log")
    hostname2_logs = testutilities.get_log_for_test("test_files_on_etc_host2", hostname2_log_file, "12:00:00")

    assert hostname2_logs >= 112, "More files %s than 112 in hostname2" % (hostname2_logs)

