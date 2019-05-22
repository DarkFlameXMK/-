from Oscilloscope import Oscilloscope
from tkinter import *
import numpy as np
import threading

#创建窗口
root = Tk()
root.title("多线程示波器")

#创建frame
frame1 = LabelFrame(height = 600,width = 700,bg='white',text = 'sin',font = ('黑体',30))
frame2 = LabelFrame(height = 600,width = 700,bg='white',text = 'cos',font = ('黑体',30))
#判断是否已经开始画图的参数
begin = 0
#定义开始画图命令
def start():
    global begin
    if begin == 0:
        begin = 1
        # 实例化示波器
        a = Oscilloscope(frame=frame1)
        b = Oscilloscope(xlim=(200, 0.05), y_lim=(-1.9, 1.9), color='red', frame=frame2)
        #导入数据
        a.input_list()
        b.input_list(xs_list=np.arange(0, 15, 0.05), ys_list=np.cos(np.arange(0, 15, 0.05)))
        #定义线程
        t1 = threading.Thread(target=a.run,kwargs={'speed':25},name='1')
        t2 = threading.Thread(target=b.run, name='2')
        #开始线程
        t2.start()
        t1.start()
    else:
        pass

#创建开始按钮
B_n = Button(root, text='开始', command=start)

#放置组件
B_n.pack(side = 'bottom',expand='no', fill='x')
frame1.pack(side='left',expand = 'yes', fill='both')
frame2.pack(side = 'right',expand = 'yes', fill='both')


root.mainloop()