![Fortinet logo|](https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Fortinet_logo.svg/320px-Fortinet_logo.svg.png)

# Ansible Collection - fortinet.fortiflexvm
The collection is the FortiFlexVM Ansible Automation project. It includes the modules that are able to interact with FlexVM.

## Installation
This collection is distributed via [ansible-galaxy](https://galaxy.ansible.com/), the installation steps are as follows:

1. Install or upgrade to Ansible 2.9+
2. Download this collection from galaxy: `ansible-galaxy collection install fortinet.fortiflexvm`

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