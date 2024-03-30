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
module: fortiflexvm_entitlements_update
short_description: Update an existing entitlement.
description:
    - This module updates an existing entitlement.
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
    serialNumber:
        description:
            - The serial number of the entitlement to update.
        type: str
        required: true
    configId:
        description:
            - The ID of the configuration.
        type: int
    description:
        description:
            - The description of the entitlement.
        type: str
    endDate:
        description:
            - The end date of the entitlement's validity.
            - Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted.
            - Recommended format is "YYYY-MM-DDThh:mm:ss".
        type: str
    status:
        description:
            - The status of the entitlement.
        type: str
        choices: ["ACTIVE", "STOPPED"]
"""

EXAMPLES = """
- name: Update entitlement
  hosts: localhost
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Update an entitlement.
      fortinet.fortiflexvm.fortiflexvm_entitlements_update:
        username: "{{ username }}"
        password: "{{ password }}"
        serialNumber: "FGVMXXXX00000000"
        # Please specify configId if you want to update configId, description or endDate
        configId: 3196
        description: "Modify through Ansible" # Optional.
        endDate: "2024-12-12T00:00:00"        # Optional. If not set, it will use the program end date automatically.
        status: "ACTIVE"                      # Optional. ACTIVE or STOPPED
      register: result

    - name: Display response
      ansible.builtin.debug:
        var: result.entitlements
"""

RETURN = """
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
"""

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
        username=dict(type="str"),
        password=dict(type="str", no_log=True),
        serialNumber=dict(type="str", required=True),
        configId=dict(type="int"),
        description=dict(type="str"),
        endDate=dict(type="str"),
        status=dict(type="str", choices=["ACTIVE", "STOPPED"])
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
    if module.params["configId"]:  # Need configId to get info
        data = {"serialNumber": module.params["serialNumber"],
                "configId": module.params["configId"]}
        response = connection.send_request("fortiflex/v2/entitlements/list", data, method="POST")
        if len(response["entitlements"]) == 0:
            module.fail_json(msg="Can't find target entitlement. Please check serialNumber %s." % (module.params["serialNumber"]),
                             response=response)
        target_entitlement = response["entitlements"][0]
        current_status = target_entitlement["status"]

    # If every params are the same, no need to update.
    if target_entitlement:
        need_update_flag = False
        for key in ["description", "endDate", "status"]:
            if module.params[key] is not None and target_entitlement[key] != module.params[key]:
                need_update_flag = True
        if not need_update_flag:
            module.exit_json(changed=False, **response)

    # Check mode
    if module.check_mode:
        module.exit_json(changed=True, input_params=module.params, **response)

    # Update status
    if module.params["status"] == "ACTIVE":
        if current_status != "ACTIVE":
            response = change_status(module, connection, "ACTIVE", check_error=False)
            if response.get("error", None) and "errorCode" in response["error"]:
                module.warn("The entitlement is already ACTIVE. You can provide configId to bypass this error.")
                module.exit_json(changed=False, **response)
    elif module.params["status"] == "STOPPED":
        if current_status != "STOPPED":
            response = change_status(module, connection, "STOPPED")
            if response.get("error", None) and "errorCode" in response["error"]:
                module.warn("The entitlement is already ACTIVE. You can provide configId to bypass this error.")
                module.exit_json(changed=False, **response)

    # Update the entitlement
    if module.params["configId"]:
        # Try to update the entitlement.
        response = update_entitlement(module, connection, check_error=False)
        # Get current status
        current_status = response["entitlements"][0]["status"]

    # Exit with response data
    module.exit_json(changed=True, **response)


if __name__ == "__main__":
    main()
