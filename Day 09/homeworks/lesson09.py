
#დავალება პირველი 


#1) შემოვიტანე ინფუთი სახელად num2 
#2) და პრინტში ვუბრძანე რომ შამოწმოს მომხმარებლის შემოტანილი რიცხვი ზუსტად იყოფა ორზე და ოთზე თუ არა
num2 = int(input("please enter your number: "))

print(num2 % 2==0 and num2 % 4==0)
# #დავალება მეორე


 # Greater than (>)
print(5 > 3)       # True

 # Less than (<)
print(10 < 20)     # True

 # Greater than or equal to (>=)
print(15 >= 15)    # True

 # Less than or equal to (<=)
print(25 <= 30)    # True

 # Equal to (==)
print(10 == 10)    # True

 # Not equal to (!=)
print(10 != 20)    # True

 # Greater than (>)
print(1000 > 999)  # True

 # Less than (<)
print(50 < 100)    # True

 # Greater than or equal to (>=)
print(7 >= 7)      # True

# Less than or equal to (<=)
print(50 <= 50)    # True

#დავალეაბა მესამე

# Example 1
result_1 = (5 > 3) and (10 < 20)
print(result_1)  # True

# Example 2
result_2 = (15 >= 15) and (25 <= 30)
print(result_2)  # True

# Example 3
result_3 = (10 == 10) and (10 != 20)
print(result_3)  # True

# Example 4
result_4 = (1000 > 999) and (50 < 100)
print(result_4)  # True

# Example 5
result_5 = (7 >= 7) and (50 <= 50)
print(result_5)  # True

# Example 6
result_6 = (5 > 3) and (10 > 20)
print(result_6)  # False

# Example 7
result_7 = (15 >= 20) and (25 <= 30)
print(result_7)  # False

# Example 8
result_8 = (10 == 20) and (10 != 20)
print(result_8)  # False

# Example 9
result_9 = (1000 < 999) and (50 < 100)
print(result_9)  # False

# Example 10
result_10 = (7 >= 8) and (50 <= 50)
print(result_10)  # False