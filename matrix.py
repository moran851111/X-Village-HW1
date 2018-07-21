import random
from copy import deepcopy

class Matrix:

    def __init__(self):
        """Construct a (nrows X ncols) matrix"""
        
        self.am = []
        self.cm = []
        self.dm = []
        self.em = []
        self.fm = []
        
        number = random.randint(0,9) 
        
       
       
        self.ar = int(input("Enter A matrix's rows:"))   
        self.ac = int(input("Enter A matrix's cols:"))  


        for i in range(1,self.ar+1):
            for j in range(1,self.ac+1):                                  
                self.am.append(random.randint(0,9))
            #print(self.am)  
      
        self.br = int(input("Enter B matrix's rows:"))
        self.bc = int(input("Enter B matrix's cols:"))
        self.bm = []    
        
        for i in range(1,self.br+1):
            for j in range(1,self.bc+1):                                  
                self.bm.append(random.randint(0,9))  
      
      
    

    def add(self):
        for i in range(0,len(self.am)):
            for j in range(i,i+1):
                self.cm.append(self.am[i]+self.bm[j])
                

    
    def sub(self):
        
        for i in range(0,len(self.am)):
            for j in range(i,i+1):
                self.dm.append(self.am[i]-self.bm[j])
                              

    def mul(self):
       
        sum = 0
        L = 0

        while L < len(self.am):   #3
            for i in range(0,self.ac):
                for j in range(0,self.ar):  # 跑 欄 數               
                    k = 0
                    sum += (self.am[j+L] * self.bm[i+k]) 
                    k += self.ac
                self.em.append(sum)
                sum = 0
           
            L += self.ac

    

    def transpose(self):
        for i in range(0,self.ar):   #
            for j in self.em[ i : (self.ar-1) * self.ar +i +1 : self.ar ]:
                self.fm.append(j)

        
    
    
    
    
    
    def display (self):
        
        print('A_Matrix:')
        for i in range(0,self.ar):   #  0 3 6
            for j in self.am[i * self.ar : i*self.ar + self.ar]:
                print(j , end=' ')
            print(' ')
               
          
        print("= = = = = = =")  
        print('B_Matrix:') 
        for i in range(0,self.br):   #  0 3 6
            for j in self.bm[i * self.br : i*self.br + self.br]:
                print(j , end=' ')
            print(' ')


        print("= = = = = = =")     
        print('Matrix_A+B:')
        for i in range(0,self.ar):   #  0 3 6
            for j in self.cm[i * self.ar : i*self.ar + self.ar]:
                print(j , end=' ')
            print(' ')

        print("= = = = = = =")        
        print('Matrix_A-B:')
        for i in range(0,self.ar):   #  0 3 6
            for j in self.dm[i * self.ar : i*self.ar + self.ar]:
                print(j , end=' ')
            print(' ')

        print("= = = = = = =")
        print('Matrix_A*B:')
        for i in range(0,self.ar):   #  0 3 6
            for j in self.em[i * self.ar : i*self.ar + self.ar]:
                print(j , end=' ')
            print(' ')
        
        print("= = = = = = =")
        print('Matrix_A/B:')
        for i in range(0,self.ar):   #  0 3 6
            for j in self.fm[i * self.ar : i*self.ar + self.ar]:
                print(j , end=' ')
            print(' ')
            




A_Matrix = Matrix()
A_Matrix.add()
A_Matrix.sub()
A_Matrix.mul()
A_Matrix.transpose()
A_Matrix.display()

