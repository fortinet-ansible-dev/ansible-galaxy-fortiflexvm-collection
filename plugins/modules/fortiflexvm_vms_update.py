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
module: fortiflexvm_vms_update
short_description: Update an existing VM.
description:
    - This module updates an existing virtual machine.
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
    serialNumber:
        description:
            - The serial number of the virtual machine to update.
        type: str
        required: true
    configId:
        description:
            - The ID of the virtual machine configuration.
        type: int
        required: false
    description:
        description:
            - The description of the virtual machine.
        type: str
        required: false
    endDate:
        description:
            - The end date of the virtual machine's validity.
            - Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted.
            - Recommended format is "YYYY-MM-DDThh:mm:ss".
        type: str
        required: false
    regenerateToken:
        description:
            - Whether to regenerate the token assigned to the virtual machine.
        type: bool
        required: false
        default: false
    status:
        description:
            - The status of the virtual machine.
        type: str
        required: false
        choices: ["ACTIVE", "STOPPED"]
'''

EXAMPLES = '''
- name: Update VM
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Update a Virtual Machine
      fortinet.fortiflexvm.fortiflexvm_vms_update:
        username: "{{ username }}"
        password: "{{ password }}"
        serialNumber: "FGVMMLTM23001324"
        # Please specify configId if you want to update configId, description or endDate
        configId: 3196
        description: "Modify through Ansible"
        endDate: "2023-12-12T00:00:00"
        status: "ACTIVE" # ACTIVE or STOPPED
        regenerateToken: False
      register: result

    - name: Display response
      debug:
        var: result.vms
'''

RETURN = '''
vms:
    description: The VM you update. This list only contains one VM.
    type: list
    returned: always
    contains:
        serialNumber:
            description: The serial number of the VM.
            type: str
            returned: always
            sample: "FGVMMLTM23001324"
        description:
            description: The description of the VM.
            type: str
            returned: always
            sample: "Modify through Ansible"
        configId:
            description: The config ID of the VM.
            type: int
            returned: always
            sample: 3196
        startDate:
            description: The start date of the VM.
            type: str
            returned: always
            sample: "2023-03-13T11:48:53.03"
        endDate:
            description: The end date of the VM.
            type: str
            returned: always
            sample: "2023-12-12T00:00:00"
        status:
            description: The status of the VM. Possible values are "PENDING", "ACTIVE", "STOPPED" or "EXPIRED".
            type: str
            returned: always
            sample: "ACTIVE"
        token:
            description: The token of the VM.
            type: str
            returned: always
        tokenStatus:
            description: The token status of the VM. Possible values are "NOTUSED" or "USED".
            type: str
            returned: always
            sample: "NOTUSED"
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def change_status(module, connection, action):
    data = {"serialNumber": module.params["serialNumber"]}
    if action == "ACTIVE":
        response = connection.send_request("vms/reactivate", data, method="POST")
    elif action == "STOPPED":
        response = connection.send_request("vms/stop", data, method="POST")
    return response


def update_vm(module, connection, check_error=False):
    data = {}
    for param in ["serialNumber", "configId", "description", "endDate"]:
        if module.params[param]:
            data[param] = module.params[param]
    response = connection.send_request("vms/update", data, method="POST", check_error=check_error)
    return response


def main():
    # Define module arguments
    module_args = dict(
        username=dict(type='str', required=False),
        password=dict(type='str', required=False, no_log=True),
        serialNumber=dict(type='str', required=True),
        configId=dict(type='int', required=False),
        description=dict(type='str', required=False),
        endDate=dict(type='str', required=False),
        regenerateToken=dict(type='bool', required=False, default=False),
        status=dict(type='str', required=False, choices=["ACTIVE", "STOPPED"])
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Check mode
    if module.check_mode:
        module.exit_json(changed=True, input_params=module.params)

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # The following part is extremely complicated because of the indecent design of FlexVM API.
    response = {}
    current_status = "UNKNOWN"

    # regenerate the token
    if module.params["regenerateToken"]:
        data = {
            "serialNumber": module.params["serialNumber"]
        }
        response = connection.send_request("vms/token", data, method="POST")
        current_status = response["vms"][0]["status"]

    # update the VM
    if (module.params["description"] or module.params["endDate"]) and not module.params["configId"]:
        module.fail_json(
            msg="Please specify configId if you want to update configId, description or endDate")

    if module.params["configId"]:
        # Try to update the vm.
        response = update_vm(module, connection, check_error=False)
        # handle error manually
        if response["status"] != 0:
            if response["message"] == "Unable to update VM from current status.":
                # This error is probably because of one of the following:
                # 1. The current status is PENDING, the user has to use the token first to activate this VM
                # 2. The current status is STOPPED. If the user set status: "ACTIVE", we could try to activate it first and update the VM.
                # Yet we can't tell it is because of case 1 or case 2 now.
                if module.params["status"] == "ACTIVE":
                    response = change_status(module, connection, "ACTIVE")
                    # Update the VM again, and check error in send(). No need to manually check error.
                    response = update_vm(module, connection, check_error=False)
                    # If error again
                    if response["status"] != 0:
                        if response["message"] == "Unable to update VM from current status.":
                            module.fail_json(msg="You can't update the status of the VM. It may be because: "
                                             "The VM is in the PENDING status, please use the token first. ", response=response)
                        else:
                            module.fail_json(msg="Request failed.", **response)
                else:
                    module.fail_json(msg="You can't update the status of the VM. It may be because one of the following: "
                                     "1) The VM is in the PENDING status, please use the token first. "
                                     "2) You are trying to update a stopped VM. Please activate the VM by adding 'status: ACTIVE' and try again.",
                                     response=response)
            else:
                module.fail_json(msg="Request failed.", **response)
        # Get current status
        current_status = response["vms"][0]["status"]

    # active or stop the VM
    if module.params["status"] and module.params["status"] != current_status:
        response = change_status(module, connection, module.params["status"])
        if response["message"] == "Unable to update VM from current status.":
            module.fail_json(msg="You can't update the status of the VM. It may be because one of the following: "
                             "1) The VM is in the PENDING status, please use the token first. "
                             "2) You only update the status without changing other parameters, "
                             "and you are trying to activate an ACTIVE VM or stop a STOPPED VM.", response=response)

    # Exit with response data
    module.exit_json(changed=True, **response)


if __name__ == '__main__':
    main()
