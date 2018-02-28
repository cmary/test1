class Home:
    def __init__(self, new_are, new_fuxing, new_addr):
        self.are = new_are
        self.fuxing = new_fuxing
        self.addr = new_addr
        self.info = new_are
        self.left_are = new_are
        self.jiaju=[]

    def __str__(self):
        return "房子的面积：%d，可用面积：%d,家具有：%s，户型：%s，地址是：%s"%(self.are, self.left_are,str(self.jiaju), self.fuxing, self.addr)
    def add_item(self,item):
        self.left_are-=item.get_are()
        self.jiaju.append(item.get_name())

class Bed:
    def __init__(self,new_name,new_are):
        self.name=new_name
        self.are=new_are
    def __str__(self):
        return "%s占用的面积：%d"%(self.name,self.are)
    def get_are(self):
        return self.are
    def get_name(self):
        return self.name
fangzi=Home(192,"四室两厅","北京市长安街888号")
print(fangzi)
bed=Bed("席梦思",4)
bed1=Bed("席梦思1",6)
print(bed)
print(bed1)
fangzi.add_item(bed)
fangzi.add_item(bed1)
print (fangzi)
