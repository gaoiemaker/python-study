# 海龟绘图（Turtle Graphics）后来被移植到各种高级语言中，Python内置了turtle库，基本上100%复制了原始的Turtle Graphics的所有功能
# 导入turtle包的所有内容:
from turtle import *

# 设置笔刷宽度:
width(4)

# 前进:
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor("red")
forward(100)
right(90)

pencolor("green")
forward(200)
right(90)

pencolor("blue")
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
