import os
from PIL import Image

# Input and output folders
input_folder = "images"        # Folder containing original images
output_folder = "resized_images"  # Folder to save resized images

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Desired size (width, height)
new_size = (400, 400)

# Loop through all files in input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        
        # Open image
        with Image.open(img_path) as img:
            # Resize image
            resized_img = img.resize(new_size)
            
            # Save to output folder
            save_path = os.path.join(output_folder, filename)
            resized_img.save(save_path)

        print(f"Resized and saved: {filename}")

print("✅ All images have been resized and saved in 'resized_images' folder.")
