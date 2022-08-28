# 6. Write a python script which takes a three digit number from the user and displays only its middle digit.

Number=int(input("Enter The Number: "))
Result=Number%100//10
print(Result)
print()


"""
2nd Logic!

Number=int(input("Enter The Number: "))
Result=Number//10%10
print(Result)
print()
"""