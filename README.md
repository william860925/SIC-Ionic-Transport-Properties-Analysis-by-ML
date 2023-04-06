## Project Objective

In this study, we focus on the ionic transport mechanism properties of Superionic Conductors (SICs), which exhibit highly concerted migration compared to the classical diffusion model. Ab initio molecular dynamics (AIMD) has been the conventional method to study diffusion mechanisms in SIC materials, but it is computationally expensive and only applicable to small systems. To address this issue, we employ E(3)-equivariant GNN　machine learning techniques, including NequIP and Allegro, to develop an accurate model with a minimal dataset. Our model has achieved high accuracy in predicting the ionic transport behavior of LLZO, a commonly used SIC material. We also compared the results of our machine learning models with those obtained from DeepMD, which is an E(3)-invariant machine learning method, and found that our models can achieve comparable accuracy while requiring significantly fewer computational resources. This work demonstrates the potential of the new E(3)-equivariant GNN machine learning techniques in addressing the computational challenges in the study of SIC materials and also other materials which need complex simulations.

## Guide of this directory
1. Most of the functions we used in training process are in the training folder.
2. The model folder contains the models we trained.
3. The examples folder includes the jupyter notebooks of diffusivity calculation and model evaluation.

## Result comparison with DeepMD:

<img src=https://github.com/william860925/SIC-Ionic-Transport-Properties-Analysis-by-ML/blob/main/doc/comparison_figure.png width=300 p align="center">

As shown in the figure above, by utilizing E(3)-equivariant graph neural network (GNN) machine learning techniques (NequIP), we were able to achieve higher accuracy with less data compared to DeepMD. Specifically, NequIP employed only 3500 data points for training, while DeepMD required 11000 data points for training.
