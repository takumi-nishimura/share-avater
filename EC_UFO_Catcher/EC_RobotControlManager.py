from xarm.wrapper import XArmAPI
import time

class RobotControl():
	def __init__(self):
		self.xArmIP = '192.168.1.240'

	def SendDataToRobot(self,isEnablexArm=False):
		if isEnablexArm:
			self.arm = XArmAPI(self.xArmIP)
			self.InitializeAll(self.arm)

		self.isMoving = False

		try:
			while True:
				if self.isMoving:
					print('aaa')

				else:
						keycode = input('Input > "q": quit, "r": Clean error and init arm, "s": start control \n')
						if keycode == 'q':
							if isEnablexArm:
								self.arm.disconnect()
							self.PrintProcessInfo()
							break

						elif keycode == 'r':
							if isEnablexArm:
								self.InitializeAll(self.arm)

						elif keycode == 's':					
							self.isMoving    = True
							self.taskStartTime = time.perf_counter()

		except KeyboardInterrupt:
			print('\nKeyboardInterrupt >> Stop: RobotControlManager.SendDataToRobot()')

			self.taskTime = time.perf_counter() - self.taskStartTime
			self.PrintProcessInfo()

	def PrintProcessInfo(self):
		print('----- Process info -----')
		print('Task time\t > ', self.taskTime, '[s]')
		print('------------------------')

	def InitializeAll(self,robotArm,isSetInitPosition=True):
		robotArm.connect()
		if robotArm.warn_code != 0:
			robotArm.clean_warn()
		if robotArm.error_code != 0:
			robotArm.clean_error()
		robotArm.motion_enable(enable=True)
		robotArm.set_mode(0)             # set mode: position control mode
		robotArm.set_state(state=0)      # set state: sport state
		if isSetInitPosition:
			initX, initY, initZ, initRoll, initPitch, initYaw = 200,0,200,180,0,0
			print(initX)
			robotArm.set_position(x=initX, y=initY, z=initZ, roll=initRoll, pitch=initPitch, yaw=initYaw, wait=True)
		else:
			robotArm.reset(wait=True)
		print('Initialized > xArm')

		robotArm.set_tgpio_modbus_baudrate(2000000)
		robotArm.set_gripper_mode(0)
		robotArm.set_gripper_enable(True)
		robotArm.set_gripper_position(850, speed=5000)
		robotArm.getset_tgpio_modbus_data(self.ConvertToModbusData(425))
		print('Initialized > xArm gripper')

		robotArm.set_mode(1)
		robotArm.set_state(state=0)

if __name__ in '__main__':
	RobotControl().SendDataToRobot(False)