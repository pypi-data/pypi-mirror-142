def getdtapath():
      import os
      import sys
      import PythonTsa 
      dtapath=os.path.dirname(PythonTsa.__file__)
      if sys.platform=='win32':
         newdtapath=dtapath+'\\Ptsadata\\'
      elif sys.platform=='darwin':   
            newdtapath=dtapath+'/Ptsadata/'
      else:
            print('Sorry, your platform should be Windows or Mac !')
            
      return newdtapath
      
