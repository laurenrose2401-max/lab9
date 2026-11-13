
mobile = 0
lengthname = 0
name = input(" enter name ")
lengthname = len(name)
mobile = input(" enter mobile ")

if lengthname < 15 and len(mobile) < 10:
    print("PASS")
else:
    print("FAIL")