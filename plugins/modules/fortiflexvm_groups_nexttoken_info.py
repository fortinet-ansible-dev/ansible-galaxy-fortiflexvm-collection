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
module: fortiflexvm_groups_nexttoken_info
short_description: Get net available (unused) token.
description:
    - Returns first available token by asset folder or Configuration id (folder path, or config id or both can be specified in request).
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
    folderPath:
        description:
            - Folder path. Please declare at least one of the two arguments folderPath and configId.
        type: str
        required: false
        default: ""
    configId:
        description:
            - The ID of a Flex VM Configuration. Please declare at least one of the two arguments folderPath and configId.
        type: int
        required: false
        default: 0
'''

EXAMPLES = '''
- name: Get next available (unused) token
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Get groups nexttoken
      fortinet.fortiflexvm.fortiflexvm_groups_nexttoken_info:
        username: "{{ username }}"
        password: "{{ password }}"
        # Please declare at least one of the following two arguments: folderPath and configId.
        # You can annotate at most one argument that you don't want to specify.
        folderPath: "My Assets"
        configId: 22
      register: result

    - name: Display response
      debug:
        var: result.entitlements
'''

RETURN = '''
entitlements:
    description: Next available (unused) token. This list only has one element.
    type: list
    returned: always
    contains:
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
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def main():
    # Define module arguments
    module_args = dict(
        username=dict(type='str', required=False),
        password=dict(type='str', required=False, no_log=True),
        folderPath=dict(type='str', required=False, default=""),
        configId=dict(type='int', required=False, default=0),
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
    if not module.params['folderPath'] and not module.params['configId']:
        module.fail_json(
            msg="Please declare at least one of the two arguments: folderPath and configId.")
    if module.params['folderPath'] != "":
        data['folderPath'] = module.params['folderPath']
    if module.params['configId'] != 0:
        data['configId'] = module.params['configId']
    response = connection.send_request("flexvm/v1/groups/nexttoken", data, method="POST")
    if "vms" in response:
        response["entitlements"] = response["vms"]
        del response["vms"]

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == '__main__':
    main()
