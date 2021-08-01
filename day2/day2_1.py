#getting the input value for number of elements in the list 
n=int(input("Enter the number of elements in list:"))
lst=[]

#getting elements for the list
for i in range(n):
         item=input()
         lst.append(item)
print(lst)
element=input("Enter the element to be deleted:")

#count the number of times the element occured
count=lst.count(element)

#removing the all occurences of that element
for i in range(count):
          lst.remove(element )
          
print("The list after deleting the element ",element)
#After removing the all occurences of the element
print(lst)
