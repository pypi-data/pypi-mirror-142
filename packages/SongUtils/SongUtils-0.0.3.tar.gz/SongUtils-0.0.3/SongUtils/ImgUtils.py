import torch
import torchvision.transforms as transforms
import numpy as np
from PIL import Image
import cv2
import os
import os.path as osp

def readSingleImagePIL(image_path, rgb=False):
    img = Image.open(image_path)
    if rgb:
        return img.convert("RGB") 
    else:
        return img

def readSingleImageCV2(image_path):
    img = cv2.imread(image_path)
    img = img[:, :, ::-1]
    img = img.transpose(2, 0, 1)
    print(img.shape)
    return img

def readTensorImage(image_path, expand=False, through='pil'):
    if through == 'pil':
        img = readSingleImagePIL(image_path)
        img_tensor = pil2tensor(img)
    elif through == 'opencv':
        arr = readSingleImageCV2(image_path)
        img_tensor = np2tensor(arr.copy())
    else:
        raise KeyError

    if expand:
        return img_tensor.unsqueeze(dim=0)
    else:
        return img_tensor

def readBatchImages(images_dir, rgb=False):
    images_list = os.listdir(images_dir)
    for image_name in imaegs_list:
        image_path = osp.join(images_dir, image_name)
    # TODO

def np2tensor(arr):
    arr = arr.astype(np.float32) / 255.
    img_tensor = torch.from_numpy(arr)
    return img_tensor

def tensor2np(img_tensor):
    arr = img_tensor.numpy()
    return arr

def pil2tensor(img, transforms=None):
    if transforms is not None:
        img_tensor = transforms(img)
    img_tensor = transforms.functional.to_tensor(img)
    return img_tensor

def tensor2pil(img_tesnor):
    img = transforms.functional.to_pil_image(img_tensor)
    return img

def getTransforms(crop=None, resize=None):
    t = []
    if crop is not None:
        t.append(transforms.Crop(crop))
    if resize is not None:
        t.append(transforms.Resize(resize))

    return transforms.Compose(t)

if __name__ == "__main__":
    pass
