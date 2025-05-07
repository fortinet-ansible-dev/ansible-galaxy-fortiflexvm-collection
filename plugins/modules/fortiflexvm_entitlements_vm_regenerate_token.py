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
module: fortiflexvm_entitlements_vm_regenerate_token
short_description: Regenerate token for a VM.
description:
    - Regenerate token for a VM.
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
    regenerate:
        description:
            - Whether regenerate a new token.
        type: bool
        required: true
    serialNumber:
        description:
            - The serial number of the entitlement to update.
        type: str
        required: true
"""

EXAMPLES = """
- name: Regenerate token
  hosts: localhost
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Regenerate token
      fortinet.fortiflexvm.fortiflexvm_entitlements_vm_regenerate_token:
        username: "{{ username }}"
        password: "{{ password }}"
        serialNumber: "FGVMMLTM00000000"
        regenerate: true # If you set it as false, FortiFlexvm ansible collection will return an empty list.
      register: result

    - name: Display response
      ansible.builtin.debug:
        var: result.entitlements
"""

RETURN = """
entitlements:
    description: The entitlement you update. This list only contains one entitlement. It will be empty if you set regenerate as false.
    type: list
    returned: always
    contains:
        accountId:
            description: Account ID.
            type: int
            returned: always
            sample: 12345
        configId:
            description: The config ID of the entitlement.
            type: int
            returned: always
            sample: 3196
        description:
            description: The description of the entitlement.
            type: str
            returned: always
            sample: "Modify through Ansible"
        endDate:
            description: The end date of the entitlement.
            type: str
            returned: always
            sample: "2023-12-12T00:00:00"
        serialNumber:
            description: The serial number of the entitlement.
            type: str
            returned: always
            sample: "FGVMMLTM23001324"
        startDate:
            description: The start date of the entitlement.
            type: str
            returned: always
            sample: "2023-03-13T11:48:53.03"
        status:
            description: The status of the VM. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".
            type: str
            returned: always
            sample: "ACTIVE"
        token:
            description: The token of the entitlement.
            type: str
            returned: always
        tokenStatus:
            description: The token status of the entitlement. Possible values are "NOTUSED" or "USED".
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
        serialNumber=dict(type="str", required=True),
        regenerate=dict(type="bool", required=True),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Check mode
    if module.check_mode:
        module.exit_json(changed=module.params["regenerate"], input_params=module.params)

    # If don't regenerate, return directly.
    if not module.params["regenerate"]:
        response = {"entitlements": []}
        module.exit_json(changed=False, **response)

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])
    data = {
        "serialNumber": module.params["serialNumber"]
    }

    # Send request
    # If something goes wrong (e.g., incorrect input, 404), the program will report an error and exist.
    response = connection.send_request("fortiflex/v2/entitlements/vm/token", data, method="POST")

    # Exit with response data
    module.exit_json(changed=True, **response)


if __name__ == "__main__":
    main()
