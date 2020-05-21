import gym
import numpy as np
import random
import time
import math
import sys
from option import choose_option
from option import execute_option
#from option_Bonus import choose_option
#from option_Bonus import execute_option

# Display percentage of advancement
def advance_statut(update):
    sys.stdout.write("\r%d%%" % update)

nb_of_options = 8
nb_of_action = 4
nb_states = 103
alpha = 0.1
gamma = 0.9
q_value =  np.zeros([nb_states+1, nb_of_options + nb_of_action])

env = gym.make('gym_option:option-v0')
nb_iterations = 10000
state = env.state


def max(state):
    max = -math.inf
    for i in range(0, 12):
        if q_value[state][i] > max and q_value[state][i] != 0:
            option = i
            max = q_value[state][i]
    if max == 0 or max == -math.inf:
        return "-"
    if option == 8:
        return "U"
    elif option == 9:
        return "R"
    elif option == 10:
        return "D"
    elif option == 11:
        return "L"
    return option

def max2(state):
    max = -math.inf
    options = []
    for i in option_available:
        if q_value[state][i] > max:
            option = i
            max = q_value[state][i]
            options = [i]
        if q_value[state][i] == max:
            options.append(i)
    return  random.choice(options)

for j in range(nb_iterations):
    state = env._reset()
    done = False
    option = -1

    while done == False:
        option_available = choose_option(state) #return the list of options available in this state
        if random.random() > 0.1:
            option = max2(state)
        else:
            option = random.choice(option_available)
        s_prime, r, k, done = execute_option(env, option)
        q_value[state, option] += alpha*(r + gamma**k*np.max(q_value[s_prime]) - q_value[state, option])

        state = s_prime

    advance_statut(j/nb_iterations*100)

print(q_value)
print(q_value[25])
print(q_value[103])
print(q_value[18])
print("|", max(0), "|", max(1), "|", max(2), "|", max(3), "|", max(4), "| X |", max(26), "|", max(27), "|", max(28), "|", max(29), "|", max(30), "|")
print("|", max(5), "|", max(6), "|", max(7), "|", max(8), "|", max(9), "| X |", max(31), "|", max(32), "|", max(33), "|", max(34), "|", max(35), "|")
print("|", max(10), "|", max(11), "|", max(12), "|", max(13), "|", max(14), "|", max(25), "|", max(36), "|", max(37), "|", max(38), "|", max(39), "|", max(40), "|")
print("|", max(15), "|", max(16), "|", max(17), "|", max(18), "|", max(19), "| X |", max(41), "|", max(42), "|", max(43), "|", max(44), "|", max(45), "|")
print("|", max(20), "|", max(21), "|", max(22), "|", max(23), "|", max(24), "| X |", max(46), "|", max(47), "|", max(48), "|", max(49), "|", max(50), "|")
print("| X |", max(103), "| X | X | X | X |", max(51), "|", max(52), "|", max(53), "|", max(54), "|", max(55))
print("|", max(78), "|", max(79), "|", max(80), "|", max(81), "|", max(82), "| X | X | X |", "G", "| X | X |")
print("|", max(83), "|", max(84), "|", max(85), "|", max(86), "|", max(87), "| X |", max(57), "|", max(58), "|", max(59), "|", max(60), "|", max(61), "|")
print("|", max(88), "|", max(89), "|", max(90), "|", max(91), "|", max(92), "| X |", max(62), "|", max(63), "|", max(64), "|", max(65), "|", max(66), "|")
print("|", max(93), "|", max(94), "|", max(95), "|", max(96), "|", max(97), "|", max(77), "|", max(67), "|", max(68), "|", max(69), "|", max(70), "|", max(71), "|")
print("|", max(98), "|", max(99), "|", max(100), "|", max(101), "|", max(102), "| X |", max(72), "|", max(73), "|", max(74), "|", max(75), "|", max(76), "|")
