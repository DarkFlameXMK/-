import numpy as np
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
class Oscilloscope():
    '''
    可以将数据进行波形动态可视化的示波器
    xlim：包含两个元素的元祖，第一个是示波器x轴的显示宽度，第二个是x轴的移动步长
    ylim：包含两个元素的元祖，第一个是y轴上边界，第二个是y轴下边界
    color：字符串，用于设置曲线颜色
    frame：窗口中的frame控件，示波器的图像就输出在这个frame上
    '''
    def __init__(self,xlim=(70,0.03),y_lim=(-1.2,1.2),color='blue',frame=None):
        #x,y是每一帧所实际用到的数据集
        self.x = []
        self.y = []
        #xs,ys是总的数据集
        self.xs = []
        self.ys = []
        #实例化一张图片
        self.fig = Figure(figsize=(7,6),facecolor="white")
        #接收frame控件
        self.frame = frame
        #将图片输出到frame
        self.canvs = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvs.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #向图片添加子图
        self.ax1 = self.fig.add_subplot(111)
        #导入示波器的坐标轴配置参数
        self.xlim_count = xlim[0]
        self.xlim_step = xlim[1]
        self.y_lim_bottom = y_lim[0]
        self.y_lim_top = y_lim[1]
        #接收颜色参数
        self.color = color
        #初始化一个数据为空的plot动作，后面会通过update方法输入数据
        self.p1, = self.ax1.plot(self.x, self.y, linestyle="-", color = self.color)

    #输入总数据集（默认输入一个0到5的sin函数）
    def input_list(self,xs_list=np.arange(0, 5, 0.03),ys_list=np.sin(np.arange(0, 5, 0.03))):
        self.xs = xs_list
        self.ys = ys_list
        print('list input')

    #定义一个数据更新器，更新示波器每一帧所用到的数据
    def update(self,i):
        self.x.append(self.xs[i])
        self.y.append(self.ys[i])
        if len(self.x) > self.xlim_count:
            self.x.pop(0)
            self.ax1.set_xlim(min(self.x), max(self.x) + self.xlim_step)
        else:
            self.ax1.set_xlim(0, self.xlim_count*self.xlim_step)
        if len(self.y) > self.xlim_count:
            self.y.pop(0)
        self.ax1.set_ylim(self.y_lim_bottom, self.y_lim_top)
        self.p1.set_data(self.x, self.y)
        if self.x[-1] == self.xs[-1]:
            self.x = []
            self.y = []
        return self.p1

    #定义示波器运行方法
    def run(self,speed = 25):
        '''
        运行示波器
        speed表示更新速度
        '''
        #利用matplotlib中的FuncAnimation方法更新图像
        ani = FuncAnimation(fig=self.fig, func=self.update, frames=len(self.xs), interval=1000/speed)
        #更新frame控件显示的内容
        self.frame.update()


