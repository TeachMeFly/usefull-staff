#!/usr/bin/env python2

BOOKMARKS = "/home/tmf/.gtk-bookmarks"

STATIC_TPL = """
<item label="Home folder">
    <action name="Execute">
        <command>pcmanfm -n ~/</command>
        <startupnotify>
            <enabled>yes</enabled>
        </startupnotify>
    </action>
</item>
<item label="Root folder">
    <action name="Execute">
        <command>pcmanfm -n /</command>
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
        <command>pcmanfm -n %(uri)s </command>
    </action>
</item>
"""

def GetBookmarks(bm_file):
    out = list()
    f = open(bm_file, 'r')
    for place in  f.readlines():
        out.append((place.replace('\n','').split(' ')[1], place.replace('\n','').split(' ')[0]))

    f.close()

    return out

def MakeXML(data):
    print "<openbox_pipe_menu>"
    print STATIC_TPL
    for name, uri in data:
        print ITEM_TPL % {'label': name, 'uri': uri}

    print "</openbox_pipe_menu>"

def Main():
    data = GetBookmarks(BOOKMARKS)
    MakeXML(data)

Main()
