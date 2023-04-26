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
module: fortiflexvm_vms_create
short_description: Create one or more VMs based on a FlexVM Configuration.
description:
    - Create one or more VMs based on a FlexVM Configuration.
    - This API is only used to create one or more VMs. To modify a VM, please refer to fortiflexvm_vms_update.
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
            - The ID of a Flex VM Configuration.
        type: int
        required: true
    count:
        description:
            - The number of VM(s) to be created. The default value is 1.
        type: int
        required: false
        default: 1
    description:
        description:
            - The description of VM(s).
        type: str
        required: false
        default: ""
    endDate:
        description:
            - VM(s) end date. It can not be before today's date or after the program's end date.
            - Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted.
            - Recommended format is "YYYY-MM-DDThh:mm:ss".
        type: str
        required: false
    folderPath:
        description:
            - The folder path of the VM(s).
        type: str
        required: false
'''

EXAMPLES = '''
- name: Create VMs
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Create Virtual Machines
      fortinet.fortiflexvm.fortiflexvm_vms_create:
        username: "{{ username }}"
        password: "{{ password }}"
        configId: 42
        count: 1
        description: "Create through Ansible"
        endDate: "2023-11-11T00:00:00"
        folderPath: "My Assets"
      register: result

    - name: Display response
      debug:
        var: result.vms
'''

RETURN = '''
vms:
    description: A list of virtual machines and their details.
    type: list
    returned: always
    contains:
        configId:
            description: The ID of the virtual machine configuration.
            type: int
            returned: always
            sample: 42
        description:
            description: The description of the virtual machine.
            type: str
            returned: always
            sample: "Create through Ansible"
        endDate:
            description: The end date of the virtual machine's validity.
            type: str
            returned: always
            sample: "2023-11-11T00:00:00"
        serialNumber:
            description: The serial number of the virtual machine.
            type: str
            returned: always
            sample: "FGVMMLTM23002016"
        startDate:
            description: The start date of the virtual machine's validity.
            type: str
            returned: always
            sample: "2023-04-06T15:49:29.643"
        status:
            description: The status of the virtual machine.
            type: str
            returned: always
            sample: "PENDING"
        token:
            description: The token assigned to the virtual machine.
            type: str
            returned: always
        tokenStatus:
            description: The status of the token assigned to the virtual machine.
            type: str
            returned: always
            sample: "NOTUSED"
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def main():
    # Define module arguments
    module_args = dict(
        username=dict(type='str', required=False),
        password=dict(type='str', required=False, no_log=True),
        configId=dict(type='int', required=True),
        count=dict(type='int', required=False, default=1),
        description=dict(type='str', required=False, default=""),
        folderPath=dict(type='str', required=False),
        endDate=dict(type='str', required=False),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Prepare data to send
    data = {}
    for param in ["configId", "count", "endDate", "folderPath", "description"]:
        if module.params[param]:
            data[param] = module.params[param]

    # Check mode
    if module.check_mode:
        module.exit_json(changed=True,
                         input_params=module.params,
                         send_data=data)

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request to get groups list
    # If something goes wrong (e.g., incorrect input, 404), the program will report an error and exist.
    response = connection.send_request("vms/create", data, method="POST")

    # Exit with response data
    module.exit_json(changed=True, **response)


if __name__ == '__main__':
    main()
