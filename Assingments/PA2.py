def to_do(is_weekend, is_rainy, is_cold):
#Function takes three boolean parameters, before assinging a string based
#off their values (true or false)
#The values determine what the user should do based off the
#day, wheather, and temperature (assigned to 'whatdo')
    
        
    if is_weekend is True and is_rainy is True:
        whatdo = 'Stay inside and watch movies'
    elif is_weekend is True and is_rainy is False and is_cold is True:
        whatdo = 'Go skiing'
    elif is_weekend is True and is_rainy is False and is_cold is False:
        whatdo = 'Go for a hike'
    elif is_weekend is False and is_rainy is True and is_cold is False:
        whatdo = 'Go to the mall'
    elif is_weekend is False and is_rainy is False and is_cold is True:
        whatdo = 'Stay inside and read a book'
    elif is_weekend is False and is_rainy is False and is_cold is False:
        whatdo = 'Go to the park'
    
    result = whatdo    #Sets result as whatdo string and returns it
    
    return result

def priority_level(amount):
#Takes a number and determines a priority level ('pri') based off its value
#lower numbers give higher priority values  

    if amount >= 10000:
        pri = 1
    elif 10000 > amount >= 7500:
        pri = 2
    elif 7500 > amount >= 5000:
        pri = 3
        
#if the amount is less than 5000, it finds the remainder when divided by 10
#after converting the number to an integer to remove any decimals        
#this will always give us the last digit, and will assign priority level
#accordingly. If the last digit is 3 or 5, priority level is 4, else it is 5
        
    elif 5000 > amount:
        amtsp = int(amount)
        amtsp %= 10
        if amtsp == 3 or amtsp == 5:
            pri = 4
        else: pri = 5
        
# Assigns result to the priority level and returns it when run

    result = pri
    
    return result


def categorize(item_price, item_units):
#categorizes the item ('cat') based on two parameters, how much it costs
#and how many units are to be sold
    
    if item_price < 10 and item_units < 10:
        cat = 'Low-priced'
    elif 10 <= item_price <= 20 and item_units < 20:
        cat = 'Mid-priced'
    elif 20 < item_price and item_units < 30:
        cat = 'High-priced'
    elif 20 < item_price and item_units >= 30:
        cat = 'Premium'
    else:
        cat = 'Other'
        
    result = cat    #Result is assigned as the category and returned 
    
    return result


def ticket_price(customer_age, day_of_week):
#Assigns ticket prices ('price') based on the age of the customer and day
#of week. Tickets for children (those under 10) cost $5, teens $8,
#adults $10 and seniors $7.
    
    if customer_age < 10:
        price = 5.0
    elif 10 <= customer_age <= 17:
        price = 8.0
    elif 18 <= customer_age <= 59:
        price = 10.0
    else:
        price = 7.0
    
#depending on the day of the week and age of the customer, price is
#discounted by various amounts.

#since every price is different among children, teens, adults and seniors,
#the price can be used to determine their age and if the discount applies
        
    if day_of_week == 'Monday':
        price = price - (price*.2)
#if it is Monday, all tickets are discounted by 20%
        
    elif day_of_week == 'Tuesday' and price == 7:
        price = price - (price*.25)
#on tuesdays, all seniors get 25% off
        
    elif day_of_week == 'Wednesday' and price == 5:
        price = price - (price*.1)
#Wednesday, all child tickets 10% off
    
    result = price # Assigns the result as the price before returning it 
    
    return result
