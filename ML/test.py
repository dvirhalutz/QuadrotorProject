from __future__ import print_function
from __future__ import division
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
import logging
from os import walk


# Models to choose from [resnet, alexnet, vgg, squeezenet, densenet, inception]
model_name = "densenet"

# TODO: Can be ADAM
optimaizer = "SGD"

# batch_size = 10

path_to_model = 'saved_models/' + model_name + '_' + optimaizer + '.pt'

test_data_dir = "./data_set"

train_data_dir = "./train"

"""
path_to_model = the path to the saved weights
test_data_dir = path to directory contains the images for evaluating
                Hirarcy is:
                    ->PreTesting - all the images that the drone took
                    ->InTraining - contains only one image at a time
                    ->Done - all th images after network inference
                    ->resualt.txt - result file with image name and its result
                                    if is_production==False so the right class as well
list_of_classes = list of the classes the model is traind on
logging_path = the path to the logging file
is_production = boolean - if True so wont print to log file the true image class (because we don't know it)
test_image_format = the format of the images the drone is taking
"""


def model_test(path_to_model, test_data_dir="../photos_taken_by_quadrotor/InTraining", list_of_classes=['withHat', 'withOutHat', 'withOutMan'], logging_path="../photos_taken_by_quadrotor/resualt.json", is_production=False, test_image_format="jpeg"):
    image_name_in_testing = ""
    for (_, _, filenames) in walk(test_data_dir):
        if filenames.endswith('.'+test_image_format):
            image_name_in_testing = filenames
            break
    if is_production == False:
        class_name = ""
        for class_name in list_of_classes:
            if class_name in image_name_in_testing:
                image_class_name = class_name
                break

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    log_file = logging_path
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(log_file, '+w')
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)

    logger.info(f'image name:\t{image_name_in_testing}')

    data_transforms = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    # Create test datasets
    test_image_datasets = datasets.ImageFolder(os.path.join(
        test_data_dir, 'test'), data_transforms)

    # Create test dataloader
    dataloaders_dict = torch.utils.data.DataLoader(
        test_image_datasets, shuffle=True)

    """ TEST BEST MODEL """
    net = torch.load(path_to_model).to(device)
    net = net.to(device)
    net.eval()
    # i = 1
    with torch.no_grad():
        for data in dataloaders_dict:
            images, _ = data
            outputs = net(images.to(device))
            for index, _ in enumerate(torch.argmax(outputs, dim=1)):
                logger.info(f'image test result:\t{list_of_classes[index]}')
                if is_production == False:
                    logger.info(f'image right class is:\t{image_class_name}')
