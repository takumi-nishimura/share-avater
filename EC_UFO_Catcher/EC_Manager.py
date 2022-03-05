import threading
import EC_GUI as gui
import EC_RobotControlManager as robot

if __name__ in '__main__':
	eye = gui.BREAK_OUT()
	arm = robot.RobotControl()
	t1 = threading.Thread(target=eye.show())
	t2 = threading.Thread(target=arm.SendDataToRobot())
	t1.start()
	t2.start()