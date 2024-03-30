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
module: fortiflexvm_entitlements_list_info
short_description: Get entitlements information.
description:
    - This module retrieves information of target entitlements.
    - Either configId or (accountId and programSerialNumber) should be provided.
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
    accountId:
        description: Filter option. Account ID.
        type: int
    configId:
        description:
            - The ID of the configuration for which to retrieve the list of VMs.
        type: int
    description:
        description: Filter option. Description.
        type: str
    serialNumber:
        description: Filter option. Serial number.
        type: str
    status:
        description: Filter option. "ACTIVE", "STOPPED", "PENDDING" or "EXPIRED".
        type: str
    tokenStatus:
        description: Filter option. Token status. "NOTUSED" or "USED".
        type: str
    programSerialNumber:
        description: Filter option. The serial number of your FortiFlex Program.
        type: str
"""

EXAMPLES = """
- name: Get information of target entitlements.
  hosts: localhost
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Get entitlements list
      fortinet.fortiflexvm.fortiflexvm_entitlements_list_info:
        username: "{{ username }}"
        password: "{{ password }}"
        # Either configId or (accountId and programSerialNumber) should be provided.
        configId: 22
        # accountId: 12345
        # programSerialNumber: "ELAVMS00XXXXX"

        # Optional filter options
        # description: "you can use description to distinguish entitlements"
        # serialNumber: "XXXXXX0000000000"
        # status: "PENDING"
        # tokenStatus: "NOTUSED"
      register: result

    - name: Display response
      ansible.builtin.debug:
        var: result.entitlements
"""

RETURN = """
entitlements:
    description: List of entitlements associated with the specified config ID.
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
            sample: 22
        description:
            description: The description of the entitlement.
            type: str
            returned: always
            sample: "VM created for department X"
        endDate:
            description: The end date of the entitlement.
            type: str
            returned: always
            sample: "2020-09-12 12:13:37"
        serialNumber:
            description: The serial number of the entitlement.
            type: str
            returned: always
            sample: "FGVMELTM20000004"
        startDate:
            description: The start date of the entitlement.
            type: str
            returned: always
            sample: "2020-08-25 10:12:25"
        status:
            description: The status of the entitlement. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".
            type: str
            returned: always
            sample: "STOPPED"
        token:
            description: The token of the entitlement.
            type: str
            returned: always
        tokenStatus:
            description: The token status of the entitlement. Possible values are "NOTUSED" or "USED".
            type: str
            returned: always
            sample: "USED"
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def main():
    # Define module arguments
    module_args = dict(
        username=dict(type="str"),
        password=dict(type="str", no_log=True),
        accountId=dict(type="int"),
        configId=dict(type="int"),
        description=dict(type="str"),
        serialNumber=dict(type="str"),
        status=dict(type="str"),
        tokenStatus=dict(type="str", no_log=False),
        programSerialNumber=dict(type="str"),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request to get VMs list
    data = {}
    if not module.params["configId"] and not (module.params["accountId"] and module.params["programSerialNumber"]):
        module.fail_json(
            msg="Please declare configId or declare accountId + programSerialNumber.")
    for key in ["accountId", "configId", "description", "programSerialNumber", "serialNumber", "status", "tokenStatus"]:
        if module.params[key]:
            data[key] = module.params[key]

    response = connection.send_request("fortiflex/v2/entitlements/list", data, method="POST")

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == "__main__":
    main()
