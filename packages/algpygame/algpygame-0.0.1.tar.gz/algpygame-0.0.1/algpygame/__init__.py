import pygame,sys
def pykj(k):#pygame的框架，k=窗口名称,必须和screen = pygame.display.set_mode((700,500))代码配合使用！！！
    pygame.init()
    pygame.display.set_caption(k)
def pysx():#pygame的刷新
    pygame.display.update()
def pytpjz(l):#pygame的图片加载
    jz=pygame.image.load(l)
    return jz
def pytpsf(tp,k,g):#pygame的图片缩放
    sf=pygame.transform.scale(tp,(k,g))
    return sf
def tpzs(dx,mc,tp,x,y):#pygame的图片展示，dx=窗口的大小mc=窗口名称tp=图片名称x=缩放的x坐标y=缩放的y坐标
    import pygame,sys
    pygame.init()
    screen = pygame.display.set_mode(dx)
    pygame.display.set_caption(mc)
    myImg = pygame.image.load(tp)
    myImg1 = pytpsf(myImg,x,y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255,255,255))
        screen.blit(myImg1,(0,0))
        pygame.display.update()
def wzzs(dx,mc,bjys,ztmc,ztdx,zsnr,ztys,zb):#pygame的文字展示
    import pygame, sys
    pygame.init()
    screen = pygame.display.set_mode(dx)
    pygame.display.set_caption(mc)
    pangwa = pygame.font.Font(ztmc,ztdx)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(bjys)
        text_code1 = pangwa.render(zsnr, True, ztys)
        screen.blit(text_code1, zb)
        pygame.display.update()
def xtwzzs(dx,mc,bjys,ztdx,zsnr,ztys,zb):#pygame的系统字体文字展示
    import pygame, sys
    pygame.init()
    screen = pygame.display.set_mode(dx)
    pygame.display.set_caption(mc)
    pangwa = pygame.font.SysFont("kaiti",ztdx)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(bjys)
        text_code1 = pangwa.render(zsnr, True, ztys)
        screen.blit(text_code1, zb)
        pygame.display.update()
#图片绘制必须使用：screen.blit(myImg,(0,0))
#内容填充必须使用：screen.fill((255,255,255))