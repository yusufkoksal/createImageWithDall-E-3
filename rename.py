import os

# Specify the directory containing the images
directory = '/Users/yusufkoksal/PycharmProjects/createPhotoWithDall-E-3/images'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Add other file extensions if needed
        # Split the filename into parts
        parts = filename.split('_')
        if len(parts) == 2:
            new_name = f"{parts[1].replace('.jpg', '').replace('.png', '')}_{parts[0]}.jpg" if filename.endswith('.jpg') else f"{parts[1].replace('.jpg', '').replace('.png', '')}_{parts[0]}.png"
            # Construct full file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')
