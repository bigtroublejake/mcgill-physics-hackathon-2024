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
            p = colorList.index(x)
            if(x != None):
                self.roomColorPos.append(p)
                self.roomColorRGB.append(x)
                colorList[p] = None
                i+=1
        
        self.wavelengths = []
        k=0
        while k<3:
            print("k loop initialized")
            match self.roomColorPos[k]:
                #red
                case 0:
                    self.wavelengths.append(np.random.randint(620,750))
                #orange
                case 1:
                    self.wavelengths.append(np.random.randint(580,619))
                #yellow
                case 2:
                    self.wavelengths.append(np.random.randint(570,579))
                #green
                case 3:
                    self.wavelengths.append(np.random.randint(495,569))
                case 4:
                    self.wavelengths.append(np.random.randint(450,494))
                case 5:
                    self.wavelengths.append(np.random.randint(620,750))
                case 6:
                    self.wavelengths.append(np.random.randint(620,750))
            k+=1

        self.cbroomColorRGB = []
        match self.type:
            #Protanopia
            case 0:
                print("Type0 match activated")
                pRed = (128,128,0)
                pOrange = (191,128,0)
                pYellow = (255,255,0)
                pGreen = (128,255,128)
                pBlue = (0,0,255)
                pIndigo = (75,0,120)
                pViolet = (214,141,214)
                pRGB = [pRed,pOrange,pYellow,pGreen,pBlue,pIndigo,pViolet]

                j = 0
                while j<3:
                    self.cbroomColorRGB.append(pRGB[self.roomColorPos[j]])
                    j+=1
                return
            #Deuteranopes
            case 1:
                print("Type1 match activated")
                dRed = (255,102,102)
                dOrange = (255,178,102)
                dYellow = (255,255,102)
                dGreen = (204,204,0)
                dBlue = (0,0,255)
                dIndigo = (64,0,114)
                dViolet = (221,159,211)
                dRGB = [dRed,dOrange,dYellow,dGreen,dBlue,dIndigo, dViolet]

                j=0
                while j<3:
                    self.cbroomColorRGB.append(dRGB[self.roomColorPos[j]])
                    j+=1
                return
            #Tritanopes
            case 2:
                print("Type2 match activated")
                tRed = (255,0,0)
                tOrange = (255,128,0)
                tYellow = (255,191,128)
                tGreen = (128,255,128)
                tBlue = (0,128,255)
                tIndigo = (64,0,114)
                tViolet = (204,169,204)
                tRGB = [tRed,tOrange,tYellow,tGreen,tBlue,tIndigo,tViolet]

                j=0
                while j<3:
                    self.cbroomColorRGB.append(tRGB[self.roomColorPos[j]])
                    j+=1
                return
        