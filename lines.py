
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
class Line:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)
        


        
        
