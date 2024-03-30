# Copyright: (c) 2023 Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.settings import PRODUCTS


def get_products(key="name"):
    products = {}
    for item in PRODUCTS:
        products[item[key]] = item
    return products


def get_product_names():
    names = []
    for item in PRODUCTS:
        names.append(item["name"])
    return names


def get_param_id(product_name, param_name):
    for item in PRODUCTS:
        if product_name == item["name"]:
            for param in item["parameters"]:
                if param["name"] == param_name:
                    return param["id"]
    return -1


def get_param_name_by_id(id):
    if not hasattr(get_param_name_by_id, 'param_id2name'):
        # Initialize the static dictionary only once
        get_param_name_by_id.param_id2name = {}
        for item in PRODUCTS:
            params = item["parameters"]
            for param in params:
                get_param_name_by_id.param_id2name[param["id"]] = param["name"]
    param_id = int(id)
    return_name = str(param_id)
    if param_id in get_param_name_by_id.param_id2name:
        return_name = get_param_name_by_id.param_id2name[param_id]
    return return_name


def get_product_name_by_id(id):
    if not hasattr(get_product_name_by_id, 'product_id2name'):
        # Initialize the static dictionary only once
        get_product_name_by_id.product_id2name = {}
        for item in PRODUCTS:
            get_product_name_by_id.product_id2name[item["id"]] = item["name"]
    product_id = int(id)
    return_name = str(product_id)
    if product_id in get_product_name_by_id.product_id2name:
        return_name = get_product_name_by_id.product_id2name[product_id]
    return return_name


def infer_product_type(module):
    specified_products = []
    for product_name in get_product_names():
        if module.params[product_name]:
            specified_products.append(product_name)
    if len(specified_products) == 0:
        module.fail_json(
            msg="You don't declared any product type, please declare one.")
    elif len(specified_products) != 1:
        module.fail_json(msg="You declared {0} product types: {1}, please declare one product type only.".format(
            len(specified_products), specified_products
        ))
    return specified_products[0]


def transform_parameters(module, check_param=False):
    # Get products information.
    products = get_products(key="name")
    product_type = infer_product_type(module)

    # Tranform parameters & sanity check
    parameters = []
    configs = module.params[product_type]
    param_requirements = products[product_type]["parameters"]

    # Consider normal params
    for item in param_requirements:
        param_id = item["id"]
        param_name = item["name"]
        if param_name not in configs:
            continue
        param_value = configs[param_name]
        if param_value is not None:
            if item["type"] == "list":
                if len(param_value) == 0:
                    parameters.append({
                        "id": param_id,
                        "value": "NONE"
                    })
                for param_item in param_value:
                    # Check the validation of the input "list"
                    if check_param and "choices" in item and param_item not in item["choices"]:
                        module.fail_json(msg="Invalid value {0} of parameter {1}. Support values: {2}".format(
                            param_item, param_name, item["choices"]))
                    parameters.append({
                        "id": param_id,
                        "value": param_item
                    })
            else:
                if check_param:
                    # Check "choices" for "str".
                    if item["type"] == "str" and "choices" in item:
                        if param_value not in item["choices"]:
                            module.fail_json(msg="Invalid value {0} of parameter {1}. Support values: {2}".format(
                                param_value, param_name, item["choices"]))
                    # Check the validation of the input "int"
                    if item["type"] == "int" and ("min" in item or "max" in item):
                        min_value = item["min"] if "min" in item else float("-inf")
                        max_value = item["max"] if "max" in item else float("inf")
                        if param_value < min_value or param_value > max_value:
                            module.fail_json(msg="Invalid value {0} of parameter {1}. Support range: {2} ~ {3} (inclusive)".format(
                                param_value, param_name, min_value, max_value))
                parameters.append({
                    "id": param_id,
                    "value": param_value
                })

    # Consider digital params
    for user_define_name in configs:
        if isinstance(user_define_name, int) or user_define_name.isdigit():
            param_id = int(user_define_name)
            param_value = configs[user_define_name]
            if isinstance(param_value, list):
                for param_value_item in param_value:
                    parameters.append({
                        "id": param_id,
                        "value": param_value_item
                    })
            else:
                parameters.append({
                    "id": param_id,
                    "value": param_value
                })
    return parameters, products[product_type]["id"]


def transform_config_output(item):
    # Trasform the format of output
    configs_response = {}
    product_type = get_product_name_by_id(item["productType"]["id"])
    configs_response[product_type] = {}
    for param in item["parameters"]:
        param_name = get_param_name_by_id(param["id"])
        if param_name not in configs_response[product_type]:
            if param["id"] in [7, 12, 29, 36, 42, 43, 44, 52]:
                configs_response[product_type][param_name] = []
                if param["value"] != "NONE":
                    configs_response[product_type][param_name].append(param["value"])
            else:
                configs_response[product_type][param_name] = param["value"]
        elif isinstance(configs_response[product_type][param_name], list):
            configs_response[product_type][param_name].append(param["value"])
        else:  # Change the format of output to list
            configs_response[product_type][param_name] = [configs_response[product_type][param_name], param["value"]]
    for param_name in item:
        if param_name == "productType" or param_name == "parameters":
            continue
        configs_response[param_name] = item[param_name]
    return configs_response


def fill_auth(module):
    if not module.params["username"]:
        username = os.environ.get('FORTIFLEX_ACCESS_USERNAME')
        if not username:
            module.fail_json(
                msg="Please specify username in your playbook, or set environment variable: FORTIFLEX_ACCESS_USERNAME.")
        module.params["username"] = username
    if not module.params["password"]:
        password = os.environ.get('FORTIFLEX_ACCESS_PASSWORD')
        if not password:
            module.fail_json(
                msg="Please specify password in your playbook, or set environment variable: FORTIFLEX_ACCESS_PASSWORD.")
        module.params["password"] = password


def replace_error_msg(msg):
    def replace_id(match):
        return get_param_name_by_id(match.group())
    import re
    return re.sub(r'\d+', replace_id, msg)
