import time
import re

start_time = time.time()
first_number = 235741
last_number = 706948

#first_number = 111
#last_number = 222

regexes = [
    ".*11.*",
    ".*22.*",
    ".*33.*",
    ".*44.*",
    ".*55.*",
    ".*66.*",
    ".*77.*",
    ".*88.*",
    ".*99.*",
    ]

combined = "(" + ")|(".join(regexes) + ")"
count = 0

for n in range(first_number, last_number + 1):
    list_of_digits = [int(d) for d in str(n)]
    if re.match(combined, str(n)) and list_of_digits == sorted(list_of_digits):
        count += 1
        #print(n)

print(count)
print("--- %s seconds ---" % (time.time() - start_time))