class Block:
    def __init__(self, dimensions):
        self.width = dimensions[0]
        self.length = dimensions[1]
        self.height = dimensions[2]
        
    def get_width(self): 
        return self.width
    
    def get_length(self):
        return self.length
    
    def get_height(self): 
        return self.height
    
    def get_volume(self):
        return self.width*self.length*self.height
    
    def get_surface_area(self):
        return 2*((self.width*self.height)+(self.width*self.length)+(self.height*self.length))