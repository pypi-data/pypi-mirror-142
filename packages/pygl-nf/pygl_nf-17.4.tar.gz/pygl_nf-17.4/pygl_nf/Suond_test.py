from pygl_nf import GL

sound1 = GL.Sound_mixer_('Jump2.wav')

mouse = GL.Sub_events_.Mouse_init()
win = GL.Display_init_(flags=GL.D_Full)



def App():
    while win.CLOSE():
        win.UPDATE()


        win.GL.Rect('red',[300,500],[300,50],0,'s','D')

        if mouse.GET_PRESS_ON_PYGL_WINDOW():
            if win.GET_COLOR(mouse.GET_POSITION()[0],mouse.GET_POSITION()[1])==[255,0,0]:
                sound1.Play()

if __name__=='__main__':
    App()



