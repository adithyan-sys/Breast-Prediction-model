import os
from skimage.io import imread
from skimage.transform import resize

input_dir = ''
category = ['empty','non-empty']

data = []
labels = []