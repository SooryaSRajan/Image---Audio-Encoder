from scipy.io import wavfile
import numpy as np
from PIL import Image
import sys
from datetime import datetime

def load_image(image_path):
    try:
        image = Image.open(image_path)
        
        if image.mode != 'RGB':
            raise ValueError("The image is not in RGB format.")
        
        image_array = np.array(image)
        
        if image_array.dtype != np.uint8:
            raise ValueError("The image is not 8-bit per channel.")
        
        if np.any(image_array < 0) or np.any(image_array > 255):
            raise ValueError("The image contains invalid pixel values outside the 8-bit range (0-255).")
        
        return image_array
    
    except Exception as e:
        raise Exception(f"Failed to load the image: {e}")

def encode_image_with_shape(image_array):
    # Encode the shape as a small integer array (3 integers: height, width, channels)
    shape_data = np.array(image_array.shape, dtype=np.int32)  # 32-bit integers
    
    # Flatten the image array to a 1D array
    flattened_image = image_array.flatten().astype(np.uint8)  # 8-bit values for image data
    
    # Concatenate the shape data with the flattened image data
    encoded_data = np.concatenate([shape_data, flattened_image])
    
    return encoded_data


if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = input("Enter the path to the image file: ")
image_array = load_image(file_name)

# Encode the image with shape data
encoded_data = encode_image_with_shape(image_array)

# Generate a safe filename using current date and time
current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"audio_encoded_image_{current_date}.wav"

# Write the encoded data to a .wav file
wavfile.write(filename, 44100, encoded_data)
print(f"Audio file saved as {filename}")

# /Users/sooryasrajan/Downloads/kanye-reeves.jpg