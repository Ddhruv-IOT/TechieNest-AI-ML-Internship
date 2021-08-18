print(5**9) #Q2 (a) double asterick shows power
print(3//2) #Q2(b) Floor division returns only the integer not the decimal part
print(7//3)#Q2(b)
print(7/3) #Q2(b)(division)
print(6 == 6) #comparison
a = 20
a += 30
print(a)#it adds 30 to the assigned value of a and stores again in a
a%=3 #it divides a by 3 and returns only the remainder
print(a)
print(True * False)
print(True & False)
print(True and False)
print ((6>3) and (7<4) or (18 == 3)) and (9>3)
##print(True in "False") -- not iterable
print("true" in "False")

print("False" in "False")
print((True == False) or (False > True)) and (False <=  True)

#Q3 Try to get following output from two python strings
s1 = "Nice to have it"
s2 = "here"
print(s1+s2)
6
#Q4 Given this nested list , use indexing to grab the word "Hello"
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

#Q5. Try to insert above strings s1 and s2 in the list 'a' mentioned in ques4 ,
#in the beginning and end of it respectively
a[len(a)-1]= s2; a[-(len(a))] = s1;
print(a)

#Q6 . Write the Python Program to print out a set constaining all the colour from color_list_1 which are not present in color_list_2.
#Test Data:
#color_list_1 = set(["White","Black","Red"])
#color_list_2 = set(["Red","Green"])
#Expected Output:
        #{'Black','White'}
#sol:-
color_list_1 = set(['White','Black','Red'])
color_list_2 = set(['Red','Green'])
c = []
for i in color_list_1:
        if i not in color_list_2:
            c.append(i)
        
print(c)

#Q7. WAP to find if the given input string is pangram nor not
def is_all(str):
    all_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in all_alphabets:
        if i not in str.lower():
            return False
        #else:
           # return False
    return True

string = 'Glib jocks quiz nymph to vex dwarf.'
if(is_all(string) == True):
    print('yes it is a panagram')
else:
    print('No it is not a panagram')
        








#Q8:- Write a program that accepts an integer (n) and computes the value of n+nn+nnn
#sample value of n is : 5
#expected result :  155
def output():
    n = eval(input('enter the input_value: '))
    c =n + n*n + n*n*n
    print(c)
output()

#Q9:- Write a program that accepts a comma seperated sequence of words as input and
#prints the words in a comma-seperated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without, hello, bag, world
#Then, the output should be:
#bag,hello,without, world
values = input("Input comma separated sequence of words:  ")
w = [i for i in values.split(",")]
print(",".join(sorted(list(set(w)))))
    
#10. Write a Python function to find the name of person obtained 
#highest marks in exam from given dictionary
#Example dictionary
#d = {‘Student’: [‘Rahul’, ‘Kishore’, ‘Vidhya’, ‘Raakhi’], 
#‘Marks’: [57,87,67,79]} 
#Output: Kishore

d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57, 87, 67, 79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])
           
