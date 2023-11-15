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
module: fortiflexvm_programs_list_info
short_description: Get list of FortiFlex Programs for the account.
description:
    - This module retrieves a list of FortiFlex Programs using the provided credentials.
version_added: "1.0.0"
author:
    - Xinwei Du (@DrMofu)
options:
    username:
        description:
            - The username to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_USERNAME.
        type: str
        required: false
    password:
        description:
            - The password to authenticate. If not declared, the code will read the environment variable FORTIFLEX_ACCESS_PASSWORD.
        type: str
        required: false
'''

EXAMPLES = '''
- name: Get list of programs for the account
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Get programs list
      fortinet.fortiflexvm.fortiflexvm_programs_list_info:
        username: "{{ username }}"
        password: "{{ password }}"
      register: result

    - name: Display response
      debug:
        var: result.programs
'''

RETURN = '''
programs:
    description: List of programs associated with the specified user.
    type: list
    returned: always
    contains:
        accountId:
            description: The ID of the account associated with the program.
            type: int
            returned: always
            sample: 12345
        endDate:
            description: The end date of the program.
            type: str
            returned: always
            sample: "2021-05-15 00:00:00"
        hasSupportCoverage:
            description: A flag indicating whether the program has support coverage.
            type: bool
            returned: always
            sample: true
        serialNumber:
            description: The serial number of the program.
            type: str
            returned: always
            sample: "ELAVMR0000000101"
        startDate:
            description: The start date of the program.
            type: str
            returned: always
            sample: "2020-05-16 00:00:00"
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

    # Send request to get programs list
    response = connection.send_request("fortiflex/v2/programs/list", {}, method="POST")

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == '__main__':
    main()
