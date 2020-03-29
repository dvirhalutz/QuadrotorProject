import torch
import argparse


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


""" PARSER """
parser = argparse.ArgumentParser()
parser.add_argument('net_key', type=str, help='the key of the desired net.',
                    choices=key_list)
parser.add_argument('use_ft', type=int,
                    help='use fourier transform on the data.', choices=list(range(2)))
parser.add_argument('-optimizer', type=str, help='what optim to use?',
                    choices=['Adam', 'SGD'], default='Adam')
parser.add_argument('-epochs', type=int,
                    help='ho many epochs to perform', default=1000)
parser.add_argument('-batch', type=int, help='ho many batches', default=4)
parser.add_argument('-lr', type=float, help='learning rate', default=0.00001)
parser.add_argument('-betas', type=float,
                    help='betas for Adam optim', default=(0.9, 0.9999))
parser.add_argument('-momentum', type=float,
                    help='momentum for SGD optim', default=0.9)
