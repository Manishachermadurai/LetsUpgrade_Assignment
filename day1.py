#getting input value for the number of elements in list
n=int(input("Enter the number of elements in list:"))
lst=[]
#getting the elements for the list
for i in range(n):
         item=input()
         lst.append(item)   
print(lst)
print("List sorted in descending order:")
#sorting the array in descending order
lst.sort(reverse=True)
print(lst)
