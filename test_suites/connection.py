import os

import zopkio.runtime as runtime
import zopkio.test_utils as testutilities

#  Set the sequency of the test.
test_phase = 1

def test_connection():
    '''
    Must connect on machine4 and receive a string.
    '''
    print "==> Test Connection machine3 and machine4"
    client = runtime.get_deployer("client")
    client.start("client1", configs={"sync": True})


def validate_files_on_etc_host1():
    '''
    Must connect on machine4 and receive a string.
    '''
    client_log_file = os.path.join(perf.LOGS_DIRECTORY, "client-run.log")
    client_logs = testutilities.get_log_for_test("test_connection", client_log_file, "12:00:00")

    assert client_logs == 'Hello, and goodbye.', "Connection problem"
