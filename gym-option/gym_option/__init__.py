from gym.envs.registration import register

register(
    id='option-v0',
    entry_point='gym_option.envs:OptionEnv',
)
register(
    id='option-extrahard-v0',
    entry_point='gym_option.envs:OptionExtraHardEnv',
)
