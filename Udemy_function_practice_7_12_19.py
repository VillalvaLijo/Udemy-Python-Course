print("Function practie Homework, Udemy 7/12/19")
print("By: Sam Villalva Lijo")

print("LESSER OF TWO EVENS")
print("write a function that returns the lesser of two given numbers if both numbers")
print("are even, but returns the greater if one or both are odd.\n")

def lesser_of_two_evens(a,b):
    if a%2==0 and b%2 == 0:
        if a<b:
            return a
        else:
            return b
    else:
        if a>b:
            return a
        else:
            return b
a1 = int(input("Enter your first number: "))
b1 = int(input("Enter your secound number: "))
print(lesser_of_two_evens(a1,b1))

print("\nAnimal CRACKERS: write a function takes two-word string and returns True if both")
print("words begin with same letter.\n")
        

def animal_crackers(text):
    text_list = text.split(' ') 
    if text_list[0][0] == text_list[1][0]:
        return True
    else:
        return False

animal_string = input("Enter a string for function animal crackers: ")
print(animal_crackers(animal_string))

print("\nMAKES TWENTY: Given two integer, return True if the sum of the integers is 20 or if")
print("one of the integers is 20. if not, return false.\n")

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20:
        return True
    elif n1 + n2 == 20:
        return True
    else:
        return False

num1 = int(input("Enter the First number for the Makes Twenty Function: "))
num2 = int(input("Enter the Secound number for the Makes Twenty Function: "))
print(makes_twenty(num1,num2))

print("\nLEVEL 1 PROBLEMS\n")

print("OLD MACDONALD: write a function that capitalizes the first and fourth letters of a name.\n")


def old_macdonald(name):
    namepf = ''
    c = 0
    for _ in name:
        c += 1
        if c==1 or c==4:
            namepf += _.upper()
        else:
            namepf += _
    return namepf

namebf = input("Enter a name for the Old MacDonald Function: ")
print(old_macdonald(namebf))


print("\nMASTER YODA: Given a sentence, return a sentence with the words reversed.\n")

def master_yoda(text):
    text_list = text.split()
    c = (len(text_list)-1)  #have to subtract one to make it obey the rules
                            # (list start at zero)
    text_list_pf = []
    for _ in text_list:
        text_list_pf.append(text_list[c])
        c -=1
    yoda_string = " ".join(text_list_pf)
    return yoda_string

yoda_i = input("Enter a string you want read Yoda style: ")
print(master_yoda(yoda_i))


print("\nALMOST THERE: given an integer n, return True if n is within 10")
print(" of either 100 or 200.\n")

def almost_there(n):
    if n <= 210 and n >= 190:
        return True
    elif n <= 110 and n >= 90:
        return True
    else:
        return False

n_input = int(input("Enter a number for the Almost There Function: "))
print(almost_there(n_input))

print("\nLEVEL TWO PROBLEMS\n")

print("FIND 33:  given a list of ints, return True if the array contains a 3 next")
print(" next to a 3 somewhere.\n")

def has_33(nums):
    c = 0
    for _ in nums:
        if _ == 3 and nums[c+1] == 3:
            return True                 #exits as soon as it returns true
                                        #otherwise, if it hasn't exited with a
                                        #True statement yet, it will exit
                                        #with a false statement
                                        
        else:
            pass
        c += 1
    return False
        

list_of_33 = input("Enter a list of numbers for the Find 33 Function: ").split(' ')

c_33=0

for _ in list_of_33:
    list_of_33[c_33] = int(list_of_33[c_33]) #this works, but int(_) does not work
                                    #returns error of invalid literal for
                                    #int with base 10: '', you have to get rid
                                    #of the quotation marks, this type of code
                                    # leaves no room for error, if user types
                                    # in a space it will come back with the
                                    #same error.
    c_33 +=1

#print(list_of_33)
print(has_33(list_of_33))           #homework is figure out how to error proof
                                    #has_33

print("\nSUMMER OF '69: Return the sum of the numbers in the array, except ignore sections")
print(" of numbers starting with a 6 and and extending to the next 9 (every 6 will be followed")
print(" by at least one 9). Return 0 for no numbers.\n")

def summer_69(arr):
    sum_69 = 0
    count = 0
    for _ in arr:
        if _ != 6 and count == 0:
            sum_69 += _
        elif _ == 6 and count == 0:
            count += 1
        elif count == 1 and _ != 9:        #qualify that _ does not equal 9, or loop will
                                           #skip without writing
            pass
        elif _==9 and count == 1:
            count += 1
        elif count == 2: 
            sum_69 += _
    return sum_69

list_69 = input("Enter a list of Numbers for the Summer of 69 Program: ").split(' ')
count_l69 = 0
for _ in list_69:
    list_69[count_l69] = int(list_69[count_l69])
    count_l69 += 1

print(summer_69(list_69))

print("\nPAPER DOLL: Given a string, return a string where for every character in the original")
print(" there are three characters.\n")

def paper_doll(text):
    text_pf = ''
    for _ in text:
        text_pf += _*3
    return text_pf

text_pd = input("Enter a string for the paper doll function: ")
print(paper_doll(text_pd))


print("\nBLACKJACK: Given there integers between 1 and 11, if their sum is less than or equal")
print("to 21, return their sum. If their sum exceedss 21 and there's an eleven, reduce the total")
print(" sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'.\n")

def blackjack(bj_values = [], *args):
    ace = 0
    sum_bj = 0
    for _ in bj_values:
        sum_bj += _
        if _ == 11:
            ace += 1
    if sum_bj <= 21:
        return sum_bj
    elif sum_bj > 21 and ace >= 1:
        for _ in range (ace):
            if sum_bj > 21:
                sum_bj -= 10
            else:
                pass
        if sum_bj > 21:
            return 'BUST'
        elif sum_bj <= 21:
            return sum_bj
    elif sum_bj > 21 and ace == 0:
        return 'BUST'

bj_args = input("Enter three numbers, 1-11 to recive your BlackJack score: ").split(' ')
count_bjargs = 0
for _ in bj_args:
    bj_args[count_bjargs] = int(_)
    count_bjargs += 1

print(blackjack(bj_args))

print("\nCHALLENGING PROBLEMS\n")

print("SPY GAME: Write a function that takes in a list of integers and returns True if it")
print(" contains 007 in order.\n")

def spy_game(nums):
    spy_count = 0
    for _ in nums:
        if _ == 0:
            if spy_count+2 <= len(nums):
                if nums[spy_count+1]==0 and nums[spy_count+2]:
                   return True
        else:
            pass
        spy_count += 1
    return False

spy_nums = input("Enter a list of numbers for the Spy Game: ").split(' ')
sn_count = 0
for _ in spy_nums:
    spy_nums[sn_count] = int(_) 
    sn_count += 1

print(spy_game(spy_nums))

print("\nCOUNT PRIMES: Write a function that returns the number of prime numbers that exist")
print(" up to and including a given number.\n")

def count_primes(num):
    prime_list = [2]
    prime_count = 1
    for _ in range(2,num+1):
        prime_yn = 'y'
        for i in prime_list:
            if _%i==0:
                prime_yn = 'n'
            else:
                pass
        if prime_yn == 'y':
            prime_list.append(_)
            prime_count +=1
        else:
            pass
    return prime_count


num_cp = int(input("Enter a number and I will tell you how many prime numbers are contained within it: "))
print(count_primes(num_cp))

print("\nPRINT BIG: Write a function that takes in a single letter, and returns a")
print(" 5X5 representation of that letter. Only do A through E.")

#pint_big('a')
#out:  *
#     * *
#    *****
#    *   *
#    *   *


def print_big(letter):

    letters_dic = {'a':"  *  \n * * \n*****\n*   *\n*   *",'b':"**** \n*   *\n**** \n*   *\n**** ",
                   'c':"*****\n*\n*\n*\n*****",'d':"***\n*  *\n*   *\n*  *\n***",
                   'e':"*****\n*\n*****\n*\n*****"}
    letter_key = letter.lower()

    print(letters_dic[letter_key])


letter_pg = input("Enter a letter A through E you would like to see printed big: ")
print_big(letter_pg)


print("\n Thank you, for taking the time to check out my function practice.")
print("Good Bye")



              
