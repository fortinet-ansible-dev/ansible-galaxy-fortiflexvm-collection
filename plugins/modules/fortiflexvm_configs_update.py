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
module: fortiflexvm_configs_update
short_description: Update a FlexVM Configuration.
description:
    - This module update a FlexVM Configuration under a program.
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
    id:
        description:
            - The ID of the configuration you want to update.
        type: int
        required: true
    name:
        description:
            - The name of your Flex VM Configuration.
        type: str
        required: false
    status:
        description:
            - Active of disable the configuration.
        type: str
        required: false
        choices: ["ACTIVE", "DISABLED"]
    fortiGateBundle:
        description:
            - FortiGate Virtual Machine - Service Bundle.
        type: dict
        required: false
        suboptions:
            cpu:
                description:
                    - The number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16",  "32" or "2147483647" (unlimited).
                type: str
                required: true
                choices: ["1", "2", "4", "8", "16", "32", "2147483647"]
            service:
                description:
                    - The value of this attribute is one of "FC" (FortiCare), "UTM", "ENT" (Enterprise) or "ATP".
                type: str
                required: true
                choices: ["FC", "UTM", "ENT", "ATP"]
            vdom:
                description:
                    - Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.
                type: int
                required: false
                default: 0
    fortiManager:
        description:
            - FortiManager Virtual Machine.
        type: dict
        required: false
        suboptions:
            device:
                description:
                    - Number of managed devices. A number between 1 and 100000 (inclusive).
                type: int
                required: true
            adom:
                description:
                    - Number of ADOMs. A number between 1 and 100000 (inclusive).
                type: int
                required: true
    fortiWeb:
        description:
            - FortiWeb Virtual Machine - Service Bundle.
        type: dict
        required: false
        suboptions:
            cpu:
                description:
                    - Number of CPUs. The value of this attribute is one of "1", "2" "4", "8" or "16".
                type: str
                required: true
                choices: ["1", "2", "4", "8", "16"]
            service:
                description:
                    - Service Package. Valid values are "FWBSTD" (Standard) or "FWBADV" (Advanced).
                type: str
                required: true
                choices: ["FWBSTD", "FWBADV"]
    fortiGateLCS:
        description:
            - FortiGate Virtual Machine - A La Carte Services.
        type: dict
        required: false
        suboptions:
            cpu:
                description:
                    - The number of CPUs. A number between 1 and 96 (inclusive).
                type: int
                required: true
            fortiGuardServices:
                description:
                    - The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list.
                    - It should contain zero, one or more elements of ["IPS", "AVDB", "FURL", "IOTH", "FGSA", "ISSS"].
                type: list
                elements: str
                required: false
                default: []
            supportService:
                description:
                    - Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).
                type: str
                required: true
                choices: ["FC247", "ASET"]
            vdom:
                description:
                    - Number of VDOMs. A number between 1 and 500 (inclusive).
                type: int
                required: true
            cloudServices:
                description:
                    - The cloud services this FortiGate Virtual Machine supports. The default value is an empty list.
                    - It should contain zero, one or more elements of ["FAMS", "SWNM", "FMGC", "AFAC"].
                type: list
                elements: str
                required: false
                default: []
    fortiAnalyzer:
        description:
            - FortiAnalyzer Virtual Machine.
        type: dict
        required: false
        suboptions:
            storage:
                description:
                    - Daily Storage (GB). A number between 5 and 8300 (inclusive).
                type: int
                required: true
            adom:
                description:
                    - Number of ADOMs. A number between 0 and 1200 (inclusive).
                type: int
                required: true
            service:
                description:
                    - Support Service. Currently, the only available option is "FAZFC247" (FortiCare Premium). The default value is "FAZFC247".
                required: true
                type: str
                choices: ["FAZFC247"]
    fortiPortal:
        description:
            - FortiPortal Virtual Machine.
        type: dict
        required: false
        suboptions:
            device:
                description:
                    - Number of managed devices. A number between 0 and 100000 (inclusive).
                type: int
                required: true
'''

EXAMPLES = '''
- name: Update VM configuration
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Update a Virtual Machine configuration
      fortinet.fortiflexvm.fortiflexvm_configs_update:
        username: "{{ username }}"
        password: "{{ password }}"
        id: 3643
        name: "ansible_modify"
        status: "DISABLED" # ACTIVE or DISABLED

        # Please only use zero or one of the following.
        # If you want to update the configuration, please use the type you declared in fortiflexvm_configs_create.

        fortiGateBundle:
          cpu: "2" # "1", "2", "4", "8", "16", "32", "2147483647"
          service: "FC" # "FC", "UTM", "ENT", "ATP"
          vdom: 10 # 0 ~ 500

        # fortiManager:
        #   device: 1 # 1 ~ 100000
        #   adom: 1 # 1 ~ 100000

        # fortiWeb:
        #   cpu: "4" # "1", "2", "4", "8", "16"
        #   service: "FWBSTD" # "FWBSTD" or "FWBADV"

        # fortiGateLCS:
        #   cpu: 4 # 1 ~ 96
        #   fortiGuardServices: [] # "IPS", "AVDB", "FURL", "IOTH", "FGSA", "ISSS"
        #   supportService: "FC247" # "FC247", "ASET"
        #   vdom: 1 # 1 ~ 500
        #   cloudServices: ["FAMS", "SWNM"] # "FAMS", "SWNM", "FMGC", "AFAC"

        # fortiAnalyzer:
        #   storage: 5 # 5 ~ 8300
        #   adom: 1 # 0 ~ 1200
        #   service: "FAZFC247" # "FAZFC247"

        # fortiPortal:
        #   device: 1 # 0 ~ 100000

      register: result

    - name: Display response
      debug:
        var: result.configs
'''

RETURN = '''
configs:
    description: The configuration you update.
    type: dict
    returned: always
    contains:
        id:
            description: The ID of the configuration.
            type: int
            returned: always
            sample: 21
        name:
            description: The name of the configuration.
            type: str
            returned: always
            sample: "Configuration Name"
        programSerialNumber:
            description: The program serial number the configuration belongs to.
            type: str
            returned: always
            sample: "ELAVMR0000000101"
        status:
            description: The status of the configuration.
            type: str
            returned: always
            sample: "ACTIVE"
        fortiGateBundle:
            description:
                - FortiGate Virtual Machine - Service Bundle.
            type: dict
            returned: changed
            contains:
                cpu:
                    description:
                        - The number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16",  "32" or "2147483647" (unlimited).
                    type: str
                    returned: always
                service:
                    description:
                        - he value of this attribute is one of "FC" (FortiCare), "UTM", "ENT" (Enterprise) or "ATP".
                    type: str
                    returned: always
                vdom:
                    description:
                        - Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.
                    type: int
                    returned: always
        fortiManager:
            description:
                - FortiManager Virtual Machine.
            type: dict
            returned: changed
            contains:
                device:
                    description:
                        - Number of managed devices. A number between 1 and 100000 (inclusive).
                    type: int
                    returned: always
                adom:
                    description:
                        - Number of ADOMs. A number between 1 and 100000 (inclusive).
                    type: int
                    returned: always
        fortiWeb:
            description:
                - FortiWeb Virtual Machine - Service Bundle.
            type: dict
            returned: changed
            contains:
                cpu:
                    description:
                        - Number of CPUs. The value of this attribute is one of "1", "2", "4", "8" or "16".
                    type: str
                    returned: always
                service:
                    description:
                        - Service Package. Valid values are "FWBSTD" (Standard) or "FWBADV" (Advanced).
                    type: str
                    returned: always
        fortiGateLCS:
            description:
                - FortiGate Virtual Machine - A La Carte Services.
            type: dict
            returned: changed
            contains:
                cpu:
                    description:
                        - The number of CPUs. A number between 1 and 96 (inclusive).
                    type: int
                    returned: always
                fortiGuardServices:
                    description:
                        - The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list.
                        - It should contain zero, one or more elements of ["IPS", "AVDB", "FURL", "IOTH", "FGSA", "ISSS"].
                    type: list
                    returned: always
                supportService:
                    description:
                        - Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).
                    type: str
                    returned: always
                vdom:
                    description:
                        - Number of VDOMs. A number between 1 and 500 (inclusive).
                    type: int
                    returned: always
                cloudServices:
                    description:
                        - The cloud services this FortiGate Virtual Machine supports. The default value is an empty list.
                        - It should contain zero, one or more elements of ["FAMS", "SWNM", "FMGC", "AFAC"].
                    type: list
                    returned: always
        fortiAnalyzer:
            description:
                - FortiAnalyzer Virtual Machine.
            type: dict
            returned: changed
            contains:
                storage:
                    description:
                        - Daily Storage (GB). A number between 5 and 8300 (inclusive).
                    type: int
                    returned: always
                adom:
                    description:
                        - Number of ADOMs. A number between 0 and 1200 (inclusive).
                    type: int
                    returned: always
                service:
                    description:
                        - Support Service. Currently, the only available option is "FAZFC247" (FortiCare Premium).
                        - The default value is "FAZFC247".
                    type: str
                    returned: always
        fortiPortal:
            description:
                - FortiPortal Virtual Machine.
            type: dict
            returned: changed
            contains:
                device:
                    description:
                        - Number of managed devices. A number between 0 and 100000 (inclusive).
                    type: str
                    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils import utils
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def get_module_args():
    # Define module arguments
    module_args = dict(
        username=dict(type='str', required=False),
        password=dict(type='str', required=False, no_log=True),
        id=dict(type='int', required=True),
        status=dict(type='str', required=False,
                    choices=["ACTIVE", "DISABLED"]),
        name=dict(type='str', required=False),
    )

    # Get product-specific parameters
    products = utils.get_products(key="name")
    for product_name in products:
        product_dict = dict(
            type='dict',
            required=False,
            options=dict()
        )
        for param in products[product_name]["parameters"]:
            param_details = dict(
                type=param["type"], required=param["required"])
            if param["type"] == "str" and "choices" in param:
                param_details["choices"] = param["choices"]
            if "default" in param:
                param_details["default"] = param["default"]
            if "elements" in param:
                param_details["elements"] = param["elements"]
            product_dict["options"][param["name"]] = param_details
        module_args[product_name] = product_dict
    return module_args


def main():
    # Define module arguments
    module_args = get_module_args()

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Prepare data to send
    parameters, data = None, None
    for product_name in utils.get_product_names():
        if module.params[product_name]:
            parameters, product_id = utils.transform_parameters(module)
            data = {
                "name": module.params["name"],
                "id": module.params["id"],
                "parameters": parameters
            }

    # Check mode
    if module.check_mode:
        module.exit_json(changed=True,
                         input_params=module.params,
                         send_data=data)

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    response = {}
    current_status = "UNKNOWN"

    # update the configuration
    if data:
        response = connection.send_request("configs/update", data, method="POST")
        current_status = response["configs"]["status"]

    # active or stop the configuration
    if module.params["status"] and module.params["status"] != current_status:
        data = {"id": module.params["id"]}
        if module.params["status"] == "ACTIVE":
            response = connection.send_request("configs/enable", data, method="POST")
        elif module.params["status"] == "DISABLED":
            response = connection.send_request("configs/disable", data, method="POST")

    # Trasform the format of output data
    response["configs"] = utils.transform_config_output(response["configs"])

    # Exit with response data
    module.exit_json(changed=True, **response)


if __name__ == '__main__':
    main()
