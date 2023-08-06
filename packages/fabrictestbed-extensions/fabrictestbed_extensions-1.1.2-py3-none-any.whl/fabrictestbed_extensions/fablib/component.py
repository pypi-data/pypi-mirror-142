#!/usr/bin/env python3
# MIT License
#
# Copyright (c) 2020 FABRIC Testbed
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Paul Ruth (pruth@renci.org)

import os
import traceback
import re

import functools
import time
import logging
from tabulate import tabulate


import importlib.resources as pkg_resources
from typing import List

from fabrictestbed.slice_editor import Labels, ExperimentTopology, Capacities, CapacityHints, ComponentType, ComponentModelType, ServiceType, ComponentCatalog
from fabrictestbed.slice_editor import (
    ExperimentTopology,
    Capacities
)
from fabrictestbed.slice_manager import SliceManager, Status, SliceState

#from fabrictestbed_extensions.fabricx.fabricx import FabricX
#from fabrictestbed_extensions.fabricx.slicex import SliceX
#from fabrictestbed_extensions.fabricx.nodex import NodeX
#from .slicex import SliceX
#from .nodex import NodeX
#from .fabricx import FabricX


from ipaddress import ip_address, IPv4Address


#from fim.user import node


#from .abc_fablib import AbcFabLIB

from .. import images


#class Component(AbcFabLIB):
class Component():
    component_model_map = { 'NIC_Basic': ComponentModelType.SharedNIC_ConnectX_6,
                            'NIC_ConnectX_6': ComponentModelType.SmartNIC_ConnectX_6,
                            'NIC_ConnectX_5': ComponentModelType.SmartNIC_ConnectX_5,
                            'NVME_P4510': ComponentModelType.NVME_P4510,
                            'GPU_TeslaT4': ComponentModelType.GPU_Tesla_T4,
                            'GPU_RTX6000': ComponentModelType.GPU_RTX6000
                            }


    def __str__(self):

        table = [   [ "Name", self.get_name() ],
                    [ "Details", self.get_details() ],
                    [ "Disk (G)", self.get_disk() ],
                    [ "Units", self.get_unit() ],
                    [ "PCI Address", self.get_pci_addr() ],
                    [ "Model", self.get_model() ],
                    [ "Type", self.get_type() ],
                    ]

        return tabulate(table)


    def list_interfaces(self):



        table = []
        for iface in self.get_interfaces():

            if iface.get_network():
                network_name = iface.get_network().get_name()

            table.append( [     iface.get_name(),
                                network_name,
                                iface.get_bandwidth(),
                                iface.get_vlan(),
                                iface.get_mac(),
                                iface.get_physical_os_interface_name(),
                                iface.get_os_interface(),
                                ] )

        return tabulate(table, headers=["Name", "Network", "Bandwidth", "VLAN", "MAC", "Physical OS Interface", "OS Interface" ])



    @staticmethod
    def calculate_name(node=None, name=None):
        #Hack to make it possile to find interfaces
        return f"{node.get_name()}-{name}"

    @staticmethod
    def new_component(node=None, model=None, name=None):
        #Hack to make it possile to find interfaces
        name = Component.calculate_name(node=node, name=name)

        return Component(node = node, fim_component = node.fim_node.add_component(model_type=Component.component_model_map[model], name=name))
        #return Component(node = node, model=model, name=name)

    def __init__(self, node=None, fim_component=None):
        """
        Constructor
        :return:
        """
        super().__init__()
        self.fim_component = fim_component
        self.node = node

    def get_interfaces(self):
        from fabrictestbed_extensions.fablib.interface import Interface

        ifaces = []
        for fim_interface in self.get_fim_component().interface_list:
            ifaces.append(Interface(component=self, fim_interface=fim_interface))

        return ifaces

    def get_fim_component(self):
        return self.fim_component

    def get_slice(self):
        return self.node.get_slice()

    def get_node(self):
        return self.node

    def get_site(self):
        return self.node.get_site()

    def get_name(self):
        return self.get_fim_component().name

    def get_details(self):
        return self.get_fim_component().details

    def get_disk(self):
        return self.get_fim_component().get_property(pname='capacity_allocations').disk

    def get_unit(self):
        return self.get_fim_component().get_property(pname='capacity_allocations').unit

    def get_pci_addr(self):
        return self.get_fim_component().get_property(pname='label_allocations').bdf

    def get_model(self):
        #TODO: This a hack that need a real fix
        if str(self.get_type()) == "SmartNIC" and str(self.get_fim_model()) == "ConnectX-6":
            return 'NIC_ConnectX_6'
        elif str(self.get_type()) == "SmartNIC" and str(self.get_fim_model()) == "ConnectX-5":
            return 'NIC_ConnectX_5'
        elif str(self.get_type()) == "NVME"  and str(self.get_fim_model()) == "P4510":
            return 'NVME_P4510'
        elif str(self.get_type())== "GPU"  and str(self.get_fim_model()) == "Tesla T4":
            return 'GPU_TeslaT4'
        elif str(self.get_type()) == "GPU"  and str(self.get_fim_model()) == "RTX6000":
            return 'GPU_RTX6000'
        elif str(self.get_type()) == "SharedNIC"  and str(self.get_fim_model()) == "ConnectX-6":
            return 'NIC_Basic'
        else:
            return None
          
    def get_reservation_id(self):
        try:
            #This does not work
            #print(f"{self.get_fim_component()}")
            return self.get_fim_component().get_property(pname='reservation_info').reservation_id
        except:
            return None

    def get_reservation_state(self):
        try:
            return self.get_fim_component().get_property(pname='reservation_info').reservation_state
        except:
            return None

    def get_error_message(self):
        try:
            return self.get_fim_component().get_property(pname='reservation_info').error_message
        except:
            return ""

    def get_fim_model(self):
        return self.get_fim_component().model

    def get_type(self):
        return self.get_fim_component().type

    def configure_nvme(self, mount_point='/mnt/nvme_mount'):
        output = []
        try:
            output.append(self.node.execute('sudo fdisk -l /dev/nvme*'))
            output.append(self.node.execute('sudo parted -s /dev/nvme0n1 mklabel gpt'))
            output.append(self.node.execute('sudo parted -s /dev/nvme0n1 print'))
            output.append(self.node.execute('sudo parted -s /dev/nvme0n1 print unit MB print free'))
            output.append(self.node.execute('sudo parted -s --align optimal /dev/nvme0n1 mkpart primary ext4 0% 960197MB'))
            output.append(self.node.execute('lsblk /dev/nvme0n1'))
            output.append(self.node.execute('sudo mkfs.ext4 /dev/nvme0n1p1'))
            output.append(self.node.execute(f'sudo mkdir {mount_point} && sudo mount /dev/nvme0n1p1 {mount_point}'))
            output.append(self.node.execute(f'df -h {mount_point}'))
        except Exception as e:
            print(f"config_nvme Fail: {self.get_name()}")
            #traceback.print_exc()
            raise Exception(str(output))

        return output
