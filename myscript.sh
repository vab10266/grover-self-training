#!/bin/bash
source grover/bin/activate
echo "Hello World" >> allout.txt 2>&1

tdps="0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.1"
pts="0.8 0.8325 0.875 0.9075 0.95"
yts="0.3 0.5 0.7"
eps="10 20 40"
for tdp in $tdps
do
for pt in $pts
do
for yt in $yts
do
for ep in $eps
do

python main.py finetune --data_path exampledata/finetune/bbbp.csv \
	--features_path exampledata/finetune/bbbp.npz \
	--save_dir model/finetune/bbbp/ \
	--self_train_data True \
	--self_train False \
	--checkpoint_path grover_base.pt \
	--dataset_type classification \
	--split_type random \
	--split_sizes $tdp 0.1 0.1  \
	--ensemble_size 1 \
	--num_folds 5 \
	--no_features_scaling \
	--ffn_hidden_size 200 \
	--batch_size 32 \
	--epochs $ep \
	--init_lr 0.00015 \
	--pseudo_thresh $pt \
	--y_thresh $yt >> allout.txt 2>&1

echo "^^^Vaud's Results^^^" >> allout.txt 2>&1
echo "TP, Epochs, PT, YT:" $tdp $ep $pt $yt >> allout.txt 2>&1
echo "--------------------" >> allout.txt 2>&1

done
done
done
done

echo "All Done"