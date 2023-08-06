# STORCK auto upload

Auto upload script checks every 2 hours if new files were dropped into the directory it is watching on.
Script will upload files into the workspace set during the installation process (based on workspace token).
We can choose to which instance of STORCK we want to coop with by seeting proper host value during installation.

## Requirements

To install script we need to set the following environment variables:

- `STORCK_AUTO_UPLOAD_DIR` - absolute path to directory to watch 
- `STORCK_API_HOST` - STORCK api host
- `STORCK_USER_TOKEN` - STORCK user token
- `STORCK_WORKSPACE_TOKEN` - STORCK workspace token

## Installation

1. clone repository
2. set environment variables listed above
3. run installation script `bash install.sh`

## Check running process

You can check if process was installed properly by running command `crontab -l`.
You should get something similar to:


```
0 */2 * * * /usr/bin/python3 $SCRIPT_DIRECTORY/script.py -a $STORCK_API_HOST -u $STORCK_USER_TOKEN -w $STORCK_WORKSPACE_TOKEN -d $STORCK_AUTO_UPLOAD_DIR >> ~/storck_auto_upload.log 2>&1
```

## Logging

To check what files were uploaded by script or if it is working properly you can check logs file
`~/storck_auto_upload.log`