import torch

# 检查是否有可用的 CUDA 设备
if torch.cuda.is_available():
    # 获取第一个可用的 CUDA 设备
    device = torch.device("cuda:0")

    # 获取 CUDA 设备的一些基本信息
    print("CUDA Device Name:", torch.cuda.get_device_name(device))
    print("CUDA Device Capability:", torch.cuda.get_device_capability(device))

    # CUDA 设备的能力值可以用来确定支持的精度
    major, minor = torch.cuda.get_device_capability(device)

    # 根据 CUDA 设备的能力值判断支持的精度
    if major >= 5:
        print("Supports half precision (FP16)")
    if major >= 7:
        print("Supports tensor cores (TF32)")
    if major >= 7:
        print("Supports mixed precision (FP16 + FP32)")
    if major >= 7:
        print("Supports full precision (FP32)")
    if major >= 7:
        print("Supports double precision (FP64)")
else:
    print("No CUDA-capable device found.")
