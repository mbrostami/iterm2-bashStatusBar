#!/bin/bash
set -e
iterm_scripts="$HOME/Library/Application Support/iTerm2/Scripts"
autolaunch="$iterm_scripts/AutoLaunch"
mkdir -p "$autolaunch"
ln -si `pwd`/bash_status_bar.py "$autolaunch/bash_status_bar.py"
