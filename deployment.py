#!/usr/bin/env python
#
#
import zopkio.adhoc_deployer as adhoc_deployer
import zopkio.runtime as runtime

pyhk_deployer = None
tcp_server = None
tcp_client = None


def setup_suite():
    print "==> Starting tests for PYHK."

    runtime.set_user('root', '')

    global pyhk_deployer
    global tcp_server

    #  Set the server deployer.
    tcp_server = adhoc_deployer.SSHDeployer(
        "server",
        {'executable': runtime.get_active_config('pyhk_exec'),
         'extract': True,
         'start_command': runtime.get_active_config('tcp_server_cmd'),
         'stop_command': "ps ax | grep '[p]ython server' | awk '{print $1}' | xargs kill -9"})
    runtime.set_deployer("server", tcp_server)

    #  Provisioning the server.
    tcp_server.install("server1",
        {"hostname": "10.0.1.23",
         "install_path": runtime.get_active_config('pyhk_install')})

    #  Set the client deployer
    tcp_client = adhoc_deployer.SSHDeployer(
        "client",
        {'executable': runtime.get_active_config('pyhk_exec'),
         'extract': True,
         'start_command': runtime.get_active_config('tcp_client_cmd')})
    runtime.set_deployer("client", tcp_client)

    #  Provisioning the client.
    tcp_client.install("client1",
        {"hostname": "10.0.1.24",
         "install_path": runtime.get_active_config('pyhk_install')})

    #  Set general deployer.
    pyhk_deployer = adhoc_deployer.SSHDeployer(
        "pyhk",
        {'executable': runtime.get_active_config('pyhk_exec'),
         'extract': True,
         'start_command': runtime.get_active_config('pyhk_cmd')})
    runtime.set_deployer("pyhk", pyhk_deployer)

    #  Hostname 1
    pyhk_deployer.install(
        "machine1",
        {"hostname": runtime.get_active_config('pyhk_hostname1'),
         "install_path": runtime.get_active_config('pyhk_install')})

    #  Hostname 2
    pyhk_deployer.install(
        "machine2",
        {"hostname": runtime.get_active_config('pyhk_hostname2'),
         "install_path": runtime.get_active_config('pyhk_install')})

def setup():
    for process in tcp_server.get_processes():
        tcp_server.start(process.unique_id)

def teardown_suite():
    for process in tcp_server.get_processes():
        tcp_server.undeploy(process.unique_id)
