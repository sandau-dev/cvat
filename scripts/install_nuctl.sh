#!/bin/bash
echo "Downloading nuctl"
curl -s https://api.github.com/repos/nuclio/nuclio/releases/latest \
			| grep -i "browser_download_url.*nuctl.*$(uname)" \
			| cut -d : -f 2,3 \
			| tr -d \" \
			| wget -O nuctl -qi - && chmod +x nuctl

echo "Installing nuctl"
sudo mv nuctl /usr/local/bin

echo "Installed to /usr/local/bin/nuctl"
