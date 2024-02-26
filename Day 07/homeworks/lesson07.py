



                                                    #დავალება ორი
                   #2) for ციკლისა და range ის მეშვეობით გამოიტანეთ ერთიდან ათამდე ლუწი რიცხვები
  


        #დიაპაზონი
start = 1
end = 100  

             # ლუწი რიცხვების დიაპაზონი
print("Even numbers from", start, "to", end, "are:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)




                                                    #დავალება სამი
                         #3) while ციკლის მეშვეობით გამოიტანეთ ერთიდან ოცამდე ციფრები
        
count = 1

while count <= 20:
    print(count)
    
    count += 1                      

 
                                                     #დავალება ოთხი     
                        #4) while ციკლის მეშვეობით ნულიდან ხუთის ჩათვლით შეკრიბეთ ციფრები
total = 0
num = 0

while num <= 5:
    total += num
    num += 1

print("The sum of numbers from 0 to 5 is:", total)
                            
                                                     #დავალება ხუთი

                        #5) for ციკლში გამოიყენეთ რაიმე string და გატესტეთ როგორ მუშაობს იგი (გამოიტანეთ სტრინგის თითო სიმბოლო ყოველ იტერაციაზე) ❤️


my_string = "Hello, world!"

for char in my_string:
    print(char)


  