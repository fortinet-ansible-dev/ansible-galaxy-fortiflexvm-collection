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
short_description: Get list of FlexVM Configurations.
description:
    - This module retrieves a list of configs from FortiFlexVM API using the provided credentials and program serial number.
version_added: "1.0.0"
author:
    - Xinwei Du (@DrMofu)
options:
    username:
        description:
            - The username to authenticate. If not declared, the code will read the environment variable FLEXVM_ACCESS_USERNAME.
        type: str
        required: false
    password:
        description:
            - The password to authenticate. If not declared, the code will read the environment variable FLEXVM_ACCESS_PASSWORD.
        type: str
        required: false
    programSerialNumber:
        description:
            - The serial number of the program to get configs for.
        type: str
        required: true
'''

EXAMPLES = '''
- name: Get list of Flex VM Configurations for a Program
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name:  Get configs list
      fortinet.fortiflexvm.fortiflexvm_configs_list_info:
        username: "{{ username }}"
        password: "{{ password }}"
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
            returned: changed
            contains:
                cpu:
                    description:
                        - The number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16",  "32" or "2147483647" (unlimited).
                    type: str
                    returned: always
                service:
                    description:
                        - he value of this attribute is one of "FC" (FortiCare), "UTM", "ENT" (Enterprise) or "ATP".
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
            returned: changed
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
            returned: changed
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
            returned: changed
            contains:
                cpu:
                    description:
                        - The number of CPUs. A number between 1 and 96 (inclusive).
                    type: int
                    returned: always
                fortiGuardServices:
                    description:
                        - The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list.
                        - It should contain zero, one or more elements of ["IPS", "AVDB", "FURL", "IOTH", "FGSA", "ISSS"].
                    type: list
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
                        - It should contain zero, one or more elements of ["FAMS", "SWNM", "FMGC", "AFAC"].
                    type: list
                    returned: always
        fortiAnalyzer:
            description:
                - FortiAnalyzer Virtual Machine.
            type: dict
            returned: changed
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
            returned: changed
            contains:
                device:
                    description:
                        - Number of managed devices. A number between 0 and 100000 (inclusive).
                    type: str
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
    data = {"programSerialNumber": module.params['programSerialNumber']}
    response = connection.send_request("configs/list", data, method="POST")

    # Trasform the format of output data
    for i in range(len(response["configs"])):
        response["configs"][i] = utils.transform_config_output(
            response["configs"][i])

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == '__main__':
    main()
