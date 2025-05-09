import os

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
    
    for folder in os.listdir(target_dir):
        folder_path = os.path.join(target_dir, folder)
        
        if os.path.isdir(folder_path) and folder.startswith('Experiment'):
            for file in os.listdir(folder_path):
                if file.startswith(filename_pattern.split('$')[0]) and file.endswith('.pdf'):
                    old_file_path = os.path.join(folder_path, file)
                    new_file_name = pre_append_string + file
                    new_file_path = os.path.join(folder_path, new_file_name)
                    
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {old_file_path} -> {new_file_path}")

def main():
    print("PDF Renamer for Experiment Folders")

    target_dir = input("Enter path to parent directory: ").strip()
    filename_pattern = input("Enter filename pattern to match (e.g., 'Codes $.pdf'): ").strip()
    pre_append_string = input("Enter string to prepend to matching files: ").strip()

    rename_files(target_dir, filename_pattern, pre_append_string)

if __name__ == "__main__":
    main()
