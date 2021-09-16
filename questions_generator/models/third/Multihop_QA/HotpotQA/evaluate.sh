#!/bin/bash

set -x

DATAHOME=./data/dev.human.json
MODELHOME=./outputs/unsupervised

export CUDA_VISIBLE_DEVICES=4

python code/run_mrqa.py \
  --do_eval \
  --eval_test \
  --model spanbert-large-cased \
  --test_file ${DATAHOME} \
  --eval_batch_size 32 \
  --max_seq_length 512 \
  --doc_stride 128 \
  --output_dir ${MODELHOME}

