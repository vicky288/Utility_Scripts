# Command line arg: name of the file containing the SHAs
# Creates file called "output_shas.txt" in current directory

from sys import argv

class SHA_DuplicateRemover:
  # Constructor
  def __init__(self):
    self.get_input_file()
    self.store_input_list()
    self.write_output()
  
  def get_input_file(self):
    # Make sure we have the input file
    if (len(argv) < 2):
      print("ERR: Please add name of input file as cmd line arg")
      exit()
      
    # Otherwise, set the input file
    self.input_file = argv[1]
    
  def store_input_list(self):
    # Read in the SHAs
    input_file = open(self.input_file, "r")
    self.SHAs = input_file.readlines()
    input_file.close()
    
    # Remove duplicates
    self.SHAs = list(dict.fromkeys(self.SHAs))
    
  def write_output(self):
    # Write the sorted SHA list to file
    output_file = open("output.txt", "w")
    output_file.writelines(self.SHAs)
    output_file.close()

# Main
if __name__ == "__main__":
  duplicate_remover = SHA_DuplicateRemover()
