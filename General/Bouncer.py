#ask for age

age = input('How old are you?\n')
if age != "" and age.isnumeric() == True:
    if int(age) >= 18 and int(age) < 21:
        print('You can enter, but need a wristband!')
    elif int(age) >= 21:
        print('You are good to enter and can drink!')
    else:
        print('You can\'t enter')

else:
    print('Enter a valid age value!')





