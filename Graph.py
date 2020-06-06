class Graphic_computation:
    '''
    这是一个新手写的计算正方体，长方体和圆柱体，圆锥体等基础图形的程序!
    不喜勿喷!!!
    教程:
       实例对象:  test=Graphic_computation()     a表示长 b表示宽 h表示高 pi表示π(3.14,可以自己修改他的精度) v表示体积
                 s表示一切面积 l表示圆锥的母线 r表示半径 d表示直径 c表示周长 bottom_area表示底面积(不常用)。
                 例子:
                     test=Graphic_computation(r=5,h=11)
                     print(test.cone())      #表示计算一个半径为5 高为11的圆锥图形的体积和表面积!
    '''
    from decimal import Decimal
    from fractions import Fraction
    import math
    def __init__(self,a=None,b=None,h=None,pi='3.14',v=None,s=None,c=None,l=None,r=None,d=None,bottom_area=None):
        self.a=a
        self.b=b
        self.h=h
        self.pi=self.Decimal(pi)
        self.v=v
        self.s=s
        self.c=c
        self.l=l
        self.r=r
        self.d=d
        self.bottom_area=bottom_area
    def rectangle(self):
        if self.a!=None and self.b!=None:
            self.a=self.Decimal(self.a)
            self.b=self.Decimal(self.b)
        def circumference():
            self.c=(self.a+self.b)*2
            print('周长:',self.c)
            return self.c
        def area():
            self.s=self.a*self.b
            print('面积:',self.s)
            return self.s
        try:
            circumference()
            area()
        except TypeError:
            print('请在实例对象的时候，输入你的长和宽!')
            return 'TypeError'
        return 'successful'
    def parallelogram(self):
        if self.h!=None and self.a!=None:
            self.h=self.Decimal(self.h)
            self.a=self.Decimal(self.a)
        def area():
            self.s=self.a*self.h
            print('面积：',self.s)
            return self.s
        try:
            area()
        except TypeError:
            print('请在实例对象的时候，输入你的长和高!')
            return 'TypeError'
        return 'successful'
    def triangle(self):
        if self.h!=None and self.a!=None:
            self.a=self.Decimal(str(self.a))
            self.h=self.Decimal(str(self.h))
        def area():
            self.s=self.a*self.h/2
            print('面积:',self.s)
            return self.s
        self.area=area()
        try:
            area()
        except TypeError:
            print('请在实例对象的时候，输入你的长和高')
            return 'TypeError'
        return 'successful'
    def cone(self,fraction=False):
        if self.l!=None and self.r!=None:
            self.l=self.Decimal(str(self.l))
            self.r=self.Decimal(str(self.r))
        elif self.l==None and self.h!=None and self.r!=None or self.d!=None or self.c!=None or self.bottom_area!=None:
            self.h=self.Decimal(str(self.h))
            if self.d!=None and self.r==None:
                self.d=self.Decimal(str(self.d))
                self.r=self.d/2
            elif self.c!=None:
                self.c=self.Decimal(self.c)
                self.r=self.c/self.pi/2
            elif self.bottom_area!=None:
                self.bottom_area=self.Decimal(str(self.bottom_area))
                self.r=self.Decimal(str(self.math.sqrt(self.bottom_area/self.pi)))
            self.l=self.math.sqrt(self.math.pow(self.r,2)+self.math.pow(self.h,2))
            self.l=self.Decimal(self.l)
        def area():
            self.s=self.pi*self.r*self.l+self.pi*self.r*self.r      #计算表面积,公式:π*r*l+π*r*r
            print('表面积:',self.s)
            if fraction == True:
                print('表面积分数形式:',self.Fraction(self.s))
            return self.s
        def volume():
            self.v=self.pi*self.r*self.r*self.h*1/3        #计算体积,公式:π*r*r*h*1/3(/3)
            print('体积:',self.v)
            if fraction==True:
                print('体积分数形式:',self.Fraction(self.v))
            return self.v
        try:
            self.surface=area()
            self.volume=volume()
            return 'successful'
        except TypeError:
            return 'TypeError'
    def Cylinder(self,fraction=False,mian=2):
        self.mian=self.Decimal(str(mian))
        if self.r!=None or self.d!=None or self.c!=None or self.bottom_area!=None and self.h!=None:
            self.h = self.Decimal(str(self.h))
            if self.d!=None and self.r==None:
                self.d=self.Decimal(str(self.d))
                self.r=self.d/2
            elif self.c!=None and self.r==None:
                self.c=self.Decimal(str(self.c))
                self.r=self.c/self.pi/2
            elif self.bottom_area!=None and self.r==None:
                self.bottom_area=self.Decimal(str(self.bottom_area))
                self.r=self.Decimal(str(self.math.sqrt(self.bottom_area/self.pi)))
            else:
                self.r=self.Decimal(str(self.r))
        def volume():
            self.v=self.pi*self.r*self.r*self.h
            print('体积:', self.v)
            if fraction == True:
                print('体积分数形式:', self.Fraction(self.v))
            return self.v
        def area():
            self.s=self.Decimal(str(self.r*2*self.pi*self.h+self.pi*self.r*self.r*self.mian))
            print('表面积:',self.s)
            if fraction == True:
                print('表面积分数形式:', self.Fraction(self.s))
            return self.s
        try:
            self.volume=volume()
            self.area=area()
            return 'successful'
        except TypeError:
            return 'TypeError'
    def Cube(self):
        if self.a!=None:
            self.a=self.Decimal(str(self.a))
        def area():
            self.s=self.Decimal(str(self.math.pow(self.a,2)*6))
            print('表面积:',self.s)
            return self.s
        def volume():
            self.v=self.Decimal(str(self.math.pow(self.a,3)))
            print('体积:',self.v)
            return self.v
        try:
            self.area=area()
            self.volume=volume()
            return 'successful'
        except TypeError:
            return 'TypeError'
if __name__ == '__main__':
    test=Graphic_computation(bottom_area=314,h=20)
    print(test.Cylinder())