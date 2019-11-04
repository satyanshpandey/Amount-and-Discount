while(1):

            money=int(input('Enter money for find the % discount: '))
            discount=int(input('Enter the discount % :'))
            disc=discount/100
            print('your discount is: ',disc*money)
            print('After discount you have to pay ',money-(disc*money))
input()