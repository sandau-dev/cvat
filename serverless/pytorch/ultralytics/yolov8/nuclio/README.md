## Troubleshooting GPU
If CUDA is, for some reason, unavaiable, but you're able to see stuff in `nvidia-smi`. Try running the following:
```bash
make stop  # Bring down the containers
sudo rmmod nvidia_uvm
sudo modprobe nvidia_uvm
make run-serverless  # Bring back up the containers
```

To verify if PyTorch can see the GPU, open up a Python3 terminal and run:
```python3
import torch
torch.cuda.is_available()
```

If the response is `True`, then you're good to go.

[Reference](https://discuss.pytorch.org/t/userwarning-cuda-initialization-cuda-unknown-error-this-may-be-due-to-an-incorrectly-set-up-environment-e-g-changing-env-variable-cuda-visible-devices-after-program-start-setting-the-available-devices-to-be-zero/129335/5)
