import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'csv/SMS_statistics_2024-03-11.csv')

with open(file_path, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines[1:]):  # Skip the first line if it's a header
        parsed = line.strip().split(',')
        name = parsed[0].split(' ')
        filtered_name = list(filter(None, name))
        if filtered_name[-1] == "Call":
            filtered_name[-1]="Unknown"
        if len(filtered_name) >= 3:

            filtered_name = [filtered_name[0], filtered_name[-1]]
        lines[i+1] = ','.join(filtered_name[::-1]+parsed[1:])+'\n'


file_path = os.path.join(script_dir, 'csv/customer_list_edited_1-1-23_to_10-1-23.csv')
with open(file_path, 'w') as file:
    file.writelines(lines)
print('Done')