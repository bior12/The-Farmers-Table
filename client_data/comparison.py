import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path1 = os.path.join(script_dir, 'csv/SMS_statistics_2024-03-11.csv')
file_path2 = os.path.join(script_dir, 'csv/conglomerate.csv')

sent_names_list = []

with open(file_path1, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines[1:]):
        sent_names_list.append(line.split(',')[1].replace('"', ''))

cong_list: list[tuple[str, str]] = []


with open(file_path2, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines[1:]):
        row = line.split(',')
        cong_list.append([f"{row[1].lower()} {row[0].lower()}", row])


new_cong_list = []

total = 0

previous_emails = []
previous_phone_numbers = []

for name in cong_list:
    print(f"looking at {name[0]}")
    if name[0] in sent_names_list:
        print(name[0])
        total += 1
    else:
        if name[1][2] not in previous_phone_numbers and name[1][3] not in previous_emails:
            previous_phone_numbers.append(name[1][2])
            previous_emails.append(name[1][3])
            new_cong_list.append(name[1])
        else:
            print(f"Duplicate found: {name[0]}")

print(total)
print(new_cong_list)

with open('new_cong_list.csv', 'w') as file:
    file.write('first_name,last_name,phone_number,email\n')
    for name in new_cong_list:
        file.write(','.join(name))