#!/bin/bash

echo "Creating /mnt/azure_nfs if it doesn't already exist"
sudo mkdir -p /mnt/azure_nfs
echo "Changing permissions"
sudo chown sandau:sandau /mnt/azure_nfs
echo "Mounting /mnt/azure_nfs"
blobfuse2 mount /mnt/azure_nfs --config-file ./azure_nfs.yaml
echo "Done"
