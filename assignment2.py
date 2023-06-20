#Ques:1 sort the value tuple of list

list = [(2,1), (5,6), (8,0), (4,7)]
def sort(list):
    return(sorted(list, key=lambda a: a[1]))

print("Sorted the given list:")
print(sort(list))

#Ques:2 ASCII values

dict = {}
string = 'abcdefghijklmnopqrstuvwxyz'
for i in string:
    dict[i] = ord(i)
print("ASCII values of a-z:")
print(dict)