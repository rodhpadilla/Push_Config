#!/usr/bin/env python3

__author__ = "Rodrigo H Padilla"
__email__ = "od.hpadilla@gmail.com"


from netmiko import ConnectHandler
from rich.console import Console
from rich.table import Table
from devices import device_list

RESULTS = []

def push_config(device, config_to_push):
    outputs_dict = {}
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_set(config_to_push)
        # output += net_connect.save_config()       # SAVE CONFIG
        outputs_dict["device"] = device["host"]
        outputs_dict["output"] = output
        RESULTS.append(outputs_dict)
    return f"SUCCESS --> {device['host']}"


def main():
    print()
    config_to_push = [
        "interface loopback33",
        "description My name is: PARANGARICUTIRIMICUARO",
        "ip address 10.0.33.1 255.255.255.255"
    ]
    for device in device_list:
        result_connect = push_config(device, config_to_push)
        if "SUCCESS" in result_connect:
            print(result_connect)
        else:
            print(f"FAILED --> {device['host']}")
    print("\n")
    

    if len(RESULTS) > 0:
        for item in RESULTS:
            table = Table()
            table.add_column(item["device"], justify="left", style="green")
            table.add_row(item["output"])
            console = Console()
            console.print(table)
            print()

if __name__ == '__main__':
    main()