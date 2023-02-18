#!/usr/bin/env bash 

FOLDER=retinaface_training
REPO_URL=git@github.com:desertSniper87/Pytorch_Retinaface.git

git subtree add \
    --prefix \
    $FOLDER \
    $REPO_URL master \
    --squash

