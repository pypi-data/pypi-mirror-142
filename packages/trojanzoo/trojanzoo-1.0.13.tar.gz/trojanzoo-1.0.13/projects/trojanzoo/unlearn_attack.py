#!/usr/bin/env python3

# CUDA_VISIBLE_DEVICES=0 python ./examples/backdoor_unlearn.py --color --verbose 1 --attack badnet --defense neural_cleanse --percent 0.01 --validate_interval 1 --epochs 50 --lr 1e-2

import trojanvision
import argparse
import os

from trojanvision.attacks import BadNet, Unlearn
from trojanvision.defenses import NeuralCleanse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    trojanvision.environ.add_argument(parser)
    trojanvision.datasets.add_argument(parser)
    trojanvision.models.add_argument(parser)
    trojanvision.trainer.add_argument(parser)
    trojanvision.marks.add_argument(parser)
    trojanvision.attacks.add_argument(parser)
    trojanvision.defenses.add_argument(parser)
    args, unknown = parser.parse_known_args()
    kwargs = args.__dict__

    env = trojanvision.environ.create(**kwargs)
    dataset = trojanvision.datasets.create(**kwargs)
    model = trojanvision.models.create(dataset=dataset, **kwargs)
    trainer = trojanvision.trainer.create(dataset=dataset, model=model, **kwargs)
    mark = trojanvision.marks.create(dataset=dataset, **kwargs)
    attack: BadNet = trojanvision.attacks.create(dataset=dataset, model=model, mark=mark, **kwargs)
    defense: NeuralCleanse = trojanvision.defenses.create(dataset=dataset, model=model, attack=attack, **kwargs)

    if env['verbose']:
        trojanvision.summary(env=env, dataset=dataset, model=model, mark=mark, trainer=trainer, attack=attack, defense=defense)

    simple_parser = argparse.ArgumentParser()
    simple_parser.add_argument('--mark_source', default='defense')
    simple_parser.add_argument('--unlearn_mode', default='batch')
    args, unknown = simple_parser.parse_known_args()
    mark_source: str = kwargs['mark_source']
    unlearn_mode: str = kwargs['unlearn_mode']

    if mark_source == 'attack':
        mark_source = attack.name
    elif mark_source in ['defense', defense.name]:
        mark_source = defense.name

    if mark_source == attack.name:
        attack.load()
    elif mark_source == f'{attack.name} {defense.name}':
        attack.load()
        defense.load()
    else:
        raise Exception(mark_source)

    atk_unlearn: Unlearn = trojanvision.attacks.create(mark=mark, target_class=attack.target_class, percent=attack.target_class,
                                                       mark_source=mark_source, train_mode=unlearn_mode,
                                                       dataset=dataset, model=model, attack_name='unlearn')

    # ------------------------------------------------------------------------ #
    atk_unlearn.attack(**trainer)
    atk_unlearn.save()
    attack.mark.load_mark(os.path.join(attack.folder_path, attack.get_filename() + '.npy'),
                          already_processed=True)
    attack.validate_fn()
