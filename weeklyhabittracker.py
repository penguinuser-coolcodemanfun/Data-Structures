

habit_info = ("coding", True,15,15.5)
print(f"Habit info: {habit_info}")

weekly_habits = (1,1,0,1,1)
print(f"Weekly habits: {weekly_habits}")

tuple_length = len(weekly_habits)
print("Days in the tuple: ", tuple_length)


print("Day 1: ", weekly_habits[1])
print("Day 2: ", weekly_habits[2])
print("Day 3: ", weekly_habits[3])

print("Full range: ", weekly_habits[0:5])
print("3 Days after day 1: ", weekly_habits[0:3])
print("3 Days back after the last day: ", weekly_habits[5:7])

add_tuple = weekly_habits + (0,1)
print(f"Adding new day... {add_tuple}")

completed_days = weekly_habits.count(1)
incomplete_days = weekly_habits.count(0)


print("===== WEEKLY HABIT TRACKER =====")
print("HABIT INFO: ", habit_info)
print("WEEKLY HABITS: ", weekly_habits)
print("COMPLETED DAYS: ", completed_days)
print("INCOMPLETE DAYS: ", incomplete_days)
print("================================")