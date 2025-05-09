import os
import argparse

def rename_files(target_dir:str, filename_pattern:str, pre_append_string:str)->None:
    """
    Renames files in the specified directory that match a given pattern.

    Args:
        target_dir (str): The directory containing the folders to search.
        filename_pattern (str): The pattern to match filenames against.
        pre_append_string (str): The string to prepend to matching filenames.
    """
    # Check if the target directory exists
    if not os.path.exists(target_dir):
        print(f"Error: The directory '{target_dir}' does not exist.")
        return
    
    # Loop through each folder in the target directory
    for folder in os.listdir(target_dir):
        folder_path = os.path.join(target_dir, folder)
        
        if os.path.isdir(folder_path) and folder.startswith('Experiment'):
            # Look for the file in the folder that matches the pattern
            for file in os.listdir(folder_path):
                if file.startswith(filename_pattern.split('$')[0]) and file.endswith('.pdf'):
                    old_file_path = os.path.join(folder_path, file)
                    new_file_name = pre_append_string + file  # Prepend the string to the filename
                    new_file_path = os.path.join(folder_path, new_file_name)
                    
                    # Rename the file
                    os.rename(old_file_path, new_file_path)
                    print(f'Renamed: {old_file_path} -> {new_file_path}')

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Rename files in experiment folders.")
    
    # Add arguments for target directory, filename pattern, and prepend string
    parser.add_argument('--target_dir', required=True, type=str, help="Path to the parent directory containing experiment folders.")
    parser.add_argument('--filename_pattern', required=True, type=str, help="Pattern of filenames to detect (e.g., 'Codes $.pdf').")
    parser.add_argument('--pre_append_string', required=True, type=str, help="String to prepend to the filename (e.g., 'ML_').")

    # Parse the arguments
    args = parser.parse_args()

    # Run the renaming function
    rename_files(args.target_dir, args.filename_pattern, args.pre_append_string)

if __name__ == '__main__':
    main()
