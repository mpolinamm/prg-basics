distances_traveled = [120, 150, 180, 90, 200, 175, 160]
sorted_distances_traveled = sorted(distances_traveled)

daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
sorted_daily_temperatures = sorted(daily_temperatures, reverse=True)

file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
   "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
sorted_file_names = sorted(file_names)
print("Original distances traveled:", distances_traveled)
print("Sorted distances traveled:", sorted_distances_traveled)

print("Original daily temperatures:", daily_temperatures)
print("Sorted daily temperatures:", sorted_daily_temperatures)

print("Original file names:", file_names)
print("Sorted file names:", sorted_file_names)