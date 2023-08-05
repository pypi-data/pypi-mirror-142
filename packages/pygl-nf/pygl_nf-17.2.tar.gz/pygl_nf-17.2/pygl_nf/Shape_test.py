from pygl_nf import GL

win = GL.Display_init(flags=GL.Full)

def App():
    while win.CLOSE():
        win.UPDATE()

        rect = win.GL.Rect(GL.c_NAVY,[200,200],[300,175],0,'s','D')
        circle = win.GL.Circle(GL.c_CRIMSON,[500,500],93,0,'s','D')
        ellips = win.GL.Ellips(GL.c_SKY_BLUE,[700,100],[300,112],0,'s','D')

if __name__ == '__main__':
    App()