ijs = 0
bolletjes = 0
def stap1():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
    try:
        global bolletjes
        bolletjes = (int)(input('Hoeveel bolletjes wilt u?: '))
    except ValueError:
        print('Voer alstublieft een nummber in')
        stap1()
    if bolletjes > 8:
        print('Sorry, zulke grote bakken hebben we niet.')
        stap1()
    return
#------It asks the amount of ice balls you'd like, and it adds it to a variable which is called bolletjes ( global )
#if bolletjes < 4:
    #print('stap 2')
def stap2():
    print('Wilt u deze ' + (str)(bolletjes) + ' in A) een hoorntje of B) een bakje?: ')
    container = input('a of b: ')
    container = container.lower()
    global ijs
    if container == 'a':
        
        ijs = 'hoorntje'
    elif container == 'b':
        
        ijs = 'bakje'
    else:
        print('Sorry, Ik snap het niet.')
        stap2()
    return 
    #---------- If the ice balls are less than 4 then this function will be used to ask whether the customer wants it in a cone or container
def stap3():
    global proceed
    proceed = input('Hier is uw ' + (str)(ijs) + ' met ' + (str)(bolletjes) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N): ')
    proceed = proceed.lower()
    if proceed == 'y':
        stap1()
        stap2()
        stap3()

    elif proceed == 'n':
        print('Bedankt en tot ziens!')

    else:
        print('Sorry, dat snap ik niet.')
        stap3()
    
    return #---------------Confirming the payment 


def kopen():
    stap1()
    if bolletjes < 4:
        stap2()
    elif bolletjes > 3:
        global ijs
        ijs = 'bakje'
    stap3()
kopen()



