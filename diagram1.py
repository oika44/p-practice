
def main():
    
    txtDiagram = create_diagrram(DiagramFactory())
    txtDiagram.save(textFilename)
    svgDIaggram= create_diagram(DiagramFactory())
    svgDiagram.save(svgFilename)
    
def create_diagram(DiagramFactory):
    diagram =factory.make_diagram(30,7)
    rectangle = factory.make_rectangle(4,1,22,5,"yellow")
    text = factory.make_text(7,3,"Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram


class DiagramFactory:
    def make_diagram(self,width,height):
        return Diagram(width,height)
    def make_rectangle(self,x,y,width,height,fill="white",stroke="black"):
        return Rectangle(self,x,y,width,height,fill,stroke)
    def make_text(self,x,y,text,fontsize=12):
        retrn Text(x,y,text,fontsize)
        
        
        
