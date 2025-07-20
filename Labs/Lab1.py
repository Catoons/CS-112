print('Enter the frequency in GHZ:')
ghz = float(input())
lam = 3*(10**8) / ghz
lamsq = lam**2
g1 = 4
g2 = 1
p  = 1 
r = 100

pr = (p*g1*g2*lamsq)/(4*3.14*r)**2

print(f"The recieved power is {str(pr)} Watt")




