import biondi
import openslide
import numpy as np
import re
import tensorflow.keras as keras
from tensorflow.keras import layers, models, losses, Model, Input

import pickle
import tensorflow as tf

class TrainingGenerator(keras.utils.Sequence):
    def __init__(self,
                 data,
                 batch_size,
                 labels=None,
                 normalize=True,
                 per_channel=False,
                 two_channel=False,
                 retinanet=False,
                 validation=False,
                 augmentation=False,
                 flip=False,
                 rotation=False,
                 rand_brightness=False,
                 rand_contrast=False,
                 simultaneous_aug=False,
                 b_delta=0.95,
                 c_factor_min=0.1,
                 c_factor_max=0.9, ):
        self.retinanet = retinanet
        self.batch_size = batch_size
        self.normalize = normalize
        self.per_channel = per_channel
        self.two_channel = two_channel
        self.validation = validation
        self.augmentation = augmentation
        self.flip = flip
        self.rotation = rotation
        self.rand_brightness = rand_brightness
        self.rand_contrast = rand_contrast
        self.simultaneous_aug = simultaneous_aug
        self.b_delta = b_delta
        self.c_factor_min = c_factor_min
        self.c_factor_max = c_factor_max
        if type(data) is str:
            if '.pickle' in data:
                with open(data, 'rb') as handle:
                    self.data = pickle.load(handle)
            elif '.npy' in data:
                self.data = np.expand_dims(np.load(data), axis=1)
            else:
                print('Warning: Filetype is not recognized. Only ".pickle" and ".npy" filetypes are supported.')
                return
        else:
            if self.retinanet:
                self.data = data
            else:
                self.data = np.expand_dims(data, axis=1)
        if self.retinanet:
            self.sample_number = len(self.data['dat'])
            self.keys = self.data.keys()
        else:
            self.sample_number = len(self.data)
            if labels is not None:
                if type(labels) is str:
                    self.labels = np.load(labels)
                else:
                    self.labels = labels
            else:
                print('Warning: Must provide labels!')
                return
        if self.two_channel:
            self.c_idx_start = 1
        else:
            self.c_idx_start = 0
        self.on_epoch_end()

    def __len__(self):
        return int(np.ceil(self.sample_number / self.batch_size))

    def __getitem__(self, index):
        batch_idx = self.indexes[index * self.batch_size:(index + 1) * self.batch_size]
        if self.retinanet:
            x_batch = {}
            y_batch = {}
            for key in self.keys:
                if 'dat' in key:
                    if self.rand_contrast and self.rand_brightness:
                        if self.simultaneous_aug:
                            x_batch[key] = biondi.dataset.random_adjust_brightness(
                                self.data[key][batch_idx, ..., self.c_idx_start:],
                                b_delta=self.b_delta,
                                batch_size=len(batch_idx)
                            )
                            x_batch[key] = biondi.dataset.random_adjust_contrast(
                                x_batch[key],
                                c_factor_min=self.c_factor_min,
                                c_factor_max=self.c_factor_max,
                                batch_size=len(batch_idx)
                            )
                        else:
                            rand_bools = np.random.choice([False, True], size=self.batch_size)
                            x_batch[key] = self.data[key][batch_idx, ..., self.c_idx_start:].astype('float32')
                            for i, j in enumerate(rand_bools):
                                if j:
                                    x_batch[key][i:i + 1] = biondi.dataset.random_adjust_contrast(
                                        x_batch[key][i:i + 1],
                                        c_factor_min=self.c_factor_min,
                                        c_factor_max=self.c_factor_max,
                                        batch_size=1
                                    )
                                else:
                                    x_batch[key][i:i + 1] = biondi.dataset.random_adjust_brightness(
                                        x_batch[key][i:i + 1],
                                        b_delta=self.b_delta,
                                        batch_size=1
                                    )
                    elif self.rand_brightness:
                        x_batch[key] = biondi.dataset.random_adjust_brightness(
                            self.data[key][batch_idx, ..., self.c_idx_start:],
                            b_delta=self.b_delta,
                            batch_size=len(batch_idx)
                        )
                    elif self.rand_contrast:
                        x_batch[key] = biondi.dataset.random_adjust_contrast(
                            self.data[key][batch_idx, ..., self.c_idx_start:],
                            c_factor_min=self.c_factor_min,
                            c_factor_max=self.c_factor_max,
                            batch_size=len(batch_idx)
                        )
                    else:
                        x_batch[key] = self.data[key][batch_idx, ..., self.c_idx_start:]
                    if self.normalize:
                        x_batch[key] = biondi.dataset.per_sample_tile_normalization(x_batch[key], per_channel=self.per_channel)
                elif 'msk' in key:
                    x_batch[key] = self.data[key][batch_idx]
                else:
                    y_batch[key] = self.data[key][batch_idx]
            return x_batch, y_batch
        else:
            if self.rand_contrast and self.rand_brightness:
                if self.simultaneous_aug:
                    x_batch = biondi.dataset.random_adjust_brightness(
                        self.data[batch_idx, ..., self.c_idx_start:],
                        b_delta=self.b_delta,
                        batch_size=len(batch_idx)
                    )
                    x_batch = biondi.dataset.random_adjust_contrast(
                        x_batch,
                        c_factor_min=self.c_factor_min,
                        c_factor_max=self.c_factor_max,
                        batch_size=len(batch_idx)
                    )
                else:
                    rand_bools = np.random.choice([False, True], size=self.batch_size)
                    x_batch = self.data[batch_idx, ..., self.c_idx_start:].astype('float32')
                    for i, j in enumerate(rand_bools):
                        if j:
                            x_batch[i:i + 1] = biondi.dataset.random_adjust_contrast(
                                x_batch[i:i + 1],
                                c_factor_min=self.c_factor_min,
                                c_factor_max=self.c_factor_max,
                                batch_size=1
                            )
                        else:
                            x_batch[i:i + 1] = biondi.dataset.random_adjust_brightness(
                                x_batch[i:i + 1],
                                b_delta=self.b_delta,
                                batch_size=1
                            )
            elif self.rand_brightness:
                x_batch = biondi.dataset.random_adjust_brightness(
                    self.data[batch_idx, ..., self.c_idx_start:],
                    b_delta=self.b_delta,
                    batch_size=len(batch_idx)
                )
            elif self.rand_contrast:
                x_batch = biondi.dataset.random_adjust_contrast(
                    self.data[batch_idx, ..., self.c_idx_start:],
                    c_factor_min=self.c_factor_min,
                    c_factor_max=self.c_factor_max,
                    batch_size=len(batch_idx)
                )
            else:
                x_batch = self.data[batch_idx, ..., self.c_idx_start:]
            if self.normalize:
                x_batch = biondi.dataset.per_sample_tile_normalization(x_batch, per_channel=self.per_channel)
            y_batch = self.labels[batch_idx]
            return x_batch, y_batch

    def on_epoch_end(self):
        if self.validation:
            self.indexes = np.arange(self.sample_number)
        else:
            # not necessary since keras shuffles the index it gives __getitem__()
            # self.indexes = np.random.permutation(self.sample_number)
            self.indexes = np.arange(self.sample_number)