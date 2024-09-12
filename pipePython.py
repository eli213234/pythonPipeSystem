def pipeSystem(fileName):
    
    pipeSymbols = [ '═', '║', '╔', '╗', '╚', '╝', '╠', '╣', '╦', '╩']
    class pipObject:
        symbol = " "
        type = -1
        connections = []
    class source(pipObject):
        symbol = "*"    
        type = 0
    class sink(pipObject): 
        type = 1
        def __init__(self, sym):
            self.symbol = sym
    class pipe(pipObject):
        type = 2
        def __init__(self, sym):
            self.symbol = sym

    def isPipe(symbol):
        for p in pipeSymbols:
            if( p == symbol):
                return True
        return False    
    grid =  [[pipObject() for i in range(100)] for j in range(100)] 
   
    sourceClaimed = False
    input = open(fileName, encoding='utf-8')
    Lines = input.readlines()
    for line in Lines:
        info = list(line.split(" "))
        symbol = info[0]
        x = int(info[1])
        y = int(info[2])
        
        if(isPipe( symbol)):           
            grid[y][x] = pipe(symbol)
        elif( symbol.isalpha() ): 
            grid[y][x] = sink(symbol)
        elif( symbol == "*"):             
            sourcePipe = source()
            grid[y][x] = sourcePipe         
            sourceClaimed =True
         
    if(not sourceClaimed):
        sourcePipe = grid[0][0]
      
    def printGrid():

        for row in grid:
            rowStr = ""
            for  col in row:          
                rowStr += " " + col.symbol
        
            print(rowStr)
     
    def connectPipes():
        height = len(grid)
        for y, row in enumerate(grid):
            length = len(row)
            for x, pip in enumerate(row):
                if(pip.type >= 0):
                    neighbors = []
                    if(x > 0 ):
                        neighbor = grid[y][x-1]
                        ourConnect = pip.symbol == "═" or pip.symbol == "╗" or pip.symbol == "╝" or pip.symbol == "╣" or pip.symbol == "╦" or pip.symbol == "╩"
                    
                        if(neighbor.type == 2 and ( neighbor.symbol == "═" or neighbor.symbol == "╔"  
                            or neighbor.symbol == "╚" or neighbor.symbol == "╠"
                            or neighbor.symbol == "╦" or neighbor.symbol == "╩")): 
                                if(pip.type == 2 ):
                                    if( ourConnect):  
                                        neighbors.append( neighbor)
                                else:                        
                                    neighbors.append( neighbor)
                        elif(neighbor.type == 0 or neighbor.type == 1):
                            if(pip.type == 2 ):
                                if( ourConnect):  
                                        neighbors.append( neighbor)
                                else:
                                    neighbors.append( neighbor)
                    if(x < length-1):
                        neighbor = grid[ y][x+1]
                        ourConnect = pip.symbol == "═" or pip.symbol == "╔" or pip.symbol == "╚" or pip.symbol == "╠" or pip.symbol == "╦" or pip.symbol == "╩"
                        
                        if(neighbor.type == 2 and ( neighbor.symbol == "═" or neighbor.symbol == "╗"  
                            or neighbor.symbol == "╝" or neighbor.symbol == "╣"
                            or neighbor.symbol == "╦" or neighbor.symbol == "╩")):                    
                                if(pip.type == 2 ):
                                    if( ourConnect):  
                                        neighbors.append( neighbor)
                                else:                        
                                    neighbors.append( neighbor)      
                        elif(neighbor.type == 0 or neighbor.type == 1):
                            if(pip.type == 2 ):
                                if( ourConnect):  
                                    neighbors.append( neighbor)
                            else:
                                neighbors.append( neighbor) 
                    if(y > 0):
                        neighbor = grid[y-1][x]
                        ourConnect = pip.symbol == "║" or pip.symbol == "╚" or pip.symbol == "╝" or pip.symbol == "╠" or pip.symbol == "╣" or pip.symbol == "╩"
                    
                        if(neighbor.type == 2 and ( neighbor.symbol == "║" or neighbor.symbol == "╔"  
                            or neighbor.symbol == "╗" or neighbor.symbol == "╠"
                            or neighbor.symbol == "╣" or neighbor.symbol == "╦")):                    
                                if(pip.type == 2 ):
                                    if( ourConnect):  
                                        neighbors.append( neighbor)
                                else:                        
                                    neighbors.append( neighbor)    
                        elif(neighbor.type == 0 or neighbor.type == 1):
                            if(pip.type == 2 ):
                                if( ourConnect):  
                                        neighbors.append( neighbor)
                            else:
                                neighbors.append( neighbor) 
                    if(y < height-1):
                        neighbor = grid[y+1][x]
                        ourConnect = pip.symbol == "║" or pip.symbol == "╔" or pip.symbol == "╗" or pip.symbol == "╠" or pip.symbol == "╣" or pip.symbol == "╦"
                    
                        if(neighbor.type == 2 and ( neighbor.symbol == "║" or neighbor.symbol == "╚"  
                            or neighbor.symbol == "╝" or neighbor.symbol == "╠"
                            or neighbor.symbol == "╣" or neighbor.symbol == "╩")):                    
                                if(pip.type == 2 ):
                                    if( ourConnect):  
                                        neighbors.append( neighbor)
                                else:                        
                                    neighbors.append( neighbor)   
                        elif(neighbor.type == 0 or neighbor.type == 1):
                            if(pip.type == 2 ):
                                if( ourConnect):  
                                    neighbors.append( neighbor)
                            else:
                                 neighbors.append( neighbor)  
                    pip.connections = neighbors

    def tranversePipes(startPipe, type, prevous, result):
        neighbors = startPipe.connections
        if(startPipe.type == type ):
            result.append( startPipe.symbol)            
        prevous.append(startPipe)
        for pipe in neighbors:
            if prevous.count(pipe) <= 0:
                tranversePipes(pipe, type, prevous, result )
    
        return(result)
    #printGrid()
  
    connectPipes()
    sinksLet = tranversePipes(sourcePipe, 1, [], [])
    sinksLet.sort()
 ##   print(sinksLet)
    result = ""
    for c in sinksLet:
        result+= c
    return result
sinks = pipeSystem("test_input.txt")
print(sinks)


    

