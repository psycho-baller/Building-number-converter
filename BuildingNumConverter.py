x = True
while x:    
    inp = input('do u live in Europe, Australia, or India?(answer with a yes or a no)')
    if inp != 'yes' and inp != 'no':
        continue
    while True:
        inp2 = input('what floor are u in?(in digits)')
        if not inp2.lstrip('-').isdigit():
            continue #if input is not a positive or negative digit, itrestarts the inner while loop(goes back to line 7) and asks for the input again
        if int(inp2) > -1: #only upper floors differ in number. basement floors are the same everywhere
            inp2 = int(inp2) + 1
        if inp == 'yes':        
            print ('your floor number would be '+ str(inp2) + ' in places other than Europe, Australia, and India')
        else: 
            print('your floor number in Europe, Australia, and India would be:', inp2)   
        x = False #when x is false, the outer while loop(line 2) would not run anymore hense avoids an infinite loop
        break #exits the inner loop 
    
