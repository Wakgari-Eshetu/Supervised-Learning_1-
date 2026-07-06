# Everything for configurations of the project will be stored here. This includes paths, hyperparameters, 
# and other configurations that are required for the project.

import os 
base_folder = os.path.dirname(os.path.dirname(__file__))
raw_data_path = os.path.join(base_folder, "data/raw/train.csv")