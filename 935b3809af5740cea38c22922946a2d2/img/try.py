#导入所需的模块
import sys
import pygame
# 使用pygame之前必须初始化
pygame.init()
# 设置主屏窗口
screen = pygame.display.set_mode((400,400))
screen.fill((156,156,156))
# 设置窗口的标题，即游戏名称
pygame.display.set_caption('hello world')
# 引入字体类型
f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',50)
# 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；
# 第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色；
text = f.render("C语言中文网",True,(255,0,0),(156,156,156))
#获得显示对象的rect区域坐标
textRect =text.get_rect()
# 设置显示对象居中
textRect.center = (200,200)
# 将准备好的文本信息，绘制到主屏幕 Screen 上。
screen.blit(text,textRect)
# 固定代码段，实现点击"X"号退出界面的功能，几乎所有的pygame都会使用该段代码
while True:
    #等待事件发生
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        print('鼠标按下',event.pos)
    if event.type == pygame.MOUSEBUTTONUP:
        print('鼠标弹起')
    if event.type == pygame.MOUSEMOTION:
        print('鼠标移动')
        # 键盘事件
    if event.type ==pygame.KEYDOWN:
        # 打印按键的英文字符
        print('键盘按下',chr(event.key))
    if event.type == pygame.KEYUP:
        print('键盘弹起')
    pygame.display.flip() #更新屏幕内容
