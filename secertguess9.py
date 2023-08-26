sn=9
guess=0
guess=int(input('GUESS : '))
if guess==sn:
    print('you win ')
else:
    for i in range(2):
        if guess != sn:
            guess=int(input('GUESS : '))
        else:
            print('you win ')
            break
    if guess!=sn :
         print('you lose sorry')

    
    
    
    

