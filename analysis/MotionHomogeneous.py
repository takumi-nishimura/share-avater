import numpy as np
import pandas as pd
import math

class HOMOGENEOUS:
	def __init__(self) -> None:
		pass

	def homogeneous(self,data):
		self.homogeneousPosition = []
		self.homogeneousRotation = []
		self.position = np.c_[data['x'],data['y'],data['z']]
		self.rotation = np.c_[data['qx'],data['qy'],data['qz'],data['qw']]

		self.originPosition = self.position[0]
		self.originRotation = self.rotation[0]
		self.inversedMatrixforPosition = self.SetInversedMatrixforPosition(self.originRotation)
		self.inversedMatrixforRotation = self.SetInversedMatrixforRotation(self.originRotation)

		for i in range(len(self.position)):
			self.pos_relative = np.dot(self.inversedMatrixforPosition,self.position[i]-self.originPosition)
			self.rot_relative = self.Quaternion2Euler(np.dot(self.inversedMatrixforRotation,self.rotation[i]))
			self.homogeneousPosition.append([self.pos_relative[2],self.pos_relative[0],self.pos_relative[1]])
			self.homogeneousRotation.append([self.rot_relative[2],self.rot_relative[0],self.rot_relative[1]])

		return self.homogeneousPosition, self.homogeneousRotation

	def SetInversedMatrixforPosition(self,rotation):
		t = self.Quaternion2Euler(rotation)
		tx = np.deg2rad(t[0])
		ty = np.deg2rad(t[1])
		tz = np.deg2rad(t[2])

		Rx = np.array([[1,0,0],[0,np.cos(tx),-np.sin(tx)],[0,np.sin(tx),np.cos(tx)]])
		Ry = np.array([[np.cos(ty),0,np.sin(ty)],[0,1,0],[-np.sin(ty),0,np.cos(ty)]])
		Rz = np.array([[np.cos(tz),-np.sin(tz),0],[np.sin(tz),np.cos(tz),0],[0,0,1]])

		mat3x3 = np.dot(Rx,np.dot(Ry,Rz))
		return np.linalg.inv(mat3x3)

	def SetInversedMatrixforRotation(self,rotation):
		q = rotation
		qw,qx,qy,qz = q[3],q[0],q[1],q[2]

		mat4x4 = np.array([[qw,-qz,qy,qx],[qz,qw,-qx,qy],[-qy,qx,qw,qz],[-qx,-qy,-qz,qw]])
		return np.linalg.inv(mat4x4)

	def Quaternion2Euler(self,q):
		qx = q[0]
		qy = q[1]
		qz = q[2]
		qw = q[3]

		m00 = 1 - (2 * qy**2) - (2 * qz**2)
		m01 = (2 * qx * qy) + (2 * qw * qz)
		m02 = (2 * qx * qz) - (2 * qw * qy)
		m10 = (2 * qx * qy) - (2 * qw * qz)
		m11 = 1 - (2 * qx**2) - (2 * qz**2)
		m12 = (2 * qy * qz) + (2 * qw * qx)
		m20 = (2 * qx * qz) + (2 * qw * qy)
		m21 = (2 * qy * qz) - (2 * qw * qx)
		m22 = 1 - (2 * qx**2) - (2 * qy**2)

		if m02 == 1:
			tx = math.atan2(m10,m11)
			ty = math.pi/2
			tz = 0
		elif m02 == -1:
			tx = math.atan2(m21,m20)
			ty = -math.pi/2
			tz = 0
		else:
			tx = -math.atan2(-m21,m22)
			ty = -math.asin(m02)
			tz = -math.atan2(-m01,m00)

		return np.array([tx,ty,tz])