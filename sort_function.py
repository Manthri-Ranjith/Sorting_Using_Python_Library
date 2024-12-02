#Sorting the values of the elements using the python liberary.
#In this we used sort function to arrange the values in Ascending Order and Descending order.
#We can also sort the values by using the sorting techniques like Bubble Sort, Insersion Sort, Selection Sort e.t.c.

list=[]
#Taking the empty list

values=int(input("How many elements you want to enter in to the list:"))
#Asking the user that how many elements does the user want to enter

for i in range (values):
    #Using the for loop
    
    elements=input("Enter the elements:")
    list.append(elements)
    #Adding the elements from the list
    
print("The list of elements before sort:",list)
#Displaying the values before sort.

list.sort(reverse=True)
#sort the elements from the list in the ascending order

print("The list of elements in Decending order:",list)
#Display the elements in the decending order

list.sort()
#sorting the elements in the Ascending order

print("The list of elements as Ascending order:",list)
#displaying the elements in the ascending order