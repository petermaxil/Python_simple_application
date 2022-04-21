import re

def word_calcu(word):
    x = word.split("and")
    #print(x)
    temp=0
    for record in x:
        #print(record)
        first_word = record.split()[0]
        numbers=re.findall(r'\d+',record)
        #print(first_word,numbers)
        if first_word=='add':
            if len(numbers) and len(numbers) > 1:
                temp = int(numbers[0]) + int(numbers[1])
            elif len(numbers) and len(numbers) < 2:
                temp = temp+int(numbers[0])
            else:
                temp = temp+int(numbers)
        #print(temp)
        if first_word == 'subtract':
            if len(numbers) and len(numbers)>1:
                temp=int(numbers[0])-int(numbers[1])
            elif len(numbers) and len(numbers)<2:
                temp = temp-int(numbers[0])
            else:
                temp=temp-int(numbers)
            #print(temp)
        if first_word == 'multiply':
            print(temp,numbers)
            if len(numbers) and len(numbers)>1:
                temp=numbers[0]*numbers[1]
            elif len(numbers) and len(numbers)<2:
                temp = temp*int(numbers[0])
                print(int(numbers[0]))
            else:
                temp=temp*int(numbers)
                print(int(numbers))
            #print(temp)
    print(word,'=',temp)
word1='add 5 with 2 and subtract 3 and multiply 3'
word2='add 5 with 2'
word3='add 5 with 2 and subtract 3 and multiply -3'
word_calcu(word1)
word_calcu(word2)
word_calcu(word3)
