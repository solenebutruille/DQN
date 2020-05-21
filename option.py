import numpy as np
import math

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
q_table_0 = [list(I_room0_right_0)]
q_table_0.append([1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0])

q_table_1 = [list(I_room0_down_1)]
q_table_1.append([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 3, 3, 3])

q_table_2 = [list(I_room1_left_2)]
q_table_2.append([2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 0])

q_table_3 = [list(I_room1_down_3)]
q_table_3.append([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 3, 3])

q_table_4 = [list(I_room2_up_4)]
q_table_4.append([1, 1, 0, 3, 3, 1, 0, 0, 0, 3, 1, 0, 0, 0, 3, 1, 1, 0, 3 ,3, 1])

q_table_5 = [list(I_room2_left_5)]
q_table_5.append([2, 2, 2, 2, 2, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3])

q_table_6 = [list(I_room3_up_6)]
q_table_6.append([3, 1, 0, 3, 3, 3, 1, 0, 3, 3, 3, 1, 0, 0, 0, 3, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3])

q_table_7 = [list(I_room3_right_7)]
q_table_7.append([1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 0, 2])

def choose_option(state):
#    available_option = [8, 9, 10, 11]
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


def take_action(q_table, index):
    return q_table[1][index]

def option_0(env):
    hallway_goal = 25
    beta = hallway_goal
    return q_learning(env, q_table_0, beta, 0)

def option_1(env):
    hallway_goal = 103
    beta = hallway_goal
    return q_learning(env, q_table_1, beta, 1)

def option_2(env):
    hallway_goal = 25
    beta = hallway_goal
    return q_learning(env, q_table_2, beta, 2)

def option_3(env):
    hallway_goal = 56
    beta = hallway_goal
    return q_learning(env, q_table_3, beta, 3)

def option_4(env):
    hallway_goal = 56
    beta = hallway_goal
    return q_learning(env, q_table_4, beta, 4)

def option_5(env):
    hallway_goal = 77
    beta = hallway_goal
    return q_learning(env, q_table_5, beta, 5)

def option_6(env):
    hallway_goal = 103
    beta = hallway_goal
    return q_learning(env, q_table_6, beta, 6)

def option_7(env):
    hallway_goal = 77
    beta = hallway_goal
    return q_learning(env, q_table_7, beta, 7)

def q_learning(env, q_table, beta, option):
    #Q_Learning parameters
    nbStep, reward, earned_reward = 0, 0, 0
    state = env.state
    gamma = 0.9
    done = False
    while True:
        try:
            index_state = q_table[0].index(state)
        except:
            if option in [0, 1]  and  57 >= state >= 25 :
                state_o, earned_reward_o, nbStep_o, done_o = option_2(env)
            elif option in [0, 1] and  103 >= state >= 77 :
                state_o, earned_reward_o, nbStep_o, done_o = option_6(env)
            elif option in [2, 3]  and  25 >= state >= 0 :
                state_o, earned_reward_o, nbStep_o, done_o = option_0(env)
            elif option in [2, 3] and  76 >= state >= 56 :
                state_o, earned_reward_o, nbStep_o, done_o = option_4(env)
            elif option in [4, 5]  and  56 >= state >= 26 :
                state_o, earned_reward_o, nbStep_o, done_o = option_3(env)
            elif option in [4, 5] and  103 >= state >= 77 :
                state_o, earned_reward_o, nbStep_o, done_o = option_7(env)
            elif option in [6, 7]  and  (24 >= state >= 0 or state == 103)  :
                state_o, earned_reward_o, nbStep_o, done_o = option_1(env)
            elif option in [6, 7] and  77 >= state >= 57 :
                state_o, earned_reward_o, nbStep_o, done_o = option_5(env)
            else:
                print("state", state)
            state = state_o
            earned_reward += earned_reward_o
            nbStep += nbStep_o
            index_state = q_table[0].index(state)
        action = take_action(q_table, index_state)
        next_state, reward, done, info = env.step(action, True)
        earned_reward += reward*gamma**nbStep
        nbStep += 1
        state = next_state
        if beta == state:
            break

    return state, earned_reward, nbStep, done
