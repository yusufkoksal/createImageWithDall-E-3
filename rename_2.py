import os


def rename_images(folder_path, starting_number):
    # Get a list of files in the specified folder
    files = os.listdir(folder_path)
    # Filter out only image files (assuming they have extensions like .jpg, .png, etc.)
    image_files = [file for file in files if file.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif', 'tiff'))]

    # Initialize the counter
    counter = starting_number

    # Iterate over each image file
    for image_file in image_files:
        # Construct the new file name
        new_file_name = f"{counter}_true_359876644704{os.path.splitext(image_file)[1]}"
        # Construct the full file paths
        old_file_path = os.path.join(folder_path, image_file)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)

        # Increment the counter
        counter += 1

    print(f"Renamed {len(image_files)} images successfully.")


# Specify the folder path and starting number
folder_path = '/Users/yusufkoksal/Desktop/ramsey_fotolar_part_2'
starting_number = 1051

# Call the function to rename images
rename_images(folder_path, starting_number)
