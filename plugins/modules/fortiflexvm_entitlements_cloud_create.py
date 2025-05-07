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
module: fortiflexvm_entitlements_cloud_create
short_description: Create one cloud entitlement based on a FortiFlex Configuration.
description:
    - Create one cloud entitlement on a FortiFlex Configuration.
    - This API is only used to create one cloud entitlement. To modify an entitlement, please refer to fortiflexvm_entitlements_update.
version_added: "2.1.0"
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
    endDate:
        description:
            - VM(s) end date. It can not be before today's date or after the program's end date.
            - Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted.
            - Recommended format is "YYYY-MM-DDThh:mm:ss".
            - If not specify, it will use the program's end date automatically.
        type: str
"""

EXAMPLES = """
- name: Create cloud entitlement.
  hosts: localhost
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
    config_id: 12345
  tasks:
    - name: Create Cloud Entitlement.
      fortinet.fortiflexvm.fortiflexvm_entitlements_cloud_create:
        username: "{{ username }}"
        password: "{{ password }}"
        configId: "{{ config_id }}"
        # endDate: "2024-02-12T00:00:00" # Optional. If not set, it will use the program end date automatically.
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
        endDate=dict(type="str"),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Prepare data to send
    data = {}
    for param in ["configId", "endDate"]:
        if module.params[param] is not None:
            data[param] = module.params[param]

    # Check mode
    if module.check_mode:
        module.exit_json(changed=False,
                         input_params=module.params,
                         send_data=data)

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request
    # If something goes wrong (e.g., incorrect input, 404), the program will report an error and exist.
    response = connection.send_request("fortiflex/v2/entitlements/cloud/create", data, method="POST")

    # Exit with response data
    module.exit_json(changed=True, **response)


if __name__ == "__main__":
    main()
