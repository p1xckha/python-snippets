# -*- coding: utf-8 -*-
"""
(None and condition) is False for any conditions.
In this case, condition is not evaluated due to short-circuiting.

"""


def find_goverment_websites(urls: list[str]) -> list[str]:
    result = []
    for url in urls:
        if url and url.find(".gov"):
            result.append(url)
    return result

# No Error
if None and None.find(".gov"):
    print("(None and condition) == False for any conditons")
    print("and condition is not evaluated")

# ERROR occurs because None.endswith(".gov") is evaluated first
try:
    if None.find(".gov") and None:
        print("fine")
except AttributeError as error:
    print(error) 

# No Error
urls = [None, "https://youtube.com", "https://edx.org", "https://www.fbi.gov", "https://www.whitehouse.gov"]
result = find_goverment_websites(urls)
print("goverment's websites:", result)


