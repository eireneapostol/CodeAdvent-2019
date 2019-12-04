import time
import re

start_time = time.time()
first_number = 235741
last_number = 706948

#first_number = 11222
#last_number = 11333

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

count = 0
multiple_occ = True
number_in_order = False
for n in range(first_number, last_number + 1):
    list_of_digits = [int(d) for d in str(n)]
    for regex in regexes:
        number_in_order = False
        if re.match(regex, str(n)) and list_of_digits == sorted(list_of_digits):
            number_in_order = True
            for occ in range(3,7):
                regex_with_multiple_digits = ".*" + str(regex[2]) + "{" + str(occ) + "}"
                if re.match(regex_with_multiple_digits, str(n)):
                    multiple_occ = True
                    number_in_order = False
                else:
                    multiple_occ = False
                    break
        if (not multiple_occ) and number_in_order:
            count += 1
            break

print("count is ", count)

print("--- %s seconds ---" % (time.time() - start_time))
