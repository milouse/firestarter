#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# firestarter - easily start different firefox profiles with dmenu

import os
import sys
import shutil
import subprocess
import configparser


default_rofi_command = "rofi -dmenu -location 6 -no-case-sensitive -width 100"


def check_rofi():
    """Check if rofi is available."""
    return bool(shutil.which("rofi"))


def rofi(options, rofi):
    """Call rofi with a list of options."""
    cmd = subprocess.Popen(rofi,
                           shell=True,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout, _ = cmd.communicate("\n".join(options).encode("utf-8"))
    return stdout.decode("utf-8").strip("\n")


def get_profile_names(mozdir="~/.mozilla"):
    """Get all firefox profiles from the profiles.ini file."""
    profile_ini_path = os.path.expanduser(
        os.path.join(mozdir, "firefox/profiles.ini"))
    cfg = configparser.ConfigParser()
    cfg.read(profile_ini_path)
    return [cfg[section]['name']
            for section in cfg.sections()
            if section.startswith('Profile')]


def start_firefox(profile="default", firefox_cmd="firefox"):
    return subprocess.call([firefox_cmd,
                            "-new-instance",
                            "-P", profile])


def main():
    if not check_rofi():
        print("This script requires rofi. Most distributions should have it "
              "packaged.")
        exit(1)
    profiles = get_profile_names()
    profile = rofi(profiles, default_rofi_command)
    if profile == "":
        sys.exit()
    start_firefox(profile)


if __name__ == "__main__":
    main()
