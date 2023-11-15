==================================
Fortinet.Fortiflexvm Release Notes
==================================

.. contents:: Topics


v2.0.2
======

Release Summary
---------------

Support 3 new configurations.

Bugfixes
--------

- Support 3 new configurations, fortiClientEMSOP, fortiCloudPrivate and fortiCloudPublic.
- Support optional argument accountId in some modules.
- Update parameters for existing products.
- entitlements_points_info supports getting results for specified entitlement.

v2.0.1
======

Release Summary
---------------

Improve document. Release to Ansible Automation Hub.

Bugfixes
--------

- Improve document quality.

v2.0.0
======

Release Summary
---------------

Update FortiFlexVM Ansible to support FortiFlex v2.

Major Changes
-------------

- Support creating hardware entitlements by using fortiflexvm_entitlements_hardware_create.

Minor Changes
-------------

- Support bypass_validation and check_parameters in fortiflexvm_configs_create and fortiflexvm_configs_update.
- Support two new configurations, fortiADC and fortiGateHardware.

Breaking Changes / Porting Guide
--------------------------------

- All vms modules are renamed to entitlements modules. The return value vms are renamed to entitlements.

Removed Features (previously deprecated)
----------------------------------------

- fortiflexvm_vms_create (renamed to fortiflexvm_entitlements_vm_create)
- fortiflexvm_vms_list_info (renamed to fortiflexvm_entitlements_list_info)
- fortiflexvm_vms_points_info (renamed to fortiflexvm_entitlements_points_info)
- fortiflexvm_vms_update (renamed to fortiflexvm_entitlements_update)

New Modules
-----------

- fortinet.fortiflexvm.fortiflexvm_entitlements_hardware_create - Create hardware entitlements based on a FortiFlex Configuration.
- fortinet.fortiflexvm.fortiflexvm_entitlements_list_info - Get list of existing entitlements for a FlexVM Configuration.
- fortinet.fortiflexvm.fortiflexvm_entitlements_points_info - Get point usage for entitlements.
- fortinet.fortiflexvm.fortiflexvm_entitlements_vm_create - Create one or more VMs based on a FortiFlex Configuration.
- fortinet.fortiflexvm.fortiflexvm_entitlements_vm_regenerate_token - Regenerate token for a VM.

v1.0.0
======

Release Summary
---------------

This is the first proper release of the fortiflex.

New Modules
-----------

- fortinet.fortiflexvm.fortiflexvm_configs_create - Create a new FlexVM Configuration.
- fortinet.fortiflexvm.fortiflexvm_configs_list_info - Get list of FlexVM Configurations.
- fortinet.fortiflexvm.fortiflexvm_configs_update - Update a FlexVM Configuration.
- fortinet.fortiflexvm.fortiflexvm_groups_list_info - Get list of FlexVM groups (asset folders).
- fortinet.fortiflexvm.fortiflexvm_groups_nexttoken_info - Get net available (unused) token.
- fortinet.fortiflexvm.fortiflexvm_programs_list_info - Get list of Flex VM Programs for the account.
- fortinet.fortiflexvm.fortiflexvm_vms_create - Create one or more VMs based on a FlexVM Configuration.
- fortinet.fortiflexvm.fortiflexvm_vms_list_info - Get list of existing VMs for FlexVM Configuration.
- fortinet.fortiflexvm.fortiflexvm_vms_points_info - Get point usage for VMs.
- fortinet.fortiflexvm.fortiflexvm_vms_update - Update an existing VM.
