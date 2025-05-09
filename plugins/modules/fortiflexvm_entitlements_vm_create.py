#!/usr/bin/python

# Copyright: (c) 2023 Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: fortiflexvm_entitlements_vm_create
short_description: Create one or more VMs based on a FortiFlex Configuration.
description:
    - Create one or more VMs based on a FortiFlex Configuration.
    - This API is only used to create one or more VMs. To modify a VM, please refer to fortiflexvm_entitlements_update.
version_added: "2.0.0"
author:
    - Xinwei Du (@dux-fortinet)
options:
    username:
        description:
            - The username to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_USERNAME.
        type: str
    password:
        description:
            - The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.
        type: str
    configId:
        description:
            - The ID of a FortiFlex Configuration.
        type: int
        required: true
    count:
        description:
            - The number of VM(s) to be created. The default value is 1.
        type: int
        default: 1
    description:
        description:
            - The description of VM(s).
        type: str
        default: ""
    endDate:
        description:
            - VM(s) end date. It can not be before today's date or after the program's end date.
            - Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted.
            - Recommended format is "YYYY-MM-DDThh:mm:ss".
            - If not specify, it will use the program's end date automatically.
        type: str
    folderPath:
        description:
            - The folder path of the VM(s).
        type: str
    skipPending:
        description:
            - Set it to true will activate the entitlement right away and charges start to incur even without downloading the license by token.
        type: bool
"""

EXAMPLES = """
- name: Create VMs.
  hosts: localhost
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Create Virtual Machines.
      fortinet.fortiflexvm.fortiflexvm_entitlements_vm_create:
        username: "{{ username }}"
        password: "{{ password }}"
        configId: 42
        count: 1 # If you set it as 0, FortiFlexvm ansible collection will not create any vm.
        # description: "Create through Ansible" # Optional.
        # endDate: "2023-11-11T00:00:00"        # Optional. If not set, it will use the program end date automatically.
        # folderPath: "My Assets"               # Optional. If not set, new VM will be in "My Assets"
        # skipPending: false                    # Optional. Set 'skipPending' to true will activate the entitlement right away and charges start.
      register: result

    - name: Display response
      ansible.builtin.debug:
        var: result.entitlements
"""

RETURN = """
entitlements:
    description: A list of virtual machine entitlements and their details.
    type: list
    returned: always
    contains:
        accountId:
            description: The ID of the account associated with the program.
            type: int
            returned: always
            sample: 12345
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
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def main():
    # Define module arguments
    module_args = dict(
        username=dict(type="str"),
        password=dict(type="str", no_log=True),
        configId=dict(type="int", required=True),
        count=dict(type="int", default=1),
        description=dict(type="str", default=""),
        endDate=dict(type="str"),
        folderPath=dict(type="str"),
        skipPending=dict(type="bool"),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Prepare data to send
    data = {}
    for param in ["configId", "count", "endDate", "folderPath", "description", "skipPending"]:
        if module.params[param] is not None:
            data[param] = module.params[param]

    # Check mode
    if module.check_mode:
        changed = (data["count"] != 0)
        module.exit_json(changed=changed,
                         input_params=module.params,
                         send_data=data)

    # If don't create any VM, return directly.
    if data["count"] == 0:
        response = {"entitlements": []}
        module.exit_json(changed=False, **response)

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request
    # If something goes wrong (e.g., incorrect input, 404), the program will report an error and exist.
    response = connection.send_request("fortiflex/v2/entitlements/vm/create", data, method="POST")

    # Exit with response data
    module.exit_json(changed=True, **response)


if __name__ == "__main__":
    main()
