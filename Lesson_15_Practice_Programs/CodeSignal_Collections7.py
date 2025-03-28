# Given mission name
mission_name = "Sort"

# TODO: Print the first and the last character of the mission name
first = mission_name[0]
last = mission_name[-1]
print(first, last)

updated_mission = "P" + mission_name[1:-1] + "k"
print(updated_mission)

# TODO: The mission needs a minor update. We aim to change its first letter to 'P' and the last letter to `k`, obtaining the word "Pork".
# Remember, strings in Python are immutable, so you cannot alter them directly.
first_letter = mission_name.replace('S', 'P')
last_letter = mission_name.replace('t', 'k')

# TODO: Print the updated mission name
print(first_letter + last_letter)


