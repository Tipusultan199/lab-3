# Joint Control Example
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np

def main():
    joint_positions = [
        0,
        np.radians(90),
        np.radians(-90),
        np.radians(45)
    ]
    
    bot = InterbotixManipulatorXS(robot_model='px100', group_name='arm', gripper_name='gripper')
    bot.arm.go_to_home_pose()
    bot.arm.set_joint_positions(joint_positions)
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()
    bot.shutdown()

if __name__ == '__main__':
    main()
