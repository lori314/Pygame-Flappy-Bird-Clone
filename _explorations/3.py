#坐标系：左上角是原点：0，0
#描述区域：(x,y)(width,height)
#pygame中的类：
#Rect
#Rect(x,y,width,height)(不用初始化也可以调用)

import pygame

hero_rect=pygame.Rect(100,500,120,126)
print("英雄原点:%d %d"%(hero_rect.x,hero_rect.y))
print("英雄大小:%d %d"%(hero_rect.width,hero_rect.height))#返回元组
