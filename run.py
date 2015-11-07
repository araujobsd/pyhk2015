import os

test = {
    "deployment_code": os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), "deployment.py"),
    "test_code": [
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), "test_suites/machine1_etc.py"),
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), "test_suites/machine1_ping.py"),
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), "test_suites/connection.py"),
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), "test_suites/machine2_ping.py"),
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), "test_suites/machine2_etc.py")],
    "perf_code": os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "perf.py"),
    "configs_directory": os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "configs/")
    }
