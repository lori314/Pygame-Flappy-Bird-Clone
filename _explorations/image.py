import pygame
pygame.init()
scr=pygame.display.set_mode((483,750))
#创建游戏时钟对象
clock=pygame.time.Clock()
#加载图像
bg=pygame.image.load(r'C:\Users\lenovo\Desktop\codes\python\game_make\tianyi4.jpg')
#绘制到屏幕上
scr.blit(bg,(0,0))
pygame.display.update()
n=0
while n<1000:
    clock.tick(60)
    n=n+1
    
pygame.quit()