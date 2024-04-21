import os

def fix_newline_in_filenames(folder_path):
    # List all files in the directory
    for filename in os.listdir(folder_path):
        # Construct full file path
        old_file_path = os.path.join(folder_path, filename)
        # Check if it's a file and not a directory
        if os.path.isfile(old_file_path):
            # Correct filename by replacing '\n.txt' with '.txt'
            if filename.endswith('\n.txt'):
                # Remove the newline character and prepare the correct filename
                new_filename = filename.replace('\n', '').strip()
                new_file_path = os.path.join(folder_path, new_filename)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Corrected '{old_file_path}' to '{new_file_path}'")

# Example usage:
folder_path = 'results/meta-llama/Llama-3-8b-chat-hf'  # Replace with your folder path
fix_newline_in_filenames(folder_path)