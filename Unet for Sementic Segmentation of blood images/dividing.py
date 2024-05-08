import splitfolders

# Define the input and output paths
input_folder = '/home/mdashif/Unet_for_binary/data_blood_images'  # Replace with the actual path to the input folder containing images and masks
output_folder = '/home/mdashif/Unet_for_binary/Dataset/'  # Replace with the desired path for the output folder structure

# Split the input folder into training and validation sets
splitfolders.ratio(input_folder, output=output_folder, seed=1337, ratio=(0.8, 0.2), group_prefix=None)
