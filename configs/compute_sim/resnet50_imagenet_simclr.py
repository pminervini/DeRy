_base_ = [
    '../_base_/datasets/imagenet_bs64.py',
    '../_base_/default_runtime.py'
]

data = dict(
    samples_per_gpu=128,
    val=dict(ann_file=None),
    test=dict(ann_file=None))

model = dict(
    type='ImageClassifier',
    train_cfg=dict(model_name='resnet50',train_strategy='simclr'),
    backbone=dict(
        type='TIMMBackbone',
        model_name='resnet50',
        checkpoint_path='/Checkpoint/yangxingyi/Pretrained/simclr_resnet50_8xb32-coslr-200e_in1k_20211213-d0e53669.pth'
    ),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        num_classes=1000,
        in_channels=2048,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5),
    ))
