import numpy as np
import math
import random

#Starting states for each option
I_room0_right_0 = np.linspace(0, 24, 25)
I_room0_right_0 = np.append(I_room0_right_0, 103)
I_room0_down_1 = range(0, 25+1)
I_room1_left_2 = range(26, 56+1)
I_room1_down_3 = range(25, 55+1)
I_room2_up_4 = range(57, 77+1)
I_room2_left_5 = range(56, 76+1)
I_room3_up_6 = range(77, 102+1)
I_room3_right_7 = range(78, 103+1)
#q_values for each option
#q_table_0 = (np.zeros([4, len(I_room0_right_0)+1]).tolist())
#q_table_0.insert(0, list(I_room0_right_0))
q_table_0 = (np.zeros([4, 103+1]).tolist())
q_table_0.insert(0, list(range(104)))

q_table_1 = (np.zeros([4, 103+1]).tolist())
q_table_1.insert(0, list(range(104)))

q_table_2 = (np.zeros([4,  103+1]).tolist())
q_table_2.insert(0, list(range(104)))

q_table_3 = (np.zeros([4,  103+1]).tolist())
q_table_3.insert(0, list(range(104)))

q_table_4 = (np.zeros([4,  103+1]).tolist())
q_table_4.insert(0, list(range(104)))

q_table_5 = (np.zeros([4,  103+1]).tolist())
q_table_5.insert(0, list(range(104)))

q_table_6 = (np.zeros([4,  103+1]).tolist())
q_table_6.insert(0, list(range(104)))

q_table_7 = (np.zeros([4,  103+1]).tolist())
q_table_7.insert(0, list(range(104)))


def choose_option(state):
    available_option = []
    if state in I_room0_right_0:
        available_option.append(0)
    if state in I_room0_down_1:
        available_option.append(1)
    if state in I_room1_left_2:
        available_option.append(2)
    if state in I_room1_down_3:
        available_option.append(3)
    if state in I_room2_up_4:
        available_option.append(4)
    if state in I_room2_left_5:
        available_option.append(5)
    if state in I_room3_up_6:
        available_option.append(6)
    if state in I_room3_right_7:
        available_option.append(7)
    available_option.append(8)
    available_option.append(9)
    available_option.append(10)
    available_option.append(11)
    return available_option

def execute_option(env, option):
    if option == 0:
        return option_0(env)
    if option == 1:
        return option_1(env)
    if option == 2:
        return option_2(env)
    if option == 3:
        return option_3(env)
    if option == 4:
        return option_4(env)
    if option == 5:
        return option_5(env)
    if option == 6:
        return option_6(env)
    if option == 7:
        return option_7(env)
    if option == 8: #"UP" = 0
        next_state, reward, done, info = env.step(0, False)
        return next_state, reward, 1, done
    if option == 9: #"RIGHT" = 1
        next_state, reward, done, info = env.step(1, False)
        return next_state, reward, 1, done
    if option == 10: #"DOWN" = 2
        next_state, reward, done, info = env.step(2, False)
        return next_state, reward, 1, done
    if option == 11: #"LEFT" = 3
        next_state, reward, done, info = env.step(3, False)
        return next_state, reward, 1, done

def max(q_table, index, beta):
    max = -math.inf
    if index == beta:
        return 0, 10
    action = -1
    if q_table[1][index] > max:
        max = q_table[1][index]
        action = 0
    if q_table[2][index] > max:
        max = q_table[2][index]
        action = 1
    if q_table[3][index] > max:
        max = q_table[3][index]
        action = 2
    if q_table[4][index] > max:
        max = q_table[4][index]
        action = 3
    return action, max


def option_0(env):
#    print(q_table_0)
    hallway_goal = 25
    beta = hallway_goal
    return q_learning(env, q_table_0, beta)

def option_1(env):
    #I_room0_down_1 = range(0, 25+1)
#    print(q_table_1)
    hallway_goal = 103
    beta = hallway_goal
    return q_learning(env, q_table_1, beta)

def option_2(env):
    #I_room1_left_2 = range(26, 56+1)
#    print(q_table_2)
    hallway_goal = 25
    beta = hallway_goal
    return q_learning(env, q_table_2, beta)

def option_3(env):
    #I_room1_down_3 = range(25, 55+1)
#    print(q_table_3)
    hallway_goal = 56
    beta = hallway_goal
    return q_learning(env, q_table_3, beta)

def option_4(env):
    #I_room2_up_4 = range(57, 77+1)
#    print(q_table_4)
    hallway_goal = 56
    beta = hallway_goal
    return q_learning(env, q_table_4, beta)

def option_5(env):
    #I_room2_left_5 = range(56, 76+1)
#    print(q_table_5)
    hallway_goal = 77
    beta = hallway_goal
    return q_learning(env, q_table_5, beta)

def option_6(env):
    #I_room3_up_6 = range(77, 102+1)
#    print(q_table_6)
    hallway_goal = 103
    beta = hallway_goal
    return q_learning(env, q_table_6, beta)

def option_7(env):
    #I_room3_right_7 = range(78, 103+1)
#    print(q_table_7)
    hallway_goal = 77
    beta = hallway_goal
    return q_learning(env, q_table_7, beta)

def q_learning(env, q_table, beta):
    #Q_Learning parameters
    nbStep, reward, = 0, 0
    earned_reward = 0
    state = env.state
    alpha = 0.9
    gamma = 0.3
    done = False

    while True:
        index_state = q_table[0].index(state)
        action, maxi = max(q_table, index_state, beta)
#        print(state)
#        print(action)
        next_state, reward, done, info = env.step(action, False)
        index_next_state = q_table[0].index(next_state)
        earned_reward += reward
        a, next_max = max(q_table, index_next_state, beta)
        q_table[action+1][index_state] = q_table[action+1][index_state] + alpha * (reward + gamma*next_max - q_table[action+1][index_state]) #Q_Leraning
        nbStep += 1
        state = next_state

        if beta == state or done:
            break


    return state, earned_reward, nbStep, done
