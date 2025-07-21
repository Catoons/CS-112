def angle_size(num_sides):
    degrees_per_angle = (180 * (num_sides -2))/num_sides
    
    return degrees_per_angle


def antique_value(year, weight):
    
    if year <= 1900:
        priceper = 10
    elif year <= 1950:
        priceper = 6
    elif year <= 1990:
        priceper = 12
    else:
        priceper = 20
        
    final_val = priceper * weight
    return final_val


def remove_zeros(purchase_list):
    new_list = []
    for x in purchase_list:
        if x != 0:
            new_list.append(x)
    return new_list


            
            
        
