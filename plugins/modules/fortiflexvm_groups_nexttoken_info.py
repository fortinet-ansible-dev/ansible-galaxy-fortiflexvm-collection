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
module: fortiflexvm_groups_nexttoken_info
short_description: Get net available (unused) token.
description:
    - Returns first available token by asset folder or Configuration id (folder path, or config id or both can be specified in request).
version_added: "1.0.0"
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
        description: Account ID. Please declare at least one of the two arguments, accountId or configId.
        type: str
    configId:
        description:
            - The ID of a Flex VM Configuration. Please declare at least one of the two arguments, accountId or configId.
        type: int
    folderPath:
        description:
            - Folder path.
        type: str
    status:
        description: Filter option. A list. Possible values are "ACTIVE", "PENDDING", "STOPPED" and "EXPIRED".
        type: list
        elements: str
"""

EXAMPLES = """
- name: Get next available (unused) token
  hosts: localhost
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Get groups nexttoken
      fortinet.fortiflexvm.fortiflexvm_groups_nexttoken_info:
        username: "{{ username }}"
        password: "{{ password }}"
        # Please declare at least one of the following two arguments: accountId or configId.
        # You can comment at most one argument that you don't want to specify.
        configId: 22
        # accountId: 12345

        # Optional parameters
        folderPath: "My Assets"
        status: ["ACTIVE", "PENDING"] # "ACTIVE", "PENDING", "STOPPED", "EXPIRED"
      register: result

    - name: Display response
      ansible.builtin.debug:
        var: result.entitlements
"""

RETURN = """
entitlements:
    description: Next available (unused) token. This list only has one element.
    type: list
    returned: always
    contains:
        accountId:
            description: Account ID.
            type: int
            returned: if specified account ID in the argument
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
            sample: "VMs created for department A"
        endDate:
            description: The end date of the entitlement.
            type: str
            returned: always
            sample: "2020-10-25 00:00:00"
        serialNumber:
            description: The serial number of the entitlement.
            type: str
            returned: always
            sample: "FGVMELTM20000020"
        startDate:
            description: The start date of the entitlement.
            type: str
            returned: always
            sample: "2020-08-01 10:12:25"
        status:
            description: The status of the entitlement. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".
            type: str
            returned: always
            sample: "ACTIVE"
        token:
            description: The token of the entitlement.
            type: str
            returned: always
        tokenStatus:
            description: The token status of the entitlement.
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
        accountId=dict(type="str"),
        configId=dict(type="int"),
        folderPath=dict(type="str"),
        status=dict(type="list", elements="str"),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request to get program list
    data = {}
    request_url = "fortiflex/v2/groups/nexttoken"
    for key in ["configId", "folderPath", "status", "accountId"]:
        if module.params[key] is not None:
            data[key] = module.params[key]
    response = connection.send_request(request_url, data, method="POST")
    if "vms" in response:  # Avoid bug in API
        response["entitlements"] = response["vms"]
        del response["vms"]

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == "__main__":
    main()
