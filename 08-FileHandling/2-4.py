employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

job_title = 'Software Engineer'

with open(employees_file, 'r') as input_file:
    with open(position_file, 'w') as output_file:
        header = next(input_file)
        output_file.write(header)
        for line in input_file:
            if job_title in line:
                output_file.write(line)