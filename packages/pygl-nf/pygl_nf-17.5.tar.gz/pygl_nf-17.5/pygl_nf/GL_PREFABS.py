from pygl_nf import GL
from colorama import Fore as FO
import sys


class Sound(object):
    def __init__(self):
        pass
    class Jamps(object):
        def __init__(self):
            self.jamp1 = 'Prefabs\Sounds\Jamps\Jump1.wav'
            self.jamp2 = 'Prefabs\Sounds\Jamps\Jump2.wav'
            self.jamp3 = 'Prefabs\Sounds\Jamps\Jump3.wav'
            self.jamp4 = 'Prefabs\Sounds\Jamps\Jump4.wav'
            self.jamp5 = 'Prefabs\Sounds\Jamps\Jump5.wav'
            self.jamp6 = 'Prefabs\Sounds\Jamps\Jump6.wav'
            self.jamp7 = 'Prefabs\Sounds\Jamps\Jump7.wav'
            self.jamp8 = 'Prefabs\Sounds\Jamps\Jump8.wav'
            self.jamp9 = 'Prefabs\Sounds\Jamps\Jump9.wav'
            self.jamp10 = 'Prefabs\Sounds\Jamps\Jump10.wav'

            jamp1 = self.jamp1
            jamp2 = self.jamp2
            jamp3 = self.jamp3
            jamp4 = self.jamp4
            jamp5 = self.jamp5
            jamp6 = self.jamp6
            jamp7 = self.jamp7
            jamp8 = self.jamp8
            jamp9 = self.jamp9
            jamp10 = self.jamp10

            self._Jamp_Sounds = [jamp1,jamp2,jamp3,jamp4,jamp5,jamp6,jamp7,jamp8,jamp9,jamp10]

        def GET_SOUND_FOR_NAME(self,Sound_file):
            sound = GL.Sound_mixer_(Sound_file)
            return sound

        def GET_SOUND_FOR_INDEX(self,Index):
            if Index > len(self._Jamp_Sounds):
                print (FO.RED+"Sound index out of range"+FO.RESET)
                sys.exit()
            sound = GL.Sound_mixer_(self._Jamp_Sounds[Index])
            return sound

    class Pickaps(object):
        def __init__(self):
            self.pickup1 = 'Prefabs\Sounds\Pickuping\Pickup_Coin1.wav'
            self.pickup2 = 'Prefabs\Sounds\Pickuping\Pickup_Coin2.wav'
            self.pickup3 = 'Prefabs\Sounds\Pickuping\Pickup_Coin3.wav'
            self.pickup4 = 'Prefabs\Sounds\Pickuping\Pickup_Coin4.wav'
            self.pickup5 = 'Prefabs\Sounds\Pickuping\Pickup_Coin5.wav'
            self.pickup6 = 'Prefabs\Sounds\Pickuping\Pickup_Coin6.wav'
            self.pickup7 = 'Prefabs\Sounds\Pickuping\Pickup_Coin7.wav'
            self.pickup8 = 'Prefabs\Sounds\Pickuping\Pickup_Coin8.wav'
            self.pickup9 = 'Prefabs\Sounds\Pickuping\Pickup_Coin9.wav'
            self.pickup10 = 'Prefabs\Sounds\Pickuping\Pickup_Coin10.wav'

            pickup1 = self.pickup1
            pickup2 = self.pickup2
            pickup3 = self.pickup3
            pickup4 = self.pickup4
            pickup5 = self.pickup5
            pickup6 = self.pickup6
            pickup7 = self.pickup7
            pickup8 = self.pickup8
            pickup9 = self.pickup9
            pickup10 = self.pickup10

            self._Pickup_Sounds = [pickup1,pickup2,pickup3,pickup4,pickup5,pickup6,pickup7,pickup8,pickup9,pickup10]

        def GET_SOUND_FOR_NAME(self,Sound_file):
            sound = GL.Sound_mixer_(Sound_file)
            return sound

        def GET_SOUND_FOR_INDEX(self,Index):
            if Index > len(self._Pickup_Sounds):
                print (FO.RED+"Sound index out of range"+FO.RESET)
                sys.exit()
            sound = GL.Sound_mixer_(self._Pickup_Sounds[Index])
            return sound

        


        