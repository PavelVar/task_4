"""
Module with sets of asserts for LinuxHost tests
"""
import logging
from pytest_check import check_func
from .models.aws_linux_host import AWSLinuxHost


@check_func
def soft_check_existence(host: AWSLinuxHost, test_data: dict) -> bool:
    """Check LinuxHost for existence.
    @param host: AWSLinuxHost
    @param test_data: dict expected data
    """
    assert host, f"Host: {test_data['hostname']} does not exist"
    return bool(host)


@check_func
def soft_check_port_is_listening(host: AWSLinuxHost, port: list):
    """Soft check for opened port.
    @param host: AWSLinuxHost
    @param port: list
    """
    assert host.get_listening_port_status(port[0]), logging.error(f'Port {port} for service {port[1]} not '
                                                                  f'available')


def check_ports_status(ports: list, host: AWSLinuxHost):
    """Checks that open and listening ports.
    @param ports: list
    @param host: AWSLinuxHost
    """
    if soft_check_existence(host):
        for port in ports:
            soft_check_port_is_listening(host, port)


def check_package_status(test_data: dict, host: AWSLinuxHost):
    """Asserts for check installed docker package
    :param test_data: dict expected data
    :param host: AWSLinuxHost
    """
    if soft_check_existence(host):
        error_msg = f"{test_data['docker_package']} package don't installed"
        assert host.get_is_package_installed(test_data['docker_package']), error_msg


def check_docker_running(test_data: dict, host: AWSLinuxHost):
    """Checks if docker running.
    @param test_data: dict expected data
    @param host: AWSLinuxHost
    """
    if soft_check_existence(host):
        error_msg = f"{test_data['docker_image_id']} is not running."
        assert test_data['docker_image_id'] in host.get_runnings_docker_container(), error_msg


def check_root_volume_size(test_data: dict, host: AWSLinuxHost):
    """Checks root volume size of EC2 Instance.
    @param test_data: dict expected data
    @param host: AWSLinuxHost
    """
    if soft_check_existence(host):
        error_msg = f"Root volume size not equal {test_data['root_volume_size']}"
        assert host.get_root_volume_size() == test_data['root_volume_size'], error_msg
