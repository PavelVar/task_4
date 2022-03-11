"""
Module contains tests for Linux host
"""
import .asserts.asserts_aws_linux_host


def test_port_status(test_data: dict, aws_linux_host):
    check_ports_status(test_data['ports'], aws_linux_host)


def test_package_status(test_data: dict, aws_linux_host):
    check_package_status(test_data['packages'], aws_linux_host)


def test_docker_status(aws_linux_host):
    check_docker_running(aws_linux_host)


def test_root_volume_size(test_data: dict, aws_linux_host):
    check_root_volume_size(test_data['root_volume_size'], aws_linux_host)
