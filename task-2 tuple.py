# 1. nums=[5,12,17,24,35,40,55]create a tuple containing only numbers that are divisible by 5 using comprehension.
nums=[5,12,17,24,35,40,55]
res=tuple(i for i in nums if i%5==0)
print(res)

# output:
# (5,35,40,55)

# 2.given a string:"HelloWorld" create a tuple of all uppercase letters present in the string comprehension.?
g="HelloWorld"
res=tuple(i for i in g if i.isupper())
print(res)

# output:
# ('H','W')

# 3.marks=[55,72,48,90,67] create a tuple where each element is "Pass" if marks are>=50 else "Fail" using comprehension.?
marks=[55,72,48,90,67]
res=tuple("Pass" if i>=50 else "Fail" for i in marks)
print(res)

# output:
# ('Pass','Pass','Fail','Pass','Pass')

# 4.Given a sentance:"Python is powerful and easy to learn" create a tuple of words that have more than 4 characters using comprehension.?
g="Python is powerful and easy to learn"
h=g.split()
print(h)
res=tuple(i for i in h if len(i)>4)
print(res)

# output:
# ['Python','is','powerful', 'and', 'easy', 'to', 'learn']
# ('Python','powerful','learn')

# 5.students=[("Alice",85),("Bob",45),("Charlie",60),("David",30)] create a tuple containing names of student who scored 50 or more using comprehension.?
students=[("Alice",85),("Bob",45),("Charlie",60),("David",30)]
res=tuple(i[0] for i in students if i[1]>50)
print(res)

# output:
# ('Alice','Charlie')