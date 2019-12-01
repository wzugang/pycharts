#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt

class chart(object):
    def __init__(self, line, row, type):
        self.line = line
        self.row = row
        self.type = type
        self.num = line*row
        self.index = 1
    
    def plot(self, title, x, y, xlabel, ylabel, color="blue", linewidth=2.0, linestyle="-", label="none"):
        if self.index <= self.num:
            plt.subplot(self.line, self.row, self.index)
            plt.title(title)
            plt.plot(x, y, color=color, linewidth=linewidth, linestyle=linestyle, label=label)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            self.index = self.index + 1
    
    def title(self, title):
        plt.title(title)
    
    def show(self):
        plt.show()
    
    def xlimit(self, min, max):
        plt.xlim(min, max)
    
    def ylimit(self, min, max):
        plt.ylim(min, max)
    
    #散点图
    def scatter(self, x, y, size=80, color="blue"):
        plt.scatter(x, y, size, color=color)
    
    #设置长(英寸)、宽(英寸)、单位分辨率
    def figure(self, length, width, resolution):
        self.fig=plt.figure(figsize=(length, width), dpi=resolution)
    
    def xticks(self, ticks):
        plt.xticks(ticks)
    
    def yticks(self, ticks):
        plt.yticks(ticks)
    
    def legend(self, location="upper left"):
        plt.legend(loc=location)
    
    def legend2(self, bbox_to_anchor=(0, 1, 1, 0.1), ncol=1, mode="expand", borderaxespad=0.):
        plt.legend(bbox_to_anchor=bbox_to_anchor, ncol=ncol, mode=mode, borderaxespad=borderaxespad)
    
    #text为文本位置, xytext为文本起始位置, xy为标记点
    def annotate(self, text, xytext, xy, fontsize=12, arrowprops=dict(arrowstyle="->", connectionstyle="arc", facecolor="red")): #width=3, headlength=5, headwidth=5, shrink=0.1
        plt.annotate(text, xytext=xytext, xy=xy, fontsize=fontsize, arrowprops=arrowprops)
    
    def grid(self, color="red", linestyle="--"):
        plt.grid(color=color, linestyle=linestyle)

    def axis(self, xmin, xmax, ymin, ymax):
        plt.axis([xmin, xmax, ymin, ymax])
    
    def save(self, name):
        self.fig.savefig(name)
    
    def marker(self, type="s", size=10, color="blue"):
        plt.marker(type)
        plt.markersize(size)
        plt.markerfacecolor(color)
    
    #条形图
    def bar(self, x, y, width):
        if self.index <= self.num:
            plt.subplot(self.line, self.row, self.index)
            plt.bar(x, y, width)
            self.index = self.index + 1
    
    #水平条形图
    def barh(self, x, y, width):
        if self.index <= self.num:
            plt.subplot(self.line, self.row, self.index)
            plt.barh(x, y, width)
            self.index = self.index + 1
    
    #饼图
    def pie(self, array, labels, labeldistance=0.3, autopct="%.6f%%", shadow=False): #, explode=[]
        if self.index <= self.num:
            plt.subplot(self.line, self.row, self.index)
            plt.pie(array, labels=labels, labeldistance=labeldistance, autopct=autopct, shadow=shadow)
            self.index = self.index + 1
    
    #文本内容显示
    def text(self, x, y, text, fontsize=10):
        plt.text(x, y, s=text, fontsize=fontsize)
    
    #文本内容显示, 无效
    def figtext(self, x, y, text, fontsize=10):
        plt.figtext(x, y, s=text, fontsize=fontsize)


# 绘制图例
# 指定边界框起始位置为(0, 1.02)，并设置宽度为1，高度为0.102
#plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), 
#           ncol=3, # 设置列数为3，默认值为1
#           mode="expand", 
# # mode为None或者expand，当为expand时，图例框会扩展至整个坐标轴区域
#           borderaxespad=0.) # 指定坐标轴和图例边界之间的间距


# 绘制注解
#plt.annotate("Important value", # 注解文本的内容
#             xy=(55,20), # 箭头终点所在位置
#             xytext=(5, 38), 
#             # 注解文本的起始位置，箭头由xytext指向xy坐标位置
#             arrowprops=dict(arrowstyle='->')); 
#       # arrowprops字典定义箭头属性，此处用arrowstyle定义箭头风格
#
#
## 绘制图例
## 指定边界框起始位置为(0, 1.02)，并设置宽度为1，高度为0.102
#plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), 
#           ncol=3, # 设置列数为3，默认值为1
#           mode="expand", 
# # mode为None或者expand，当为expand时，图例框会扩展至整个坐标轴区域
#           borderaxespad=0.) # 指定坐标轴和图例边界之间的间距
#
## xy参数设置箭头指示的位置，xytext参数设置注释文字的位置
## arrowprops参数以字典的形式设置箭头的样式
## width参数设置箭头长方形部分的宽度，
## headlength参数设置箭头尖端的长度，
## headwidth参数设置箭头尖端底部的宽度，
## shrink参数设置箭头顶点、尾部与指示点、注释文字的距离（比例值）
#plt.annotate('this spot must really\nmean something', xy=(6, 30),
#			 xytext=(8, 31.5),
#             arrowprops=dict(width=15, 
#             headlength=20, headwidth=20, 
#             facecolor='black', shrink=0.1));
#
#
#``'-'``        None
#``'->'``       head_length=0.4,head_width=0.2
#``'-['``       widthB=1.0,lengthB=0.2,angleB=None
#``'|-|'``      widthA=1.0,widthB=1.0
#``'-|>'``      head_length=0.4,head_width=0.2
#``'<-'``       head_length=0.4,head_width=0.2
#``'<->'``      head_length=0.4,head_width=0.2
#``'<|-'``      head_length=0.4,head_width=0.2
#``'<|-|>'``    head_length=0.4,head_width=0.2
#``'fancy'``    head_length=0.4,head_width=0.4,tail_width=0.4
#``'simple'``   head_length=0.5,head_width=0.5,tail_width=0.2
#``'wedge'``    tail_width=0.3,shrink_factor=0.5
#plt.figure(figsize=(12,9))
#plt.axis([0, 10, 0, 20]);
#arrstyles = ['-', '->', '-[', '<-', '<->', 'fancy', 
#'simple', 'wedge']
#for i, style in enumerate(arrstyles):
#    plt.annotate(style, xytext=(1, 2+2*i), xy=(4, 1+2*i),
#			     arrowprops=dict(arrowstyle=style));
#
#connstyles=["arc", "arc,angleA=10,armA=30,rad=30", "arc3,rad=.2",
#		 "arc3,rad=-.2", "angle", "angle3"]
#for i, style in enumerate(connstyles):
#    plt.annotate(style, xytext=(6, 2+2*i), xy=(8, 1+2*i),
#	     arrowprops=dict(arrowstyle='->', connectionstyle=style));
#plt.show()
#
#
#
#text()	mpl.axes.Axes.text()	在Axes对象的任意位置添加文字
#xlabel()	mpl.axes.Axes.set_xlabel()	为X轴添加标签
#ylabel()	mpl.axes.Axes.set_ylabel()	为Y轴添加标签
#title()	mpl.axes.Axes.set_title()	为Axes对象添加标题
#legend()	mpl.axes.Axes.legend()	为Axes对象添加图例
#figtext()	mpl.figure.Figure.text()	在Figure对象的任意位置添加文字
#suptitle()	mpl.figure.Figure.suptitle()	为Figure对象添加中心化的标题
#annnotate()	mpl.axes.Axes.annotate()	为Axes对象添加注释（箭头可选）
#x=[1,2,3]
#y=[1,2,3]
#plt.bar(x,y)
#plt.text(0.7,1,s='第三',fontsize=40)
#plt.figtext(0.4,0.8,s='排名',fontsize=40)
#
#annotate() xy参数设置箭头指示的位置，xytext参数设置注释文字的位置 arrowprops参数以字典的形式设置箭头的样式 width参数设置箭头长方形部分的宽度，headlength参数设置箭头尖端的长度， headwidth参数设置箭头尖端底部的宽度，shrink参数设置箭头顶点、尾部与指示点、注释文字的距离（比例值）

# 设置刻度标记的大小
#plt.tick_params(axis='both', which="major", labelsize=14)







