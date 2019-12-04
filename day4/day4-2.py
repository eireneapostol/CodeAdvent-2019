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
for n in range(first_number, last_number + 1):
    list_of_digits = [int(d) for d in str(n)]
    if list_of_digits == sorted(list_of_digits):
        for regex in regexes:
            multiple_occ = True
            if re.match(regex, str(n)):
                for occ in range(3,7):
                    regex_with_multiple_digits = ".*" + str(regex[2]) + "{" + str(occ) + "}"
                    if re.match(regex_with_multiple_digits, str(n)):
                        multiple_occ = True
                        break
                    else:
                        multiple_occ = False
                        break
            if not multiple_occ:
                count += 1
                break

print("count is ", count)

print("--- %s seconds ---" % (time.time() - start_time))
