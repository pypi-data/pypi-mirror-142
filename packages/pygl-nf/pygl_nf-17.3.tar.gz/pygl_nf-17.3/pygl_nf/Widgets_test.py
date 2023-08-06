#from pygl_nf import GL
import time
import GL

GL.Widgets_().Get_Print_Widgets()

win = GL.Display_init_(
    flags=GL.D_Full
)

startTime = time.time()



text_box = GL.Widgets_.TextBoxs(
    win.screen,
    [10,10],[600,60],
    50,
    (200,200,200),
    (100,100,100),
    GL.Passing,
    10
)

button = GL.Widgets_.Buttons(
    win.screen,
    [10,80],[300,80],
    'Click',(20,180,60),
    60,60,
    (100,50,200),(60,60,170),(120,60,160),
    10,GL.Passing,
    10,(100,100,100)
)

drop_down = GL.Widgets_.DropDowns(
    win.screen,
    [650,10],[180,60],
    'Colors',
    [
        'red',
        'green',
        'blue',
        'yellow',
        'pink',
        'black',
        'white'
    ],
    10,
    (10,120,60),
    [
        'red',
        'green',
        'blue',
        'yellow',
        'pink',
        'black',
        'white'
    ],
    'down',
    False,(100,190,30),
    None,
    40
)

toggle = GL.Widgets_.Toggles(
    win.screen,
    [20,190],[60,30],
    'True'
)

slider = GL.Widgets_.Sliders(
    win.screen,
    [20,250],
    200,27,
    0,200,
    1,(100,200,160),(60,220,180)
)

GL.Progress_bar_time = 20
progressbar = GL.Widgets_.ProgressBar(
    win.screen,
    [100,700],[300,50],GL.Progres_bar_buffer,Curved=True)


def App():
    while win.CLOSE():
        win.UPDATE().SET_BG_COLOR()

        text_box.Update()
        button.Update()
        drop_down.Update()
        toggle.Update()
        slider.Update()
        progressbar.Update()
        text_box.Set_text(str(progressbar.Get_prcent()))

if __name__ == '__main__':
    App()
    

