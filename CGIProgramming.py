# CGI stands for common gateway interface
class LazyClass:
    def __init__(self,width,length,height):
        """:arg"""
        self.width=width
        self.length=length
        self.height=height
    def getMeasurements(self):
        print (f"""
Height:{self.height}
Width: {self.width} 
Height: {self.height}""")

if __name__=="__main__":
    day=LazyClass(10,20,30)
    day.getMeasurements()
class BusyClass:
    def __init__(self):
        """:arg"""
        pass