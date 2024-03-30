# Copyright: (c) 2023 Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

AUTH_URL = "https://customerapiauth.fortinet.com/api/v1/oauth/token/"
API_URL = "https://support.fortinet.com/ES/api/"

PRODUCTS = [
    {
        "id": 1,
        "name": "fortiGateBundle",
        "parameters": [
            {"id": 1, "name": "cpu", "type": "int",
                "min": 1, "max": 96, "required": True},
            {"id": 2, "name": "service", "type": "str", "choices": [
                "FC", "UTP", "ENT", "ATP"], "required": True},
            {"id": 10, "name": "vdom", "type": "int", "min": 0,
                "max": 500, "required": False, "default": 0},
            {"id": 43, "name": "fortiGuardServices", "type": "list", "elements": "str",
                "choices": ["FGTAVDB", "FGTFAIS", "FGTISSS", "FGTDLDB", "FGTFGSA", "FGTFCSS"], "required": False, "default": []},
            {"id": 44, "name": "cloudServices", "type": "list", "elements": "str",
                "choices": ["FGTFAMS", "FGTSWNM", "FGTSOCA", "FGTFAZC", "FGTSWOS", "FGTFSPA"], "required": False, "default": []},
            {"id": 45, "name": "supportService", "type": "str",
                "choices": ["FGTFCELU"], "required": False, "default": "NONE"},
        ],
    },
    {
        "id": 2,
        "name": "fortiManager",
        "parameters": [
            {"id": 30, "name": "device", "type": "int",
                "min": 1, "max": 100000, "required": True},
            {"id": 9, "name": "adom", "type": "int",
                "min": 1, "max": 100000, "required": True},
        ],
    },
    {
        "id": 3,
        "name": "fortiWeb",
        "parameters": [
            {"id": 4, "name": "cpu", "type": "str", "choices": [
                "1", "2", "4", "8", "16"], "required": True},
            {"id": 5, "name": "service", "type": "str",
                "choices": ["FWBSTD", "FWBADV"], "required": True},
        ],
    },
    {
        "id": 4,
        "name": "fortiGateLCS",
        "parameters": [
            {"id": 6, "name": "cpu", "type": "int",
                "min": 1, "max": 96, "required": True},
            {"id": 7, "name": "fortiGuardServices", "type": "list", "elements": "str",
                "choices": ["IPS", "AVDB", "FGSA", "DLDB", "FAIS", "FURLDNS"], "required": False, "default": []},
            {"id": 8, "name": "supportService", "type": "str",
                "choices": ["FC247", "ASET"], "required": True},
            {"id": 11, "name": "vdom", "type": "int",
                "min": 1, "max": 500, "required": True},
            {"id": 12, "name": "cloudServices", "type": "list", "elements": "str",
                "choices": ["FAMS", "SWNM", "AFAC", "FAZC"], "required": False, "default": []},
        ],
    },
    {
        "id": 5,
        "name": "fortiClientEMSOP",
        "parameters": [
            {"id": 13, "name": "ZTNA", "type": "int",
                "min": 0, "max": 25000, "required": True},
            {"id": 14, "name": "EPP", "type": "int",
                "min": 0, "max": 25000, "required": True},
            {"id": 15, "name": "chromebook", "type": "int",
                "min": 0, "max": 25000, "required": True},
            {"id": 16, "name": "service", "type": "str",
                "choices": ["FCTFC247"], "required": True},
            {"id": 36, "name": "addons", "type": "list", "elements": "str",
                "choices": ["BPS"], "required": False, "default": []},
        ],
    },
    {
        "id": 7,
        "name": "fortiAnalyzer",
        "parameters": [
            {"id": 21, "name": "storage", "type": "int",
                "min": 5, "max": 8300, "required": True},
            {"id": 22, "name": "adom", "type": "int",
                "min": 0, "max": 1200, "required": True},
            {"id": 23, "name": "service", "type": "str",
                "choices": ["FAZFC247"], "required": True},
        ],
    },
    {
        "id": 8,
        "name": "fortiPortal",
        "parameters": [
            {"id": 24, "name": "device", "type": "int",
                "min": 0, "max": 100000, "required": True},
        ],
    },
    {
        "id": 9,
        "name": "fortiADC",
        "parameters": [
            {"id": 25, "name": "cpu", "type": "str",
                "choices": ["1", "2", "4", "8", "16", "32"], "required": True},
            {"id": 26, "name": "service", "type": "str",
                "choices": ["FDVSTD", "FDVADV", "FDVFC247"], "required": True},
        ],
    },
    {
        "id": 101,
        "name": "fortiGateHardware",
        "parameters": [
            {"id": 27, "name": "model", "type": "str",
                "choices": ["FGT40F", "FGT60F", "FGT70F", "FGT80F", "FG100F", "FGT60E",
                            "FGT61F", "FG100E", "FG101F", "FG200E", "FG200F", "FG201F",
                            "FG4H0F", "FG6H0F", "FWF40F", "FWF60F", "FGR60F", "FR70FB",
                            "FGT81F", "FG101E", "FG4H1F", "FG1K0F", "FG180F", "F2K60F",
                            "FG3K0F", "FG3K1F", "FG3K2F", "FG40FI", "FW40FI", "FWF61F",
                            "FR60FI", "FGT71F", "FG80FP", "FG80FB", "FG80FD", "FWF80F",
                            "FW80FS", "FWF81F", "FW81FS", "FW81FD", "FW81FP", "FG81FP",
                            "FGT90G", "FGT91G", "FG201E", "FG4H0E", "FG4HBE", "FG4H1E",
                            "FD4H1E", "FG6H0E", "FG6H1E", "FG6H1F", "FG9H0G", "FG9H1G",
                            "FG1K1F", "FG181F", "FG3K7F", "FG39E6", "FG441F"], "required": True},
            {"id": 28, "name": "service", "type": "str",
                "choices": ["FGHWFC247", "FGHWFCEL", "FGHWATP", "FGHWUTP", "FGHWENT"], "required": True},
            {"id": 29, "name": "addons", "type": "list", "elements": "str",
                "choices": ["FGHWFCELU", "FGHWFAMS", "FGHWFAIS", "FGHWSWNM", "FGHWDLDB",
                            "FGHWFAZC", "FGHWSOCA", "FGHWMGAS", "FGHWSPAL", "FGHWFCSS"], "required": False, "default": []},
        ],
    },
    {
        "id": 202,
        "name": "fortiCloudPrivate",
        "parameters": [
            {"id": 32, "name": "throughput", "type": "int", "min": 10, "max": 10000, "required": True},
            {"id": 33, "name": "applications", "type": "int", "min": 0, "max": 2000, "required": True},
        ],
    },
    {
        "id": 203,
        "name": "fortiCloudPublic",
        "parameters": [
            {"id": 34, "name": "throughput", "type": "int", "min": 25, "max": 10000, "required": True},
            {"id": 35, "name": "applications", "type": "int", "min": 0, "max": 2000, "required": True},
        ],
    },
    {
        "id": 204,
        "name": "fortiClientEMSCloud",
        "parameters": [
            {"id": 37, "name": "ZTNA", "type": "int",
                "min": 0, "max": 25000, "required": True},
            {"id": 38, "name": "ZTNA_FGF", "type": "int",
                "min": 0, "max": 25000, "required": True},
            {"id": 39, "name": "EPP_ZTNA", "type": "int",
                "min": 0, "max": 25000, "required": True},
            {"id": 40, "name": "EPP_ZTNA_FGF", "type": "int",
                "min": 0, "max": 25000, "required": True},
            {"id": 41, "name": "chromebook", "type": "int",
                "min": 0, "max": 25000, "required": True},
            {"id": 42, "name": "addons", "type": "list", "elements": "str",
                "choices": ["BPS"], "required": False, "default": []},
        ],
    },
    {
        "id": 205,
        "name": "fortiSASE",
        "parameters": [
            {"id": 48, "name": "users", "type": "int",
                "min": 50, "max": 50000, "required": True},
            {"id": 49, "name": "service", "type": "str",
                "choices": ["FSASESTD", "FSASEADV"], "required": True},
            {"id": 50, "name": "bandwidth", "type": "int",  # value should be divisible by 25
                "min": 25, "max": 10000, "required": True},
            {"id": 51, "name": "dedicatedIPs", "type": "int",
                "min": 4, "max": 65534, "required": True},
        ],
    },
    {
        "id": 206,
        "name": "fortiEDR",
        "parameters": [
            {"id": 46, "name": "service", "type": "str",
                "choices": ["FEDRPDR"], "required": True},
            {"id": 47, "name": "endpoints", "type": "int",
                "readonly": True, "required": False},  # Read only
            {"id": 52, "name": "addons", "type": "list", "elements": "str",
                "choices": ["FEDRXDR"], "required": False, "default": []},
        ],
    },
]
