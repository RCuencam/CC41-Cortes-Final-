class box: 
      
    def __init__(self, h, w, d): 
        self.h = h 
        self.w = w 
        self.d = d 
  
    def __lt__(self, other): 
        return self.d * self.w < other.d * other.w 