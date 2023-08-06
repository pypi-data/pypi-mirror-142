from pygl_nf import GL


win = GL.Display_init_(flags=GL.D_Resize)

rect = win.GL.Rect(GL.c_NAVY,[200,200],[300,175],0,'s')
circle = win.GL.Circle(GL.c_CRIMSON,[500,500],93,0,'s')
ellips = win.GL.Ellips(GL.c_SKY_BLUE,[700,100],[300,112],0,'s')
triangl = win.GL.Triangl('red',[100,100],[200,100],[150,200],0,'s')
lines = win.GL.Line('green',[100,700],[700,600],6,'s','R')



draw_shapes = win.FUNCTION('draw',
    [
        rect.FILL,
        circle.FILL,
        ellips.FILL,
        triangl.FILL, 
        lines.OUTLINE
    ]
)

print('Shapes Count =',win.GET_SHAPES_COUNT())

def App():
    while win.CLOSE():
        win.UPDATE()
        
        draw_shapes.LOOP()
        
        

if __name__ == '__main__':
    App()