#An online bookstore gives free 2nd class mail delivery (code 2) for any order value greater than or equal to £15.00 

#For order values less than £15.00, 2nd class mail delivery costs £3.50. 

#For any value of order, a customer may choose to pay £5.00 for guaranteed next day delivery (code 1). 
#(a)	Write pseudocode for an algorithm which allows the user to enter the total value of their order. They are then asked whether they want to pay for guaranteed next day delivery. Depending on their answer, and the value of the order, the program displays the postage charge and the overall total charge. 

val = int(input('Enter the total value of your order: '))
ndd = int(input('Do you want to pay for next day delivery with an additional cost of £5? \nEnter 1 for Yes and enter 2 for No \nChoice: '))
nddp = 5
scd = 3.5
if ndd == 1:
  nval = val+nddp
  print(f'The total price for your order is: \n£{val} - item cost \n£{nddp} - next day delivery cost \n£{nval} - total cost ')
elif ndd == 2:
  if val >= 15:
    print(f'You are entitled to free second class delivery as your item costs more than £15. The total price for your order is: £{val} ')
  else:
    dval = val + scd
    print(f'You are required to purchase second class delivery for an additional £3.5 as your item cost (£{val}) is under £15. \nThe total price for your order is: \n£{val} - item cost \n£{scd} - second class delivery cost \n£{dval} - total cost')
