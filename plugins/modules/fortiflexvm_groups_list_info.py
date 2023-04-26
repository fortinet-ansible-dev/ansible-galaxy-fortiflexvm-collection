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
module: fortiflexvm_groups_list_info
short_description: Get list of FlexVM groups (asset folders).
description:
    - This module returns list of FlexVM groups (asset folders that have FlexVM products in them).
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
'''

EXAMPLES = '''
- name: Get list of FlexVM groups
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Get groups list
      fortinet.fortiflexvm.fortiflexvm_groups_list_info:
        username: "{{ username }}"
        password: "{{ password }}"
      register: result

    - name: Display response
      debug:
        var: result.groups
'''

RETURN = '''
groups:
    description: List of groups associated with the specified user.
    type: list
    returned: always
    contains:
        folderPath:
            description: The folder path of the FlexVM group.
            type: str
            returned: always
            sample: "My Assets/Department A/FlexVM Group 1"
        availableTokens:
            description: The number of available tokens for the FlexVM group.
            type: int
            returned: always
            sample: 5
        usedTokens:
            description: The number of used tokens for the FlexVM group.
            type: int
            returned: always
            sample: 22
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def main():
    # Define module arguments
    module_args = dict(
        username=dict(type='str', required=False),
        password=dict(type='str', required=False, no_log=True),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request to get groups list
    response = connection.send_request("groups/list", {}, method="POST")

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == '__main__':
    main()
