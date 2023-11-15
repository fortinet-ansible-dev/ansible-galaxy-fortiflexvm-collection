#!/usr/bin/python

# Copyright: (c) 2023 Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = '''
---
module: fortiflexvm_configs_list_info
short_description: Get list of FortiFlex Configurations.
description:
    - This module retrieves a list of configs from FortiFlexVM API using the provided credentials and program serial number.
version_added: "1.0.0"
author:
    - Xinwei Du (@DrMofu)
options:
    username:
        description:
            - The username to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_USERNAME.
        type: str
        required: false
    password:
        description:
            - The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.
        type: str
        required: false
    accountId:
        description: Account ID.
        type: int
        required: false
    programSerialNumber:
        description:
            - The serial number of the program to get configs for.
        type: str
        required: true
'''

EXAMPLES = '''
- name: Get list of FortiFlex Configurations for a Program
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Get configs list
      fortinet.fortiflexvm.fortiflexvm_configs_list_info:
        username: "{{ username }}"
        password: "{{ password }}"
        # accountId: 12345 # optional
        programSerialNumber: "ELAVMS000000XXXX"
      register: result

    - name: Display response
      debug:
        var: result.configs
'''

RETURN = '''
configs:
    description: List of configurations for the specified program serial number.
    type: list
    returned: always
    contains:
        accountId:
            description: The ID of the account associated with the program.
            type: int
            returned: always
            sample: 12345
        id:
            description: The ID of the configuration.
            type: int
            returned: always
            sample: 21
        name:
            description: The name of the configuration.
            type: str
            returned: always
            sample: "Configuration Name"
        programSerialNumber:
            description: The program serial number the configuration belongs to.
            type: str
            returned: always
            sample: "ELAVMR0000000101"
        status:
            description: The status of the configuration.
            type: str
            returned: always
            sample: "ACTIVE"
        fortiGateBundle:
            description:
                - FortiGate Virtual Machine - Service Bundle.
            type: dict
            contains:
                cpu:
                    description:
                        - The number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16",  "32" or "2147483647" (unlimited).
                    type: str
                    returned: always
                service:
                    description:
                        - The value of this attribute is one of "FC" (FortiCare), "UTP", "ENT" (Enterprise) or "ATP".
                    type: str
                    returned: always
                vdom:
                    description:
                        - Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.
                    type: int
                    returned: always
        fortiManager:
            description:
                - FortiManager Virtual Machine.
            type: dict
            contains:
                device:
                    description:
                        - Number of managed devices. A number between 1 and 100000 (inclusive).
                    type: int
                    returned: always
                adom:
                    description:
                        - Number of ADOMs. A number between 1 and 100000 (inclusive).
                    type: int
                    returned: always
        fortiWeb:
            description:
                - FortiWeb Virtual Machine - Service Bundle.
            type: dict
            contains:
                cpu:
                    description:
                        - Number of CPUs. The value of this attribute is one of "1", "2", "4", "8" or "16".
                    type: str
                    returned: always
                service:
                    description:
                        - Service Package. Valid values are "FWBSTD" (Standard) or "FWBADV" (Advanced).
                    type: str
                    returned: always
        fortiGateLCS:
            description:
                - FortiGate Virtual Machine - A La Carte Services.
            type: dict
            contains:
                cpu:
                    description:
                        - The number of CPUs. A number between 1 and 96 (inclusive).
                    type: int
                    returned: always
                fortiGuardServices:
                    description:
                        - The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list.
                        - It should contain zero, one or more elements of ["IPS", "AVDB", "FGSA", "DLDB", "FAIS", "FURLDNS"].
                    type: list
                    elements: str
                    returned: always
                supportService:
                    description:
                        - Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).
                    type: str
                    returned: always
                vdom:
                    description:
                        - Number of VDOMs. A number between 1 and 500 (inclusive).
                    type: int
                    returned: always
                cloudServices:
                    description:
                        - The cloud services this FortiGate Virtual Machine supports. The default value is an empty list.
                        - It should contain zero, one or more elements of ["FAMS", "SWNM", "AFAC", "FAZC"].
                    type: list
                    elements: str
                    returned: always
        fortiClientEMSOP:
            description:
                - FortiClient EMS On-Prem.
            type: dict
            contains:
                ZTNA:
                    description:
                        - ZTNA/VPN (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                    returned: always
                EPP:
                    description:
                        - EPP/ATP + ZTNA/VPN (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                    returned: always
                chromebook:
                    description:
                        - Chromebook (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                    returned: always
                service:
                    description:
                        - Support Services. Possible value is "FCTFC247" (FortiCare Premium)
                    type: str
                    returned: always
                addons:
                    description: Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).
                    type: list
                    elements: str
        fortiAnalyzer:
            description:
                - FortiAnalyzer Virtual Machine.
            type: dict
            contains:
                storage:
                    description:
                        - Daily Storage (GB). A number between 5 and 8300 (inclusive).
                    type: int
                    returned: always
                adom:
                    description:
                        - Number of ADOMs. A number between 0 and 1200 (inclusive).
                    type: int
                    returned: always
                service:
                    description:
                        - Support Service. Currently, the only available option is "FAZFC247" (FortiCare Premium).
                        - The default value is "FAZFC247".
                    type: str
                    returned: always
        fortiPortal:
            description:
                - FortiPortal Virtual Machine.
            type: dict
            contains:
                device:
                    description:
                        - Number of managed devices. A number between 0 and 100000 (inclusive).
                    type: str
                    returned: always
        fortiADC:
            description:
                - FortiADC Virtual Machine.
            type: dict
            contains:
                cpu:
                    description:
                        - Number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16" or "32".
                    type: str
                    returned: always
                service:
                    description:
                        - Support Service. "FDVSTD" (Standard), "FDVADV" (Advanced) or "FDVFC247" (FortiCare Premium).
                    type: str
                    returned: always
        fortiGateHardware:
            description:
                - FortiGate Hardware.
            type: dict
            contains:
                model:
                    description:
                        - The device model. Possible values are
                        - FGT40F (FortiGate-40F), FGT60F (FortiGate-60F), FGT70F (FortiGate-70F), FGT80F (FortiGate-80F),
                        - FG100F (FortiGate-100F), FGT60E (FortiGate-60E), FGT61F (FortiGate-61F), FG100E (FortiGate-100E),
                        - FG101F (FortiGate-101F), FG200E (FortiGate-200E), FG200F (FortiGate-200F), FG201F (FortiGate-201F),
                        - FG4H0F (FortiGate-400F), FG6H0F (FortiGate-600F), FWF40F (FortiWifi-40F), FWF60F (FortiWifi-60F),
                        - FGR60F (FortiGateRugged-60F), FR70FB (FortiGateRugged-70F), FGT81F (FortiGate-81F), FG101E (FortiGate-101E),
                        - FG4H1F (FortiGate-401F), FG1K0F (FortiGate-1000F), FG180F (FortiGate-1800F), F2K60F (FortiGate-2600F),
                        - FG3K0F (FortiGate-3000F), FG3K1F (FortiGate-3001F), FG3K2F (FortiGate-3200F).
                    type: str
                    returned: always
                service:
                    description:
                        - Support Service. Possible values are FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite),
                        - FDVFC247 (ATP), FGHWUTP (UTP) or FGHWENT (Enterprise).
                    type: str
                    returned: always
                addons:
                    description:
                        - Addons. A list, possible values are
                        - FGHWFCELU (FortiCare Elite Upgrade), FGHWFAMS (FortiGate Cloud Management),
                        - FGHWFAIS (AI-Based In-line Sandbox), FGHWSWNM (SD-WAN Underlay), FGHWDLDB (FortiGuard DLP),
                        - FGHWFAZC (FortiAnalyzer Cloud), FGHWSOCA (SOCaaS), FGHWMGAS (Managed FortiGate),
                        - FGHWSPAL (SD-WAN Connector for FortiSASE), FGHWFCSS (FortiConverter Service).
                    type: list
                    elements: str
                    returned: always
        fortiCloudPrivate:
            description:
                - FortiWeb Cloud, Private.
            type: dict
            contains:
                throughput:
                    description:
                        - Average Throughput (Mbps).
                        - Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600,
                        - 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
                        - 7000, 7500, 8000, 8500, 9000, 9500, 10000.
                    type: int
                    returned: always
                applications:
                    description: Number of web applications. Number between 0 and 2000 (inclusive).
                    type: int
                    returned: always
        fortiCloudPublic:
            description:
                - FortiWeb Cloud, Public.
            type: dict
            contains:
                throughput:
                    description:
                        - Average Throughput (Mbps).
                        - Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600,
                        - 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
                        - 7000, 7500, 8000, 8500, 9000, 9500, 10000.
                    type: int
                    returned: always
                applications:
                    description: Number of web applications. Number between 0 and 2000 (inclusive).
                    type: int
                    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils import utils
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def main():
    # Define module arguments
    module_args = dict(
        username=dict(type="str", required=False),
        password=dict(type="str", required=False, no_log=True),
        accountId=dict(type='int', required=False),
        programSerialNumber=dict(type="str", required=True),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request to get config list
    data = {"programSerialNumber": module.params["programSerialNumber"]}
    if module.params["accountId"]:
        data["accountId"] = module.params["accountId"]
    response = connection.send_request("fortiflex/v2/configs/list", data, method="POST")

    # Trasform the format of output data
    for i in range(len(response["configs"])):
        response["configs"][i] = utils.transform_config_output(response["configs"][i])

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == '__main__':
    main()
