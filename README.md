![Fortinet logo|](https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Fortinet_logo.svg/320px-Fortinet_logo.svg.png)

# fortinet.fortiflexvm:2.3.0 - interacting with Fortiflex

## Description

FortiFlexVM Ansible Collection includes the modules that are able to interact with [FortiFlex](https://docs.fortinet.com/product/flex-vm/) (also known as FlexVM).

You can use FortiFlexVM Ansible Collection to create entitlements (licenses) for fortinet products.

For details, please read our [documentation](https://ansible-galaxy-fortiflexvm-docs.readthedocs.io/en/latest/).

## Requirements

- Ansible 2.15.0 or above
- Python 3.9 or above

## Installation
This collection is distributed via [ansible-galaxy](https://galaxy.ansible.com/).

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```
ansible-galaxy collection install fortinet.fortiflexvm
```

You can also include it in a requirements.yml file and install it with ansible-galaxy collection install -r requirements.yml, using the format:


```yaml
collections:
  - name: fortinet.fortiflexvm
```

Note that if you install any collections from Ansible Galaxy, they will not be upgraded automatically when you upgrade the Ansible package.
To upgrade the collection to the latest available version, run the following command:

```
ansible-galaxy collection install fortinet.fortiflexvm --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version 2.0.0:

```
ansible-galaxy collection install fortinet.fortiflexvm:==2.0.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.


## Use Cases

Due to the design of the FortiFlex API, **all modules ending with `_create` are not idempotent.** You will create a correspond resource every time you call the modules end with `_create`.
**It is highly recommended you use a separate playbook to run `_create` modules, and only run it when you need new resources.** 

Follow the instruction [Generate an API token for FortiFlexVM](https://ansible-galaxy-fortiflexvm-docs.readthedocs.io/en/latest/token.html), and you will get your apiID (username) and password.

You can specify your username and password in the playbook (not recommended) or the environment variables: FORTIFLEX_ACCESS_USERNAME and FORTIFLEX_ACCESS_PASSWORD.

Create `create_vm_config.yml` with the following template:
```yaml
- name: Create VM configuration
  hosts: localhost
  tasks:
    - name: Create a configuration
      fortinet.fortiflexvm.fortiflexvm_configs_create:
        # You can specify your username and password in the environment variables: FORTIFLEX_ACCESS_USERNAME and FORTIFLEX_ACCESS_PASSWORD.
        username: "xxx" 
        password: "xxx"
        programSerialNumber: "ELAVMS000000XXXX"
        name: "ansible"
        fortiGateBundle:
          cpu: "2"
          service: "FC"
          vdom: 10
```

Run the playbook:
```bash
ansible-playbook create_vm_config.yml
```
You can find more example playbooks [here](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortiflexvm-collection/tree/main/examples)


## Testing

Testing is done by the Fortinet team. Before each new FMG Ansible release, it is tested with the latest patches from all FMG minor releases.


## Support

For any questions regarding FortiFlexVM Ansible Collection, please create a [github issue](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortiflexvm-collection/issues).


## Release Notes and Roadmap

Please check [release note here](CHANGELOG.rst).

FortiFlexVM Ansible Collection is expected to be updated every two months.

## Related Information

[Documentation](https://ansible-galaxy-fortiflexvm-docs.readthedocs.io/en/latest) for the collection.

## Modules
The collection provides the following modules:

* `fortiflexvm_configs_create` Create a new FlexVM Configuration.
* `fortiflexvm_configs_list_info` Get list of FlexVM Configurations.
* `fortiflexvm_configs_update` Update a FlexVM Configuration.
* `fortiflexvm_groups_list_info` Get list of FlexVM groups (asset folders).
* `fortiflexvm_groups_nexttoken_info` Get net available (unused) token.
* `fortiflexvm_programs_list_info` Get list of Flex VM Programs for the account.
* `fortiflexvm_vms_create` Create one or more VMs based on a FlexVM Configuration.
* `fortiflexvm_vms_list_info` Get list of existing VMs for FlexVM Configuration.
* `fortiflexvm_vms_points_info` Get point usage for VMs.
* `fortiflexvm_vms_update` Update an existing VM.
* `fortiflexvm_tools_calc_info` Estimate cost.

## License Information

FortiFlexvm Ansible Collection follows [GNU General Public License v3.0](LICENSE).