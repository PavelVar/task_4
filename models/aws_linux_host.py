"""
Module aws_linux_host contains Class AWSLinuxHost which creates AWS Linux host object and provides attributes of this
host.
"""
import testinfra
import logging


class AWSLinuxHost:
    """Class AWSLinuxHost creates AWS Linux host object and provides attributes of this host."""

    def __init__(self, user_name: str, host: str, ssh_config_path: str, backend_type: str = 'ssh'):
        """Takes necessary parameters and initialize connection AWS Linux Host.
        @param user_name: str username on Linux host
        @param host: str host name from ssh_config or host IP address
        @param ssh_config_path: str path to ssh config file
        @param backend_type: str connection type, tcp on default
        """
        self._host = testinfra.get_host(f'{backend_type}://{user_name}@{host}', sudo=True, ssh_config=ssh_config_path)

    def get_list_of_listening_ports(self) -> list:
        """Returns list of open ports on host."""
        return self._host.socket.get_listening_sockets()

    def get_listening_ports_status(self, port_num: int) -> bool:
        """Verifies and returns given port status.
        @param port_num:  int
        @return: bool port status
        """
        return self._host.socket(f'tcp://{port_num}').is_listening

    def get_package_installation_status(self, package_name: str) -> bool:
        """Checks if package is installed on a host.
        @param package_name: str package name
        @return: boolean package installation status
        """
        return self._host.package(package_name).is_installed

    def get_service_running_status(self, service_name: str) -> bool:
        """Checks if service is running on host.
        @param service_name: str name of service
        @return: boolean service status
        """
        return self._host.service(service_name).is_running

    def get_docker_container_status(self) -> list:
        """Returns running containers."""
        containers = []
        info = self._host.run('sudo docker ps')
        if info.exit_status == 0:
            list_of_containers = info.stdout.split()
            return list_of_containers
        else:
            if info.stderr:
                logging.error(info.stderr)
            else:
                logging.error("Can't get list of running containers")
            return containers

    def get_root_volume_size(self) -> str:
        """Returns root volume size."""
        mount_point = self._host.mount_point("/").device
        info = self._host.run(f'lsblk {mount_point}')
        if info.exit_status == 0:
            list_of_point = info.stdout.split()
            return list_of_point[-4]
        else:
            if info.stderr:
                logging.error(info.stderr)
            else:
                logging.error("Can't get volume size")
            return None

host = '3.68.105.182'
user_name ='ec2-user'
ssh_config_path = '/home/pavel/PycharmProjects/testinfra/ssh_config'
# a = AWSLinuxHost(user_name, host, ssh_config_path)
a = testinfra.get_host("ssh://ec2-user@3.68.105.182", ssh_config="/home/pavel/PycharmProjects/testinfra/ssh_config")
print(a)
print(dir(a))
print(a.__getattribute__)
print(a.backend)
print(a.socket.get_listening_sockets())

# print(a.get_list_of_listening_ports())
# print(a.get_listening_ports_status(22))
# print(a.get_package_installation_status('docker'))
# print(a.get_service_running_status('docker'))
# print(a.get_docker_container_status())
# print(a.get_root_volume_size())
