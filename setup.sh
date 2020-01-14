#!/bin/bash

git clone https://github.com/neologd/mecab-ipadic-neologd.git
xz -dkv mecab-ipadic-neologd/seed/*.csv.xz
cat mecab-ipadic-neologd/seed/*.csv > neologd.csv

git clone https://github.com/facebookresearch/fastText.git
cd fastText
pip install .

cd -

fastTest/download_model.py en
fastTest/download_model.py ja
