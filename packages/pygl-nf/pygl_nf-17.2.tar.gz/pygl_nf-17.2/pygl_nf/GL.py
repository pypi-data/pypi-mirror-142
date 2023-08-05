from ast import Str
from tkinter.messagebox import NO
from xmlrpc.client import TRANSPORT_ERROR
import colorama
import sys



from pyclbr import Function
import py
import pygame.gfxdraw
import pygame_widgets
import pygame
import keyboard
import math
import time
import random
import mouse


import pygame.camera

from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.toggle import Toggle
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.progressbar import ProgressBar


start_time = 0
anim_time = 1

startTime = time.time()

pygame.init()


def Passing():
    pass
def Get_CAM_zvt_prost():
        return ['RGB','HSV','YUV']
def Mod(num):
    if num < 0:num = -num
    return num
def Get_GRPgraph_wersion():
    print(colorama.Fore.BLUE+'GRPgraph version (17.2)'+colorama.Fore.RESET)

    


# Progress_bar
Progress_bar_time = 10
Progres_bar_buffer = lambda:  1 - (time.time() - startTime) / Progress_bar_time

# Display
Full = 'FULL'
Resize = 'RESZ'
Nones = 'NONE'

# Colors
c_RED = (255, 0, 0)
c_GREEN = (0, 128, 0)
c_BLUE = (0, 0, 255)
c_YELLOW = (255, 255, 0)
c_WHITE = (255, 255, 255)
c_BLACK = (0, 0, 0)
c_CYAN = (0, 255, 255)
c_LIME = (0, 255, 0)
c_DARK_GREEN = (0, 100, 0)
c_CRIMSON = (220, 20, 60)
c_PINK = (255, 192, 203)
c_VIOLET = (238, 130, 238)
c_PURPLE = (128, 0, 128)
c_NAVY = (0, 0, 128)
c_SKY_BLUE = (135, 206, 250)
c_AQUA = (0, 255, 255)
c_MAROON = (128, 0, 0)
c_SILVER = (192, 192, 192)
c_GRAY = (128, 128, 128)



















# 1
class Fonts(object):
    def __init__(self):
        pass

    def Get_():
        return pygame.font.get_fonts()

    def Get_index(self,index):
        return pygame.font.get_fonts()[index]

    class Print_():
        def __init__(self,Nums=False):
            if Nums == False:
                fonts = pygame.font.get_fonts()
                for i in range(len(fonts)):
                    print(colorama.Fore.GREEN + fonts[i] + colorama.Fore.RESET)

            elif Nums == True:
                fonts = pygame.font.get_fonts()
                for i in range(len(fonts)):
                    print(colorama.Fore.YELLOW +  '['+str(i)+'] - ' + colorama.Fore.RESET , end='') 
                    print(colorama.Fore.GREEN + fonts[i] + colorama.Fore.RESET)      
# 2
class Vec2_:
        def __init__(self,vect2d_start=[-1],vect2d_end=[-1],pos=[0,0]): 
            if vect2d_start[0]!=-1 and vect2d_end[0]!=-1:
                self.vect2d_start = vect2d_start
                self.vect2d_end = vect2d_end
                self.vec2D = [self.vect2d_start,self.vect2d_end]
                self.x = vect2d_end[0]-vect2d_start[0]
                self.y = vect2d_end[1]-vect2d_start[1]
            else:
                self.x = pos[0]
                self.y = pos[1]
            self.size = int(math.sqrt(self.x**2+self.y**2))
            self.absv = Mod(self.size)
            self.pos1 = [self.x,self.y]

        def RAV_2D(self,vector2D):
            parperx_st_ = int(vector2D.vect2d_start[0]-self.vect2d_start[0])
            parperx_en_ = int(vector2D.vect2d_end[0]-self.vect2d_end[0])
            parpery_st_ = int(vector2D.vect2d_start[1]-self.vect2d_start[1])
            parpery_en_ = int(vector2D.vect2d_end[1]-self.vect2d_end[1])
            if Mod(parperx_st_) == Mod(parperx_en_) and Mod(parpery_st_) == Mod(parpery_en_):
                return True
            else:
                return False

        def POV_2D(self,ugl):
            pos = [int(self.x*math.cos(ugl)-self.y*math.sin(ugl)),int(self.y*math.cos(ugl)+self.x*math.sin(ugl))]
            vec3 = Vec2_(pos=pos)
            return vec3

        def SUM(self,vector2D):
            pos=[self.x+vector2D.x,self.y+vector2D.y]
            vec3 = Vec2_(pos=pos)
            return vec3

        def RAZ(self,vector2D):
            pos=[self.x-vector2D.x,self.y-vector2D.y]
            vec3 = Vec2_(pos=pos)
            return vec3

        def UMN(self,delta):
            pos=[self.x*delta,self.y*delta]
            vec3 = Vec2_(pos=pos)
            return vec3

        def SCAL(self,vector2D):
            scl = self.x*vector2D.x+self.y*vector2D.y
            return scl

        def NUL(self):
            if self.vect2d_end==self.vect2d_start:return True
            else:return False

        def NAP(self,vector2D):
            parperx_st_ = int(vector2D.vect2d_start[0]-self.vect2d_start[0])
            parperx_en_ = int(vector2D.vect2d_end[0]-self.vect2d_end[0])
            parpery_st_ = int(vector2D.vect2d_start[1]-self.vect2d_start[1])
            parpery_en_ = int(vector2D.vect2d_end[1]-self.vect2d_end[1])
            
            if parperx_en_ == parperx_st_ and parpery_en_ == parpery_st_ :
                    return True
            else:
                    return False     
# 3
class Surfases_:
    def __init__(self,size=[],pos=[0,0],color=(200,200,200),alpha=0):
        self.screen = pygame.Surface((size[0],size[1]))
        self.screen.fill(color)
        self.color = color
        self.size = size
        self.alpha = alpha
        self.pos = pos
        if self.alpha > 255:self.alpha=255
        if self.alpha < 0:self.alpha=0
        self.screen.set_alpha(self.alpha)

    def SET_ALPHA(self,al):
        if al > 255:al=255
        if al < 0:al=0
        self.screen.set_alpha(al)
        
    def GET_PIXEL_COLOR(self,pos):
        col = self.screen.get_at(pos)
        return [col[0],col[1],col[2]]
        
    def DRAW_SURF_ON_SCREEN(self,screen_surf,pos=None):
        if pos!=None:self.pos = pos
        screen_surf.blit(self.screen,(self.pos[0],self.pos[1]))

    def SAVE_SURF(self,filename):
        pygame.image.save(self.screen,filename)

    def SET_BG_COLOR(self,color):
        self.color = color
    
    def GET_BG_COLOR(self):
        return self.color

    def UPDATE(self):
        self.screen.fill(self.color)

    def FILL_SURF(self,col=()):
        self.screen.fill(col)

    def GET_SIZE(self):
        return self.size
    
    def GET_WIDTH(self):
        return self.size[0]

    def GET_POS(self):
        return self.pos

    def GET_HEIGHT(self):
        return self.size[1]

    def SET_POS(self,pos=[]):
        self.pos = pos

    def GET_LEFT(self):
        return [self.pos[0],self.pos[1]+self.size[1]/2]

    def GET_RIGHT(self):
        return [self.pos[0]+self.size[0],self.pos[1]+self.size[1]/2]

    def GET_UP(self):
        return [self.pos[0]+self.size[0]/2,self.pos[1]]

    def GET_DOWN(self):
        return [self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]]
# 4       
class Kamera_:
    def __init__(self,SIZE=[],zvet_prost='RGB',NUM=0):
        self.size = SIZE
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[NUM],(self.size[0],self.size[1]), zvet_prost)
        self.cam.set_controls(True,False,1)

    def LIST_CAM(self):
        cams = pygame.camera.list_cameras()
        return cams
    
    def START(self):self.cam.start()

    def END(self):self.cam.stop()

    def GET_IMG(self):
        img = self.cam.get_image()
        im = Img_(img)
        return im

    def GET_SIZE(self):
        width , height = self.cam.get_size()
        return width , height
    
    def SET_SETINGS(self,wflip,hflip,sun):
        self.cam.set_controls(wflip,hflip,sun)

    def GET_SETINGS(self):
        cont = self.cam.get_controls()
        return cont
# 5
class Time_:
    def __init__(self):
        pass
    def DELLAY(self,MILISECONDS):
        pygame.time.delay(MILISECONDS)
    def WAIT(self,MILISECONDS):
        pygame.time.wait(MILISECONDS)
    class TIMER():
        def __init__(self):
            colc = pygame.time.Clock()
            self.time = colc.get_time()
        def return_time(self):
            return self.time
# 6 
class Text_:
    def __init__(self,TEXT='',GLASS=False,COLOR=(),FONT='arial',SIZE=0,POSITION=[],BG_COLOR=None):  
        pygame.font.init()    
        self.text = TEXT
        self.pos = POSITION
        self.pix = SIZE
        self.font = FONT

        self.x = self.pos[0]
        self.y = self.pos[1]

        self.pos = [self.x,self.y]

        self.glass = GLASS
        self.col = COLOR
        self.bg_color = BG_COLOR

        self.RENDER_TEXT = pygame.font.SysFont(self.font,self.pix)
        RENDERING = self.RENDER_TEXT.render(self.text,self.glass,self.col,self.bg_color) 
        self.RENDERING = RENDERING
        self.screen = screen
        

    def RENDER(self,POSITION=[None,None]): 
        if POSITION[0]!=None and POSITION[1]!=None:
            self.x = POSITION[0] ; self.y = POSITION[1]
        self.screen.blit(self.RENDERING,(self.x,self.y))

    def SET_TEXT(self,text=''):
        self.text = text
        RENDERING = self.RENDER_TEXT.render(self.text,self.glass,self.col,self.bg_color) 
        self.RENDERING = RENDERING

    def GET_POSITION(self):
        return self.pos

    def SET_FONT(self,FONT=None):
        self.font = FONT
        self.RENDER_TEXT = pygame.font.SysFont(self.font,self.pix)
        RENDERING = self.RENDER_TEXT.render(self.text,self.glass,self.col,self.bg_color) 
        self.RENDERING = RENDERING

    def GET_FONT(self):
        return self.font

    def SET_UNDERLINE(self,UNDERLINE=True):
        self.RENDER_TEXT.set_underline(UNDERLINE)

    def SET_POS(self,POSITION=[]):
        self.pos = POSITION
        self.x = POSITION[0]
        self.y = POSITION[1]  

    def SET_TEXT_COLOR(self,COLOR=None):
        self.col = COLOR
        self.RENDERING = self.RENDER_TEXT.render(self.text,self.glass,self.col,self.bg_color)

    def GET_TEXT_COLOR(self):
        return self.col

    def GET_BG_COLOR(self):
        return self.bg_color

    def GET_TEXT(self):
        return self.text

    def SET_BG_COLOR(self,COLOR=None):
        self.bg_color = COLOR
        self.RENDERING = self.RENDER_TEXT.render(self.text,self.glass,self.col,self.bg_color)
# 7 -- new !! do not work
class Math_:
    def __init__(self):
        pass

    def COS(self,ugl):
        return math.cos(ugl)

    def SIN(self,ugl):
        return math.sin(ugl) 

    def RAST(self,pos1=[],pos2=[]):
        if pos1[0]>pos2[0]:w = pos1[0]-pos2[0]
        else:              w = pos2[0]-pos1[0]
        if pos1[1]>pos2[1]:h = pos1[1]-pos2[1]
        else:              h = pos2[1]-pos1[1]
        dl = math.sqrt(w*w+h*h)
        return dl   

    class Randomings():
        def __init__(self):
            pass

        class Randints():
            def __init__(self,a,b):
                self.a = a
                self.b = b
                self.num = random.randint(self.a,self.b)
            def Get(self):
                return self.num

        class Randrages():
            def __init__(self,a,b,step):
                self.a = a
                self.b = b
                self.step = step
                self.num = random.randrange(self.a,self.b,self.step)
            def Get(self):
                return self.num

        class Randoms():
            def __init__(self):
                self.num = random.random()
            def Get(self):
                return self.num
# 8 
class Color_:
    def __init__(self,r,g,b,hsv=0):
        self.hsv = hsv
        self.r = r
        self.b = b
        self.g = g
        if self.r == 'r' or self.r == 'R':self.r = random.randint(0,255)
        if self.g == 'r' or self.g == 'R':self.g = random.randint(0,255)
        if self.b == 'r' or self.b == 'R':self.b = random.randint(0,255)
        self.r = self.r - self.hsv
        self.g = self.g - self.hsv
        self.b = self.b - self.hsv
        if self.r < 0:    self.r = 0
        if self.g < 0:    self.g = 0
        if self.b < 0:    self.b = 0
        if self.r > 255:  self.r = 255
        if self.g > 255:  self.g = 255
        if self.b > 255:  self.b = 255
        self.color = (self.r,self.g,self.b)

    def SETHSV(self,hsv):
        self.hsv = hsv
        self.r = self.r - self.hsv
        self.g = self.g - self.hsv
        self.b = self.b - self.hsv
        if self.r < 0:    self.r = 0
        if self.g < 0:    self.g = 0
        if self.b < 0:    self.b = 0
        if self.r > 255:  self.r = 255
        if self.g > 255:  self.g = 255
        if self.b > 255:  self.b = 255
        self.color = (self.r,self.g,self.b)
        return self.color

    def Color_mesh(self,color,mesh=0.5):
        hsv = (self.hsv + color.hsv)/mesh
        r = (self.r + color.r)/mesh
        g = (self.g + color.g)/mesh
        b = (self.b + color.b)/mesh
        col = Color_(r,g,b,hsv)
        return col   

    def Color_Reverse(self):
        if self.r <= 127.5:r = 127.5+(127.5-self.r) 
        if self.g <= 127.5:g = 127.5+(127.5-self.g) 
        if self.b <= 127.5:b = 127.5+(127.5-self.b)  
        if self.r >  127.5:r = 127.5-(self.r - 127.5 ) 
        if self.g >  127.5:g = 127.5-(self.g - 127.5 ) 
        if self.b >  127.5:b = 127.5-(self.b - 127.5 ) 
        hsv = -self.hsv
        col = Color_(r,g,b,hsv)
        return col  

    def Set_chb(self):
        gr = (self.color[0]+self.color[1]+self.color[2])/3
        hsv = 0
        col = Color_(gr,gr,gr,hsv)
        return col
# 9 
class Sub_events_:
    def __init__(self):
        pass
    class Board_init:
        def __init__(self):
            pass

        def PRESS_SUB(self,key):
            on = keyboard.is_pressed(key)
            return on

        def PRESS_FUNCTION(self,key,function):
            if True==keyboard.is_pressed(key):
                function()
            
    class Mouse_init:
        def __init__(self):
            pass

        def GET_POSITION(self,PYGL_WINDOW='y'): 
            if PYGL_WINDOW=='y':
                pos = pygame.mouse.get_pos();  
                pos = [pos[0],pos[1]]
                return pos
            elif PYGL_WINDOW=='n':
                pos = mouse.get_position(); 
                pos = [pos[0],pos[1]]
                return pos
            else:
                print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'None flag'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'''flags : y , n'''+colorama.Fore.RESET)
                sys.exit()

        def GET_PRESS_ON_DISPLAY(self,BUTTON='left'):
            if BUTTON!='left' and BUTTON!='right' :
                print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'None flag'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'''flags : left , right'''+colorama.Fore.RESET)
                sys.exit()
            bol = mouse.is_pressed(BUTTON)
            return bol

        def GET_PRESS_ON_PYGL_WINDOW(self,BUTTON="l"):
            if BUTTON!='l' and BUTTON!='r' :
                print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'None flag'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'''flags : l , r'''+colorama.Fore.RESET)
                sys.exit()
            pr = pygame.mouse.get_pressed()
            if BUTTON == "l":  return pr[0]
            elif BUTTON == "r":  return pr[2]
            elif BUTTON == "m":  return pr[1]

        def PRESS_FUNCTION_ON_PYGL_WINDOW(self,button,function):
            pr = pygame.mouse.get_pressed()
            if button == "l" and pr[0] == True:  
                function()
            elif button == "r" and pr[2] == True:  
                function()
            elif button == "m" and pr[1] == True:  
                function()

        def SET_VISIBLE_ON_PYGL_WINDOW(self,viz):
            pygame.mouse.set_visible(viz)  

        def SET_POS_ON_PYGL_WINDOW(self,pos=[]):
            pygame.mouse.set_pos([pos[0],pos[1]])

        def SET_POS_ON_DISPLAY(self,pos=[]):
            mouse.move(pos[0],pos[1])

        def ON_DISPLAY_MOVE(self,pos=[],absolute=True,second=0):
            mouse.move(pos[0],pos[1],absolute,second)

        def ON_CLICK(self,BUTTON='left'):
            if BUTTON!='left' and BUTTON!='right':
                print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'None flag'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'''flags : left , right'''+colorama.Fore.RESET)
                sys.exit()
            mouse.click(BUTTON)

        def ON_DUBLE_CLICK(self,BUTTON='left'):
            if BUTTON!='left' and BUTTON!='right':
                print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'None flag'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'''flags : left , right'''+colorama.Fore.RESET)
                sys.exit()
            mouse.double_click(BUTTON)
# 10 
class Display_init:
    
    def __init__(self,size=[600,400],caption='Program',flags=Nones,BG_COLOR=c_WHITE):
        global screen,clock,bg_color
        self.caption = caption

        pygame.init()
        pygame.display.init()
        
        
        clock = pygame.time.Clock()
        if flags == 'FULL':
            screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        elif flags == 'RESZ':
            self.width = size[0]
            self.height = size[1]
            screen = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE)
        elif flags == 'NONE':
            self.width = size[0]
            self.height = size[1]
            screen = pygame.display.set_mode((self.width,self.height))
        else:
            print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
            print(colorama.Fore.YELLOW+'None flag'+colorama.Fore.RESET)
            print(colorama.Fore.YELLOW+'''flags : FULL - this is full screen
        NONE - this is none'''+colorama.Fore.RESET)
            sys.exit()

        self.width = screen.get_size()[0]
        self.height = screen.get_size()[1]
        self.win_size = screen.get_size()
        
        self.col = BG_COLOR 
        

        self.up = 0
        self.down = self.height
        self.left = 0
        self.right = self.width

        self.clock = clock
        self.screen = screen
        pygame.display.set_caption(self.caption)

    def GET_DISPLAY_INFO(self):
        return pygame.display.Info()

    def SET_FULL(self):
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

    def SET_RESIZE(self):
        self.screen = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE)
        

    def SET_NONE(self):
        self.screen = pygame.display.set_mode((self.width,self.height))

    def GET_TOGGLE_FULLSCREEN(self):
        return pygame.display.toggle_fullscreen()

    def SET_CAPTION(self,caption=''):
        self.caption = caption
        pygame.display.set_caption(self.caption)

    def GET_ACTIVE(self):
        return pygame.display.get_active()
    
    def SET_ALPHA(self,alp):
        screen.set_alpha(alp)

    def GET_COLOR(self,x,y):
        col = screen.get_at([x,y])
        col1 = [col[0],col[1],col[2]]
        return col1

    def GET_WIN_CENTER(self):
        xc = self.screen.get_width()/2
        yc = self.screen.get_height()/2
        return xc , yc

    def SET_FPS(self,fps):
        if type(fps)==str:
            if fps == "MAX":fps = 1000
            elif fps == "MIN":fps = 30
            else:
                print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
                print(colorama.Fore.YELLOW+'None fps'+colorama.Fore.RESET)
                sys.exit()
        self.clock.tick(fps)

    def GET_INIT(self):
        return pygame.display.get_init()
    
    def GET_DISPLAY_DRIVER(self):
        return pygame.display.get_driver()

    def GET_TOP(self,cor='X',storona='left'):   
        if cor=='X' or cor=='x' and storona=='left':return 0
        elif cor=='X' or cor=='x' and storona=='right':return self.screen.get_width()
        elif cor=='Y' or cor=='y' and storona=='left':return 0
        elif cor=='Y' or cor=='y' and storona=='right':return 0
        else:
            print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
            print(colorama.Fore.YELLOW+'None cordinate'+colorama.Fore.RESET)
            print(colorama.Fore.YELLOW+'Uses left or fight'+colorama.Fore.RESET)
            sys.exit()

    def GET_DOWN(self,cor='X',storona='left'):
        if cor=='X' or cor=='x' and storona=='left':return 0
        elif cor=='X' or cor=='x' and storona=='right':return self.screen.get_width()
        elif cor=='Y' or cor=='y' and storona=='left':return self.screen.get_height()
        elif cor=='Y' or cor=='y' and storona=='right':return self.screen.get_height()
        else:
            print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
            print(colorama.Fore.YELLOW+'None cordinate'+colorama.Fore.RESET)
            print(colorama.Fore.YELLOW+'Uses left or fight'+colorama.Fore.RESET)
            sys.exit()

    def GET_LEFT(self,cor='X',storona='up'):
        if cor=='X' or cor=='x' and storona=='up':return 0
        elif cor=='X' or cor=='x' and storona=='down':return 0
        elif cor=='Y' or cor=='y' and storona=='up':return 0
        elif cor=='Y' or cor=='y' and storona=='down':return self.screen.get_height()
        else:
            print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
            print(colorama.Fore.YELLOW+'None cordinate'+colorama.Fore.RESET)
            print(colorama.Fore.YELLOW+'Uses up or down'+colorama.Fore.RESET)
            sys.exit()

    def GET_RIGHT(self,cor='X',storona='up'):
        if cor=='X' or cor=='x' and storona=='up':return self.screen.get_width()
        elif cor=='X' or cor=='x' and storona=='down':return self.screen.get_width()
        elif cor=='Y' or cor=='y' and storona=='up':return 0
        elif cor=='Y' or cor=='y' and storona=='down':return self.screen.get_height()
        else:
            print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
            print(colorama.Fore.YELLOW+'None cordinate'+colorama.Fore.RESET)
            print(colorama.Fore.YELLOW+'Uses up or down'+colorama.Fore.RESET)
            sys.exit()

    def GET_FPS(self):return int(self.clock.get_fps())

    def CLOSE(self,running=True,EXIT_BUTTON='esc'):  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        events = pygame.event.get()        
        pygame_widgets.update(events)
        if keyboard.is_pressed(EXIT_BUTTON):
            sys.exit()
        return running

    def EXIT(self,EXIT_BUTTON='esc'):
        if keyboard.is_pressed(EXIT_BUTTON):
            sys.exit()
    
    def GET_WIN_SIZE(self):
        return self.screen.get_size()

    def GET_WIN_WIDTH(self):
        return self.screen.get_size()[0]

    def GET_WIN_HEIGHT(self):
        return self.screen.get_size()[1]
        
    def GET_EVENT(self):
        events = pygame.event.get()
        return events

    def FUNCTION(self,functions=[]):
        for i in range(len(functions)):
            functions[i]()

    def GET_GL_FUNCTIONS(self):
        print(colorama.Fore.GREEN+'GL_FUNCTIONS---')
        print('''   
        Draw f- D-none
        Obv f- O-(rrr)(ggg)(bbb)-THICKNESS
        DrOb f- OD-(rrr)(ggg)(bbb)-THICKNESS
        '''+colorama.Fore.RESET)

    def UPDATE_SCREEN(self):
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    class UPDATE(object):
        def __init__(self):     
            pygame.display.flip()

        def GETTIME(self):
            global start_time
            start_time+=1
            return start_time    

        def SET_BG_COLOR(self,COLOR=None):
            if COLOR is None:
                COLOR = 'white'
            screen.fill(COLOR)

    class GL:
                                            def __init__(self):
                                                pass
                                            
                                            class Rect:
                                                def __init__(self,COLOR=(),POSITION=[],SIZE=[],THICKNESS=0,SURF=None,FUNCTION='none'):
                                                    sh2 = 1
                                                    center =  [POSITION[0] + SIZE[0]/2,POSITION[1]+SIZE[1]/2]
                                                    pos=[POSITION[0],POSITION[1]]
                                                    up = [POSITION[0],POSITION[1]]
                                                    down = [POSITION[0]+SIZE[1],POSITION[1]+SIZE[0]]
                                                    right = [POSITION[0]+SIZE[1],POSITION[1]+SIZE[0]]
                                                    left = [POSITION[0],POSITION[1]]
                                                    self.pos = pos
                                                    self.size = SIZE

                                                    if SURF=='s' and type(SURF)==str:self.surf = screen
                                                    else:self.surf = SURF
                                                    
                                                    self.col = COLOR
                                                    self.obv_color = 'black'
                                                    self.sh = THICKNESS
                                                    self.sh2 = sh2
                                                    self.center = center    
                                                    self.up = up
                                                    self.down = down   
                                                    self.left = left 
                                                    self.right = right   
                                                    self.DL_diagonal = math.sqrt(SIZE[0]**2+SIZE[1]**2)

                                                    if FUNCTION=='D':
                                                        rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                        pygame.draw.rect(self.surf,self.col,rect,self.sh)
                                                    elif FUNCTION[1]=='D':
                                                        col = [int(FUNCTION[3:6]),int(FUNCTION[7:10]),int(FUNCTION[11:14])]
                                                        sh2 = int(FUNCTION[15:len(FUNCTION)])
                                                        if col!=None:self.obv_color = col
                                                        if sh2!=None:self.sh2 = sh2
                                                        rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                        pygame.draw.rect(self.surf,self.col,rect,self.sh)     
                                                        pygame.draw.rect(self.surf,self.obv_color,rect,self.sh2)  
                                                    elif FUNCTION[0]=='O':
                                                        col = [int(FUNCTION[2:5]),int(FUNCTION[6:9]),int(FUNCTION[10:13])]
                                                        sh2 = int(FUNCTION[14:len(FUNCTION)])
                                                        if col!=[0,0,0]:self.obv_color = col
                                                        if sh2!=None:self.sh2 = sh2
                                                        rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                        pygame.draw.rect(self.surf,self.obv_color,rect,self.sh2)    
                                                    else:
                                                        pass
                                                                                                                                                                              
                                                def FILL(self):
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    pygame.draw.rect(self.surf,self.col,rect,self.sh)
                                                                                                   
                                                def FILLOUT(self,COLOR=None,THICKNESS=None):
                                                    if COLOR!=None:self.obv_color = COLOR
                                                    if THICKNESS!=None:self.sh2 = THICKNESS
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    pygame.draw.rect(self.surf,self.col,rect,self.sh)     
                                                    pygame.draw.rect(self.surf,self.obv_color,rect,self.sh2)  

                                                def OUTLINE(self,COLOR=None,THICKNESS=None):
                                                    if COLOR!=None:self.obv_color = COLOR
                                                    if THICKNESS!=None:self.sh2 = THICKNESS
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    pygame.draw.rect(self.surf,self.obv_color,rect,self.sh2)   

                                                def SET_SIZE(self,SIZE=[]):
                                                    self.size = SIZE

                                                def SET_THICKNESS(self,THICKNESS):
                                                    self.sh = THICKNESS

                                                def SET_COLOR(self,COLOR=()):
                                                    self.col = COLOR

                                                def GET_SIZE(self):
                                                    return self.size

                                                def GET_THICKNESS(self):
                                                    return self.sh

                                                def SET_OUTLINE_THICKNESS(self,THICKNESS):
                                                    self.sh2=THICKNESS

                                                def GET_CENTER(self):
                                                    return self.center

                                                def GET_SURF(self):
                                                    return self.surf

                                                def GET_OUTLINE_THICKNESS(self):
                                                    return self.sh2

                                                def SET_POSITION(self,POSITION):
                                                    self.pos = POSITION
                                                    up = [self.pos[0],self.pos[1]]
                                                    down = [self.pos[0]+self.size[1],self.pos[1]+self.size[0]]
                                                    right = [self.pos[0]+self.size[1],self.pos[1]+self.size[0]]
                                                    left = [self.pos[0],self.pos[1]]
                                                    self.up = up
                                                    self.down = down   
                                                    self.left = left 
                                                    self.right = right 

                                                def GET_POSITION(self):
                                                    return self.pos
                                                    
                                                

                                            class Poligon:
                                                def __init__(self,COLOR=(),POINTS=(),THICKNESS=0,SURF=None,FUNCTION='none'):
                                                    self.points = POINTS
                                                    self.col = COLOR
                                                    self.sh = THICKNESS
                                                    self.sh2 = 1

                                                    if SURF=='s' and type(SURF)==str:self.surf=screen
                                                    else:self.surf = SURF

                                                    self.obv_col = 'black'
                                                    if FUNCTION=='D':
                                                        pygame.draw.polygon(self.surf,self.col,self.points,self.sh)
                                                    elif FUNCTION[1]=='D':
                                                        COLOR = [int(FUNCTION[3:6]),int(FUNCTION[7:10]),int(FUNCTION[11:14])]
                                                        THICKNESS = int(FUNCTION[15:len(FUNCTION)])
                                                        pygame.draw.polygon(self.surf,self.col,self.points,self.sh)
                                                        if COLOR!=None:self.obv_col = COLOR
                                                        if THICKNESS!=None:self.sh2 = THICKNESS
                                                        pygame.draw.polygon(self.surf,self.obv_col,self.points,self.sh2) 
                                                    elif FUNCTION[0]=='O':
                                                        COLOR = [int(FUNCTION[2:5]),int(FUNCTION[6:9]),int(FUNCTION[10:13])]
                                                        THICKNESS = int(FUNCTION[14:len(FUNCTION)])
                                                        if COLOR!=None:self.obv_col = COLOR
                                                        if THICKNESS!=None:self.sh2 = THICKNESS
                                                        pygame.draw.polygon(self.surf,self.obv_col,self.points,self.sh2) 
                                                    else:
                                                        pass

                                                def FILL(self):
                                                    pygame.draw.polygon(self.surf,self.col,self.points,self.sh)

                                                def OUTLINE(self,COLOR=None,THICKNESS=None):
                                                    if COLOR!=None:self.obv_col = COLOR
                                                    if THICKNESS!=None:self.sh2 = THICKNESS
                                                    pygame.draw.polygon(self.surf,self.obv_col,self.points,self.sh2)

                                                def FILLOUT(self,COLOR=None,THICKNESS=None):
                                                    pygame.draw.polygon(self.surf,self.col,self.points,self.sh)
                                                    if COLOR!=None:self.obv_col = COLOR
                                                    if THICKNESS!=None:self.sh2 = THICKNESS
                                                    pygame.draw.polygon(self.surf,self.obv_col,self.points,self.sh2) 

                                                def GET_POINTS(self):
                                                    return self.points

                                                def GET_COLOR(self):
                                                    return self.col

                                                def GET_OUTLINE_COLOR(self):
                                                    return self.obv_col

                                                def GET_THICKNESS(self):
                                                    return self.sh

                                                def GET_OUTLINE_THICKNESS(self):
                                                    return self.sh2

                                                def GET_SURF(self):
                                                    return self.surf

                                                def SET_THICKNESS(self,THICKNESS):
                                                    self.sh = THICKNESS

                                                def SET_OUTLINE_THICKNESS(self,THICKNESS):
                                                    self.sh2 = THICKNESS

                                                def SET_OUTLINE_COLOR(self,COLOR=()):
                                                    self.obv_col = COLOR

                                                def SET_COLOR(self,COLOR=()):
                                                    self.col = COLOR



                                            class Circle:
                                                def __init__(self,COLOR=(),POSITION=[],RADIUS=0,THICKNESS=0,SURF=0,FUNCTION='none'):
                                                    global g_c_pos , g_c_rad

                                                    center = [POSITION[0],POSITION[1]]
                                                    sh2 = 1
                                                    self.sh2 = sh2
                                                    self.col = COLOR
                                                    self.sh = THICKNESS
                                                    self.rad = RADIUS ; g_c_rad = self.rad
                                                    self.obv_col = (0,0,0)

                                                    if SURF=='s' and type(SURF)==str:self.surf=screen
                                                    else:self.surf = SURF

                                                    self.center = center
                                                    self.pos = POSITION ; g_c_pos = self.pos
                                                    up_cic = [POSITION[0],POSITION[1]-self.rad] ; self.up = up_cic
                                                    down_cic = [POSITION[0],POSITION[1]+self.rad] ; self.down = down_cic
                                                    left_cic = [POSITION[0]-self.rad,POSITION[1]] ; self.left = left_cic
                                                    right_cic = [POSITION[0]+self.rad,POSITION[1]] ; self.right = right_cic

                                                    if FUNCTION=='D':
                                                        pygame.draw.circle(self.surf,self.col,(self.pos[0],self.pos[1]),self.rad,self.sh)  
                                                    elif FUNCTION[1]=='D':
                                                        COLOR = [int(FUNCTION[3:6]),int(FUNCTION[7:10]),int(FUNCTION[11:14])]
                                                        THICKNESS = int(FUNCTION[15:len(FUNCTION)])
                                                        pygame.draw.circle(self.surf,self.col,(self.pos[0],self.pos[1]),self.rad,self.sh) 
                                                        if COLOR!=None:self.obv_col = COLOR
                                                        if THICKNESS!=None:self.sh2 = THICKNESS  
                                                        pygame.draw.circle(self.surf,COLOR,(self.pos[0],self.pos[1]),self.rad,self.sh2)
                                                    elif FUNCTION[0]=='O':
                                                        COLOR = [int(FUNCTION[2:5]),int(FUNCTION[6:9]),int(FUNCTION[10:13])]
                                                        THICKNESS = int(FUNCTION[14:len(FUNCTION)])
                                                        if COLOR!=None:self.obv_col = COLOR
                                                        if THICKNESS!=None:self.sh2 = THICKNESS
                                                        pygame.draw.circle(self.surf,COLOR,(self.pos[0],self.pos[1]),self.rad,self.sh2)
                                                    else:
                                                        pass
                                                        
                                                def FILL(self):
                                                    global g_c_pos
                                                    if g_c_pos!=None:self.pos = g_c_pos
                                                    pygame.draw.circle(self.surf,self.col,(self.pos[0],self.pos[1]),self.rad,self.sh)     

                                                def OUTLINE(self,COLOR=None,THICKNESS=None):
                                                    global g_c_pos
                                                    if g_c_pos!=None:self.pos = g_c_pos
                                                    if COLOR!=None:self.obv_col = COLOR
                                                    if THICKNESS!=None:self.sh2 = THICKNESS
                                                    pygame.draw.circle(self.surf,self.obv_col,(self.pos[0],self.pos[1]),self.rad,self.sh2)

                                                def FILLOUT(self,COLOR=None,THICKNESS=None):
                                                    global g_c_pos
                                                    if g_c_pos!=None:self.pos = g_c_pos
                                                    pygame.draw.circle(self.surf,self.col,(self.pos[0],self.pos[1]),self.rad,self.sh)
                                                    if COLOR!=None:self.obv_col = COLOR
                                                    if THICKNESS!=None:self.sh2 = THICKNESS
                                                    pygame.draw.circle(self.surf,self.obv_col,(self.pos[0],self.pos[1]),self.rad,self.sh2)  

                                                def SET_RADIUS(self,RADIUS):
                                                    self.rad = RADIUS

                                                def SET_COLOR(self,COLOR=()):
                                                    self.col = COLOR

                                                def GET_RADIUS(self):
                                                    return self.rad

                                                def GET_THICKNESS(self):
                                                    return self.sh

                                                def GET_CENTER(self):
                                                    return self.center

                                                def GET_SURF(self):
                                                    return self.surf

                                                def SET_OUTLINE_THICKNESS(self,sh2):
                                                    self.sh2 = sh2

                                                def SET_THICKNESS(self,THICKNESS):
                                                    self.sh=THICKNESS

                                                def GET_OUTLINE_THICKNESS(self):
                                                    return self.sh2

                                                class SET_POSITION():
                                                    def __init__(self,POSITION=[]):
                                                        global g_c_rad , g_c_pos
                                                        self.POSITION = POSITION
                                                        g_c_pos = [POSITION[0]+g_c_rad, POSITION[1]+g_c_rad]
                                                        up_cic = [POSITION[0],POSITION[1]-g_c_rad]
                                                        down_cic = [POSITION[0],POSITION[1]+g_c_rad]
                                                        left_cic = [POSITION[0]-g_c_rad,POSITION[1]]
                                                        right_cic = [POSITION[0]+g_c_rad,POSITION[1]]
                                                        self.up = up_cic
                                                        self.down = down_cic
                                                        self.left = left_cic
                                                        self.right = right_cic
                                                    def ON_CENTER(self):
                                                        global g_c_rad , g_c_pos
                                                        POSITION = self.POSITION
                                                        g_c_pos = POSITION
                                                        up_cic = [POSITION[0],POSITION[1]-g_c_rad]
                                                        down_cic = [POSITION[0],POSITION[1]+g_c_rad]
                                                        left_cic = [POSITION[0]-g_c_rad,POSITION[1]]
                                                        right_cic = [POSITION[0]+g_c_rad,POSITION[1]]
                                                        self.up = up_cic
                                                        self.down = down_cic
                                                        self.left = left_cic
                                                        self.right = right_cic

                                                def GET_POSITION(self):
                                                    return self.pos



                                            class Ellips:
                                                def __init__(self,COLOR=(),POSITION=[],SIZE=[],THICKNESS=0,SURF=0,FUNCTION='none'):
                                                    global g_e_size , g_e_pos

                                                    center =  [POSITION[0] + SIZE[0]/2,POSITION[1] + SIZE[1]/2]
                                                    
                                                    self.sh2 = 1
                                                    self.sh = THICKNESS
                                                    self.center = center
                                                    self.size = SIZE ; g_e_size = self.size
                                                    self.col = COLOR
                                                    self.obv_color = 'black'
                                                    self.pos = POSITION ; g_e_pos = self.pos
                                                    

                                                    if SURF=='s' and type(SURF)==str:self.surf=screen
                                                    else:self.surf = SURF

                                                    el_up = [POSITION[0]+SIZE[0]/2,POSITION[1]] ; self.up = el_up
                                                    el_down = [POSITION[0]+SIZE[0]/2,POSITION[1]+SIZE[1]] ; self.down = el_down
                                                    el_left = [POSITION[0],POSITION[1]+SIZE[1]/2] ; self.left = el_left
                                                    el_right = [POSITION[0]+SIZE[0],POSITION[1]+SIZE[1]/2] ; self.right = el_right
                                                    
                                                    if FUNCTION=='D':    
                                                        if g_e_pos!=None:self.pos = g_e_pos
                                                        rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                        pygame.draw.ellipse(self.surf,self.col,rect,self.sh)
                                                    elif FUNCTION[1]=='D':
                                                        COLOR = [int(FUNCTION[3:6]),int(FUNCTION[7:10]),int(FUNCTION[11:14])]
                                                        THICKNESS = int(FUNCTION[15:len(FUNCTION)])
                                                        if g_e_pos!=None:self.pos = g_e_pos

                                                        rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])   
                                                        pygame.draw.ellipse(self.surf,self.col,rect,self.sh)

                                                        if COLOR!=None:self.obv_color = COLOR
                                                        if THICKNESS!=None:self.sh2 = THICKNESS

                                                        rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1]) 
                                                        pygame.draw.ellipse(self.surf,self.obv_color,rect,self.sh2)
                                                    elif FUNCTION[0]=='O':
                                                        COLOR = [int(FUNCTION[2:5]),int(FUNCTION[6:9]),int(FUNCTION[10:13])]
                                                        THICKNESS = int(FUNCTION[14:len(FUNCTION)])
                                                        if COLOR!=None:self.obv_color = COLOR
                                                        if THICKNESS!=None:self.sh2 = THICKNESS
                                                        if g_e_pos!=None:self.pos = g_e_pos

                                                        rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                        pygame.draw.ellipse(self.surf,self.obv_color,rect,self.sh2)
                                                    else:
                                                        pass

                                                def FILL(self):
                                                    global g_e_pos
                                                    if g_e_pos!=None:self.pos = g_e_pos
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    pygame.draw.ellipse(self.surf,self.col,rect,self.sh)

                                                def OUTLINE(self,COLOR=None,THICKNESS=None):
                                                    global g_e_pos
                                                    if COLOR!=None:self.obv_color = COLOR
                                                    if THICKNESS!=None:self.sh2 = THICKNESS
                                                    if g_e_pos!=None:self.pos = g_e_pos

                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    pygame.draw.ellipse(self.surf,self.obv_color,rect,self.sh2)

                                                def FILLOUT(self,COLOR=None,THICKNESS=None):
                                                    global g_e_pos
                                                    if g_e_pos!=None:self.pos = g_e_pos

                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])   
                                                    pygame.draw.ellipse(self.surf,self.col,rect,self.sh)

                                                    if COLOR!=None:self.obv_color = COLOR
                                                    if THICKNESS!=None:self.sh2 = THICKNESS

                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1]) 
                                                    pygame.draw.ellipse(self.surf,self.obv_color,rect,self.sh2)

                                                def SET_SIZE(self,SIZE=[]):
                                                    self.size = SIZE

                                                def GET_CENTER(self):
                                                    return self.center

                                                def GET_THICKNESS(self):
                                                    return self.sh

                                                def GET_SURF(self):
                                                    return self.surf

                                                def SET_COLOR(self,COLOR=()):
                                                    self.col = COLOR

                                                def GET_SIZE(self):
                                                    return self.size

                                                def GET_OUTLINE_THICKNESS(self):
                                                    return self.sh2

                                                def SET_OUTLINE_THICKNESS(self,OUTLINE_THICKNESS):
                                                    self.sh2 = OUTLINE_THICKNESS

                                                def SET_THICKNESS(self,THICKNESS):
                                                    self.sh = THICKNESS
                                                    
                                                class SET_POSITION():
                                                    def __init__(self,POSITION=[]):
                                                        global g_e_pos , g_e_size
                                                        self.POSITION = POSITION
                                                        g_e_pos = POSITION

                                                        el_up = [POSITION[0]+g_e_size[0]/2,POSITION[1]]
                                                        el_down = [POSITION[0]+g_e_size[0]/2,POSITION[1]+g_e_size[1]]
                                                        el_left = [POSITION[0],POSITION[1]+g_e_size[1]/2]
                                                        el_right = [POSITION[0]+g_e_size[0],POSITION[1]+g_e_size[1]/2]
                                                        self.up = el_up
                                                        self.down = el_down
                                                        self.left = el_left
                                                        self.right = el_right

                                                    def ON_CENTER(self):
                                                        global g_pos
                                                        POSITION = self.POSITION
                                                        g_e_pos = [POSITION[0]-g_e_size[0]/2,POSITION[1]-g_e_size[1]/2]

                                                        el_up = [POSITION[0]+g_e_size[0]/2,POSITION[1]]
                                                        el_down = [POSITION[0]+g_e_size[0]/2,POSITION[1]+g_e_size[1]]
                                                        el_left = [POSITION[0],POSITION[1]+g_e_size[1]/2]
                                                        el_right = [POSITION[0]+g_e_size[0],POSITION[1]+g_e_size[1]/2]
                                                        self.up = el_up
                                                        self.down = el_down
                                                        self.left = el_left
                                                        self.right = el_right
                                                    
                                                    
                                                


                                            class Triangl:
                                                def __init__(self,COLOR=(),POSITION_1=[],POSITION_2=[],POSITION_3=[],THICKNESS=0,SURF=None):  
                            
                                                    sh2 = 1
                                                    self.sh2 = sh2
                                                    self.col = COLOR
                                                    self.pos1 = POSITION_1
                                                    self.pos2 = POSITION_2
                                                    self.pos3 = POSITION_3
                                                    self.poses = [self.pos1,self.pos2,self.pos3]
                                                    self.sh = THICKNESS
                                                    self.surf = SURF
                                                    

                                                def Draw(self):
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        self.col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh
                                                    )

                                                def Obv(self,col=(0,0,0)):
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh2
                                                    )

                                                def DrOb(self,col=(0,0,0)):
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        self.col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh
                                                    )
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh2
                                                    )

                                                def Get_sh(self):
                                                    return self.sh

                                                def Get_sh2(self):
                                                    return self.sh2

                                                def Set_sh(self,sh2):
                                                    self.sh = sh2

                                                def Set_sh2(self,sh2):
                                                    self.sh2 = sh2

                                                def Set_col(self,col):
                                                    self.col = col

                                                def Set_poses(self,poses=[]):
                                                    self.poses = poses
                                                    self.pos1 = poses[0]
                                                    self.pos2 = poses[1]
                                                    self.pos3 = poses[2]

                                                def Set_pos1(self,pos1=[]):
                                                    self.pos1 = pos1

                                                def Set_pos2(self,pos2=[]):
                                                    self.pos2 = pos2

                                                def Set_pos3(self,pos3=[]):
                                                    self.pos3 = pos3



                                            class Line:
                                                def __init__(self,col=(),start_pos=[],end_pos=[],sh=1,surf=0,type='R'):
                                                    xcnt = start_pos[0]+(end_pos[0]-start_pos[0])/2;ycnt = start_pos[1]+(end_pos[1]-start_pos[1])/2
                                                    center = [xcnt,ycnt]
                                                    rectt = [start_pos,end_pos,center,col,sh]
                                                    self.x_center = xcnt
                                                    self.y_center = ycnt
                                                    self.center = center
                                                    self.rectt = rectt
                                                    self.col = col
                                                    self.start_pos = start_pos
                                                    self.end_pos = end_pos
                                                    self.sh = sh
                                                    self.surf = surf
                                                    self.type = type
                                                    self.poses = [self.start_pos,self.end_pos]

                                                def Draw(self):
                                                    pygame.draw.line( 
                                                        self.surf,
                                                        self.col,
                                                        (self.start_pos[0],self.start_pos[1]),
                                                        (self.end_pos[0],self.end_pos[1]),
                                                        self.sh
                                                    )
                                                    if self.type == 'S' or self.type == 's':
                                                        Display_init.GL.Circle(self.col,[self.start_pos[0]+self.sh/12-1,self.start_pos[1]+1]
                                                        ,self.sh/2,0,self.surf).FILL()
                                                        Display_init.GL.Circle(self.col,[self.end_pos[0]+self.sh/12-1,self.end_pos[1]+1]
                                                        ,self.sh/2,0,self.surf).FILL()
                                                    elif self.type == 'r' or self.type == 'R':
                                                        pass
                                                    else:
                                                        print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
                                                        print(colorama.Fore.YELLOW+'(none) type detected'+colorama.Fore.RESET)
                                                        print(colorama.Fore.YELLOW+'Uses s(S) or r(R)'+colorama.Fore.RESET)
                                                        sys.exit()

                                                def Set_col(self,col):
                                                    self.col = col

                                                def Set_type(self,type2):
                                                    self.type = type2

                                                def Set_poses(self,poses=[]):
                                                    self.poses = poses
                                                    self.start_pos = poses[0]
                                                    self.end_pos = poses[1]

                                                def Set_start_pos(self,pos=[]):
                                                    self.start_pos = pos

                                                def Set_end_pos(self,pos=[]):
                                                    self.end_pos = pos

                                                def Set_sh(self,sh2):
                                                    self.sh = sh2

                                                def Get_col(self):
                                                    return self.col

                                                def Get_poses(self):
                                                    return self.poses

                                                def Get_start_pos(self):
                                                    return self.start_pos

                                                def Get_end_pos(self):
                                                    return self.end_pos



                                            class Liness:
                                                def __init__(self,col=(),points=(),snap=False,sh=1,surf=0):
                                                    rectt = [points,col,snap,sh]

                                                    self.col = col
                                                    self.points = points
                                                    self.snap = snap
                                                    self.sh = sh
                                                    self.surf = surf
                                                    self.rectt = rectt  
                                                def Draw(self):
                                                    pygame.draw.lines( 
                                                        self.surf,
                                                        self.col,
                                                        self.snap,
                                                        self.points,
                                                        self.sh
                                                    )
                                                def Get_points_ind(self,index=0,cor=None):
                                                    if cor == None:
                                                        return self.points[index]
                                                    elif cor == "x" or cor == "X":
                                                        return self.points[index][0]
                                                    elif cor == "y" or cor == "Y":
                                                        return self.points[index][1]
                                                    else:
                                                        print(colorama.Fore.RED+'Error'+colorama.Fore.RESET)
                                                        print(colorama.Fore.YELLOW+'None 2D cords detected.'+colorama.Fore.RESET)
                                                        sys.exit()
                                                def Get_points(self):
                                                    return self.points
                                                def Get_col(self):
                                                    return self.col
                                                def Get_sh(self):
                                                    return self.sh
                                                def Get_snap(self):
                                                    return self.snap
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2



                                            class Pixel:
                                                def __init__(self,col=(),pos=[],sh=1,surf=0):   
                                                    rectt = [pos,col,sh]
                                                    
                                                    self.rectt = rectt
                                                    self.pos = pos
                                                    self.col = col
                                                    self.sh = sh
                                                    self.surf = surf
                                                def Draw(self):
                                                    pygame.draw.line(   
                                                        self.surf,
                                                        self.col,
                                                        (self.pos[0],self.pos[1]),
                                                        (self.pos[0],self.pos[1]),
                                                        self.sh
                                                    )
                                                def Get_pos(self):
                                                    return self.pos
                                                def Get_col(self):
                                                    return self.col
                                                def Get_sh(self):
                                                    return self.sh
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_pos(self,pos=[]):
                                                    self.pos = pos
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2



                                            class Arc:
                                                def __init__(self,col=(),pos=[],start_angle=0,stop_angle=0,rad=1,sh=1,st='-',surf=0):
                                                    grad = 56.5
                                                    ugl1 = start_angle/grad
                                                    rectt=[pos,start_angle,stop_angle,col,sh,st]

                                                    self.grad = grad
                                                    self.ugl = ugl1
                                                    self.start_angl = start_angle
                                                    self.end_angl = stop_angle
                                                    self.col = col
                                                    self.pos = pos
                                                    self.rad = rad
                                                    self.sh = sh
                                                    self.st = st
                                                    self.surf = surf
                                                    self.rectt = rectt                                                   
                                                def Draw(self):
                                                    
                                                    for l in range(int(self.end_angl*3.5)):
                                                        if self.st=='-': self.ugl+=0.005
                                                        elif self.st=='+': self.ugl-=0.005
                                                        else:
                                                            print('no positions detected.')
                                                            sys.exit()
                                                        for i in range(0,self.rad,2): 
                                                            xl=self.pos[0]+i*math.sin(self.ugl);yl=self.pos[1]+i*math.cos(self.ugl)
                                                            if i == self.rad - self.sh:
                                                                xpos = xl;ypos = yl
                                                        pygame.draw.line(self.surf,
                                                                        self.col,
                                                                        [xl,yl],
                                                                        [xpos,ypos],
                                                                        5)     
                                                def Set_end_ugl(self,ugl):
                                                    self.end_angl = ugl       
                                                def Set_start_ugl(self,ugl):
                                                    self.start_angl = ugl
                                                def Set_st(self,st='-'):
                                                    self.st = st     
                                                def Get_st(self):
                                                    return self.st
                                                def Get_col(self):
                                                    return self.col
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_rad(self,rad):
                                                    self.rad = rad
                                                def Get_rad(self):
                                                    return self.rad
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2
                                                def Get_sh(self):
                                                    return self.sh
# 11 
class Sprites_(Surfases_):
    def __init__(self,file=''):
        img = pygame.image.load(file)
        self.img = img
        self.start_img = img
        self.img_rect = self.start_img.get_rect()

    def Draw(self,pos=[]):
        self.pos = pos
        self.rect = self.img.get_rect(bottomright=(pos[0]+self.img.get_width(),pos[1]+self.img.get_height())) 
        screen.blit(self.img,self.rect)
        return self.rect

    def Draw_on_surf(self,surf,pos=[]):
        self.pos = pos
        self.rect = self.img.get_rect(bottomright=(pos[0]+self.img.get_width(),pos[1]+self.img.get_height())) 
        surf.screen.blit(self.img,self.rect)
    def Set_pos(self,pos=[]):
        self.img_rect = self.start_img.get_rect(center=(pos[0],pos[1]))
        self.pos = pos

    def Scale(self,size=[]):
        self.img = pygame.transform.scale(self.img,(size[0],size[1]))
    
    def Rotate(self,ugl):
        self.img = pygame.transform.rotate(self.start_img,ugl)
    
    def Rotate_center(self,ugl):
        rot_img = pygame.transform.rotate(self.start_img,ugl)
        self.rect = rot_img.get_rect(center = self.img_rect.center)
        self.img = rot_img

    def Blit(self,rect):
        screen.blit(self.img,rect)

    def Get_rect(self):
        return self.start_img.get_rect()

    def Save(self,plane,file_name = ''):
        pygame.image.save(plane,file_name)


    def Get_pos(self):
        return self.pos
# 12 -- new !! do not work
class Sprites_Group_:
    def __init__(self,sprites=[]):
        self.sprites = sprites
        self.sprites_pack = []
        for i in self.sprites:
            self.sprites_pack.append(pygame.image.load(i))
    def Draw(self,pos=[0,0],sprite_index=0):
        self.pos = pos
        self.rect = self.sprites_pack[sprite_index].get_rect(bottomright=(pos[0]+self.sprites_pack[sprite_index].get_width(),
                                                                          pos[1]+self.sprites_pack[sprite_index].get_height())) 
        screen.blit(self.sprites_pack[sprite_index],self.rect)
# 13
class Graphick_:
    def __init__(self):
        pass
    def SETcirclGRAPH(self,col=[],znh=[]):
        pit = [col,znh]
        return pit
    def DRcirclGRAPH_2D(self,r=1,xp=1,yp=1,grph=[]):
        kf = 0
        ugl = 1;ugl1=1
        c=r
        g1 = 0
        for g in range(len(grph[0])):
            kf = kf + grph[0][g]

        for g in range(len(grph[1])):
            coll = grph[1][g]
            ugl = ugl1
            for n in range(int(700/kf*grph[0][g1])):
                xl = xp + c * math.sin(ugl)
                yl = yp + c * math.cos(ugl)
                ugl+=0.009
                pygame.draw.line(screen,coll,(xp,yp),(xl,yl),4)
                ugl1 = ugl


            g1 +=1
# 14 -- new !!
class Widgets_:
    def __init__(self):
        self.widgets = [
            'Slider',
            'Button',
            'Toggle',
            'TextBox',
            'DropDown',
            'ProgrsBar'
        ]

    def Get_Print_Widgets(self,index=None):
        if index is None:
            for i in range(len(self.widgets)):
                print(colorama.Fore.RED + f'[ {i+1} ] - ' + colorama.Fore.RESET,end='')
                print(colorama.Fore.YELLOW + self.widgets[i] + colorama.Fore.RESET)

        elif index is not None:
            print(self.widgets)

    def Get_Widgets(self):
        return self.widgets

    class Sliders:
        def __init__(self,plane,
                            pos=[],
                            len=100,
                            size=10,
                            min=0,
                            max=100,
                            step=1,
                            color_slider=(0,0,0),
                            handl_color=(30,30,30),
                            handl_radius=10,
                            curved = True
                            ):
            self.plane = plane
            self.pos = pos
            self.posx = pos[0]
            self.posy = pos[1]
            self.len = len
            self.curved = curved
            self.size = size
            self.min = min
            self.max = max
            self.step = step
            self.color_slider = color_slider
            self.handl_color = handl_color
            self.handl_radius = handl_radius
            slide = Slider(self.plane,
                            self.posx,
                            self.posy,
                            self.len,
                            self.size,
                            min = self.min,
                            max = self.max,
                            step = self.step,
                            colour = self.color_slider,
                            handleColour = self.handl_color,
                            handleRadius = self.handl_radius,
                            curved = self.curved)
            self.slide = slide

        def Get_value(self):
            val = self.slide.getValue()
            return val

        def Update(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame_widgets.update(events)

        def Set_pos(self,pos=[]):
            self.pos = pos
            self.posx = pos[0]
            self.posy = pos[1]
            self.slide.setX(pos[0])
            self.slide.setY(pos[1])

        def Set_posx(self,x):
            self.posx = x
            self.slide.setX(x)

        def Set_posy(self,y):
            self.posy = y
            self.slide.setY(y)

        def Set_width(self,width):
            self.len = width
            self.slide.setWidth(width)

        def Set_height(self,height):
            self.size = height
            self.slide.setHeight(height)

        def Set_size(self,size=[]):
            self.size = size[1]
            self.len = size[0]
            self.slide.setHeight(size[1])
            self.slide.setWidth(size[0])

        def Hide(self):
            self.slide.hide()

        def Show(self):
            self.slide.show()

        def Set_value(self,value):
            self.slide.setValue(value)

        def Get_curved(self):
            return self.curved

        def Get_pos(self):
            return self.pos

        def Get_posx(self):
            return self.posx

        def Get_posy(self):
            return self.posy

        def Get_size(self):
            return self.size

        def Get_value(self):
            return self.slide.getValue()

        def Get_min(self):
            return self.min

        def Get_max(self):
            return self.max

        def Get_step(self):
            return self.step

        def Get_slider_color(self):
            return self.color_slider

        def Get_handl_color(self):
            return self.handl_color

        def Get_handl_radius(self):
            return self.handl_radius

        def Disable(self):
            self.slide.disable()

        def Enable(self):
            self.slide.enable()

        def Set_orintation(self,orint):
            self.slide.vertical = orint

        def Get_selected(self):
            return self.slide.selected

    class TextBoxs:
        def __init__(self,plane,
                            pos=[],
                            size=[],
                            font_size=30,
                            border_color=(0,0,0),
                            text_color = (0,0,0),
                            onSub=Function,radius = 1,
                            border_size=5
                            ):
            self.plane = plane
            self.pos = pos
            self.size = size
            self.width = size[0]
            self.height = size[1]
            self.font_size = font_size
            self.border_color = border_color
            self.text_color = text_color
            self.radius = radius
            self.border_size = border_size
            self.posx = self.pos[0]
            self.posy = self.pos[1]
            tb = TextBox(self.plane,
                            self.posx,self.posy,
                            self.width,self.height,
                            fontSize = self.font_size,
                            borderColour = self.border_color,
                            textColour = text_color,
                            onSubmit = onSub,
                            radius = self.radius,
                            borderThickness = self.border_size)
            self.tb = tb

        def Get_text(self):
            text = self.tb.getText()
            return text

        def Set_text(self,text=''):
            self.tb.setText(text)

        def Update(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame_widgets.update(events)

        def Set_size(self,size=[]):
            self.width = size[0]
            self.height = size[1]
            self.tb.setWidth(size[0])
            self.tb.setHeight(size[1])

        def Set_posx(self,x):
            self.posx = x
            self.tb.setX(x)

        def Set_posy(self,y):
            self.posy = y
            self.tb.setY(y)

        def Set_pos(self,pos=[]):
            self.posy = pos[1]
            self.tb.setY(pos[1])
            self.posx = pos[0]
            self.tb.setX(pos[0])

        def Hide(self):
            self.tb.hide()

        def Show(self):
            self.tb.show()

        def Set_output_disable(self):
            self.tb.disable()

        def Set_output_enable(self):
            self.tb.enable()

        def Set_width(self,width):
            self.width = width
            self.tb.setWidth(width)

        def Set_height(self,height):
            self.height = height
            self.tb.setHeight = height

        def Get_height(self):
            return self.tb.getHeight()

        def Get_width(self):
            return self.tb.getWidth()

        def Get_pos(self):
            return self.pos

        def Get_posx(self):
            return self.posx

        def Get_posy(self):
            return self.posy

        def Get_size(self):
            return self.size

        def Get_font_size(self):
            return self.font_size

        def Get_border_color(self):
            return self.border_color

        def Get_text_color(self):
            return self.text_color

        def Get_radius(self):
            return self.radius

        def Get_border_size(self):
            return self.border_size  

        def Disable(self):
            self.tb.disable()

        def Enable(self):
            self.tb.enable()

        def Get_selected(self):
            return self.tb.selected

    class Buttons:
        def __init__(self,plane,
                            pos=[],
                            size=[],
                            text='',
                            text_color=(0,0,0),
                            font_size=20,
                            margin = 20,
                            no_activ_color = (10,10,10),
                            activ_color = (30,30,30),
                            pressed_color=(60,60,60),
                            radius=20,
                            functions=Function,
                            shadow_dist = 0,
                            shadow_color = (0,0,0)
                            ):
            self.plane = plane
            self.pos = pos
            self.size = size
            self.posx = self.pos[0]
            self.posy = self.pos[1]
            self.width = self.size[0]
            self.height = self.size[1]
            self.text = text
            self.font_size = font_size
            self.margin = margin
            self.no_activ_color = no_activ_color
            self.activ_color = activ_color
            self.pressed_color = pressed_color
            self.radius = radius
            self.text_color = text_color
            self.shadow_dist = shadow_dist
            self.shadow_color = shadow_color
            bt = Button(
                self.plane,
                self.posx,self.posy,
                self.width,self.height,
                text=self.text,
                fontSize = self.font_size,
                margin = self.margin,
                inactiveColour = self.no_activ_color,
                hoverColour = self.activ_color,
                pressedColour = self.pressed_color,
                radius = self.radius,
                onClick = functions,
                textColour = self.text_color,
                shadowColour = self.shadow_color,
                shadowDistance = self.shadow_dist
            )
            self.bt = bt

        def Update(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame_widgets.update(events)

        def Set_posx(self,x):
            self.posx = x
            self.bt.setX(x)

        def Set_posy(self,y):
            self.posy = y
            self.bt.setY(y)

        def Set_width(self,width):
            self.width = width
            self.bt.setWidth(width)

        def Set_height(self,height):
            self.height = height
            self.bt.setHeight(height)

        def Set_size(self,size=[]):
            self.height = size[1]
            self.width = size[0]
            self.bt.setWidth(size[0])
            self.bt.setHeight(size[1])

        def Set_pos(self,pos = []):
            self.posx = pos[0]
            self.posy = pos[1]
            self.bt.setX(pos[0])
            self.bt.setY(pos[1])

        def Set_pressed_color(self,color):
            self.pressed_color = color
            self.bt.setPressedColour(color)

        def Set_activ_color(self,color):
            self.activ_color = color
            self.bt.setHoverColour(color)

        def Set_no_activ_color(self,color):
            self.no_activ_color = color
            self.bt.setInactiveColour(color)

        def Get_pos(self):
            return self.pos

        def Get_posx(self):
            return self.posx

        def Get_posy(self):
            return self.posy

        def Get_size(self):
            return self.size

        def Get_width(self):
            return self.width

        def Get_height(self):
            return self.height

        def Get_text(self):
            return self.text

        def Get_font_size(self):
            return self.font_size

        def Get_margin(self):
            return self.margin

        def Get_no_activ_color(self):
            return self.no_activ_color

        def Get_activ_color(self):
            return self.activ_color

        def Get_pressed_color(self):
            return self.pressed_color

        def Get_radius(self):
            return self.radius

        def Get_text_color(self):
            return self.text_color

        def Get_shadow_color(self):
            return self.shadow_color

        def Get_shadow_distance(self):
            return self.shadow_dist

        def Show(self):
            self.bt.show()

        def Hide(self):
            self.bt.hide()

        def Get_pressed(self):
            return self.bt.clicked

        def Sleep(self):
            self.bt.disable()

        def Stendup(self):
            self.bt.enable()

        def Disable(self):
            self.bt.disable()

        def Enable(self):
            self.bt.enable()

    class Toggles:
        def __init__(self,plane,
                            pos = [],
                            size = [],
                            startType = False,
                            oncolor = (141, 185, 244),
                            offcolor = (150, 150, 150),
                            handl_oncolor = (26, 115, 232),
                            handl_offcolor = (200, 200, 200),
                            radius = 20
                            ):
            self.plane = plane
            self.pos = pos
            self.posx = self.pos[0]
            self.posy = self.pos[1]
            self.size = size
            self.width = self.size[0]
            self.height = self.size[1]
            self.startType = startType
            self.oncolor = oncolor
            self.offcolor = offcolor
            self.handl_oncolor = handl_oncolor
            self.handl_offcolor = handl_offcolor
            self.radius = radius
            tg = Toggle(
                self.plane,
                self.posx,self.posy,
                self.width,self.height,
                startOn = self.startType,
                offColour = self.offcolor,
                onColour = self.oncolor,
                handleOnColour = self.handl_oncolor,
                handleOffColour = self.handl_offcolor,
                handleRadius = self.radius
            )
            self.tg = tg

        def Update(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame_widgets.update(events)

        def Set_pos(self,pos=[]):
            self.posx = pos[0]
            self.posy = pos[1]
            self.tg.setX(pos[0])
            self.tg.setY(pos[1])

        def Set_posx(self,x):
            self.posx = x
            self.tg.setX(x)

        def Set_posy(self,y):
            self.posy = y
            self.tg.setY(y)

        def Set_width(self,width):
            self.width = width
            self.tg.setWidth(width)

        def Set_height(self,height):
            self.height = height
            self.tg.setHeight(height)

        def Hide(self):
            self.tg.hide()

        def Show(self):
            self.tg.show()

        def Get_value(self):
            val = self.tg.getValue()
            return val

        def Get_height(self):
            return self.tg.getHeight()

        def Get_width(self):
            return self.tg.getWidth()

        def Get_size(self):
            return self.size

        def Get_pos(self):
            return self.pos

        def Get_posx(self):
            return self.posx

        def Get_posy(self):
            return self.posy

        def Get_start_Type(self):
            return self.startType

        def Get_oncolor(self):
            return self.oncolor

        def Get_offcolor(self):
            return self.offcolor

        def Get_handl_oncolor(self):
            return self.handl_oncolor

        def Get_handl_offcolor(self):
            return self.handl_offcolor

        def Get_radius(self):
            return self.radius

    class DropDowns:
        def __init__(self,plane,
                            pos = [],
                            size = [],
                            name = '',
                            choices = [],
                            radius = 0,
                            color = (),
                            values = [],
                            direction = 'down',
                            issubwidget = False,
                            text_color=(0,0,0),
                            font=None,
                            font_size=20):
            self.plane = plane
            self.pos = pos
            self.posx = pos[0]
            self.posy = pos[1]
            self.size = size
            self.width = size[0]
            self.height = size[1]
            self.name = name
            self.choices = choices
            self.radius = radius
            self.color = color
            self.values = values
            self.direction = direction
            self.issubwidget = issubwidget
            self.text_color = text_color
            self.font = font
            self.font_size = font_size
            dd = Dropdown(
                self.plane,
                self.posx,self.posy,
                self.width,self.height,
                self.name,
                self.choices,
                self.issubwidget, 
                borderRadius = self.radius,
                colour = self.color,
                values = self.values,
                direction = self.direction,
                textColour = self.text_color,
                fontSize = self.font_size
            )
            self.dd = dd

        def Update(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame_widgets.update(events)

        def Get_selected(self):
            return self.dd.getSelected()

        def Get_dropped(self):
            return self.dd.isDropped()

        def Get_x(self):
            return self.dd.getX()

        def Get_y(self):
            return self.dd.getY()

        def Set_pos(self,pos=[]):
            self.posx = pos[0]
            self.posy = pos[1]
            self.dd.setX(pos[0])
            self.dd.setY(pos[1])

        def Get_pos(self):
            return [self.dd.getX(),self.dd.getY()]

        def Get_size(self):
            return [self.dd.getWidth(),self.dd.getHeight()]

        def Get_width(self):
            return self.dd.getWidth()
        
        def Get_height(self):
            return self.dd.getHeight()

        def Set_height(self, height):
            self.height = height
            self.dd.setHeight(height)

        def Set_width(self, width):
            self.width = width
            self.dd.setWidth(width)

        def Set_posx(self,x):
            self.posx = x
            self.dd.setX(x)

        def Set_posy(self,y):
            self.posy = y
            self.dd.setY(y)

        def Hide(self):
            self.dd.hide()

        def Show(self):
            self.dd.show()

        def Enable(self):
            self.dd.enable()

        def Disable(self):
            self.dd.disable()

    class ProgressBar:
        def __init__(self,plane,
                        pos = [],
                        size = [],
                        Progress_function = None,
                        Completed_color = (0,200,0),
                        Incompleted_color = (100,100,100),
                        Curved = False,
                        ):

            self.plane = plane
            self.pos = pos
            self.size = size
            self.Completed_color = Completed_color
            self.Incompleted_color = Incompleted_color
            self.Curved = Curved

            self.pb = ProgressBar(
                self.plane,
                self.pos[0],self.pos[1],
                self.size[0],self.size[1],
                Progress_function,
                completedColour = self.Completed_color,
                incompletedColour = self.Incompleted_color,
                curved = self.Curved
            )

        def Update(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame_widgets.update(events)

        def Get_prcent(self):
            return self.pb.percent

        def Get_width(self):
            return self.pb.getWidth()

        def Get_height(self):
            return self.pb.getHeight()

        def Get_pos(self):
            return [self.pb.getX(), self.pb.getY()]

        def Get_size(self):
            return [self.pb.getWidth(), self.pb.getHeight()]

        def Get_posx(self):
            return self.pb.getX()

        def Get_posy(self):
            return self.pb.getY()

        def Set_size(self, size=[]):
            self.pb.setHeight(size[1])
            self.pb.setWidth(size[0])

        def Set_width(self,width):
            self.pb.setWidth(width)

        def Set_height(self,height):
            self.pb.setHeight(height)

        def Hide(self):
            self.pb.hide()

        def Show(self):
            self.pb.show()

        def Disable(self):
            self.pb.disable()

        def Enable(self):
            self.pb.enable()
# 15 -- new !!
class Objectes_:
    def __init__(self,name='obj'):
        self.name = name
        self.pack = []

    def Add(self,obj,mass=False):
        if mass == True:
            self.pack.append(obj)
        else:
            if len(obj)>1:
                for i in range(len(obj)):
                    self.pack.append(obj[i])
            else:
                self.pack.append(obj)   

    def Del_min(self,index):
        self.pack.pop(index)

    def Del_max(self,a_index,b_index):
        del self.pack[a_index-1:b_index]

    def Get_name(self):
        return self.name

    def Set_name(self,name):
        self.name = name

    def Get_pack(self):
        return self.pack
# 16 -- new !!
class Img_:
    def __init__(self,surface):
        self.surface = surface
        
    def Draw(self,pos =[]):
        self.pos = pos
        self.rect = self.surface.get_rect(bottomright=(pos[0]+self.surface.get_width(),pos[1]+self.surface.get_height())) 
        screen.blit(self.surface,self.rect)








































