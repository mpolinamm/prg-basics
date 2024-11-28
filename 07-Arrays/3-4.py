meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

def day_meal_plan(meal_plan, day_number):
   meals = meal_plan[day_number]
   return ", ".join(meals)

for i in range(len(meal_plan)):
   day_name = weekday(i + 1)  
   meals = day_meal_plan(meal_plan, i)
   print(f"{day_name}: {meals}")