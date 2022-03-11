"""
Module contains fixtures for test of AWS Linux Host.
"""
import pytest

from modules.aws_linux_host import AWSLinuxHost


@pytest.fixture()
def aws_linux_host(test_data: dict) -> AWSLinuxHost:
    """Creates AWS Linux Host instance.
    @param test_data: dict contains parameters from test_data.yaml file.
    @return: AWSLinuxHost
    """
    return AWSLinuxHost(test_data['user_name'], test_data['host'], test_data['ssh_config_file_path'],
                        test_data['backend_type'])
