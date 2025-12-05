
#250

#0h - 1
#<5h - 1.1
#<10 - 1.25
#<20 - 1.4
#<20+ - 1.6


def react_to_sleep_dept(hours):
    ms = 250
    factor = 1
    if 0 == hours:
        factor = 1
    elif hours<5:  
        factor = 1.1
    elif hours<10:
        factor = 1.25
    elif hours<20:
        factor = 1.4
    elif hours>=20:
        factor = 1.6
    return ms * factor

print(react_to_sleep_dept(0))
print(react_to_sleep_dept(4))
print(react_to_sleep_dept(5) )
print(react_to_sleep_dept(10) )
print(react_to_sleep_dept(20) )
print(react_to_sleep_dept(30) )

def ok_to_drive(hours):
    minimal_needed_reaction_time = 275
    ms = react_to_sleep_dept(hours)
    return ms <= minimal_needed_reaction_time

print(ok_to_drive(0))
print(ok_to_drive(3))
print(ok_to_drive(5))
