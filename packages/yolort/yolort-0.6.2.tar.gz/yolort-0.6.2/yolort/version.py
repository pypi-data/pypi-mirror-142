__version__ = '0.6.2'
git_version = '1a9083323949541d6e27bca7c63e495cc7ee6777'
from torchvision.extension import _check_cuda_version
if _check_cuda_version() > 0:
    cuda = _check_cuda_version()
