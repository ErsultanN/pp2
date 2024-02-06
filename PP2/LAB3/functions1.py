#Exercise 1
def my_function1(grams):
    return grams / 28.3495231

print(my_function1(100))     #Вместо '100' можем поставить любое число и из граммов перейдет в ounces.

#Exercise 2
def my_function2(F):
    return (0.5555556 * (F-32))

print(my_function2(100))    #Вместо '100' можем поставить любое число и из фаренгейта перейдет в целсий.

#Exercise 3
def my_function3(head,legs):
    chickens = (legs - (4*head)) / -2
    rabbits = head-chickens
    return int(chickens,int(rabbits))

print(my_function3(35,94))

#Exercise 4 
def filter_prime(lister):
    simple = []
    for i in lister:
        count=0
        if i==2:
            simple.append(i)
            continue
        elif i==1:
            continue
        for j in range(2,i):
            if(i%j==0):
                count+=1
        if(count==0):
            simple.append(i)
    return simple
lister = [1,2,3,4,5,6,7,8,9,10]
print(filter_prime(lister))




#Exercise 5 
from itertools import permutations

def print_permutations(user_string):
    perms = [''.join(p) for p in permutations (user_string)]
    for perm in perms:
        print(perm)

user_input = input("  ")
print_permutations(user_input)

#Exercise 6
def sentence(my_string):
    words = my_string.split()
    matching = ' '.join(reversed(words))
    return matching

#Exercise 7
def three(numbers):
    for i in range(len(numbers)-1):
        if(numbers[i]==numbers[i+1]==3):
            return True
    return False

#Exercise 8
def spy_game(nums):
    my_list = []
    for i in nums:
        if i == 0:
            my_list.append(i)
        elif i == 7:
            my_list.append(i)
    
    if len(my_list) >= 3 and my_list[:3] == [0, 0, 7]:
        return True
    return False

#Exercise 9
def volume(radius):
    V = 4/3*3.14*radius**3
    return V
print(volume(5))     #вместо 5 можем поставить любое число.

#Exercise 10
def unique(digits):
    unique_digits = []
    for i in digits:
        if i not in unique_digits:
            unique_digits.append(i)
            return unique_digits 
        
    digits = [1, 2, 3, 2, 5, 3]
    print(unique(digits))           #вместо digits можем подставить любые числа и нам дадут уникальные из них

#Exercise 11
def palindrome_words(string):
    k = string[::-1]
    if k == string:
        return True
    return False
print(palindrome_words("madam"))

#Exercise 12
def histogram(numbers):
    for i in numbers:
        for j in range(i):
            print("*" , end = "")
        print()
histogram([4, 9 ,7])

#Exercise 13
import random
def guessGame():
    guessnumber = random.randint(1,20)
    attempt = 0
    print("Hello! What is your name?")
    name = input()
    print(f"Well,{name}, I am thinking of a number between 1 and 20")
    while True:
        print("Take a guess")
        num = int(input())
        attempt+=1
        if(num<guessnumber):
            print("Your guess is too low.")
        elif(num>guessnumber):
            print("You guess is too big")
        else:
            print(f"Good job, {name}! You guessed my number in {attempt} guesses!")
            break
guessGame()