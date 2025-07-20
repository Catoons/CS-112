#works
def calculate_final_speed(initial_speed, acceleration, time):
    final_speed = initial_speed + (acceleration * time)
    return int(final_speed)
#works
def calculate_distance(initial_speed, final_speed, time):
    distance = (initial_speed + final_speed) * (time/2)
    return int(distance)

def motion_calculator(initial_speed, acceleration, time):
    
    final_speed = calculate_final_speed(initial_speed, acceleration, time)
    far = calculate_distance(initial_speed, final_speed, time)
    
    mytuple = (final_speed, far, time)
    return mytuple
