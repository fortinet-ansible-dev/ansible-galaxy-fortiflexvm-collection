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
module: fortiflexvm_entitlements_points_info
short_description: Get point usage for entitlements.
description:
    - Returns total points consumed by one or more entitlements in a date range.
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
        description: Account ID.
        type: int
    configId:
        description:
            - The ID of the configuration.
        type: int
    endDate:
        description:
            - The end date of the date range to query. Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted.
            - Recommended format is YYYY-MM-DD.
        type: str
        required: true
    programSerialNumber:
        description:
            - The serial number of your FortiFlex Program.
        type: str
    serialNumber:
        description:
            - The entitlement serial number.
            - Instead of configId you can pass serialNumber to get results for one VM only.
        type: str
    startDate:
        description:
            - The start date of the date range to query. Any format that satisfies [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) is accepted.
            - Recommended format is YYYY-MM-DD.
        type: str
        required: true
"""

EXAMPLES = """
- name: Get point usage for entitlementss
  hosts: localhost
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Get entitlements points
      fortinet.fortiflexvm.fortiflexvm_entitlements_points_info:
        username: "{{ username }}"
        password: "{{ password }}"
        # Either configId or (accountId and programSerialNumber) should be provided.
        # configId: 3196
        accountId: 12345
        programSerialNumber: "ELAVMS0XXXXXX"
        # Instead of configId you can pass serialNumber to get results for one VM only.
        serialNumber: "FZVMMLTMXXXXXX"
        startDate: "2020-10-01"
        endDate: "2020-10-25"
      register: result

    - name: Display response
      ansible.builtin.debug:
        var: result.entitlements
"""

RETURN = """
entitlements:
    description: List of entitlements and their consumed points in the specified date range.
    type: list
    returned: always
    contains:
        accountId:
            description: The ID of the account associated with the program.
            type: int
            returned: always
            sample: 12345
        points:
            description: The total points consumed by the entitlement in the specified date range.
            type: int
            returned: always
            sample: 425
        serialNumber:
            description: The serial number of the entitlement.
            type: str
            returned: always
            sample: "FGVMELTM20000029"
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
        endDate=dict(type="str", required=True),
        programSerialNumber=dict(type="str"),
        serialNumber=dict(type="str"),
        startDate=dict(type="str", required=True),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request to get entitlements points
    if not module.params["configId"] and not (module.params["accountId"] and module.params["programSerialNumber"]):
        module.fail_json(
            msg="Please declare configId or declare accountId + programSerialNumber.")
    data = {
        "startDate": module.params["startDate"],
        "endDate": module.params["endDate"]
    }
    for key in ["accountId", "configId", "programSerialNumber", "serialNumber"]:
        if module.params[key]:
            data[key] = module.params[key]
    response = connection.send_request("fortiflex/v2/entitlements/points", data, method="POST")

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == "__main__":
    main()
