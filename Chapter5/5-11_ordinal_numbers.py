#~ looped a list of numbers 1 through 9
#~ Used an if-elif-else chain inside the loop to print 
#~ the proper ordinal ending for each number 
#~ eg "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", 
#~ with each result printed on a separate line


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#~ for number in numbers:
    #~ if number >= '4':
        #~ print(number + "th")
    #~ elif number == '3':
        #~ print(number + "rd")
    #~ elif number == '2':
        #~ print(number + "nd")
    #~ elif number == '1':
        #~ print(number + "st")
        
for number in numbers:
    if number == '1':
        print(number + "st")
    elif number == '2':
        print(number + "nd")
    elif number == '3':
        print(number + "rd")
    else:
        print(number + "th")
