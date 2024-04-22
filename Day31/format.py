import re

# Open the input and output files
input_file_path = 'Day31//swedish_words.txt'
output_file_path = 'Day31//output.txt'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Read each line from the input file
    for line in input_file:
        # Remove digits from the line using regular expression
        text_only = re.sub(r'\d+', '', line)
        # Write the modified line to the output file
        output_file.write(text_only)

print("Digits removed and saved to 'output.txt'.")