class StudentRecord:
    
    def __init__(self, studentname, studentID):
        
        self.name = studentname
        self.ID = studentID
    
    def updateMid(self, midterm):
        self.midterm = midterm
    
    def updateFinal(self, final):
        self.final = final 
    
    def updateLab(self, Lab):
        self.lab = Lab
    
    def calculateTotal(self):
        
        self.total = self.midterm + self.final + self.lab
        return self.total