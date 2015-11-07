import os

import zopkio.runtime as runtime
import zopkio.test_utils as testutilities

#  Set the sequency of the test.
test_phase = 2

def test_files_on_etc_host1():
    print "==> Check how many files on /etc/ (machine1)"
    pyhk_deployer = runtime.get_deployer("pyhk")
    pyhk_deployer.start("machine1", configs={
        "start_command": runtime.get_active_config('pyhk_cmd'),
        "sync": True})



def validate_files_on_etc_host1():
    '''
    Must return the number of files <= 112.
    '''
    hostname1_log_file = os.path.join(perf.LOGS_DIRECTORY, "machine1-run.log")
    hostname1_logs = testutilities.get_log_for_test("test_files_on_etc_host1", hostname1_log_file, "12:00:00")

    assert hostname1_logs <= 112, "More files %s than 112 in hostname1" % (hostname1_logs)

