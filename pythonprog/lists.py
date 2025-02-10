courses = ["English","Maths","Science","Humanities"]
print(courses)
print(courses[2])
print(courses[-1]) #prints last element
print(courses[0:1])#slicing can also be done for lists

courses.insert(2,"PE")
print(courses)

sort=sorted(courses)
print(sort)
