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
module: fortiflexvm_entitlements_update
short_description: Update an existing entitlement.
description:
    - This module updates an existing entitlement.
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
    serialNumber:
        description:
            - The serial number of the entitlement to update.
        type: str
        required: true
    configId:
        description:
            - The ID of the configuration.
        type: int
        required: false
    description:
        description:
            - The description of the entitlement.
        type: str
        required: false
    endDate:
        description:
            - The end date of the entitlement's validity.
            - Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted.
            - Recommended format is "YYYY-MM-DDThh:mm:ss".
        type: str
        required: false
    status:
        description:
            - The status of the entitlement.
        type: str
        required: false
        choices: ["ACTIVE", "STOPPED"]
'''

EXAMPLES = '''
- name: Update entitlement
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Update an entitlement.
      fortinet.fortiflexvm.fortiflexvm_entitlements_update:
        username: "{{ username }}"
        password: "{{ password }}"
        serialNumber: "FGVMMLTM23001324"
        # Please specify configId if you want to update configId, description or endDate
        configId: 3196
        description: "Modify through Ansible" # Optional.
        endDate: "2023-12-12T00:00:00"  # Optional. If not set, it will use the program end date automatically.
        status: "ACTIVE" # ACTIVE or STOPPED
      register: result

    - name: Display response
      debug:
        var: result.entitlements
'''

RETURN = '''
entitlements:
    description: The entitlement you update. This list only contains one entitlement.
    type: list
    returned: always
    contains:
        accountId:
            description: The ID of the account associated with the program.
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
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def change_status(module, connection, action, check_error=True):
    data = {"serialNumber": module.params["serialNumber"]}
    if action == "ACTIVE":
        response = connection.send_request("fortiflex/v2/entitlements/reactivate", data, method="POST", check_error=check_error)
    elif action == "STOPPED":
        response = connection.send_request("fortiflex/v2/entitlements/stop", data, method="POST", check_error=check_error)
    if "vms" in response:
        response["entitlements"] = response["vms"]
        del response["vms"]
    return response


def update_entitlement(module, connection, check_error=True):
    data = {}
    for param in ["serialNumber", "configId", "description", "endDate"]:
        if module.params[param] is not None:
            data[param] = module.params[param]
    response = connection.send_request("fortiflex/v2/entitlements/update", data, method="POST", check_error=check_error)
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
        status=dict(type='str', required=False, choices=["ACTIVE", "STOPPED"])
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # The following part is extremely complicated because of the indecent design of FlexVM API.
    response = {}
    current_status = "UNKNOWN"

    if ((module.params["description"] is not None) or (module.params["endDate"] is not None)) and not module.params["configId"]:
        module.fail_json(msg="Please specify configId if you want to update configId, description or endDate")

    # Try to get current status.
    target_entitlement = None
    if module.params["configId"]:
        data = {"configId": module.params["configId"]}
        response = connection.send_request("fortiflex/v2/entitlements/list", data, method="POST")
        target_serial_number = module.params["serialNumber"]
        for entitlement in response["entitlements"]:
            if entitlement["serialNumber"] == target_serial_number:
                target_entitlement = entitlement
                current_status = entitlement["status"]
                break

    if target_entitlement:
        response["entitlements"] = target_entitlement
        # If every params are the same, no need to update.
        need_update_flag = False
        for key in ["description", "endDate", "status"]:
            if module.params[key] is not None and target_entitlement[key] != module.params[key]:
                need_update_flag = True
        if not need_update_flag:
            module.exit_json(changed=False, **response)
        if module.check_mode:
            module.exit_json(changed=True, input_params=module.params, **response)

        # Status check before update
        if current_status == "PENDING":
            module.fail_json(msg="You can't update this entitlement. "
                                 "Current entitlemt status is PENDING, please use the token first. ", response=response)
        elif current_status == "STOPPED":
            if module.params["status"] == "ACTIVE":
                response = change_status(module, connection, "ACTIVE")
            else:
                module.fail_json(msg="You can't update this entitlement. "
                                     "Current entitlemt status is STOPPED, please set 'status: ACTIVE'. ", response=response)

    # Check mode
    if module.check_mode:
        module.exit_json(changed=True, input_params=module.params)

    # Update the entitlement
    if module.params["configId"]:
        # Try to update the entitlement.
        response = update_entitlement(module, connection, check_error=False)
        # handle error manually
        if response["status"] != 0:
            if response["message"].startswith("Unable to update"):
                # This error is probably because of one of the following:
                # 1. The current status is PENDING, the user has to use the token first to activate this entitlement
                # 2. The current status is STOPPED. If the user set status: "ACTIVE", we could try to activate it first and update the entitlement.
                # Yet we can't tell it is because of case 1 or case 2 now.
                if module.params["status"] == "ACTIVE":
                    response = change_status(module, connection, "ACTIVE")
                    # Update the entitlement again.
                    response = update_entitlement(module, connection, check_error=False)
                    # If error again
                    if response["status"] != 0:
                        if response["message"].startswith("Unable to update"):
                            module.fail_json(msg="You can't update the status of the entitlement. It may be because: "
                                             "This entitlemt is in the PENDING status, please use the token first. ", response=response)
                        else:
                            module.fail_json(msg="Request failed.", response=response)
                else:
                    module.fail_json(msg="You can't update the status of the entitlement. It may be because one of the following: "
                                     "1) This entitlemt is in the PENDING status, please use the token first. "
                                     "2) You are trying to update a stopped entitlement. "
                                     "Please activate the entitlement by adding 'status: ACTIVE' and try again.",
                                     response=response)
            else:
                module.fail_json(msg="Request failed.", response=response)
        # Get current status
        current_status = response["entitlements"][0]["status"]

    # active or stop the entitlement
    if module.params["status"] and module.params["status"] != current_status:
        response = change_status(module, connection, module.params["status"], check_error=False)
        if response["message"].startswith("Unable to update"):
            module.fail_json(msg="You can't update the status of the entitlement. It may be because one of the following: "
                             "1) The entitlement is in the PENDING status, please use the token first. "
                             "2) You only update the status without providing other parameters. "
                             "Please add configID, it can help FortiFlexVM Ansible to properly avoid this error.", response=response)

    # Exit with response data
    module.exit_json(changed=True, **response)


if __name__ == '__main__':
    main()
