def header():
    print('***************************************************************************')
    print('****************** Welcome To Unlucky Numbers *****************************')
    print('***************************************************************************')
    print('\n')

header()

for num in range(1,21):
    if num in [4,13]:
        print(f'{num} is unlucky')
    elif num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

