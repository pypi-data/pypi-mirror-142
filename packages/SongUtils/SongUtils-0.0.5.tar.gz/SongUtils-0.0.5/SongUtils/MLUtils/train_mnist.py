import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
import sys
import argparse
from BaseTrainers import BaseTrainer
from BaseArgs import YamlParams, get_basic_parser

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


def get_args():
    parser = get_basic_parser()
    parser.add_argument("--dataset-name", type=str, default="mnist")
    cfg = parser.parse_args()
    return cfg

def main(cfg):
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST('../data', train=True, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))
                       ])),
        batch_size=cfg.batchSize, shuffle=True)
    val_loader = torch.utils.data.DataLoader(
        datasets.MNIST('../data', train=False, transform=transforms.Compose([
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))
                       ])),
        batch_size=cfg.batchSize, shuffle=True)
    loader_list = [train_loader, val_loader]
    model = Net()
    mnist_trainer = BaseTrainer(cfg, model, loader_list, metrics_list=['loss', 'acc'])
    mnist_trainer.forward()


if __name__ == "__main__":
    # cfg = YamlParams(sys.argv[1])
    cfg = get_args()
    main(cfg)