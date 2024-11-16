import numpy as np

class roomBuidler:
    #Roygbiv

    def __init__(self):
        colorList = [(255,0,0),(255,165,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130),(238,130,238)]
        self.type = np.random.randint(0,2)
        self.roomColorPos = []
        self.roomColorRGB = []
        i=0
        while i<3:
            x = colorList[np.random.randint(0,len(colorList))]
            self.roomColorPos.append(colorList.index(x))
            self.roomColorRGB.append(x)
            colorList.pop(x)
            i+=1
        self.cbroomColorRGB = []
        match self.type:
            #Protanopia
            case 0:
                pRed = (128,128,0)
                pOrange = (191,128,0)
                pYellow = (255,255,0)
                pGreen = (128,255,128)
                pBlue = (0,0,255)
                pIndigo = (75,0,120)
                pViolet = (214,141,214)
                pRGB = [pRed,pOrange,pYellow,pGreen,pBlue,pIndigo,pViolet]

                while i<3:
                    self.cbroomColorRGB.append(pRGB[self.roomColorPos[i]])

                return
            #Deuteranopes
            case 1:
                dRed = (255,102,102)
                dOrange = (255,178,102)
                dYellow = (255,255,102)
                dGreen = (204,204,0)
                dBlue = (0,0,255)
                dIndigo = (64)
                dViolet = ()
                dRGB = ()
                return
            #Tritanopes
            case 2:
                return
        