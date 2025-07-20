#原理：逐帧(Frame)拼凑起来（至少每秒60次）

#游戏循环：意味着游戏的正式开始
import pygame
import sys
pygame.init()
scr=pygame.display.set_mode((343,480))
bg=pygame.image.load(r'C:\Users\lenovo\Desktop\codes\python\game_make\935b3809af5740cea38c22922946a2d2\img\bg.jpg').convert()
scr.blit(bg,(0,0))
pygame.display.update()
clock=pygame.time.Clock()
bird=pygame.image.load(r'C:\Users\lenovo\Desktop\codes\python\game_make\935b3809af5740cea38c22922946a2d2\img\bird0.png')
#定义初始位置
bird_rect=pygame.Rect(100,300,40,26)
while True:
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            #卸载所有模块
            pygame.quit()
            #终止程序，确保退出程序
            sys.exit()
    clock.tick(60)
    bird_rect.y+=25
    if bird_rect.y>480:
        bird_rect.y=0
    scr.blit(bg,(0,0))
    scr.blit(bird,bird_rect)
    pygame.display.update()
    #修改鸟的位置
    #用bilt重绘图像
    #调用update更新
