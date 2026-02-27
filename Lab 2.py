#Step 1
# We use int() because the input comes in as text (string)
total_minutes = int(input("Enter the total number of minutes: "))

#Step 2
# // is the floor division operator (gives whole hours)
hours = total_minutes // 60

# % is the modulo operator (gives the remainder minutes)
remaining_minutes = total_minutes % 60

#Step 3 Print the result
print("Result:", hours, "hour(s) and", remaining_minutes, "minute(s).")