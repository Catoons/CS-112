#function to convert lbs to kg
def pounds_to_kg(pounds):
	kg = pounds/2.2046
	return kg


#START
print("Welcome to Mael's Calculator")
apounds = float(input('Total Coffee A Pounds: '))
bpounds = float(input('Total Coffee B Pounds: '))
cpounds = float(input('Total Coffee C Pounds: '))

coffa_p = float(input('Coffee A Price/Kg: '))
coffb_p = float(input('Coffee B Price/Kg: '))
coffc_p = float(input('Coffee C Price/Kg: '))

akg = pounds_to_kg(apounds)
coff_a_fin = akg*coffa_p

bkg = pounds_to_kg(bpounds)
coff_b_fin = bkg*coffb_p

ckg = pounds_to_kg(cpounds)
coff_c_fin = ckg*coffc_p
all_coff_fin = coff_a_fin + coff_b_fin + coff_c_fin


print(f'Selling all of Coffee A makes: ${round(coff_a_fin,2)}')
print(f'Selling all of Coffee B makes: ${round(coff_b_fin,2)}')
print(f'Selling all of Coffee C makes: ${round(coff_c_fin,2)}')
print(f'Selling all of the Coffee makes: ${round(all_coff_fin,2)}')

price_red_vel = (pounds_to_kg(2) * coffa_p) + (pounds_to_kg(1)*coffb_p)
price_red_final = (price_red_vel + price_red_vel*.10)
price_val_frapp = (pounds_to_kg(2.5)*coffb_p) + (pounds_to_kg(1.5)*coffc_p)
price_of_love = (pounds_to_kg(0.45)*coffa_p) + (pounds_to_kg(2.16)*coffc_p)
pack_cups = 50 
tax = 0.10



print("***Valentine's Day Special***")
total_orders = float(input('Enter total orders: '))

print(f'Charge ${round((total_orders * price_red_vel)*1.10,2)} for Red Velvet Mocha')
print(f'Need {round(total_orders * (pounds_to_kg(2)),2)}kg of Coffee A and {round((total_orders*pounds_to_kg(1)),2)}kg of Coffee B')

print(f"Charge ${round((total_orders * price_val_frapp)*1.10,2)} for Valentine's Day Frapp")
print(f'Need {round((total_orders * (pounds_to_kg(2.5))),2)}kg of Coffee B and {round((total_orders*(pounds_to_kg(1.5))),2)}kg of Coffee C')

print(f"Charge ${round((total_orders * price_of_love)*1.10,2)} for Lover's Spice")
print(f'Need {round((total_orders * (pounds_to_kg(0.45))),2)}kg of Coffee A and {round((total_orders*(pounds_to_kg(2.16))),2)}kg of Coffee C')

amt_cups = int(total_orders / pack_cups)
extra_cups = int((total_orders % pack_cups))
print(f'Need {amt_cups} packages of cups and {extra_cups} additional cup(s)')





