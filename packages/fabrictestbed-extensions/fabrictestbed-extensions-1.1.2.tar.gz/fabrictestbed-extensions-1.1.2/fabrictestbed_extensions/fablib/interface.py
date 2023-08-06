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


#class Interface(AbcFabLIB):
class Interface():
    def __init__(self, component=None, fim_interface=None):
        """
        Constructor
        :return:
        """
        super().__init__()
        self.fim_interface  = fim_interface
        self.component = component


    def __str__(self):
        if self.get_network():
            network_name = self.get_network().get_name()
        else:
            network_name = None
            
        table = [   [ "Name", self.get_name() ],
                    [ "Network", network_name ],
                    [ "Bandwidth", self.get_bandwidth() ],
                    [ "VLAN", self.get_vlan() ],
                    [ "MAC", self.get_mac() ],
                    [ "Physical OS Interface", self.get_physical_os_interface_name() ],
                    [ "OS Interface", self.get_os_interface() ],
                    ]

        return tabulate(table)


    def get_os_interface(self):
        try:
            os_iface = self.get_physical_os_interface_name()
            vlan = self.get_vlan()

            if vlan != None:
                os_iface = f"{os_iface}.{vlan}"
        except:
            os_iface = None


        return os_iface

    def get_mac(self):
        try:
            os_iface = self.get_physical_os_interface()
            mac = os_iface['mac']
        except:
            mac = None

        return mac


    def get_physical_os_interface(self):


        if self.get_network() == None:
            return None

        network_name = self.get_network().get_name()
        node_name = self.get_node().get_name()

        try:
            return self.get_slice().get_interface_map()[network_name][node_name]
        except:
            return None

    def get_physical_os_interface_name(self):
        if self.get_physical_os_interface():
            return self.get_physical_os_interface()['ifname']
        else:
            return None

    def config_vlan_iface(self):
        if self.get_vlan() != None:
            self.get_node().add_vlan_os_interface(os_iface=self.get_physical_os_interface_name(),
                                                  vlan=self.get_vlan(), interface=self)

    def set_ip(self, ip=None, cidr=None, mtu=None):
        if cidr: cidr=str(cidr)
        if mtu: mtu=str(mtu)

        self.get_node().set_ip_os_interface(os_iface=self.get_physical_os_interface_name(),
                                            vlan=self.get_vlan(),
                                            ip=ip, cidr=cidr, mtu=mtu)


    def ip_addr_add(self, addr, subnet):
        self.get_node().ip_addr_add(addr, subnet, self)


    def ip_addr_del(self, addr, subnet):
        self.get_node().ip_addr_del(addr, subnet, self)

    def ip_link_up(self):
        self.get_node().ip_link_up(self)

    def ip_link_down(self):
        self.get_node().ip_link_down(self)




    def set_vlan(self, vlan=None):
        if vlan: vlan=str(vlan)

        if_labels = self.get_fim_interface().get_property(pname="labels")
        if_labels.vlan = str(vlan)
        self.get_fim_interface().set_properties(labels=if_labels)

    def get_fim_interface(self):
        return self.fim_interface

    def get_bandwidth(self):
        return self.get_fim_interface().capacities.bw

    def get_vlan(self):
        try:
            vlan = self.get_fim_interface().get_property(pname="labels").vlan
        except:
            vlan = None
        return vlan

    def get_reservation_id(self):
        try:
            #TODO THIS DOESNT WORK.
            #print(f"{self.get_fim_interface()}")
            return self.get_fim_interface().get_property(pname='reservation_info').reservation_id
        except:
            return None

    def get_reservation_state(self):
        try:
            return self.get_fim_interface().get_property(pname='reservation_info').reservation_state
        except:
            return None

    def get_error_message(self):
        try:
            return self.get_fim_interface().get_property(pname='reservation_info').error_message
        except:
            return ""


    def get_name(self):
        return self.get_fim_interface().name

    def get_component(self):
        return self.component

    def get_model(self):
        return self.get_component().get_model()

    def get_site(self):
        return self.get_component().get_site()

    def get_slice(self):
        return self.get_node().get_slice()

    def get_node(self):
        return self.get_component().get_node()

    def get_network(self):
        if hasattr(self, 'network'):
            #print(f"hasattr(self, 'network'): {hasattr(self, 'network')}, {self.network.get_name()}")
            return self.network
        else:
            for net in self.get_slice().get_networks():
                if net.has_interface(self):
                    self.network = net
                    #print(f"return found network, {self.network.get_name()}")
                    return self.network

        #print(f"hasattr(self, 'network'): {hasattr(self, 'network')}, None")
        return None
