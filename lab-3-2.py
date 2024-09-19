# Pick-and-Place Example
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np
import time

def main():
    bot = InterbotixManipulatorXS(robot_model='px100', group_name='arm', gripper_name='gripper')
    bot.arm.go_to_home_pose()
    time.sleep(2)
    bot.arm.set_ee_cartesian_trajectory(z=0.1)
    time.sleep(2)
    bot.arm.set_ee_cartesian_trajectory(x=0.15)
    time.sleep(2)
    bot.arm.set_ee_cartesian_trajectory(z=-0.10)
    time.sleep(2)
    bot.gripper.grasp(50.0)
    time.sleep(2)
    bot.arm.set_ee_cartesian_trajectory(z=0.2)
    time.sleep(2)
    bot.arm.set_single_joint_position(joint_name='waist', position=np.radians(-90))
    time.sleep(2)
    bot.arm.set_ee_cartesian_trajectory(z=-0.15)
    time.sleep(2)
    bot.gripper.release(50.0)
    time.sleep(2)
    bot.arm.set_ee_cartesian_trajectory(z=0.1)
    time.sleep(2)
    bot.arm.go_to_home_pose()
    time.sleep(2)
    bot.arm.go_to_sleep_pose()
    bot.shutdown()

if __name__ == '__main__':
    main()
