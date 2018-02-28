def main():
	'''控制'''
	pass


class Person(object):
	"""docstring for proson"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name
		self.qiang=None
		self.hp=100

	def anzhaung(self,danjia,zidan,shu):
		'''把子弹装入弹夹中'''
		return danjia.baocun(shu,zidan)


	def danjia_anzhuang(self,gun,danjia):
		''''把弹夹安装到枪里'''
		#gun.baocun_danjia(danjia)
		gun.baocun_danjia(danjia)

	def nagun(self,gun):
		self.qiang=gun

	def __str__(self):
		if self.qiang:
			return "%s 的血量：%d ,他有枪%s"%(self.name,self.hp,self.qiang)
		else:
			return"%s 的血量：%d ,他没有枪"%(self.name,self.hp)

	def shoot(self,ci,diren):
		if self.qiang:
			self.qiang.fire(ci)
		else:
			return"他没有枪"
	def diaoxue(self,diren,ci):
		xue = self.qiang.dazhong(ci)
		#print (xue)
		diren.hp = diren.hp - xue

	
	
		


class Gun(object):
	"""docstring for Gun"""
	def __init__(self, gun):
		super(Gun, self).__init__()
		self.gun = gun
		self.dj=None

	def baocun_danjia(self,danjia):
		'''用一个属性来保存弹夹'''
		self.dj= danjia

	def fire(self,ci):
		self.dj.tan(ci)

	def dazhong(self,ci):
		return self.dj.ss(ci)



	def __str__(self):
		return "枪的型号：%s,弹夹为：%s"%(self.gun,self.dj)




class Danjia(object):
		"""docstring for Danjia"""
		def __init__(self, num):
			super(Danjia, self).__init__()
			self.num = num
			self.shuliang = 0
			self.max = 0  #每颗子弹的威力


		def baocun(self,shu,zidan):
			'''将子弹保存'''

			self.shuliang = shu
			self.max = zidan.max
			return "弹夹的子弹数量%d ,每颗子弹的威力：%d"%(self.shuliang,self.max)

		def tan(self,ci):
			self.shuliang =self.shuliang - ci

		def ss(self,ci):
			return int(ci * self.max)
			


		def __str__(self):
			return "弹夹容量：%d ,弹夹现有子弹：%d 颗"%(self.num,self.shuliang)


class Zidan(object):
			"""docstring for Zidan"""
			def __init__(self, max,number):
				super(Zidan, self).__init__()
				self.max = max
				self.number=number

			def dazhong(self):
				return self.max


			def __str__(self):
				return "子弹的杀伤力为：%s 数量为:%s"%(self.max,self.number)
					
#创建老王
laowang = Person("老王")

#创建枪对象
ak = Gun("ak47")

#创建弹夹
danjia = Danjia(20)

#创建子弹
zidan = Zidan(5,15)
print (zidan.__str__())

#创建敌人
diren =Person("敌人")

#创建老王把子弹装入弹夹
shu = int(input("需要装入弹夹的子弹数量："))

laowang.anzhaung(danjia,zidan,shu)

#创建老王把弹夹装到抢中
laowang.danjia_anzhuang(ak,danjia)
print(ak)
#创建老王拿枪
laowang.nagun(ak)

print(laowang)
print(diren)
#创建老王开枪
ci=int(input("要射击次数"))
laowang.shoot(ci,diren)
print(laowang)
laowang.diaoxue(diren,ci)
#创建老王打敌人
print(diren)