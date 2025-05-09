# Copyright: (c) 2023 Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import json
import hashlib
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.settings import API_URL, AUTH_URL
from ansible_collections.fortinet.fortiflexvm.plugins.module_utils.utils import replace_error_msg
import traceback
from ansible.module_utils.basic import missing_required_lib

try:
    import requests
except ImportError:
    HAS_ANOTHER_LIBRARY = False
    ANOTHER_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_ANOTHER_LIBRARY = True
    ANOTHER_LIBRARY_IMPORT_ERROR = None


class Connection():
    def __init__(self, module, username="", password=""):
        self.module = module
        self.access_token = ""
        self.validation_hash = None
        self.session_file = "fortiflex_session.json"
        self.username = username
        self.password = password
        self.save_session_file = False
        self.log_path = False
        self.retry_times = 4
        self.login()

    def login(self, check_error=True):
        if not self.username:
            self.username = os.environ.get('FORTIFLEX_ACCESS_USERNAME')
        if not self.password:
            self.password = os.environ.get('FORTIFLEX_ACCESS_PASSWORD')
        if not self.username:
            self.module.fail_json(
                msg="Please specify username in your playbook, or set environment variable: FORTIFLEX_ACCESS_USERNAME.")
        if not self.password:
            self.module.fail_json(
                msg="Please specify password in your playbook, or set environment variable: FORTIFLEX_ACCESS_PASSWORD.")
        self.validation_hash = self._hash_str(self.username + self.password)
        self.log_path = os.environ.get('FORTIFLEX_LOG_PATH')
        if self._load_session():
            # already login
            return
        data = {
            "username": self.username,
            "password": self.password,
            "client_id": "flexvm",
            "grant_type": "password"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.send(AUTH_URL, data, headers=headers)
        if check_error and response.status_code >= 400:
            self.module.fail_json(msg="Request failed with status code {0}".format(
                response.status_code), response=response.json())
        self.access_token = response.json()['access_token']
        if self.save_session_file:
            self._save_session()

    def send_request(self, url, data, method="post", check_error=True):
        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json"
        }
        query_url = os.path.join(API_URL, url)
        response = self.send(query_url, data, headers=headers, method=method)
        retry = 0
        while retry <= self.retry_times and response.json()["status"] == -1 and response.json()["message"] == "Invalid security token.":
            if retry == self.retry_times:
                # token expired, login again
                self.logout()
                self.login()
            headers["Authorization"] = "Bearer " + self.access_token
            response = self.send(
                query_url, data, headers=headers, method=method)
            retry += 1

        if check_error and response.status_code >= 400:
            response_data = response.json()
            response_message = response_data.get("message", "")
            try:
                if response_message and "parameter id" in response_message.lower():
                    response_data["message"] = replace_error_msg(response_message)
            except Exception as e:
                pass
            self.module.fail_json(msg="Request failed with status code {0}".format(
                response.status_code), response=response_data)
        return response.json()

    def send(self, url, data, headers=None, method="post"):
        if not HAS_ANOTHER_LIBRARY:
            self.module.fail_json(
                msg=missing_required_lib('requests'),
                exception=ANOTHER_LIBRARY_IMPORT_ERROR)
        response = None
        method = method.lower()
        if self.log_path:
            log_data = data.copy()
            for sensitive_key in ["username", "password"]:
                if sensitive_key in log_data:
                    log_data[sensitive_key] = "******"
            self.log("FortiFlex request to {0}: {1}".format(
                url, str(log_data)))
        try:
            if method == "post":
                response = requests.post(url, json=data, headers=headers)
            elif method == "get":
                response = requests.get(url, params=data, headers=headers)
            else:
                raise ValueError(
                    "Invalid method. Only 'post' and 'get' are supported.")
        except Exception as e:
            self.module.fail_json(
                msg="An error occurred while sending the {0} request: {1}".format(method, e))
        if self.log_path:
            log_data = response.json()
            for sensitive_key in ["access_token", "refresh_token"]:
                if sensitive_key in log_data:
                    log_data[sensitive_key] = "******"
            self.log("FortiFlex response: " + str(log_data))
        return response

    def logout(self):
        self._remove_session()

    def log(self, data):
        try:
            if self.log_path:
                with open(self.log_path, "a") as f:
                    if isinstance(data, list):
                        for item in data:
                            f.write(str(item) + "\n")
                    else:
                        f.write(str(data) + "\n")
        except (IOError, KeyError):
            pass

    def _load_session(self):
        try:
            with open(self.session_file, "r") as f:
                session_data = json.load(f)
                if self.validation_hash != session_data["validation_hash"]:
                    return False
                self.access_token = session_data["access_token"]
            return True
        except (IOError, KeyError):
            return False

    def _save_session(self):
        with open(self.session_file, "w") as f:
            json.dump({"access_token": self.access_token,
                      "validation_hash": self.validation_hash}, f)

    def _remove_session(self):
        try:
            os.remove(self.session_file)
        except OSError:
            pass

    def _hash_str(self, input_str):
        md5_hash = hashlib.md5()
        md5_hash.update(input_str.encode('utf-8'))
        md5_digest = md5_hash.hexdigest()
        return md5_digest
