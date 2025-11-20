# Dictionaries: Exercise 4 (Nested Dictionary)

# Program Description: Class Performance

students = {
   'Harris': {
   'Grade': 'A*',
   'Attendance': 90,
   'Behaviour': 'Excellent',
   'Overall': 'Near Perfection',
   },
   'Ahsan': {
   'Grade': 'A',
   'Attendance': 100,
   'Behaviour': 'Good',
   'Overall': 'Very Good',
   },
   'Saad': {
   'Grade': 'C',
   'Attendance': 95,
   'Behaviour': 'Bad',
   'Overall': 'Needs Improvement',
   },
}

for name, performance in students.items():
   print(f"Student: {name}")
   print("Performance:")
   print(f"\tGrade: {performance['Grade']}")
   print(f"\tAttendance: {performance['Attendance']}")
   print(f"\tBehaviour: {performance['Behaviour']}")
   print(f"\tOverall Performance: {performance['Overall']}\n")


