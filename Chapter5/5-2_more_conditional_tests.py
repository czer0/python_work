#~ testing for equality and inequality with strings
#~ age = str(25) 
#~ if age == str(25): 
    #~ print("this is correct")
#~ if age != str(25): 
    #~ print("this is incorrect")  

#~ test using upper() function
#~ tools = ['hammer', 'saw', 'wrench', 'socket driver']

#~ for tool in tools:
    #~ if tool == 'saw':
        #~ print(tool.upper())
    #~ else:
        #~ print(tool.title())
        
#~ test using lower() function
#~ tool = 'Hammer'
#~ if tool == 'Hammer':
    #~ print(tool.lower())
#~ else:
    #~ print(tool.title()) 
    
#~ numerical tests involving equality and inequality, greater than and
#~ less than, greater than or equal to, and less than or equal to
#~ age = str(10)
#~ if age >= str(11):
    #~ print("this number is too large") 
#~ if age <= str(9):
    #~ print( "this number is too small")
#~ if age == str(10):
    #~ print("this is the correct number")

#~ test using and 
#~ age_00 = str(10)
#~ age_01 = str(1)
#~ if age_00 >= str(10) and age_01 >= str(10):
    #~ print("go to bed")

#~ test using or
#~ age_00 = str(9)
#~ age_01 = str(19)
#~ if age_00 <= str(10) or age_01 >= str(11):
    #~ print("go to bed")

toolbox = ['hammer', 'saw', 'screw driver']
tool = 'wrench'
if tool not in toolbox:
    print("\nWhere the hell is my " + tool.title() + "?")
    

