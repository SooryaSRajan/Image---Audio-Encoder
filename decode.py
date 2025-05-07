from scipy.io import wavfile
import numpy as np
from PIL import Image
from datetime import datetime
import sys

# Load the .wav file
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Enter the path to the encoded audio file: ")
sample_rate, data = wavfile.read(filename)

# Display the sample rate and the data
print(f"Sample rate: {sample_rate}")
print(f"Data array shape: {data.shape}")
print(f"Data array:\n{data}")

# Extract the shape data (first 3 values represent height, width, and channels)
shape_data = data[:3]

# Print the extracted shape data
print(f"Extracted shape data: {shape_data}")

height, width, channels = shape_data
print(f"Image dimensions - Height: {height}, Width: {width}, Channels: {channels}")

# Extract the image data (after the first 3 values)
image_data = data[3:]

# Reshape the data into a 3D array (height, width, channels)
image_array = image_data[:height * width * channels].reshape((height, width, channels))

# Ensure the pixel values are within the valid range [0, 255]
image_array = np.clip(image_array, 0, 255).astype(np.uint8)

# Convert the numpy array back to an image using PIL
image = Image.fromarray(image_array)

# Save the image
current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
image.save(f"image_decoded_{current_date}.png")
print("Image saved as 'decoded_image.png'")