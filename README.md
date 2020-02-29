# Iterm2 bash status bar component
This component allows you to run bash command in iterm2 status bar

# Installation
Run `./install.sh`  
You can also copy bash_status_bar.py into the AutoLaunch directory under Scripts directory.  
If there is no AutoLaunch directory just create it.  
Relaunch Iterm2  

# Examples
- Get IP Address  
`echo "$(curl ifconfig.co)" | tr -d '[:space:]'`
- Gmail unread messages
![alt text](https://raw.githubusercontent.com/mbrostami/iterm2-bashStatusBar/master/images/gmail.png)
