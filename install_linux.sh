#!/bin/bash

# Check for root user
if [ $(id -u) -ne 0 ]; then
	echo "[!] Must be run as root user" >&2
	exit 1
fi

# Set path to source install directory
SCRIPT_PATH=$(echo $0 | sed s/install_linux.sh$//)
if [ ! $SCRIPT_PATH ]; then
	SCRIPT_PATH="."
else
	SCRIPT_PATH=$(echo $SCRIPT_PATH | sed 's/^\///')
	SCRIPT_PATH=$(echo $SCRIPT_PATH | sed 's/\/$//')
	SCRIPT_PATH="./${SCRIPT_PATH}"
fi

# Check if local binary directory exists in PATH
LOCAL_BIN="/usr/local/bin"
echo $PATH | grep $LOCAL_BIN >/dev/null 2>/dev/null
if [ $? -ne 0 ]; then
	echo "[!] Missing $LOCAL_BIN in PATH environment variable" >&2
	echo "[!] Add the following line to your shell's rc script" >&2
	echo "export PATH=$LOCAL_BIN:$PATH"
fi
rm -f

# Check if local share directory already exists
LOCAL_SHARE="/usr/local/share/hercules"
if [ -d $LOCAL_SHARE ]; then
	echo "[*] Wiping the existing installation"
	rm -rf $LOCAL_SHARE
fi
mkdir -p $LOCAL_SHARE

# Copy installation files to the local share directory
cp -r "$SCRIPT_PATH/threader" $LOCAL_SHARE
cp -r "$SCRIPT_PATH/attack" $LOCAL_SHARE
cp -r "$SCRIPT_PATH/parse" $LOCAL_SHARE

# Adjust main script to contain a shebang
SHEBANG=$(which python3)
echo "#!${SHEBANG}" > "$LOCAL_SHARE/hercules.py"
cat "$SCRIPT_PATH/hercules.py" >> "$LOCAL_SHARE/hercules.py"

# Setup local share permissions
chown -R root:root $LOCAL_SHARE
chmod 755 "$LOCAL_SHARE/hercules.py"

# Create a symlink in the local bin pointing to the local share directory
ln -sf "$LOCAL_SHARE/hercules.py" "$LOCAL_BIN/hercules"

echo "[+] Finished!  Type: 'hercules -h' to test it."

