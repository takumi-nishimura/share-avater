from cProfile import label
from turtle import position
import numpy as np
import pandas as pd
import math
import os

class HOMOGENEOUS:
	def __init__(self):
		pass

	def main(self, data:list):
		self.homogeneousPosition = []
		self.homogeneousRotation = []
		self.position = np.c_[data['x'],data['y'],data['z']]
		self.rotation = np.c_[data['qx'],data['qy'],data['qz'],data['qw']]
		
		self.originPosition = self.position[0]
		self.originRotation = self.rotation[0]
		self.inversedMatrixforPosition = self.SetInversedMatrixforPosition(self.originRotation)
		self.inversedMatrixforRotation = self.SetInversedMatrixforRotation(self.originRotation)

		for i in range(len(self.position)):
			self.homogeneousPosition.append(self.GetRelativePosition(self.position[i]))
			self.homogeneousRotation.append(self.GetRelativeRotation(self.rotation[i]))

		return self.homogeneousPosition, self.homogeneousRotation
		
	def GetRelativePosition(self, position):
		return np.dot(self.inversedMatrixforPosition, position - self.originPosition)

	def GetRelativeRotation(self, rotation):
		return np.dot(self.inversedMatrixforRotation, rotation)

	def SetInversedMatrixforPosition(self, rotation):		
		t = self.Quaternion2Euler(rotation)
		tx=np.deg2rad(t[0])
		ty=np.deg2rad(t[1])
		tz=np.deg2rad(t[2])
		
		Rx = np.array([[1, 0, 0],
			[0, np.cos(tx), -np.sin(tx)],
			[0, np.sin(tx), np.cos(tx)]])
		Ry = np.array([[np.cos(ty), 0, np.sin(ty)],
			[0, 1, 0],
			[-np.sin(ty), 0, np.cos(ty)]])
		Rz = np.array([[np.cos(tz), -np.sin(tz), 0],
			[np.sin(tz), np.cos(tz), 0],
			[0, 0, 1]])

		mat3x3 = np.dot(Rz, np.dot(Ry, Rx))

		return np.linalg.inv(mat3x3)

	def SetInversedMatrixforRotation(self, rotation) -> None:
		q = rotation

		qw, qx, qy, qz = q[3], q[0], q[1], q[2]
		mat4x4 = np.array([ [qw, -qz, qy, qx],
							[qz, qw, -qx, qy],
							[-qy, qx, qw, qz],
							[-qx,-qy, -qz, qw]])

		return np.linalg.inv(mat4x4)	

	def Quaternion2Euler(self, q, isDeg: bool = True):
		qx = q[0]
		qy = q[1]
		qz = q[2]
		qw = q[3]

		# 1 - 2y^2 - 2z^2
		m00 = 1 - (2 * qy**2) - (2 * qz**2)
		# 2xy + 2wz
		m01 = (2 * qx * qy) + (2 * qw * qz)
		# 2xz - 2wy
		m02 = (2 * qx * qz) - (2 * qw * qy)
		# 2xy - 2wz
		m10 = (2 * qx * qy) - (2 * qw * qz)
		# 1 - 2x^2 - 2z^2
		m11 = 1 - (2 * qx**2) - (2 * qz**2)
		# 2yz + 2wx
		m12 = (2 * qy * qz) + (2 * qw * qx)
		# 2xz + 2wy
		m20 = (2 * qx * qz) + (2 * qw * qy)
		# 2yz - 2wx
		m21 = (2 * qy * qz) - (2 * qw * qx)
		# 1 - 2x^2 - 2y^2
		m22 = 1 - (2 * qx**2) - (2 * qy**2)

		# 回転軸の順番がX->Y->Zの固定角(Rz*Ry*Rx)
		# if m01 == -1:
		# 	tx = 0
		# 	ty = math.pi/2
		# 	tz = math.atan2(m20, m10)
		# elif m20 == 1:
		# 	tx = 0
		# 	ty = -math.pi/2
		# 	tz = math.atan2(m20, m10)
		# else:
		# 	tx = -math.atan2(m02, m00)
		# 	ty = -math.asin(-m01)
		# 	tz = -math.atan2(m21, m11)

		# 回転軸の順番がX->Y->Zのオイラー角(Rx*Ry*Rz)
		if m02 == 1:
			tx = math.atan2(m10, m11)
			ty = math.pi/2
			tz = 0
		elif m02 == -1:
			tx = math.atan2(m21, m20)
			ty = -math.pi/2
			tz = 0
		else:
			tx = -math.atan2(-m12, m22)
			ty = -math.asin(m02)
			tz = -math.atan2(-m01, m00)

		if isDeg:
			tx = np.rad2deg(tx)
			ty = np.rad2deg(ty)
			tz = np.rad2deg(tz)

		rotEuler = np.array([tx, ty, tz])
		return rotEuler

	def Graph(self, position, position1, position2):
		self.x = []
		self.y = []
		self.z = []
		self.x1 = []
		self.y1 = []
		self.z1 = []
		self.x2 = []
		self.y2 = []
		self.z2 = []
		for i in range(len(position)):
			self.x.append(position[i][0])
			self.y.append(position[i][1])
			self.z.append(position[i][2])
			self.x1.append(position1[i][0])
			self.y1.append(position1[i][1])
			self.z1.append(position1[i][2])
			self.x2.append(position2[i][0])
			self.y2.append(position2[i][1])
			self.z2.append(position2[i][2])
		print(self.x[1])
		print(self.x1[1])
		print(self.x2[1])
		import matplotlib.pyplot as plt
		self.fig = plt.figure()
		self.ax = plt.gca(projection='3d')
		self.ax.plot(self.x,self.y,self.z,label='robot')
		self.ax.plot(self.x1,self.y1,self.z1,label='1')
		self.ax.plot(self.x2,self.y2,self.z2,label='2')
		self.ax.set_box_aspect((1,1,1))
		self.ax.legend(loc="upper right",bbox_to_anchor=(1.1,1.1))
		plt.show()

if __name__ == '__main__':
	d_r = pd.read_csv('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/data/ExportData/Tanaka_B_1_Transform_endEffector_20220117_1837.csv')
	d_1 = pd.read_csv('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/data/ExportData/Tanaka_B_1_Transform_Participant_1_20220117_1837.csv')
	d_2 = pd.read_csv('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/data/ExportData/Tanaka_B_1_Transform_Participant_2_20220117_1837.csv')
	homogeneous = HOMOGENEOUS()
	pos_r, rot_r = homogeneous.main(data=d_r)
	pos_1, rot_1 = homogeneous.main(data=d_1)
	pos_2, rot_2 = homogeneous.main(data=d_2)
	homogeneous.Graph(pos_r,pos_1,pos_2)