import os
from PIL import Image
import numpy as np

# Define paths
raw_data_paths = {
    'digital_art': 'data/raw/digital_art',
    'met_faces': 'data/raw/met_faces'
}
processed_data_path = 'data/processed'

# Create processed data directory if it doesn't exist
os.makedirs(processed_data_path, exist_ok=True)

# Image processing parameters
target_size = (128, 128)  # Resize images to 128x128
normalization_factor = 255.0  # Normalize pixel values to [0, 1]

def preprocess_image(image_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Resize image
        img = img.resize(target_size)
        # Convert image to numpy array and normalize
        img_array = np.array(img) / normalization_factor
        return img_array

def save_preprocessed_image(image_array, save_path):
    # Convert numpy array back to image
    img = Image.fromarray((image_array * normalization_factor).astype(np.uint8))
    # Save processed image
    img.save(save_path)

def process_and_save_images(data_type):
    raw_data_path = raw_data_paths[data_type]
    processed_data_type_path = os.path.join(processed_data_path, data_type)
    
    # Create subdirectory for processed data type if it doesn't exist
    os.makedirs(processed_data_type_path, exist_ok=True)
    
    # Process each image
    for image_name in os.listdir(raw_data_path):
        image_path = os.path.join(raw_data_path, image_name)
        processed_image_path = os.path.join(processed_data_type_path, image_name)
        
        try:
            # Preprocess image
            processed_image = preprocess_image(image_path)
            # Save processed image
            save_preprocessed_image(processed_image, processed_image_path)
            print(f'Processed and saved: {processed_image_path}')
        except Exception as e:
            print(f'Failed to process {image_path}: {e}')

# Process both datasets
process_and_save_images('digital_art')
process_and_save_images('met_faces')

print("Data preprocessing complete.")
