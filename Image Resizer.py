from PIL import Image
import os

def resize_and_convert_image(input_path, output_path):
    with Image.open(input_path) as image:
        image.thumbnail((512, 512))
        
        if image.size != (512, 512):
            left_margin = (image.width - 512) / 2
            top_margin = (image.height - 512) / 2
            right_margin = (image.width + 512) / 2
            bottom_margin = (image.height + 512) / 2

            image = image.crop((left_margin, top_margin, right_margin, bottom_margin))

        image.save(output_path, "PNG")

source_folder = input("Enter folder path with all your images that you want to rezise:\n")
target_folder = input("Enter output path\n")

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        source_path = os.path.join(source_folder, file_name)
        base_name = os.path.splitext(file_name)[0]
        target_file_name = base_name + " edited.png"
        target_path = os.path.join(target_folder, target_file_name)
        resize_and_convert_image(source_path, target_path)
        print(f"Processed {file_name} to {target_file_name}")
