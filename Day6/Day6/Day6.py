# Day 6 - Escaping The Maze

# Functions & Karel

#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
    
#def jump():
#    move()
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left()

#for i in range(6):
#    jump()

# OR

#while at_goal() == False:
#    jump()

# OR FOR RANDOMLY SPACED HURDLES:

# Take the first 'move()' out of 'jump()'
# while not at_goal():
    #if front_is_clear():
    #    move()
    #else:
    #    jump()

# MODIFIED FOR RANDOM HEIGHT HURDLES:

#def jump():
#    turn_left()
#    while not right_is_clear():
#        move()
#    turn_right()
#    move()
#    turn_right()
#    while front_is_clear():
#        move()
#    turn_left()

#while not at_goal():
#    if wall_in_front():
#        jump()
#    else:
#        move()

# 

#while not at_goal():
    
#    if wall_on_right() and wall_in_front():
#        turn_left()
        
#    elif wall_on_right():
#        move()
       
#    else:
#        turn_right()
#        move()
