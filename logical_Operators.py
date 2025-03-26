#logical Operators
is_sunny = True
is_warm = False

#and
print(is_sunny and is_warm) 
#or
print(is_sunny or is_warm)
#not
print(not is_sunny)
print(is_warm)


is_weekend = True
has_work_meeting = False
can_relax = not (is_weekend and not has_work_meeting)
print(can_relax)