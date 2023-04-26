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
module: fortiflexvm_vms_list_info
short_description: Get list of existing VMs for FlexVM Configuration.
description:
    - This module retrieves a list of VMs associated with a specific config ID from FortiFlexVM API using the provided credentials.
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
    configId:
        description:
            - The ID of the configuration for which to retrieve the list of VMs.
        type: int
        required: true
'''

EXAMPLES = '''
- name: Get list of VMs for a specific config ID
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Get VMs list
      fortinet.fortiflexvm.fortiflexvm_vms_list_info:
        username: "{{ username }}"
        password: "{{ password }}"
        configId: 22
      register: result

    - name: Display response
      debug:
        var: result.vms
'''

RETURN = '''
vms:
    description: List of VMs associated with the specified config ID.
    type: list
    returned: always
    contains:
        serialNumber:
            description: The serial number of the VM.
            type: str
            returned: always
            sample: "FGVMELTM20000004"
        description:
            description: The description of the VM.
            type: str
            returned: always
            sample: "VM created for department X"
        configId:
            description: The config ID of the VM.
            type: int
            returned: always
            sample: 22
        startDate:
            description: The start date of the VM.
            type: str
            returned: always
            sample: "2020-08-25 10:12:25"
        endDate:
            description: The end date of the VM.
            type: str
            returned: always
            sample: "2020-09-12 12:13:37"
        status:
            description: The status of the VM. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".
            type: str
            returned: always
            sample: "STOPPED"
        token:
            description: The token of the VM.
            type: str
            returned: always
        tokenStatus:
            description: The token status of the VM. Possible values are "NOTUSED" or "USED".
            type: str
            returned: always
            sample: "USED"
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def main():
    # Define module arguments
    module_args = dict(
        username=dict(type='str', required=False),
        password=dict(type='str', required=False, no_log=True),
        configId=dict(type='int', required=True),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request to get VMs list
    data = {"configId": module.params["configId"]}
    response = connection.send_request("vms/list", data, method="POST")

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == '__main__':
    main()
