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
module: fortiflexvm_configs_list_info
short_description: Get list of FortiFlex Configurations.
description:
    - This module retrieves a list of configs from FortiFlexVM API using the provided credentials and program serial number.
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
        type: int
    programSerialNumber:
        description:
            - The serial number of the program to get configs for.
        type: str
        required: true
"""

EXAMPLES = """
- name: Get list of FortiFlex Configurations for a Program
  hosts: localhost
  vars:
    username: "<your_own_value>"
    password: "<your_own_value>"
  tasks:
    - name: Get configs list
      fortinet.fortiflexvm.fortiflexvm_configs_list_info:
        username: "{{ username }}"
        password: "{{ password }}"
        # accountId: 12345 # optional
        programSerialNumber: "ELAVMS000000XXXX"
      register: result

    - name: Display response
      ansible.builtin.debug:
        var: result.configs
"""

RETURN = """
configs:
    description: List of configurations for the specified program serial number.
    type: list
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
                        - The number of CPUs. Number between 1 and 96 (inclusive).
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
                        - It should contain zero, one or more elements of ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA"].
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
                        - Number of ADOMs. A number between 0 and 100000 (inclusive).
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
                        - Service Package. Valid values are "FWBSTD" (Standard), "FWBADV" (Advanced) or "FWBENT" (Advanced).
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
                        - It should contain zero, one or more elements of ["IPS", "AVDB", "FURLDNS", "FGSA", "ISSS", "DLDB", "FAIS", "FURL", "IOTH"].
                    type: list
                    elements: str
                supportService:
                    description:
                        - Valid values are "FC247" (FortiCare 24x7) or "ASET" (FortiCare Elite).
                    type: str
                vdom:
                    description:
                        - Number of VDOMs. A number between 0 and 500 (inclusive).
                    type: int
                cloudServices:
                    description:
                        - The cloud services this FortiGate Virtual Machine supports. The default value is an empty list.
                        - It should contain zero, one or more elements of ["FAMS", "SWNM", "AFAC", "FAZC", "FSPA", "SWOS", "FMGC"].
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
                        - Value should be 0 or between 25 and 25000.
                    type: int
                EPP:
                    description:
                        - EPP/ATP + ZTNA/VPN (number of endpoints).
                        - Value should be 0 or between 25 and 25000.
                    type: int
                chromebook:
                    description:
                        - Chromebook (number of endpoints).
                        - Value should be 0 or between 25 and 25000.
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
                addons:
                    description:
                        - Addons. A list. "FAZISSS" (OT Security Service), "FAZFGSA" (Attack Surface Security Service), "FAZAISN" (FortiAI Service).
                    type: list
                    elements: str
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
                        - Support Service. "FDVFC247" (FortiCare Premium), "FDVNET" (Network Security), "FDVAPP" (Application Security), "FDVAI" (AI Security).
                    type: str
        fortiSOAR:
            description:
                - FortiSOAR Virtual Machine.
            type: dict
            contains:
                service:
                    description:
                        -  Service Package. One of ["FSRE", "FSRM", "FSRD", "FSRR"].
                    type: str
                licenseNum:
                    description:
                        - Additional Users License. Number between 0 and 1000 (inclusive).
                    type: int
                addons:
                    description:
                        - Addons. A list. The default value is an empty list.
                        - Possible value is "FSRTIMS" (Threat Intelligence Management).
                    type: list
                    elements: str
        fortiMail:
            description:
                - FortiMail Virtual Machine.
            type: dict
            contains:
                cpu:
                    description:
                        - Number of CPUs. The value of this attribute is one of ["1", "2", "4", "8", "16", "32"].
                    type: str
                service:
                    description:
                        - Service Package. Valid values are "FMLBASE" (Base Bundle) or "FMLATP" (ATP Bundle).
                    type: str
                addons:
                    description:
                        - Addons. A list. The default value is an empty list.
                        - It should contain zero, one or more elements of ["FMLFEMS", "FMLFCAS", "FMLFEOP", "FMLFEEC"]
                    type: list
                    elements: str
        fortiNAC:
            description:
                - FortiNAC Virtual Machine.
            type: dict
            contains:
                service:
                    description:
                        - Service Package. Valid values are "FNCPLUS" (Plus) or "FNCPRO" (Pro).
                    type: str
                endpoints:
                    description:
                        - Number of endpoints. A number between 25 and 100000 (inclusive).
                    type: int
                supportService:
                    description:
                        - Support Service. Currently, the only available option is "FNCFC247" (FortiCare Premium).
                    type: str
        fortiGateHardware:
            description:
                - FortiGate Hardware.
            type: dict
            contains:
                model:
                    description:
                        - Device model. For all supported models, please check FNDN.
                        - Possible values include
                        - FGT40F (FortiGate 40F), FGT60F (FortiGate 60F), FGT70F (FortiGate 70F), FGT80F (FortiGate 80F),
                        - FG100F (FortiGate 100F), FGT60E (FortiGate 60E), FGT61F (FortiGate 61F), FG100E (FortiGate 100E),
                        - FG101F (FortiGate 101F), FG200E (FortiGate 200E), FG200F (FortiGate 200F), FG201F (FortiGate 201F),
                        - FG4H0F (FortiGate 400F), FG6H0F (FortiGate 600F), FWF40F (FortiWiFi 40F), FWF60F (FortiWiFi 60F),
                        - FGR60F (FortiGateRugged 60F), FR70FB (FortiGateRugged 70F), FGT81F (FortiGate 81F), FG101E (FortiGate 101E),
                        - FG4H1F (FortiGate 401F), FG1K0F (FortiGate 1000F), FG180F (FortiGate 1800F), F2K60F (FortiGate 2600F),
                        - FG3K0F (FortiGate 3000F), FG3K1F (FortiGate 3001F), FG3K2F (FortiGate 3200F), FG40FI (FortiGate 40F-3G4G),
                        - FW40FI (FortiWiFi 40F-3G4G), FWF61F (FortiWiFi 61F), FR60FI (FortiGateRugged 60F 3G4G), FGT71F (FortiGate 71F),
                        - FG80FP (FortiGate 80F-PoE), FG80FB (FortiGate 80F-Bypass), FG80FD (FortiGate 80F DSL), FWF80F (FortiWiFi 80F-2R),
                        - FW80FS (FortiWiFi 80F-2R-3G4G-DSL), FWF81F (FortiWiFi 81F 2R), FW81FS (FortiWiFi 81F-2R-3G4G-DSL),
                        - FW81FD (FortiWiFi 81F-2R-3G4G-PoE), FW81FP (FortiWiFi 81F 2R POE), FG81FP (FortiGate 81F-PoE),
                        - FGT90G (FortiGate 90G), FGT91G (FortiGate 91G), FG201E (FortiGate 201E), FG4H0E (FortiGate 400E),
                        - FG4HBE (FortiGate 400E BYPASS), FG4H1E (FortiGate 401E), FD4H1E (FortiGate 401E DC), FG6H0E (FortiGate 600E),
                        - FG6H1E (FortiGate 601E), FG6H1F (FortiGate 601F), FG9H0G (FortiGate 900G), FG9H1G (FortiGate 901G),
                        - FG1K1F (FortiGate 1001F), FG181F (FortiGate 1801F), FG3K7F (FortiGate 3700F), FG39E6 (FortiGate 3960E),
                        - FG441F (FortiGate 4401F), FGR35D (FortiGateRugged 35D), FR70FM (FortiGateRugged 70F 3G4G), FG60EV (FortiGate 60E DSL),
                        - FG60EP (FortiGate 60E POE), FGT61E (FortiGate 61E), FGT80E (FortiGate 80E), FG80EP (FortiGate 80E POE),
                        - FGT81E (FortiGate 81E), FG81EP (FortiGate 81E POE), FGT90E (FortiGate 90E), FGT91E (FortiGate 91E),
                        - FG3H0E (FortiGate 300E), FG3H1E (FortiGate 301E), FG10E0 (FortiGate 1100E), FD10E0 (FortiGate 1100E DC),
                        - FG10E1 (FortiGate 1101E), FD180F (FortiGate 1800F DC), FD181F (FortiGate 1801F DC), FG2K2E (FortiGate 2200E),
                        - FG22E1 (FortiGate 2201E), FD260F (FortiGate 2600F DC), F2K61F (FortiGate 2601F), FD261F (FortiGate 2601F DC),
                        - FD3K0F (FortiGate 3000F DC), FD3K1F (FortiGate 3001F DC), FG32F1 (FortiGate 3201F), FG3K3E (FortiGate 3300E),
                        - FG33E1 (FortiGate 3301E), FG3K4E (FortiGate 3400E), FD3K4E (FortiGate 3400E DC), FG34E1 (FortiGate 3401E),
                        - FD34E1 (FortiGate 3401E DC), FG3K5F (FortiGate 3500F), FG35F1 (FortiGate 3501F), FG3K6E (FortiGate 3600E),
                        - FD3K6E (FortiGate 3600E-DC), FG36E1 (FortiGate 3601E), FG37F1 (FortiGate 3701F), FG39E8 (FortiGate 3980E),
                        - FGD398 (FortiGate 3980E-DC), FG420F (FortiGate 4200F), FD420F (FortiGate 4200F DC), FG421F (FortiGate 4201F),
                        - FD421F (FortiGate 4201F DC), FG440F (FortiGate 4400F), FD440F (FortiGate 4400F DC), FD441F (FortiGate 4401F DC),
                        - FG480F (FortiGate 4800F), FD480F (FortiGate 4800F-DC), FG481F (FortiGate 4801F), FD481F (FortiGate 4801F-DC),
                        - FGT2KE (FortiGate 2000E), FG2K5E (FortiGate 2500E), FG120G (FortiGate 120G), FG121G (FortiGate 121G),
                        - FGT30E (FortiGate 30E), FG30EG (FortiGate 30E 3G4G GBL), FGT50E (FortiGate 50E), FGT51E (FortiGate 51E),
                        - FG60EJ (FortiGate 60E DSLJ), FG1HEF (FortiGate 100EF), F140EP (FortiGate 140E POE), FG5H0E (FortiGate 500E),
                        - FG5H1E (FortiGate 501E), FGD396 (FortiGate 3960E-DC), FWF30E (FortiWiFi 30E), FWF50E (FortiWiFi 50E),
                        - FW502R (FortiWiFi 50E 2R), FWF51E (FortiWiFi 51E), FWF60E (FortiWiFi 60E), FW60EV (FortiWiFi 60E DSL),
                        - FW60EJ (FortiWiFi 60E DSLJ), FWF61E (FortiWiFi 61E), FW50GD (FortiWiFi-50G-DSL), FW50GS (FortiWiFi-50G-SFP),
                        - FG50GD (FortiGate-50G-DSL), FG50GS (FortiGate-50G-SFP), FG50GP (FortiGate-50G-SFP-PoE), FG51GP (FortiGate-51G-SFP-PoE),
                        - FG2H0G (FortiGate-200G), FG2H1G (FortiGate-201G), FGT30G (FortiGate-30G), FGT50G (FortiGate-50G),
                        - FG50G5 (FortiGate-50G-5G), FGT51G (FortiGate-51G), FG51G5 (FortiGate-51G-5G), FGT70G (FortiGate-70G),
                        - FGT71G (FortiGate-71G), FD9H0G (FortiGate-900G-DC), FD9H1G (FortiGate-901G-DC).
                    type: str
                service:
                    description:
                        - Service Package.
                        - Possible values include FGHWFC247 (FortiCare Premium), FGHWFCEL (FortiCare Elite),
                        - FGHWATP (ATP), FGHWUTP (UTP), FGHWENT (Enterprise), FGHWFCESN (FortiCare Essential).
                    type: str
                addons:
                    description:
                        - Add-on services. A list, can be empty.
                        - Possible values include FGHWFCELU (FortiCare Elite Upgrade), FGHWFAMS (FortiGate Cloud Management),
                        - FGHWFAIS (AI-Based In-line Sandbox), FGHWSWNM (SD-WAN Underlay), FGHWDLDB (FortiGuard DLP),
                        - FGHWFAZC (FortiAnalyzer Cloud), FGHWSOCA (SOCaaS), FGHWMGAS (Managed FortiGate),
                        - FGHWSPAL (SD-WAN Connector for FortiSASE), FGHWISSS (FortiGuard OT Security Service),
                        - FGHWSWOS (SD-WAN Overlay-as-a-Service), FGHWAVDB (Advanced Malware Protection),
                        - FGHWNIDS (Intrusion Prevention), FGHWFGSA (Attack Surface Security Service),
                        - FGHWFURL (Web, DNS & Video Filtering), FGHWFSFG (FortiSASE Subscription).
                    type: list
                    elements: str
        fortiAPHardware:
            description:
                - FortiAP Hardware.
            type: dict
            contains:
                model:
                    description:
                        - Device model. For all supported models, please check FNDN.
                        - Possible values include
                        - FP23JF (FortiAP-23JF), FP221E (FortiAP-221E), FP223E (FortiAP-223E), FP231E (FortiAP-231E),
                        - FP231F (FortiAP-231F), FP231G (FortiAP-231G), FP233G (FortiAP-233G), FP234F (FortiAP-234F),
                        - FP234G (FortiAP-234G), FP431F (FortiAP-431F), FP431G (FortiAP-431G), FP432F (FortiAP-432F),
                        - F432FR (FortiAP-432FR), FP432G (FortiAP-432G), FP433F (FortiAP-433F), FP433G (FortiAP-433G),
                        - FP441K (FortiAP-441K), FP443K (FortiAP-443K), FP831F (FortiAP-831F),
                        - PU231F (FortiAP-U231F), PU234F (FortiAP-U234F), PU422E (FortiAP-U422EV),
                        - PU431F (FortiAP-U431F), PU432F (FortiAP-U432F), PU433F (FortiAP-U433F),
                        - FP222E (FortiAP-222E), FP224E (FortiAP-224E).
                    type: str
                service:
                    description:
                        - Support Service
                        - Possible values include FAPHWFC247 (FortiCare Premium), FAPHWFCEL (FortiCare Elite).
                    type: str
                addons:
                    description:
                        - Add-on services. A list, can be empty.
                        - Possible values include FAPHWFSFG (FortiSASE Cloud Managed AP).
                    type: list
                    elements: str
        fortiSwitchHardware:
            description:
                - FortiSwitch Hardware.
            type: dict
            contains:
                model:
                    description:
                        - Device model. For all supported models, please check FNDN.
                        - Possible values include
                        - S108EN (FortiSwitch-108E), S108EF (FortiSwitch-108E-FPOE), S108EP (FortiSwitch-108E-POE),
                        - S108FN (FortiSwitch-108F), S108FF (FortiSwitch-108F-FPOE), S108FP (FortiSwitch-108F-POE),
                        - S124EN (FortiSwitch-124E), S124EF (FortiSwitch-124E-FPOE), S124EP (FortiSwitch-124E-POE),
                        - S124FN (FortiSwitch-124F), S124FF (FortiSwitch-124F-FPOE), S124FP (FortiSwitch-124F-POE),
                        - S148EN (FortiSwitch-148E), S148EP (FortiSwitch-148E-POE), S148FN (FortiSwitch-148F),
                        - S148FF (FortiSwitch-148F-FPOE), S148FP (FortiSwitch-148F-POE), S224DF (FortiSwitch-224D-FPOE),
                        - S224EN (FortiSwitch-224E), S224EP (FortiSwitch-224E-POE), S248DN (FortiSwitch-248D),
                        - S248EF (FortiSwitch-248E-FPOE), S248EP (FortiSwitch-248E-POE), S424DN (FortiSwitch-424D),
                        - S424DF (FortiSwitch-424D-FPOE), S424DP (FortiSwitch-424D-POE), S424EN (FortiSwitch-424E),
                        - S424EF (FortiSwitch-424E-FPOE), S424EI (FortiSwitch-424E-Fiber), S424EP (FortiSwitch-424E-POE),
                        - S448DN (FortiSwitch-448D), S448DP (FortiSwitch-448D-POE), S448EN (FortiSwitch-448E),
                        - S448EF (FortiSwitch-448E-FPOE), S448EP (FortiSwitch-448E-POE), S524DN (FortiSwitch-524D),
                        - S524DF (FortiSwitch-524D-FPOE), S548DN (FortiSwitch-548D), S548DF (FortiSwitch-548D-FPOE),
                        - S624FN (FortiSwitch-624F), S624FF (FortiSwitch-624F-FPOE), S648FN (FortiSwitch-648F),
                        - S648FF (FortiSwitch-648F-FPOE), FS1D24 (FortiSwitch-1024D), FS1E24 (FortiSwitch-1024E),
                        - FS1D48 (FortiSwitch-1048D), FS1E48 (FortiSwitch-1048E), FS2F48 (FortiSwitch-2048F),
                        - FS3D32 (FortiSwitch-3032D), FS3E32 (FortiSwitch-3032E), S426EF (FortiSwitch-M426E-FPOE),
                        - ST1E24 (FortiSwitch-T1024E), SR12DP (FortiSwitchRugged-112D-POE), SR24DN (FortiSwitchRugged-124D),
                        - SM10GF (FortiSwitch-110G-FPOE), SR16FP (FortiSwitchRugged-216F-POE), SR24FP (FortiSwitchRugged-424F-POE).
                    type: str
                service:
                    description:
                        - Support service package.
                        - Possible values include FSWHWFC247 (FortiCare Premium), FSWHWFCEL (FortiCare Elite).
                    type: str
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
                    description: Number of web applications. Number between 1 and 5000 (inclusive).
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
                    description: Number of web applications. Number between 1 and 5000 (inclusive).
                    type: int
        fortiClientEMSCloud:
            description:
                - FortiClient EMS Cloud.
            type: dict
            contains:
                ZTNA:
                    description:
                        - ZTNA/VPN (number of endpoints).
                        - Value should be 0 or between 25 and 25000.
                    type: int
                ZTNA_FGF:
                    description:
                        - ZTNA/VPN + FortiGuard Forensics (number of endpoints).
                        - Value should be 0 or between 25 and 25000.
                    type: int
                EPP_ZTNA:
                    description:
                        - EPP/ATP + ZTNA/VPN (number of endpoints).
                        - Value should be 0 or between 25 and 25000.
                    type: int
                EPP_ZTNA_FGF:
                    description:
                        - EPP/ATP + ZTNA/VPN + FortiGuard Forensics (number of endpoints).
                        - Value should be 0 or between 25 and 25000.
                    type: int
                chromebook:
                    description:
                        - Chromebook (number of endpoints).
                        - Value should be 0 or between 25 and 25000.
                    type: int
                addons:
                    description: Addons. A list. Possible value is "BPS" ( FortiCare Best Practice).
                    type: list
                    elements: str
        fortiSASE:
            description: fortiSASE Cloud Configuration.
            type: dict
            contains:
                users:
                    description:
                        - Number of users. Number between 50 and 50,000 (inclusive).
                        - Number between 50 and 50,000 (inclusive). Value should be divisible by 25.
                    type: int
                service:
                    description:
                        - Service package.
                        - Possible values include "FSASESTD" (Standard), "FSASEADV" (Advanced), "FSASECOM" (Comprehensive).
                    type: str
                bandwidth:
                    description: Number between 25 and 10,000 (inclusive). Value should be divisible by 25.
                    type: int
                dedicatedIPs:
                    description: Number between 4 and 65,534 (inclusive). Value should be divisible by 4.
                    type: int
                computeRegion:
                    description:
                        - Additional Compute Region. Number between 0 and 16 (inclusive).
                        - It can be scaled up in an increment of 1 but scaling down is NOT allowed.
                    type: int
                onRampLocations:
                    description:
                        - SD-WAN On-Ramp Locations. Number between 0 and 8 (inclusive).
                        - It can be scaled up in an increment of 1 but scaling down is NOT allowed.
                    type: int
        fortiEDR:
            description: fortiEDR Cloud Configuration.
            type: dict
            contains:
                service:
                    description: Service package. "FEDRPDR" (Discover/Protect/Respond).
                    type: str
                endpoints:
                    description: Number of Endpoints. Read only.
                    type: int
                addons:
                    description:
                        - Add-on services. A list, can be empty.
                        - Possible value is "FEDRXDR" (XDR).
                    type: list
                    elements: str
                repoStorage:
                    description:
                        - Repository Storage. Number between 0 and 30720 (inclusive)
                        - It can be scaled up in an increment of 512 but scaling down is NOT allowed.
                    type: int
        fortiNDRCloud:
            description: fortiNDR Cloud Configuration.
            type: dict
            contains:
                meteredUsage:
                    description: Metered Usage. Read only.
                    type: int
        fortiRecon:
            description: fortiRecon Cloud Configuration.
            type: dict
            contains:
                service:
                    description:
                        - Service package.
                        - FRNEASM (External Attack Surface Monitoring).
                        - FRNEASMBP (External Attack Surface Monitoring & Brand Protect)
                        - FRNEASMBPACI (External Attack Surface Monitoring & Brand Protect & Adversary Centric Intelligence)
                    type: str
                assets:
                    description: Number of Monitored Assets. Number between 200 and 1,000,000 (inclusive). Value should be divisible by 50.
                    type: int
                networks:
                    description: Internal Attack Surface Monitoring (number of networks). Number between 0 and 100 (inclusive).
                    type: int
                executives:
                    description: Executive Monitoring (number of executives). Number between 0 and 1,000 (inclusive).
                    type: int
                vendors:
                    description: Vendor Monitoring (number of vendors). Number between 0 and 1,000 (inclusive).
                    type: int
        fortiSIEMCloud:
            description: fortiSIEM Cloud Configuration.
            type: dict
            contains:
                computeUnits:
                    description: Number of Compute Units. Number between 10 and 600 (inclusive).
                    type: int
                onlineStorage:
                    description:
                        - Additional Online Storage. Number between 500 and 60,000 (inclusive). Value should be divisible by 500.
                        - It can be scaled up in an increment of 500 but scaling down is NOT allowed.
                    type: int
                archiveStorage:
                    description:
                        - Archive Storage. Number between 0 and 60,000 (inclusive). Value should be divisible by 500.
                        - can be scaled up in an increment of 500 but scaling down is NOT allowed.
                    type: int
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils import utils
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.connection import Connection


def main():
    # Define module arguments
    module_args = dict(
        username=dict(type="str"),
        password=dict(type="str", no_log=True),
        accountId=dict(type="int"),
        programSerialNumber=dict(type="str", required=True),
    )

    # Initialize AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Create connection
    connection = Connection(module, module.params["username"], module.params["password"])

    # Send request to get config list
    data = {"programSerialNumber": module.params["programSerialNumber"]}
    if module.params["accountId"]:
        data["accountId"] = module.params["accountId"]
    response = connection.send_request("fortiflex/v2/configs/list", data, method="POST")

    # Trasform the format of output data
    for i in range(len(response["configs"])):
        response["configs"][i] = utils.transform_config_output(response["configs"][i])

    # Exit with response data
    module.exit_json(changed=False, **response)


if __name__ == "__main__":
    main()
