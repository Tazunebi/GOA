#1 დავალება
# შექმენით სია სადაც გადასცემთ 10 ინტეგერს, შემდეგ გადაუარეთ ამ სიას და თითოეული მათგანი გაამრავლეთ/გაყეთ/დაუმატეთ/გამოაკელით ერთმანეთს.




my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# gamravleba
print("gamravleba")
for i in range(len(my_list)):
    my_list[i] *= 2
print(my_list)

# gayofa 
print("gayofa")
for i in range(len(my_list)):
    if my_list[i] != 0:
        my_list[i] /= 3
print(my_list)

# mimateba
print("mimateba")
for i in range(len(my_list)):
    my_list[i] += 1
print(my_list)

# gamokleba
print("gamokleba")
for i in range(len(my_list)):
    my_list[i] -= 1
print(my_list)



#დავალება 2
#შექმენით სია, სადაც გამოიტანთ სათითაოდ მნიშვნელობებს და ასევე ჩაანაცვლებთ სხვა მნიშვნელობებით

# list = ["str" , 1, 1.0, True]

# list[1] = "dog"

# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])

#დავალება 3
#შექმენით სია და მომხმარებელს აარჩევინეთ სასურველი მნიშვნელობა

# list = [1, 2, 3]
# print(list)
# choose_number = int(input("please choose number: ")) 

# if choose_number == 1:
#     print("you choosse first number")
# elif choose_number == 2:
#     print("you choose second number")
# elif choose_number == 3:
#     print("you choose third number")
# else:
#     print("Error")

#დავალება 4

