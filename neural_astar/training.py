import torch
import pytorch_lightning as pl

class PlannerModule(pl.LightningModule):
    def __init__(self, model, config):
        super().__init__()
        self.model = model
        self.config = config

    def forward(self, map_designs, start_maps, goal_maps):
        return self.model(map_designs, start_maps, goal_maps)

def load_from_ptl_checkpoint(path):
    return torch.load(path)
