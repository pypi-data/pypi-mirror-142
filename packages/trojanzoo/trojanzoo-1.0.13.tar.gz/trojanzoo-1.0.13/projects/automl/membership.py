#!/usr/bin/env python3

# python scripts/membership.py --model densenet121_comp --dataset cifar100 --pretrained   # noqa: E501

import trojanvision
from trojanzoo.utils.data import dataset_to_tensor

from sklearn import metrics
from scipy.special import softmax
import argparse
import warnings
import numpy as np

warnings.filterwarnings("ignore")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    trojanvision.environ.add_argument(parser)
    trojanvision.datasets.add_argument(parser)
    trojanvision.models.add_argument(parser)
    kwargs = parser.parse_args().__dict__
    env = trojanvision.environ.create(**kwargs)
    dataset = trojanvision.datasets.create(**kwargs)
    model = trojanvision.models.create(dataset=dataset, **kwargs)

    from art.estimators.classification import PyTorchClassifier  # type: ignore
    classifier = PyTorchClassifier(
        model=model._model,
        loss=model.criterion,
        input_shape=dataset.data_shape,
        nb_classes=model.num_classes,
        clip_values=(0, 1)
    )
    max_iter = 10
    max_eval = 100
    sample_size = 50
    init_size = 50
    init_eval = 25

    x_train, y_train = dataset_to_tensor(dataset.get_dataset('train'))
    x_train, y_train = x_train.numpy(), y_train.numpy()
    t_idx = np.arange(len(x_train))

    x_valid, y_valid = dataset_to_tensor(dataset.get_dataset('valid'))
    x_valid, y_valid = x_valid.numpy(), y_valid.numpy()
    preds = np.amax(softmax(classifier.predict(x_valid), axis=1), axis=1)
    v_idx = np.arange(len(x_valid))[(preds <= 0.99999) & (preds >= 0.999)]

    x_valid = x_valid[v_idx]
    y_valid = y_valid[v_idx]
    v_idx = np.arange(len(x_valid))

    np.random.seed(30)
    np.random.shuffle(t_idx)
    np.random.shuffle(v_idx)
    train_idx = t_idx[:sample_size]
    valid_idx = v_idx[:sample_size]

    x = np.concatenate((x_train[train_idx], x_valid[valid_idx]))
    y = np.concatenate((y_train[train_idx], y_valid[valid_idx]))
    y_truth = np.concatenate(([0] * sample_size, [1] * sample_size))

    from art.attacks.evasion.hop_skip_jump import HopSkipJump  # type: ignore
    hsj = HopSkipJump(classifier=classifier, targeted=False,
                      norm=2, max_iter=max_iter,
                      init_size=init_size, init_eval=init_eval,
                      max_eval=max_eval, verbose=False)
    x_adv = hsj.generate(x=x, y=None)
    distance = np.linalg.norm(
        (x_adv - x).reshape((x.shape[0], -1)), ord=np.inf, axis=1)

    fpr, tpr, _ = metrics.roc_curve(y_truth, distance)
    auc = metrics.auc(fpr, tpr)
    auc = auc if auc >= 0.5 else 1 - auc
    print(f'{model.name:20}    AUC:  {str(auc)}')
