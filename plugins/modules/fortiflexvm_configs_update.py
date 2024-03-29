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
short_description: Update a FortiFlex Configuration.
description:
    - This module update a FortiFlex Configuration under a program.
version_added: "1.0.0"
author:
    - Xinwei Du (@dux-fortinet)
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
    bypass_validation:
        description:
            - Only set to True when module schema diffs with FortiFlex API structure, module continues to execute without validating parameters.
        type: bool
        required: false
        default: false
        version_added: 2.0.0
    check_parameters:
        description:
            - Check whether the parameters are set correctly before sending the data.
            - If set to true, FortiFlexVM Ansible will check the parameter correctness based on the rules.
            - It is only for debugging purposes, not recommended to set it as true since the rules in FortiFlexVM Ansible may be outdated.
        type: bool
        required: false
        default: false
        version_added: 2.0.0
    fortiGateBundle:
        description:
            - FortiGate Virtual Machine - Service Bundle.
        type: dict
        required: false
        suboptions:
            cpu:
                description:
                    - The number of CPUs. Number between 1 and 96 (inclusive).
                type: int
                required: true
            service:
                description:
                    - The value of this attribute is one of "FC" (FortiCare), "UTP", "ENT" (Enterprise) or "ATP".
                type: str
                required: true
            vdom:
                description:
                    - Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.
                type: int
                required: false
                default: 0
            fortiGuardServices:
                description:
                    - Fortiguard Services. The default value is an empty list.
                    - It should contain zero, one or more elements of ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA", "FGTFCSS"].
                type: list
                elements: str
                required: false
                default: []
            cloudServices:
                description:
                    - Cloud Services. The default value is an empty list.
                    - It should contain zero, one or more elements of ["FGTFAMS", "FGTSWNM", "FGTSOCA", "FGTFAZC", "FGTSWOS", "FGTFSPA"].
                type: list
                elements: str
                required: false
                default: []
            supportService:
                description:
                    - Suport service. "FGTFCELU" or "NONE". Default is "NONE".
                type: str
                required: false
                default: "NONE"
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
            service:
                description:
                    - Service Package. Valid values are "FWBSTD" (Standard) or "FWBADV" (Advanced).
                type: str
                required: true
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
                    - It should contain zero, one or more elements of ["IPS", "AVDB", "FGSA", "DLDB", "FAIS", "FURLDNS"].
                type: list
                elements: str
                required: false
                default: []
            supportService:
                description:
                    - Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).
                type: str
                required: true
            vdom:
                description:
                    - Number of VDOMs. A number between 1 and 500 (inclusive).
                type: int
                required: true
            cloudServices:
                description:
                    - The cloud services this FortiGate Virtual Machine supports. The default value is an empty list.
                    - It should contain zero, one or more elements of ["FAMS", "SWNM", "AFAC", "FAZC"].
                type: list
                elements: str
                required: false
                default: []
    fortiClientEMSOP:
        description:
            - FortiClient EMS On-Prem.
        type: dict
        required: false
        suboptions:
            ZTNA:
                description:
                    - ZTNA/VPN (number of endpoints).
                    - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                type: int
                required: true
            EPP:
                description:
                    - EPP/ATP + ZTNA/VPN (number of endpoints).
                    - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                type: int
                required: true
            chromebook:
                description:
                    - Chromebook (number of endpoints).
                    - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                type: int
                required: true
            service:
                description:
                    - Support Services. Possible value is "FCTFC247" (FortiCare Premium)
                type: str
                required: true
            addons:
                description: Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).
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
    fortiADC:
        description:
            - FortiADC Virtual Machine.
        type: dict
        required: false
        version_added: 2.0.0
        suboptions:
            cpu:
                description:
                    - Number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16" or "32".
                type: str
                required: true
            service:
                description:
                    - Support Service. "FDVSTD" (Standard), "FDVADV" (Advanced) or "FDVFC247" (FortiCare Premium).
                type: str
                required: true
    fortiGateHardware:
        description:
            - FortiGate Hardware.
        type: dict
        required: false
        version_added: 2.0.0
        suboptions:
            model:
                description:
                    - The device model. For all supported models, please check FNDN.
                    - Possible values are
                    - FGT40F (FortiGate-40F), FGT60F (FortiGate-60F), FGT70F (FortiGate-70F), FGT80F (FortiGate-80F),
                    - FG100F (FortiGate-100F), FGT60E (FortiGate-60E), FGT61F (FortiGate-61F), FG100E (FortiGate-100E),
                    - FG101F (FortiGate-101F), FG200E (FortiGate-200E), FG200F (FortiGate-200F), FG201F (FortiGate-201F),
                    - FG4H0F (FortiGate-400F), FG6H0F (FortiGate-600F), FWF40F (FortiWifi-40F), FWF60F (FortiWifi-60F),
                    - FGR60F (FortiGateRugged-60F), FR70FB (FortiGateRugged-70F), FGT81F (FortiGate-81F), FG101E (FortiGate-101E),
                    - FG4H1F (FortiGate-401F), FG1K0F (FortiGate-1000F), FG180F (FortiGate-1800F), F2K60F (FortiGate-2600F),
                    - FG3K0F (FortiGate-3000F), FG3K1F (FortiGate-3001F), FG3K2F (FortiGate-3200F).
                type: str
                required: true
            service:
                description:
                    - Support Service. Possible values are FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite),
                    - FDVFC247 (ATP), FGHWUTP (UTP) or FGHWENT (Enterprise).
                type: str
                required: true
            addons:
                description:
                    - Addons. A list, can be empty, possible values are
                    - FGHWFCELU (FortiCare Elite Upgrade), FGHWFAMS (FortiGate Cloud Management),
                    - FGHWFAIS (AI-Based In-line Sandbox), FGHWSWNM (SD-WAN Underlay), FGHWDLDB (FortiGuard DLP),
                    - FGHWFAZC (FortiAnalyzer Cloud), FGHWSOCA (SOCaaS), FGHWMGAS (Managed FortiGate),
                    - FGHWSPAL (SD-WAN Connector for FortiSASE), FGHWFCSS (FortiConverter Service).
                type: list
                elements: str
                required: false
                default: []
    fortiCloudPrivate:
        description:
            - FortiWeb Cloud, Private.
        type: dict
        required: false
        version_added: 2.0.0
        suboptions:
            throughput:
                description:
                    - Average Throughput (Mbps).
                    - Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600,
                    - 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
                    - 7000, 7500, 8000, 8500, 9000, 9500, 10000.
                type: int
                required: true
            applications:
                description: Number of web applications. Number between 0 and 2000 (inclusive).
                type: int
                required: true
    fortiCloudPublic:
        description:
            - FortiWeb Cloud, Public.
        type: dict
        required: false
        version_added: 2.0.0
        suboptions:
            throughput:
                description:
                    - Average Throughput (Mbps).
                    - Possible values are 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600,
                    - 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
                    - 7000, 7500, 8000, 8500, 9000, 9500, 10000.
                type: int
                required: true
            applications:
                description: Number of web applications. Number between 0 and 2000 (inclusive).
                type: int
                required: true
    fortiClientEMSCloud:
        description:
            - FortiClient EMS Cloud.
        type: dict
        required: false
        suboptions:
            ZTNA:
                description:
                    - ZTNA/VPN (number of endpoints).
                    - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                type: int
                required: true
            ZTNA_FGF:
                description:
                    - ZTNA/VPN + FortiGuard Forensics (number of endpoints).
                    - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                type: int
                required: true
            EPP_ZTNA:
                description:
                    - EPP/ATP + ZTNA/VPN (number of endpoints).
                    - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                type: int
                required: true
            EPP_ZTNA_FGF:
                description:
                    - EPP/ATP + ZTNA/VPN + FortiGuard Forensics (number of endpoints).
                    - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                type: int
                required: true
            chromebook:
                description:
                    - Chromebook (number of endpoints).
                    - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                type: int
                required: true
            addons:
                description: Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).
                type: list
                elements: str
                required: false
                default: []
'''

EXAMPLES = '''
- name: Update a FortiFlex configuration
  hosts: localhost
  collections:
    - fortinet.fortiflexvm
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Update a FortiFlex configuration
      fortinet.fortiflexvm.fortiflexvm_configs_update:
        username: "{{ username }}"
        password: "{{ password }}"
        id: 3643
        name: "ansible_modify"
        status: "DISABLED" # ACTIVE or DISABLED

        # If FortiFlex API supports new params while FortiFlex Ansible does not support them yet,
        # you can set bypass_validation: true. The FortiFlex Ansible will allow you to use new param
        # without perforam any sanity check. The default value is false.
        bypass_validation: false

        # Check whether the parameters are set correctly before sending the data. The default value is false.
        # If set to true, FortiFlexVM Ansible will check the parameter correctness based on the rules.
        # It is only for debugging purposes, not recommended to set it as true since the rules in FortiFlexVM Ansible may be outdated.
        check_parameters: false

        # Please only use zero or one of the following.
        # If you want to update the configuration, please use the type you declared in fortiflexvm_configs_create.

        fortiGateBundle:
          cpu: 2                          # 1 ~ 96
          service: "UTP"                  # "FC", "UTP", "ENT", "ATP"
          vdom: 10                        # 0 ~ 500
          fortiGuardServices: ["FGTFAIS"] # ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA", "FGTFCSS"]
          cloudServices: ["FGTFAMS"]      # ["FGTFAMS", "FGTSWNM", "FGTSOCA", "FGTFAZC", "FGTSWOS", "FGTFSPA"]
          supportService: "NONE"          # "FGTFCELU", "NONE"

        # fortiManager:
        #   device: 1                         # 1 ~ 100000
        #   adom: 1                           # 1 ~ 100000

        # fortiWeb:
        #   cpu: "4"                          # "1", "2", "4", "8", "16"
        #   service: "FWBSTD"                 # "FWBSTD" or "FWBADV"

        # fortiGateLCS:
        #   cpu: 4                            # 1 ~ 96
        #   fortiGuardServices: []            # "IPS", "AVDB", "FGSA", "DLDB", "FAIS", "FURLDNS"
        #   supportService: "FC247"           # "FC247", "ASET"
        #   vdom: 1                           # 1 ~ 500
        #   cloudServices: ["FAMS", "SWNM"]   # "FAMS", "SWNM", "AFAC", "FAZC"

        # fortiClientEMSOP:
        #   ZTNA: 2000                        # 0 ~ 25000. Value should be divisible by 25.
        #   EPP: 2000                         # 0 ~ 25000. Value should be divisible by 25.
        #   chromebook: 2000                  # 0 ~ 25000. Value should be divisible by 25.
        #   service: "FCTFC247"               # "FCTFC247"
        #   addons: ["BPS"]                   # Empty or "BPS"

        # fortiAnalyzer:
        #   storage: 5                        # 5 ~ 8300
        #   adom: 1                           # 0 ~ 1200
        #   service: "FAZFC247"               # "FAZFC247"

        # fortiPortal:
        #   device: 1                         # 0 ~ 100000

        # fortiADC:
        #   cpu: "1"                          # "1", "2", "4", "8", "16", "32"
        #   service: "FDVSTD"                 # "FDVSTD", "FDVADV" or "FDVFC247"

        # fortiGateHardware:
        #   model: "FGT60F"                   # For all supported modules, please check FNDN.
        #                                     # "FGT40F", "FGT60F", "FGT70F", "FGT80F", "FG100F", "FGT60E", "FGT61F",
        #                                     # "FG100E", "FG101F", "FG200E", "FG200F", "FG201F", "FG4H0F", "FG6H0F",
        #                                     # "FWF40F", "FWF60F", "FGR60F", "FR70FB", "FGT81F", "FG101E", "FG4H1F",
        #                                     # "FG1K0F", "FG180F", "F2K60F", "FG3K0F", "FG3K1F", "FG3K2F"...
        #   service: "FGHWFCEL"               # "FGHWFC247", "FGHWFCEL", "FDVFC247", "FGHWUTP" or "FGHWENT"
        #   addons: ["FGHWFAMS", "FGHWFAIS"]  # "FGHWFCELU", "FGHWFAMS", "FGHWFAIS", "FGHWSWNM", "FGHWDLDB",
        #                                     # "FGHWFAZC", "FGHWSOCA", "FGHWMGAS", "FGHWSPAL", "FGHWFCSS"

        # fortiCloudPrivate:
        #   throughput: 1000                  # 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800,
        #                                     # 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
        #                                     # 7000, 7500, 8000, 8500, 9000, 9500, 10000.
        #   applications: 20                  # 0 ~ 2000

        # fortiCloudPublic:
        #   throughput: 1000                  # 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800,
        #                                     # 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
        #                                     # 7000, 7500, 8000, 8500, 9000, 9500, 10000.
        #   applications: 20                  # 0 ~ 2000

        # fortiClientEMSCloud:
        #   ZTNA: 200
        #   ZTNA_FGF: 200
        #   EPP_ZTNA: 200
        #   EPP_ZTNA_FGF: 200
        #   chromebook: 200
        #   addons: []                        # [] or "BPS"

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
        accountId:
            description: The ID of the account associated with the program.
            type: int
            returned: always
            sample: 12345
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
            contains:
                cpu:
                    description:
                        - The number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16",  "32" or "2147483647" (unlimited).
                    type: int
                service:
                    description:
                        - The value of this attribute is one of "FC" (FortiCare), "UTP", "ENT" (Enterprise) or "ATP".
                    type: str
                vdom:
                    description:
                        - Number of VDOMs. A number between 0 and 500 (inclusive). The default number is 0.
                    type: int
                fortiGuardServices:
                    description:
                        - Fortiguard Services. The default value is an empty list.
                        - It should contain zero, one or more elements of ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA", "FGTFCSS"].
                    type: list
                    elements: str
                cloudServices:
                    description:
                        - Cloud Services. The default value is an empty list.
                        - It should contain zero, one or more elements of ["FGTFAMS", "FGTSWNM", "FGTSOCA", "FGTFAZC", "FGTSWOS", "FGTFSPA"].
                    type: list
                    elements: str
                supportService:
                    description:
                        - Suport service. "FGTFCELU" or "NONE". Default is "NONE".
                    type: str
        fortiManager:
            description:
                - FortiManager Virtual Machine.
            type: dict
            contains:
                device:
                    description:
                        - Number of managed devices. A number between 1 and 100000 (inclusive).
                    type: int
                adom:
                    description:
                        - Number of ADOMs. A number between 1 and 100000 (inclusive).
                    type: int
        fortiWeb:
            description:
                - FortiWeb Virtual Machine - Service Bundle.
            type: dict
            contains:
                cpu:
                    description:
                        - Number of CPUs. The value of this attribute is one of "1", "2", "4", "8" or "16".
                    type: str
                service:
                    description:
                        - Service Package. Valid values are "FWBSTD" (Standard) or "FWBADV" (Advanced).
                    type: str
        fortiGateLCS:
            description:
                - FortiGate Virtual Machine - A La Carte Services.
            type: dict
            contains:
                cpu:
                    description:
                        - The number of CPUs. A number between 1 and 96 (inclusive).
                    type: int
                fortiGuardServices:
                    description:
                        - The fortiguard services this FortiGate Virtual Machine supports. The default value is an empty list.
                        - It should contain zero, one or more elements of ["IPS", "AVDB", "FGSA", "DLDB", "FAIS", "FURLDNS"].
                    type: list
                    elements: str
                supportService:
                    description:
                        - Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).
                    type: str
                vdom:
                    description:
                        - Number of VDOMs. A number between 1 and 500 (inclusive).
                    type: int
                cloudServices:
                    description:
                        - The cloud services this FortiGate Virtual Machine supports. The default value is an empty list.
                        - It should contain zero, one or more elements of ["FAMS", "SWNM", "AFAC", "FAZC"].
                    type: list
                    elements: str
        fortiClientEMSOP:
            description:
                - FortiClient EMS On-Prem.
            type: dict
            contains:
                ZTNA:
                    description:
                        - ZTNA/VPN (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                EPP:
                    description:
                        - EPP/ATP + ZTNA/VPN (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                chromebook:
                    description:
                        - Chromebook (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                service:
                    description:
                        - Support Services. Possible value is "FCTFC247" (FortiCare Premium)
                    type: str
                addons:
                    description: Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).
                    type: list
                    elements: str
        fortiAnalyzer:
            description:
                - FortiAnalyzer Virtual Machine.
            type: dict
            contains:
                storage:
                    description:
                        - Daily Storage (GB). A number between 5 and 8300 (inclusive).
                    type: int
                adom:
                    description:
                        - Number of ADOMs. A number between 0 and 1200 (inclusive).
                    type: int
                service:
                    description:
                        - Support Service. Currently, the only available option is "FAZFC247" (FortiCare Premium).
                        - The default value is "FAZFC247".
                    type: str
        fortiPortal:
            description:
                - FortiPortal Virtual Machine.
            type: dict
            contains:
                device:
                    description:
                        - Number of managed devices. A number between 0 and 100000 (inclusive).
                    type: str
        fortiADC:
            description:
                - FortiADC Virtual Machine.
            type: dict
            contains:
                cpu:
                    description:
                        - Number of CPUs. The value of this attribute is one of "1", "2", "4", "8", "16" or "32".
                    type: str
                service:
                    description:
                        - Support Service. "FDVSTD" (Standard), "FDVADV" (Advanced) or "FDVFC247" (FortiCare Premium).
                    type: str
        fortiGateHardware:
            description:
                - FortiGate Hardware.
            type: dict
            contains:
                model:
                    description:
                        - The device model. Possible values are
                        - FGT40F (FortiGate-40F), FGT60F (FortiGate-60F), FGT70F (FortiGate-70F), FGT80F (FortiGate-80F),
                        - FG100F (FortiGate-100F), FGT60E (FortiGate-60E), FGT61F (FortiGate-61F), FG100E (FortiGate-100E),
                        - FG101F (FortiGate-101F), FG200E (FortiGate-200E), FG200F (FortiGate-200F), FG201F (FortiGate-201F),
                        - FG4H0F (FortiGate-400F), FG6H0F (FortiGate-600F), FWF40F (FortiWifi-40F), FWF60F (FortiWifi-60F),
                        - FGR60F (FortiGateRugged-60F), FR70FB (FortiGateRugged-70F), FGT81F (FortiGate-81F), FG101E (FortiGate-101E),
                        - FG4H1F (FortiGate-401F), FG1K0F (FortiGate-1000F), FG180F (FortiGate-1800F), F2K60F (FortiGate-2600F),
                        - FG3K0F (FortiGate-3000F), FG3K1F (FortiGate-3001F), FG3K2F (FortiGate-3200F)...
                    type: str
                service:
                    description:
                        - Support Service. Possible values are FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite),
                        - FDVFC247 (ATP), FGHWUTP (UTP) or FGHWENT (Enterprise).
                    type: str
                addons:
                    description:
                        - Addons. Possible values are
                        - NONE, FGHWFCELU (FortiCare Elite Upgrade), FGHWFAMS (FortiGate Cloud Management),
                        - FGHWFAIS (AI-Based In-line Sandbox), FGHWSWNM (SD-WAN Underlay), FGHWDLDB (FortiGuard DLP),
                        - FGHWFAZC (FortiAnalyzer Cloud), FGHWSOCA (SOCaaS), FGHWMGAS (Managed FortiGate),
                        - FGHWSPAL (SD-WAN Connector for FortiSASE), FGHWFCSS (FortiConverter Service).
                    type: list
                    elements: str
        fortiCloudPrivate:
            description:
                - FortiWeb Cloud, Private.
            type: dict
            contains:
                throughput:
                    description:
                        - Average Throughput (Mbps).
                        - Possible values are 10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600,
                        - 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
                        - 7000, 7500, 8000, 8500, 9000, 9500, 10000.
                    type: int
                applications:
                    description: Number of web applications. Number between 0 and 2000 (inclusive).
                    type: int
        fortiCloudPublic:
            description:
                - FortiWeb Cloud, Public.
            type: dict
            contains:
                throughput:
                    description:
                        - Average Throughput (Mbps).
                        - Possible values are 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600,
                        - 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500,
                        - 7000, 7500, 8000, 8500, 9000, 9500, 10000.
                    type: int
                applications:
                    description: Number of web applications. Number between 0 and 2000 (inclusive).
                    type: int
        fortiClientEMSCloud:
            description:
                - FortiClient EMS Cloud.
            type: dict
            contains:
                ZTNA:
                    description:
                        - ZTNA/VPN (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                ZTNA_FGF:
                    description:
                        - ZTNA/VPN + FortiGuard Forensics (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                EPP_ZTNA:
                    description:
                        - EPP/ATP + ZTNA/VPN (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                EPP_ZTNA_FGF:
                    description:
                        - EPP/ATP + ZTNA/VPN + FortiGuard Forensics (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                chromebook:
                    description:
                        - Chromebook (number of endpoints).
                        - Number between 0 and 25000 (inclusive). Value should be divisible by 25.
                    type: int
                addons:
                    description: Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).
                    type: list
                    elements: str
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import _load_params
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils import utils
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def get_module_args():
    # Define module arguments
    module_args = dict(
        username=dict(type='str', required=False),
        password=dict(type='str', required=False, no_log=True),
        id=dict(type='int', required=True),
        status=dict(type='str', required=False, choices=["ACTIVE", "DISABLED"]),
        name=dict(type='str', required=False),
        bypass_validation=dict(type="bool", required=False, default=False),
        check_parameters=dict(type="bool", required=False, default=False),
    )

    # Get product-specific parameters
    products = utils.get_products(key="name")
    ignore_validation = False
    params = _load_params()
    if params and 'bypass_validation' in params and params['bypass_validation'] is True:
        ignore_validation = True
    for product_name in products:
        if ignore_validation:
            module_args[product_name] = {"type": "dict", "required": False}
        else:
            product_dict = {"type": "dict", "required": False, "options": {}}
            for param in products[product_name]["parameters"]:
                param_details = dict(type=param["type"], required=param["required"])
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
        response = connection.send_request("fortiflex/v2/configs/update", data, method="POST")
        current_status = response["configs"]["status"]

    # active or stop the configuration
    if module.params["status"] and module.params["status"] != current_status:
        data = {"id": module.params["id"]}
        if module.params["status"] == "ACTIVE":
            response = connection.send_request("fortiflex/v2/configs/enable", data, method="POST")
        elif module.params["status"] == "DISABLED":
            response = connection.send_request("fortiflex/v2/configs/disable", data, method="POST")

    # Trasform the format of output data
    response["configs"] = utils.transform_config_output(response["configs"])

    # Exit with response data
    module.exit_json(changed=True, **response)


if __name__ == '__main__':
    main()
