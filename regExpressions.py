import re
def isPhoneNumber(text: str):
    # this is literal ass, dont do this
    if len(text) != 12: return False
    for i in range(0,3):
        if not text[i].isdecimal(): return False
    if text[3] != '-': return False
    for i in range(4,7):
        if not text[i].isdecimal(): return False
    if text[7] != '-': return False
    for i in range(8,12):
        if not text[i].isdecimal(): return False
    return True

print(isPhoneNumber('415-555-4242'))
print(isPhoneNumber('Moshi moshi'))

def isPhoneNumberButBetter(text: str):
    # long hand: \d\d\d-\d\d\d-\d\d\d\d
    # here is a better method
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumRegex.search(text)
    return mo.group()

print('phone number is: ', isPhoneNumberButBetter('my num is 817-341-9457'))    