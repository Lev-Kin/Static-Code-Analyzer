def check_line_length(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for idx, line in enumerate(lines, start=1):
        line = line.rstrip('\n')
        if len(line) > 79:
            print(f"Line {idx}: S001 Too long")


file_path = input()

check_line_length(file_path)
