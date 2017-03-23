value = ("Michael", "Instructor", "Coding Dojo")
number = (3,7,9,12,26)
(name, position, butt) = value
for index, item in enumerate(number):
    print(str(index)+" = "+str(item))
print name
print position
print butt
print len(value)
print max(value)
print min(value)
print sum(number)
print any(value)
print all(value)
print sorted(number)
print tuple(reversed(number))
