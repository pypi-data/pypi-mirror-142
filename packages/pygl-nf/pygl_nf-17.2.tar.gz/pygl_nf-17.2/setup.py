from setuptools import setup  
requirements = ["Pygame==2.1.1","keyboard","pygame_widgets","colorama"]
setup(name='pygl_nf',
       version='17.2',
       description='small and compact graphick distributions',
       packages=['pygl_nf'],       
       author_email='pvana621@gmail.com', 
       install_requires=requirements,      
       zip_safe=False)