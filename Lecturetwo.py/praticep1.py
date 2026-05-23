list1 = input("enter the number :")
list2 = input("enter the number :")

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not a panandrome")
            