# import necessary packages
from azureml.core import Workspace, Dataset, Run
import os, tempfile, tarfile, yaml

import wandb
wandb.login(key="38bb5db0c42adac1ad00fc1c5cec7b7dd12ef2bb")

import numpy as np

# Make a temporary directory and mount image dataset
# print("Create temporary directory...")
# mounted_path = './tmp'
# print('Temporary directory made at' + mounted_path)


# Get the molecule dataset from the current workspace, and download it
# print("Fetching dataset")
ws = Run.get_context().experiment.workspace
dataset = Dataset.get_by_name(ws, name='LLZO_la3d_Al20_outcar')
dataset.download(target_path='.', overwrite=False)
# dataset.download(mounted_path,overwrite=True)
# print("Check that the tar file is there:")
# print(os.listdir(mounted_path))
# print("images dataset download done")


# untar all files under this directory, 
# for file in os.listdir(mounted_path):
#     if file.endswith('.tar'):
#         print(f"Found tar file: {file}")
#         tar = tarfile.open(os.path.join(mounted_path, file))
#         tar.extractall()
#         tar.close()

# print("")
# print("Content of the train_images folder:")
# train_images_folder = os.path.join(".","data_train_images")
# print(os.listdir(train_images_folder))



# this is needed for container
os.system("apt-get update && apt-get install -y python3-opencv")


print("Current Directory:")
print(os.getcwd())
print()

print("Cloning nequip")
os.system('git clone https://github.com/william860925/nequip.git')
print("Check content of '.' folder:")
print(os.listdir('.'))

# Let's check that pytorch recognizes the GPU
import torch
print(f"nequip enviroment setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")




# Let's copy the yaml file to the "./outputs" folder we well so we can find it in the logs of the experiment once it's complete
# os.system('cp ./molecule_detection_yolov5.yaml ./outputs/molecule_detection_yolov5.yaml')

os.system('rm -rf ./results')
os.system('nequip-train nequip/configs/LLZO_la3d_Al20_2500.yaml')
os.system('cp -r ./results ./outputs')

