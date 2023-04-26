# Copyright: (c) 2023 Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

AUTH_URL = "https://customerapiauth.fortinet.com/api/v1/oauth/token/"
API_URL = "https://support.fortinet.com/ES/api/flexvm/v1/"

PRODUCTS = [
    {
        "id": 1,
        "name": "fortiGateBundle",
        "parameters": [
            {"id": 1, "name": "cpu", "type": "str", "choices": [
                "1", "2", "4", "8", "16", "32", "2147483647"], "required":True},
            {"id": 2, "name": "service", "type": "str", "choices": [
                "FC", "UTM", "ENT", "ATP"], "required":True},
            {"id": 10, "name": "vdom", "type": "int", "min": 0,
                "max": 500, "required": False, "default": 0},
        ],
    },
    {
        "id": 2,
        "name": "fortiManager",
        "parameters": [
            {"id": 3, "name": "device", "type": "int",
                "min": 0, "max": 100000, "required": True},
            {"id": 9, "name": "adom", "type": "int",
                "min": 0, "max": 100000, "required": True},
        ],
    },
    {
        "id": 3,
        "name": "fortiWeb",
        "parameters": [
            {"id": 4, "name": "cpu", "type": "str", "choices": [
                "1", "2", "4", "8", "16"], "required":True},
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
            {"id": 7, "name": "fortiGuardServices", "type": "list", "elements": "str", "choices": [
                "IPS", "AVDB", "FURL", "IOTH", "FGSA", "ISSS"], "required":False, "default":[]},
            {"id": 8, "name": "supportService", "type": "str",
                "choices": ["FC247", "ASET"], "required":True},
            {"id": 11, "name": "vdom", "type": "int",
                "min": 1, "max": 500, "required": True},
            {"id": 12, "name": "cloudServices", "type": "list", "elements": "str", "choices": [
                "FAMS", "SWNM", "FMGC", "AFAC"], "required":False, "default":[]},
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
                "choices": ["FAZFC247"], "required":True},
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
]
