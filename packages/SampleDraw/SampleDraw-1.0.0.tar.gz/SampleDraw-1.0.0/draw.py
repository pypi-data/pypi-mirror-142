'''这是一个自制的简易画图程序'''

from tkinter import *
from tkinter.colorchooser import askcolor

class Application(Frame):
    def __init__(self,master=None):
        self.master=master
        super().__init__(master)
        self.pack()
        self.last=0
        self.StartDraw=True                #判断是不是第一次画
        self.x=0
        self.y=0
        self.bg='gray'
        self.pencolor='red'
        
        self.createWidget()
        
    #创建主键功能区
    def createWidget(self):
        #创建一个画布
        self.cav=Canvas(self,bg=self.bg,width=2000,height=450)
        self.cav.pack()
        #创建操作按钮
        self.linebtn=Button(self,relief='groove',border=2,name='line',text='直线',padx=30)
        self.linebtn.pack(side='left',padx=5,pady=10)
        self.circlebtn=Button(self,relief='groove',border=2,name='circle',text='圆形',padx=30)
        self.circlebtn.pack(side='left',padx=5,pady=10)  
        self.squrbtn=Button(self,relief='groove',border=2,name='squr',text='矩形',padx=30)
        self.squrbtn.pack(side='left',padx=5,pady=10) 
        self.quxianbtn=Button(self,relief='groove',border=2,name='arrow',text='带箭头直线',padx=30)
        self.quxianbtn.pack(side='left',padx=5,pady=10)  
        self.quxianbtn=Button(self,relief='groove',border=2,name='quxian',text='曲线',padx=30)
        self.quxianbtn.pack(side='left',padx=5,pady=10)  
        self.xiangpi=Button(self,relief='groove',border=2,name='xiangpi',text='橡皮',padx=30)
        self.xiangpi.pack(side='left',padx=5,pady=10)
        self.clearAll=Button(self,relief='groove',border=2,name='clear',text='清屏',padx=30)
        self.clearAll.pack(side='left',padx=5,pady=10)  
        self.pen=Button(self,relief='groove',border=2,name='pencolor',text='画笔颜色',padx=30)
        self.pen.pack(side='left',padx=5,pady=10) 
        self.cavcolor=Button(self,relief='groove',border=2,name='cavcolor',text='画布颜色',padx=30)
        self.cavcolor.pack(side='left',padx=5,pady=10) 
        #绑定所有按钮左键单击触发事件
        self.pen.bind_class('Button','<1>',self.MainManger)
        #绑定所有松开鼠标左键时的案件
        self.cav.bind('<ButtonRelease-1>',self.stopDraw)
    
    #停止画画的程序，并重新进行初始化
    def stopDraw(self,event):
         self.StartDraw=True  #重新开始画
         self.last=0          #另删除变量为0，则无法删除上一回画的
    
    #统一的画笔主管理器
    def MainManger(self,event):
        name=event.widget.winfo_name()
        if(name=='line' ): #画直线
             self.cav.bind('<B1-Motion>',self.line) 
        elif(name=='clear'):#清屏
            self.cav.delete(ALL)  
        elif(name=='circle'):#画圆形 
            self.cav.bind('<B1-Motion>',self.circle) 
        elif(name=='squr' ):#画圆形 
            self.cav.bind('<B1-Motion>',self.squr) 
        elif(name=='quxian'):#画曲线 
            self.cav.bind('<B1-Motion>',self.quxian) 
        elif(name=='arrow' ):#画箭头直线 
            self.cav.bind('<B1-Motion>',self.arrow) 
        elif(name=='cavcolor'):#修改画布颜色
            cavcolor=askcolor(title='选择画布颜色',color=self.bg)
            self.cav.config(bg=cavcolor[1])
        elif(name=='pencolor'):#修改画布颜色
            cavcolor=askcolor(title='选择画布颜色',color=self.pencolor)
            self.pencolor=cavcolor[1]
        elif(name=='xiangpi'):#修改画布颜色
           self.cav.bind('<B1-Motion>',self.xiangpica)
        else:pass
            
    #绘画前的统一封装设置
    def DrawSet(self,event):  
         self.cav.delete(self.last)  #清除的是每次画完图返回来的ID，所以无论如何都只会留下最后一个   
         #此if只执行一次的目的就只是为了得到当前鼠标点击时的坐标参数，从而得到起始点开始画画
         if(self.StartDraw==True):
            self.x=event.x
            self.y=event.y
            self.StartDraw=False
             
    #画直线的方法         
    def line(self,event):
        self.DrawSet(event)
        self.last= self.cav.create_line(self.x,self.y,event.x,event.y,fill=self.pencolor)      
    #画圆形的方法         
    def circle(self,event):
        self.DrawSet(event)
        self.last= self.cav.create_oval(self.x,self.y,event.x,event.y,outline=self.pencolor)
    #画矩形的方法         
    def squr(self,event):
        self.DrawSet(event)
        self.last= self.cav.create_rectangle(self.x,self.y,event.x,event.y,outline=self.pencolor)
    #画箭头直线的方法         
    def arrow(self,event):
        self.DrawSet(event)
        self.last= self.cav.create_line(self.x,self.y,event.x,event.y,fill=self.pencolor,arrow='last')
    #画曲线的方法         
    def quxian(self,event):
        self.DrawSet(event)
        self.cav.create_line(self.x,self.y,event.x,event.y,fill=self.pencolor)  #不要回传参数是避免删除画布
        #把最后一个点的坐标当作新画的起始坐标
        self.x=event.x
        self.y=event.y
    #橡皮擦的方法
    def xiangpica(self,event):
        self.DrawSet(event)
        self.cav.create_rectangle(self.x,self.y,event.x,event.y,fill=self.bg,outline=self.bg)
        #橡皮的实质就是画一个矩形，用背景色填充
    
root=Tk()
Application(master=root)
root.title('简易画图')
root.geometry('1000x500+100+100')
root.mainloop()