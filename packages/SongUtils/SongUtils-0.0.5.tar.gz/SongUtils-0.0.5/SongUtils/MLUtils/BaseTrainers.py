import torch
import torch.nn as nn
from torch.optim import SGD
from tensorboardX import SummaryWriter
import os
import os.path as osp
import logging

import sys
sys.path.append('..')
from MetricUtils import AverageMeter, accuracy

class BaseTrainer(object):
    def __init__(self, cfg, model, dataloader_list, metrics_list):
        self.cfg = cfg
        self.device = torch.device(self.cfg.device)
        self.model = model.to(self.device)
        self.optimizer = self.get_optimizer()
        self.train_loader, self.val_loader = dataloader_list
        self.metrics_list = metrics_list
        self.writer = SummaryWriter(self.cfg.summary_path)
        logging.basicConfig(level=eval(f"logging.{self.cfg.log_level}"), format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.loss_func = self.get_loss_func()
    
    def get_optimizer(self):
        if self.cfg.optimizer_type == "sgd":
            return SGD(self.model.parameters(), lr=self.cfg.lr, momentum=0.9, weight_decay=self.cfg.weight_decay)
    
    def get_loss_func(self): return torch.nn.CrossEntropyLoss()
    
    def epoch_forward(self, isTrain, epoch):
        # for metric in self.metrics_list:
        #     exec(f"_{metric} = AverageMeter()")
        _loss = AverageMeter()
        _acc = AverageMeter()

        if isTrain:
            self.model.train()
            loader = self.train_loader
        else:
            self.model.eval()
            loader = self.val_loader
        
        correct = 0
        for epoch_step, data in enumerate(loader):
            image = data[0].to(self.device)
            label = data[1].to(self.device)
            if isTrain:
                self.optimizer.zero_grad()
            output = self.model(image)
            loss = self.loss_func(output, label)
            acc = accuracy(output, label, [1, ])[0]
            if isTrain:
                loss.backward()
                self.optimizer.step()
            
            _loss.update(loss.item())
            _acc.update(acc)
            if (epoch_step + 1) % self.cfg.log_freq == 0:
                self.logger.debug(f"Epoch: {epoch}/{self.cfg.epochs}, Step: {epoch_step}/{len(loader)}")
                for metric in self.metrics_list:
                    self.logger.debug(f"\t {metric}: {eval(f'_{metric}.avg')}")

        metrics_value_list = []
        for metric in self.metrics_list:
            metric_value = eval(f"{'_' + metric}.avg")
            metrics_value_list.append(metric_value)
        metrics_dict = {metric: value for metric, value in zip(self.metrics_list, metrics_value_list)}
        return metrics_dict

    def plot_epoch_metric(self, epoch, train_dict, val_dict):
        for metric in self.metrics_list:
            self.writer.add_scalars(metric, {"train " + metric: train_dict[metric], "val " + metric: val_dict[metric]}, epoch)

    def save_model(self, epoch):
        if not osp.isdir(self.cfg.model_path):
            os.mkdir(self.cfg.model_path)
        state = {'state_dict': self.model.state_dict(), 'optimizer': self.optimizer.state_dict(), 'epoch': epoch}
        torch.save(state, osp.join(self.cfg.model_path, f"model_{epoch}.pth"))
    
    def update_lr(self):
        pass

    def forward(self):
        for epoch in range(self.cfg.epochs):
            self.logger.info("Training:")
            train_metrics_dict = self.epoch_forward(isTrain=True, epoch=epoch)
            with torch.no_grad():
                self.logger.info("Validating:")
                val_metrics_dict = self.epoch_forward(isTrain=False, epoch=epoch)
            self.plot_epoch_metric(epoch, train_metrics_dict, val_metrics_dict)
            self.save_model(epoch)

            





