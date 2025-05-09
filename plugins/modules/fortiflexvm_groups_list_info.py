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
module: fortiflexvm_groups_list_info
short_description: Get list of FortiFlex groups (asset folders).
description:
    - This module returns list of FortiFlex groups (asset folders that have FortiFlex products in them).
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
        description: Account ID.
        type: str
"""

EXAMPLES = """
- name: Get list of FortiFlex groups
  hosts: localhost
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Get groups list
      fortinet.fortiflexvm.fortiflexvm_groups_list_info:
        username: "{{ username }}"
        password: "{{ password }}"
        # accountId: 12345 # Optional
      register: result

    - name: Display response
      ansible.builtin.debug:
        var: result.groups
"""

RETURN = """
groups:
    description: List of groups associated with the specified user.
    type: list
    returned: always
    contains:
        accountId:
            description: Account ID.
            type: int
            returned: if specified account ID in the argument
            sample: 12345
        availableTokens:
            description: The number of available tokens for the FortiFlex group.
            type: int
            returned: always
            sample: 5
        folderPath:
            description: The folder path of the FortiFlex group.
            type: str
            returned: always
            sample: "My Assets/Department A/Group 1"
        usedTokens:
            description: The number of used tokens for the FortiFlex group.
            type: int
            returned: always
            sample: 22
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def main():
    # Define module arguments
    module_args = dict(
        username=dict(type="str"),
        password=dict(type="str", no_log=True),
        accountId=dict(type="str"),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request to get groups list
    data = {}
    request_url = "flexvm/v1/groups/list"
    if module.params["accountId"]:
        request_url = "fortiflex/v2/groups/list"
        data["accountId"] = module.params["accountId"]
    response = connection.send_request(request_url, data, method="POST")

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == "__main__":
    main()
