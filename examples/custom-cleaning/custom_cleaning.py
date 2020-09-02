# Copyright 2015 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

from oslo_log import log

from ironic_python_agent import errors
from ironic_python_agent import hardware

LOG = log.getLogger()


class CustomCleaningHardwareManager(hardware.HardwareManager):
    # All hardware managers have a name and a version.
    # Version should be bumped anytime a change is introduced. This will
    # signal to Ironic that if automatic node cleaning is in progress to
    # restart it from the beginning, to ensure consistency. The value can
    # be anything; it's checked for equality against previously seen
    # name:manager pairs.
    HARDWARE_MANAGER_NAME = 'custom_cleaning_manager'
    HARDWARE_MANAGER_VERSION = '1.0'

    def evaluate_hardware_support(self):
        """Declare level of hardware support provided.

        Since this example is explicitly about enforcing business logic during
        cleaning, we want to return a static value.

        :returns: HardwareSupport level for this manager.
        """
        return hardware.HardwareSupport.SERVICE_PROVIDER

    def get_clean_steps(self, node, ports):
        return [
            {
                'step': 'erase_devices',
                'priority': 0,
                'interface': 'deploy',
                'reboot_requested': False,
                'abortable': False
            },
            {
                'step': 'erase_devices_metadata',
                'priority': 0,
                'interface': 'deploy',
                'reboot_requested': False,
                'abortable': False
            },
            {
                'step': 'get_root_disks',
                'priority': 90,
                'interface': 'deploy',
                # If you need Ironic to coordinate a reboot after this step
                # runs, but before continuing cleaning, this should be true.
                'reboot_requested': False,
                # If it's safe for Ironic to abort cleaning while this step
                # runs, this should be true.
                'abortable': False
            },
            {
                'step': 'erase_root_disks',
                'priority': 80,
                'interface': 'deploy',
                'reboot_requested': False,
                'abortable': False
            },
        ]

    def get_root_disks(self, node, ports):
        # find the list of the root disks by calling ironic_lib package
        root_disks = utils.find_devices_by_hints(devices, root_device_hints)
        
        """Find all devices that match the root device hints.

        Reference: https://github.com/openstack/ironic-lib/blob/6c9d5dc58b976c30be95340b8799daf485203994/ironic_lib/utils.py#L329

        Try to find devices that match the root device hints. In order
        for a device to be matched it needs to satisfy all the given hints.

        :param root_device_hints: A dictionary with the root device hints.
        :param devices: A list of dictionaries representing the devices
                    containing one or more of the following keys:

        :name: (String) The device name, e.g /dev/sda
        :size: (Integer) Size of the device in *bytes*
        :model: (String) Device model
        :vendor: (String) Device vendor name
        :serial: (String) Device serial number
        :wwn: (String) Unique storage identifier
        :wwn_with_extension: (String): Unique storage identifier with
                             the vendor extension appended
        :wwn_vendor_extension: (String): United vendor storage identifier
        :rotational: (Boolean) Whether it's a rotational device or
                     not. Useful to distinguish HDDs (rotational) and SSDs
                     (not rotational).
        :hctl: (String): The SCSI address: Host, channel, target and lun.
                         For example: '1:0:0:0'.
        :by_path: (String): The alternative device name,
                  e.g. /dev/disk/by-path/pci-0000:00


        :raises: ValueError, if some information is invalid.
        :returns: A generator with all matching devices as dictionaries."""
        
        return True

    def erase_root_disks(self, node, ports):
        """ Add logic to wipe out the root disks"""
        return True