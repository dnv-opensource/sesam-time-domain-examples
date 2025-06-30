import sys
import os
import re
#Edit existing LCOM card to point to new SCAL card
def update_lcom_to_point_to_scaling_factor(file_path):
    try:
        with open(file_path, 'r') as f:
            text = f.read()
        lines = text.split('\n')
        new_lines = []
        for line in lines:
            if line.startswith('LCOM'):
                new_line = line[:14] +  '1.0   ' + line[20:]
                new_lines.append(new_line)
            else:
                new_lines.append(line)
            new_text = '\n'.join(new_lines)
            with open(file_path, 'w') as f:
                f.write(new_text)
    except Exception as e:
        print(f"Error: {e}")





def replace_last_number(line, new_number):
    # Split the line into parts
    parts = line.split()
    
    # Ensure there are at least four items
    if len(parts) >= 4:
        # Find the start position of the fourth item
        fourth_item_start = line.find(parts[3])
        
        # Replace the fourth item with the new number
        new_line = line[:fourth_item_start] + f"{new_number:<{len(parts[3])}}" + line[fourth_item_start + len(parts[3]):]
        return new_line
    else:
        return line









#Append SCAL card with modified factor 
def append_or_replace_scaling_factor(file_path, scaling_factor):
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Check if the line already exists
        line_exists = False
        for i, line in enumerate(lines):
            if line.startswith("SCAL"):
                lines[i] = replace_last_number(line, scaling_factor)
                line_exists = True
                break

        # If the line does not exist, append it
        if not line_exists:
            text_to_append = f"SCAL    1.           24.       {scaling_factor}"
            lines.append(f"{text_to_append}  \n")

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)

        print(f"Scaling factor {scaling_factor} processed in {file_path} successfully.")
    except Exception as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    
    print(f"running appendscalingfactor.py in folder {os.getcwd()}")
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <scaling factor>")
        sys.exit(1)

    file_path = sys.argv[1]
    scaling_factor = sys.argv[2]
    
    #scaling_factor = 0.65#sys.argv[2]
    #file_path = "STR_TotalS1.FEM"
    update_lcom_to_point_to_scaling_factor(file_path)
    append_or_replace_scaling_factor(file_path, scaling_factor)
    