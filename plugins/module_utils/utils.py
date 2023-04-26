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


def camel_to_snake_case(camel_dict):
    """
    Recursively converts the keys of a given dictionary from camelCase to snake_case.

    Args:
        camel_dict (dict): The input dictionary with keys in camelCase format. The dictionary can be nested.

    Returns:
        dict: A new dictionary with keys converted to snake_case format. The structure of the input dictionary is preserved.

    Example:
        input_dict = {
            "thisIsVariable": 1,
            "anotherVariable": {
                "nestedCamelCase": 2,
                "deeplyNested": {
                    "veryDeep": 3
                }
            }
        }
        converted_dict = camel_to_snake_case(input_dict)
        print(converted_dict)
        # Output:
        # {
        #     'this_is_variable': 1,
        #     'another_variable': {
        #         'nested_camel_case': 2,
        #         'deeply_nested': {
        #             'very_deep': 3
        #         }
        #     }
        # }
    """
    def convert_key(key):
        snake_key = []
        for char in key:
            if char.isupper():
                snake_key.append('_')
                snake_key.append(char.lower())
            else:
                snake_key.append(char)
        return ''.join(snake_key)

    snake_dict = {}
    for key, value in camel_dict.items():
        snake_key = convert_key(key)
        if isinstance(value, dict):
            snake_dict[snake_key] = camel_to_snake_case(value)
        else:
            snake_dict[snake_key] = value
    return snake_dict


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
    return get_param_name_by_id.param_id2name[int(id)]


def get_product_name_by_id(id):
    if not hasattr(get_product_name_by_id, 'product_id2name'):
        # Initialize the static dictionary only once
        get_product_name_by_id.product_id2name = {}
        for item in PRODUCTS:
            get_product_name_by_id.product_id2name[item["id"]] = item["name"]
    return get_product_name_by_id.product_id2name[int(id)]


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


def transform_parameters(module):
    # Get products information.
    products = get_products(key="name")
    product_type = infer_product_type(module)

    # Tranform parameters & sanity check
    parameters = []
    configs = module.params[product_type]
    param_requirements = products[product_type]["parameters"]
    for item in param_requirements:
        param_id = item["id"]
        param_name = item["name"]
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
                    if "choices" in item and param_item not in item["choices"]:
                        module.fail_json(msg="Invalid value {0} of parameter {1}. Support values: {2}".format(
                            param_item, param_name, item["choices"]))
                    parameters.append({
                        "id": param_id,
                        "value": param_item
                    })
            else:
                # Check the validation of the input "int"
                # No need to check "choices" for "str". It is already done by Ansible.
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
    return parameters, products[product_type]["id"]


def transform_config_output(item):
    # Trasform the format of output
    configs_response = {}
    product_type = get_product_name_by_id(item["productType"]["id"])
    configs_response[product_type] = {}
    for param in item["parameters"]:
        param_name = get_param_name_by_id(param["id"])
        if param_name not in configs_response[product_type]:
            configs_response[product_type][param_name] = param["value"]
        elif isinstance(configs_response[product_type][param_name], list):
            configs_response[product_type][param_name].append(param["value"])
        else:
            configs_response[product_type][param_name] = [
                configs_response[product_type][param_name], param["value"]]
    for param_name in item:
        if param_name == "productType" or param_name == "parameters":
            continue
        configs_response[param_name] = item[param_name]
    return configs_response


def fill_auth(module):
    if not module.params["username"]:
        username = os.environ.get('FLEXVM_ACCESS_USERNAME')
        if not username:
            module.fail_json(
                msg="Please specify username in your playbook, or set environment variable: FLEXVM_ACCESS_USERNAME.")
        module.params["username"] = username
    if not module.params["password"]:
        password = os.environ.get('FLEXVM_ACCESS_PASSWORD')
        if not password:
            module.fail_json(
                msg="Please specify password in your playbook, or set environment variable: FLEXVM_ACCESS_PASSWORD.")
        module.params["password"] = password
