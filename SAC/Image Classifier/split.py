import os
import shutil
import random

def split_data(source_dir, train_dir, val_dir, split_ratio=0.8):
    # Create directories if they don't exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    
    # Iterate over each category in the source directory
    for category in os.listdir(source_dir):
        category_dir = os.path.join(source_dir, category)
        
        if not os.path.isdir(category_dir):
            continue
        
        # Create category subdirectories in train and validation directories
        os.makedirs(os.path.join(train_dir, category), exist_ok=True)
        os.makedirs(os.path.join(val_dir, category), exist_ok=True)
        
        # Get all file names in the category directory
        files = os.listdir(category_dir)
        random.shuffle(files)
        
        # Split files into training and validation sets
        split_index = int(len(files) * split_ratio)
        train_files = files[:split_index]
        val_files = files[split_index:]
        
        # Copy files to respective directories
        for file in train_files:
            shutil.copy(os.path.join(category_dir, file), os.path.join(train_dir, category, file))
        
        for file in val_files:
            shutil.copy(os.path.join(category_dir, file), os.path.join(val_dir, category, file))

# Define source, train, and validation directories
source_dir = 'C:\\Users\\Dinak\\Desktop\\SEM_5\\SAC\\Image Classifier\\dataset'
train_dir = 'C:\\Users\\Dinak\\Desktop\\SEM_5\\SAC\\Image Classifier\\data\\train'
val_dir = 'C:\\Users\\Dinak\\Desktop\\SEM_5\\SAC\\Image Classifier\\data\\validation'

# Split the data
split_data(source_dir, train_dir, val_dir)
