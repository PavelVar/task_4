"""
Mmodule contains fixture to get data from yaml file to use in tests.
"""
import pytest
import yaml

file_name = '../tests/aws_linux_host_test_data.yaml'
file_path = 'F:\\environments\\task4\\onboarding-qa\\testinfra\\tests'


@pytest.fixture()
def test_data() -> dict:
    """Gets test data from yaml file."""
    with open(f'{file_path}\\{file_name}') as yaml_file:
        test_data = yaml.safe_load(yaml_file)
    return test_data
