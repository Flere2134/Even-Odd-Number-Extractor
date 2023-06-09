#open number txt file and read
with open("numbers.txt") as my_file:
    content = my_file.read()
#split content into list of int
numbers = [int(i) for i in content.split()]
#create two lists
even_numbers = []
odd_numbers = []
#checks each number and sorts them into the list
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
#open even txt file and writes the even numbers
with open("even.txt", "w") as my_file:
    for num in even_numbers:
        my_file.write(str(num) + "\n")
#open even txt file and writes the odd numbers
with open("odd.txt", "w") as my_file:
    for num in odd_numbers:
        my_file.write(str(num) + "\n")