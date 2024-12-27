from os import listdir, getcwd
from os.path import isfile, join, basename
from hashlib import sha256

def hash_file(file_name):
    # Read the file to be hashed
    with open(file_name, "rb") as input_file:
        file_bytes = input_file.read()
        
        # Return the hex string
        return sha256(file_bytes).hexdigest()

def get_files():
    # Get all files in current directory
    directory_files = listdir(getcwd())
    
    # Remove the name of this script so it's not included in the list
    directory_files.remove(basename(__file__))
    
    # Write the input list to a file
    output_file = open("o_file_hashes.txt","w+")
    for file in directory_files:
        # Output the file hash
        output_file.write(hash_file(file) + " - ")
        
        # Now output the name of the file
        output_file.write(file + "\n")
  
  
# Main
if __name__ == "__main__":
    get_files()