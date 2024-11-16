import numpy as np
import equations as eq

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
            match self.roomColorPos[k]:
                #red
                case 0:
                    self.wavelengths.append(np.random.randint(620,700))
                #orange
                case 1:
                    self.wavelengths.append(np.random.randint(580,619))
                #yellow
                case 2:
                    self.wavelengths.append(np.random.randint(570,579))
                #green
                case 3:
                    self.wavelengths.append(np.random.randint(495,569))
                #blue
                case 4:
                    self.wavelengths.append(np.random.randint(450,494))
                #indigo
                case 5:
                    self.wavelengths.append(np.random.randint(425,449))
                #violet
                case 6:
                    self.wavelengths.append(np.random.randint(400,424))
            k+=1

        self.angularResolution = np.round(eq.angularResolution(np.random.randint(10,20),self.wavelengths[0])*100,1)
        

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

                j = 0
                while j<3:
                    self.cbroomColorRGB.append(pRGB[self.roomColorPos[j]])
                    j+=1
            #Deuteranopes
            case 1:
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
            #Tritanopes
            case 2: 
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
        print('The chosen type: ',self.type,', The RGB values chosen: ',self.roomColorRGB,', The wavelengths generated: ',self.wavelengths,", the color perceived: ",self.cbroomColorRGB ,', The angular resolution required for room 1: ', self.angularResolution,"*10^-11") 