## Installing Serverless Tooling
```
sudo scripts/install_nuctl.sh
```

## Azure NFS YAML Requirements
A standard Azure NFS YAML for use by Sandau will follow a similar template to what's below:

```yaml
allow-other: true

logging:
  type: syslog
  level: log_debug

components:
  - libfuse
  - stream
  - attr_cache
  - azstorage

libfuse:
  attribute-expiration-sec: 120
  entry-expiration-sec: 120
  negative-entry-expiration-sec: 240

stream:
  block-size-mb: 8
  max-buffers: 64
  buffer-size-mb: 36

attr_cache:
  timeout-sec: 7200

azstorage:
  type: adls
  mode: key
  account-name: <AzureStorageAccountToUse>
  container: <ContainerToStoreIn>
  account-key: <StorageAccountKey>
```

![NOTE] Ensure that the Azure Storage Account is configured such that NFS is enabled _and_ networking is set up to allow external connections.

## Set up the CVAT environment & connect to blob storage
Connect to the remote storage, either:

Run this script:
```
./scripts/mount_nfs_drive.sh
```
or
```
sudo mkdir -p /mnt/azure_nfs
sudo chown sandau:sandau /mnt/azure_nfs

# Alter the location to the config file depending on your environment
blobfuse2 mount /mnt/azure_nfs --config-file azure_nfs.yaml
```

Once mounted successfully, start the CVAT containers by running:
```
# If using automated annotation tooling
make run-serverless

# Otherwise
make run
```

If deploying YOLO, ensure that the model weights are first copied to `serverless/pytorch/yolov8/nuclio`. Update [./serverless/pytorch/ultralytics/yolov8/nuclio/main.py](./serverless/pytorch/ultralytics/yolov8/nuclio/main.py#L13) with the new weights filename if necessary.

Deploy the auto-annotation tooling by running
```
make deploy-sam
make deploy-yolo
```

![NOTE] If inference is slow (100s of ms), stop all containers, then you may need to run `sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm` to reset the NVIDIA module.

You may also want to access the Nuclio front-end on port 8070 to manage/alter the models that are currently being used. To easily do this, add a `LocalForward` entry to your `.ssh/config` like this:

```
Host asbuilt-cvat
  HostName <instanceIp>
  User sandau
  IdentitiesOnly yes
  IdentityFile <YourKeyPath
  LocalForward 9070 127.0.0.1:8070
```
