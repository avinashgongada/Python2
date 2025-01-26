
#RANGE
# Examples
r1=range(0,15)
print(r1)
output = range(0,15)
print(list(r1))
#output = [0,1,2,.............................,14]

r2=range(10,30)
print(list(r2))
#output = [10,11,12,13..................................,29]

r2=range(30,10)
print(list(r2))
#output = [''] # empty string

r2=range(30,10,-2)
print(list(r2))
#output = [30,28,26,24,22,20,18,16,14,12]

r1=range(15,0,-3)
print(list(r1))
output = [15,12,9,6,3]

# using range we can find the range for list also
# Example

print(list(range(100,0,-1)))
#output = [100,99,98,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,1]
list=[1,35,8,9,"grape"]
for i in list : 
    print(i)
#output = 1
#         35
#         8
#         9
#         grape

for i in range(len(list)):
    print( i,list[i])
#output = 0  1  2  3  4 
#         1 35  8  9  grape 
# both indexes , lengtghhs of list are printed

for i in range(0, len(list))  :
    print(i)     