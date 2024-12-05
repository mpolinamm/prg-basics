file_name = 'it_company.csv'

job_title = 'Software Engineer'

with open(file_name, 'r') as file:
   next(file)
   count = 1
   for line in file:
      if job_title in line:
         print (f"{count}. {line.strip()}")
         count += 1