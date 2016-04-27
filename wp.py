#!/usr/bin/env python

import os
def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)
 


def get_current_wp():
    # gets the most current stimonstalenhag drawing as a local file. add to cron, or window manager startup script etc...

    simonspage = "http://simonstalenhag.se/"
    local_wp_file = "simonstalenhag_wallpaper.jpg"
    import os.path
    import datetime
    import email.utils as eut


    current_timestamp = datetime.datetime.today()
    print "now time: %s"%current_timestamp

    last_modified_local = datetime.datetime(01,01,01,01,01,01)
    if os.path.isfile(local_wp_file):
        # local wp file exists. read its modified date!
        last_modified_local = datetime.datetime.fromtimestamp(os.path.getmtime(local_wp_file))

    print "loc file: %s"%last_modified_local

    if current_timestamp -  last_modified_local < datetime.timedelta(hours=1):
        # local file is at least 24h old
        print "Old image is still quite up-to-date. Try again later..."
        return


    import urllib2
    req = urllib2.Request(simonspage)
    f = urllib2.urlopen(req)
    last_modified_remote = datetime.datetime(*eut.parsedate(f.headers["last-modified"])[:6])

    print "rem file: %s"%(last_modified_remote)

    remote_filename = ""

    if last_modified_remote.date() > last_modified_local.date(): # remote file is newer.
        print "download check."
        # download the file, search for first link to "bilderbig/" and get that one.

        content = f.read()
        for item in content.split("\""):
            if "bilderbig" in item:
                if not "kartan.jpg" in item:
                    remote_filename = simonspage+item
                    break
        print "remote file: ",remote_filename

        print "download start."
        imagefile = urllib2.urlopen(remote_filename).read()
        local_img = file(local_wp_file,"wb")
        local_img.write(imagefile)
        local_img.close()
        print "download end."
    else:
        print "nothing to do, already up to date :) Touching the local file."
        touch(local_wp_file)
    f.close()
        

def deamon():
    from time import sleep
    while True:
        get_current_wp()
        sleep(60*60)


if __name__ == "__main__":
    import sys
    if len(sys.argv)>1 and sys.argv[1]=="d":
        deamon()
    else:
        get_current_wp()

