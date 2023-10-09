#Test
import sys
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result


my_config = sys.argv[1]
nr = InitNornir(config_file=my_config)


def test_connect(task):
    task.run(task=netmiko_send_command, command_string="show ip interfaces brief")


result = nr.run(task=test_connect)
print_result(result)
