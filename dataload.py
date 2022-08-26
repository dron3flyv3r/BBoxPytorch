import torch

class DataSet(torch.utils.data.Dataset):
    """Some Information about DataSet"""
    def __init__(self, tranform=None, classes=[], dataPath=''):
        super(DataSet, self).__init__()
        self.tran = tranform
        self.classes = classes
        self.path = dataPath

    def __getitem__(self, index):
        return 

    def __len__(self):
        return 