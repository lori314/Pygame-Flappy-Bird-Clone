import pygame
import sys
import random

class pile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        y=random.uniform(1,35)*2
        self.up_mod_rect=pygame.Rect(343,149,62,y)
        self.up_pipe_rect=pygame.Rect(343,149+y,62,60)
        self.down_mod_rect=pygame.Rect(343,352+y,62,70-y)
        self.down_pipe_rect=pygame.Rect(343,292+y,62,60)
        self.rect1=self.up_mod_rect.union(self.up_pipe_rect)
        self.rect2=self.down_mod_rect.union(self.down_pipe_rect)
    def move(self):
        self.up_mod_rect.x-=1
        self.up_pipe_rect.x-=1
        self.down_mod_rect.x-=1
        self.down_pipe_rect.x-=1
        self.rect1.x-=1
        self.rect2.x-=1
    def draw(self):
        for x in range(0,self.up_mod_rect.height,2):
            scr.blit(up_mod,(self.up_mod_rect.x,self.up_mod_rect.y+x,self.up_mod_rect.width,2))
        scr.blit(up_pipe,self.up_pipe_rect)
        for x in range(0,self.down_mod_rect.height,2):
            scr.blit(down_mod,(self.down_mod_rect.x,self.down_mod_rect.y+x,self.down_mod_rect.width,2))
        scr.blit(down_pipe,self.down_pipe_rect)
    def is_out(self):
        if self.up_mod_rect.x<=-62:
            return True
    def is_coliderect(self):
        if bird_rect.colliderect(self.rect1) or bird_rect.colliderect(self.rect2):
            return True
        
def init():
    global up
    global down
    global status
    global bird_rect
    global score
    global banner_rect1,banner_rect2,banner_rect3,banner_rect4
    pipe_list.clear()
    score=0
    bird_rect=pygame.Rect(15,240,40,26)
    banner_rect1=pygame.Rect(0,422,343,14)
    banner_rect2=pygame.Rect(343,422,34,14)
    banner_rect3=pygame.Rect(0,135,343,14)
    banner_rect4=pygame.Rect(343,135,34,14)
    scr.blit(head,head_rect)
    scr.blit(bnt_start,bnt_start_rect)
    if head_rect.y>=80 and down==1:
        down=0
        up=1
    if head_rect.y<=55 and up==1:
        down=1
        up=0
    if down==1:
        head_rect.y+=1
    if up==1:
        head_rect.y-=1
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            #卸载所有模块
            pygame.quit()
            #终止程序，确保退出程序
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.pos[0]>=bnt_start_rect.x and event.pos[0]<= bnt_start_rect.x+bnt_start_rect.width and event.pos[1]>=bnt_start_rect.y and event.pos[1]<=bnt_start_rect.y+bnt_start_rect.height:
                status=1

def start():
    global up_flag
    global j
    global status
    scr.blit(message_bg,message_bg_rect)
    scr.blit(banner,banner_rect3)
    scr.blit(banner,banner_rect4)
    if i%160==0:
        pipe=pile()
        pipe_list.append(pipe)
    for pipe in pipe_list:
        pipe.move()
        pipe.draw()
        if pipe.is_out()==True:
            pipe_list.remove(pipe)
        if pipe.is_coliderect()==True:
            status=2
            break
    if bird_rect.colliderect(banner_rect1) or bird_rect.colliderect(banner_rect2) or bird_rect.colliderect(banner_rect3) or bird_rect.colliderect(banner_rect4):
        status=2
    banner_rect3.x-=1
    banner_rect4.x-=1
    if banner_rect4.x<=-343:
        banner_rect4.x=343
    if banner_rect3.x<=-343:
        banner_rect3.x=343
    get_score()
    if not up_flag==0:
        bird_up()
    else:
        j=j+1
        bird_rect.y+=1
        if i%10==0:
            scr.blit(bird0,bird_rect)
        else:
            scr.blit(bird1,bird_rect)
        if j>=5:
            if i%10==0:
                scr.blit(down_bird0,bird_rect)
            else:
                scr.blit(down_bird1,bird_rect)
        for event in pygame.event.get():
            # 判断用户是否点了"X"关闭按钮,并执行if代码段
            if event.type == pygame.QUIT:
                #卸载所有模块
                pygame.quit()
                #终止程序，确保退出程序
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    up_flag=1
                    j=0
                    bird_up()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    up_flag=1
                    j=0
                    bird_up()

def bird_up():
    global up_flag
    up_flag=up_flag+1
    if up_flag<=10:
        bird_rect.y-=4
    else:
        up_flag=0
    if i%15==0:
        scr.blit(up_bird0,bird_rect)
    else:
        scr.blit(up_bird1,bird_rect)
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            #卸载所有模块
            pygame.quit()
            #终止程序，确保退出程序
            sys.exit()

def get_score():
    global score
    global best_score
    for pipe in pipe_list:
        if bird_rect.x==pipe.up_mod_rect.x:
            score=score+1
            if score>best_score:
                best_score=score
    if score<10:
        path='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(score)+'.jpg'
        score_picture=pygame.image.load(path)
        scr.blit(score_picture,score_rect1)
    elif score>=0 and score<100:
        path1='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(score%10)+'.jpg'
        path2='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(score//10)+'.jpg'
        score_picture1=pygame.image.load(path1)
        score_picture2=pygame.image.load(path2)
        scr.blit(score_picture1,score_rect3)
        scr.blit(score_picture2,score_rect2)
    if best_score<10:
        path='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(best_score)+'.jpg'
        best_score_picture=pygame.image.load(path)
        scr.blit(best_score_picture,score_rect11)
    elif best_score>=0 and best_score<100:
        path1='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(best_score%10)+'.jpg'
        path2='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(best_score//10)+'.jpg'
        best_score_picture1=pygame.image.load(path1)
        best_score_picture2=pygame.image.load(path2)
        scr.blit(best_score_picture1,score_rect33)
        scr.blit(best_score_picture2,score_rect22)

def over():
    global status
    scr.blit(message_bg,message_bg_rect)
    scr.blit(banner,banner_rect3)
    scr.blit(banner,banner_rect4)
    for pipe in pipe_list:
        pipe.draw()
    if score<10:
        path='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(score)+'.jpg'
        score_picture=pygame.image.load(path)
        scr.blit(score_picture,score_rect1)
    elif score>=0 and score<100:
        path1='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(score%10)+'.jpg'
        path2='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(score//10)+'.jpg'
        score_picture1=pygame.image.load(path1)
        score_picture2=pygame.image.load(path2)
        scr.blit(score_picture1,score_rect3)
        scr.blit(score_picture2,score_rect2)
    if best_score<10:
        path='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(best_score)+'.jpg'
        best_score_picture=pygame.image.load(path)
        scr.blit(best_score_picture,score_rect11)
    elif best_score>=0 and best_score<100:
        path1='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(best_score%10)+'.jpg'
        path2='935b3809af5740cea38c22922946a2d2\\img'+'\\'+str(best_score//10)+'.jpg'
        best_score_picture1=pygame.image.load(path1)
        best_score_picture2=pygame.image.load(path2)
        scr.blit(best_score_picture1,score_rect33)
        scr.blit(best_score_picture2,score_rect22)
    while bird_rect.y<=396 and i%15==0:
        bird_rect.y+=1
    while game_over_rect.y>=150 and i%100==0:
        game_over_rect.y-=1
    scr.blit(bird0,bird_rect)
    scr.blit(game_over,game_over_rect)
    if game_over_rect.y<=150:
        scr.blit(submit,submit_rect)
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            #卸载所有模块
            pygame.quit()
            #终止程序，确保退出程序
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if submit_rect.collidepoint(event.pos):
                status=0

pygame.init()
pygame.mixer.init()
music=pygame.mixer.music.load('1.DELA[乐师]-NOVA.mp3')
scr=pygame.display.set_mode((343,480))
bg=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\bg.jpg').convert()
bird0=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\bird0.png')
bird1=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\bird1.png')
up_bird0=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\up_bird0.png')
up_bird1=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\up_bird1.png')
down_bird0=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\down_bird0.png')
down_bird1=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\down_bird1.png')
down_mod=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\down_mod.png')
down_pipe=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\down_pipe.png')
up_mod=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\up_mod.png')
up_pipe=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\up_pipe.png')
banner=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\banner.jpg')
head=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\head.jpg')
bnt_start=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\start.jpg')
bnt_score=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\score.jpg')
message_bg=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\message.jpg')
game_over=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\game_over.jpg')
submit=pygame.image.load(r'935b3809af5740cea38c22922946a2d2\img\submit.jpg')
scr.blit(bg,(0,0))
pygame.display.update()
clock=pygame.time.Clock()
pygame.display.set_caption("my first game")
pygame.display.set_icon(bird0)
#定义初始位置
head_rect=pygame.Rect(85,70,236,77)
up=1
down=0
up_flag=0
best_score=0
pipe_list=[]
bnt_start_rect=pygame.Rect(130,280,85,29)
banner_rect1=pygame.Rect(0,422,343,14)
banner_rect2=pygame.Rect(343,422,34,14)
banner_rect3=pygame.Rect(0,135,343,14)
banner_rect4=pygame.Rect(343,135,34,14)
bird_rect=pygame.Rect(15,240,40,26)
message_bg_rect=pygame.Rect(37,0,269,135)
score_rect1=(247,40,28,39)
score_rect11=(247,90,28,39)
score_rect2=(230,40,28,39)
score_rect3=(260,40,28,39)
score_rect22=(230,90,28,39)
score_rect33=(260,90,28,39)
game_over_rect=pygame.Rect(61,480,221,40)
submit_rect=pygame.Rect(130,280,85,29)
scr.blit(banner,banner_rect1)
status=0
i=0
j=0
score=0
while True:
    clock.tick(60)
    i=i+1
    if i>=10000:
        i=0
    if pygame.mixer.music.get_busy()==False:
	    pygame.mixer.music.play()
    if banner_rect1.x<=-343:
        banner_rect1.x=343
    if banner_rect2.x<=-343:
        banner_rect2.x=343
    scr.blit(bg,(0,0))
    scr.blit(banner,banner_rect1)
    scr.blit(banner,banner_rect2)
    if status==0:
        banner_rect1.x-=1
        banner_rect2.x-=1
        init()
    elif status==1:
        banner_rect1.x-=1
        banner_rect2.x-=1
        start()
    elif status==2:
        over()
    pygame.display.update()