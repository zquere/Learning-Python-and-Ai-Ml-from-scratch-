# First see what is variable and data type-
# variable is  a box so we store over thing like
a = "banana"
print(a)
print(type(a))

# i dont thing that basic is good for learning like if you read given pdf you know much better

# this is a string there are-
# 1) float
# 2) list 
# 3) set
# 4) tuple
# 5) integer
# 6) string 
# 7) dictionary  


# so let go on index thing 
# see i make a list


# Chapter-01 string,list,for loop 


l = [1,2,3,4,"hello"]
print(l[0])  # so here i print  l[0] mean first element of list

b = "banana"
print(b[0:4:2]) # same as in string , IMPORTANT  l[starting:end:jump] that called string slicing 
# in sting ther is  
print(b.capitalize())
print(b.lower())
print(b.upper())
print(b.removeprefix("ba"))
print(b.removesuffix("na"))

# for list - 
l.append(3)
# l.remove("hello")
l.pop
#and other thing  (reed book)

# in for loop it take a value of a list as a varible like normal if it index 0 have  int so  it  take as int and so on 
# and perform task 

for i in l:
    if isinstance(i, str):
        print(f"string {i}")
    else:
        print(f"integer {i}")

for i in range(0,len(l)):
    print(l[i])

# at know i thnik i hold it 