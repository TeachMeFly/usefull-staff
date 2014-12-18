#!/usr/bin/env python2

import os

VB_FOLDER = "/home/tmf/.VirtualBox/"

STATIC_TPL = """
<item label="VirtualBox">
    <action name="Execute">
        <command>VirtualBox</command>
        <startupnotify>
            <enabled>yes</enabled>
        </startupnotify>
    </action>
</item>
<separator />
"""

ITEM_TPL = """
<item label="%(label)s">
    <action name="Execute">
        <command>VBoxManage startvm "%(label)s"</command>
    </action>
</item>
"""

def GetMachines(path):
    out = list()
    for folder in os.listdir(path + "/Machines"):
        out.append(folder)

    return out

def MakeXML(data):
    print "<openbox_pipe_menu>"
    print STATIC_TPL
    for machine in data:
        print ITEM_TPL % {'label': machine}
    print "</openbox_pipe_menu>"

def Main():
    data = GetMachines(VB_FOLDER)
    MakeXML(data)

Main()
