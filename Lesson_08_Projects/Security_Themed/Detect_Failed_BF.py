# Task: Detect if more than 5 failed logins occur within 1 minute and output suspicious usernames

# Import built-in modules because treat log file as a dictionary and parse it
from collections import defaultdict
from datetime import datetime

def detect_bruteforce(log_file):
    # Create data structure to store failed timestamps per user
    user_failures = defaultdict(list)
   
    # Read log file
    with open (log_file, 'r') as file:
         # Step 1: Parse logs
         for line in file:
              timestamp, user, status, ip = line.strip().split(",")

              if status == "FAIL":
                   # converts timestamp string into a datetime object
                   time_obj = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                   # store failure timestamp
                   user_failures[user].append(time_obj)
    # result list    
    suspicious_users = []
    
    # Detection Logic - iterate through each user
    for user, times in user_failures.items():
            times.sort()
            # Sliding window detection - check groups of 6 failed logins
            for i in range(len(times) - 5):
                 # calculate time difference
                 diff = (times[i+5] - times[i]).seconds

                 if diff <= 60:
                     # add suspicious user
                     suspicious_users.append(user)
                     break

    return suspicious_users

log_file = '/Users/mirzamansooralibaig/Desktop/Python_Development/Lesson_08_Projects/Security_Themed/BF.syslog'
print(detect_bruteforce(log_file))



