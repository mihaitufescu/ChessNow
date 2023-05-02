class Cal:
    culoare = 'default'
    activ = 'default'
    coordonata_x = -1
    coordonata_y = -1
    def __init__(self,culoare='default',activ=-1,coordonata_x=-1,coordonata_y=-1):
        self.culoare = culoare
        self.activ = activ
        self.coordonata_x=coordonata_x
        self.coordonata_y=coordonata_y
    def setCoord(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
    def createInstance(self):
        obj = Cal()
        return obj
    def canMove(self):
        print('Test')
    def died(self):
        print('Test')
    def __del__(self):
        print("Dctr")

