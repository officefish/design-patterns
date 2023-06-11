from enum import Enum

class Sides(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

class MapSite:
    def Enter():
        pass

class Room(MapSite):
    def __init__(self, roomNumber):
        self.roomNumber = roomNumber
    
    def Enter():
        pass

    def SetSide(self, direction:Sides, site:MapSite):
        pass

    def GetSide():
        pass

class Wall(MapSite):
    def Enter():
        pass
    

class Door(MapSite):
    def Enter():
        pass

    def isOpen():
        pass



class Maze():
    def AddRoom(room):
        pass
    
    def RoomNo():
        pass


class MazeFactory:
    def __init__():
        pass

    def MakeMaze():
        return Maze()
    
    def MakeWall():
        return Wall()
    
    def MakeRoom(self, roomNumber):
        return Room(roomNumber)
    
    def MakeDoor():
        return Door()
    
    
    
    

    
class MazeGame(MazeFactory):
    @staticmethod
    def CreateMaze():
        factory = MazeFactory()
        aMaze = factory.MakeMaze()
        r1 = factory.MakeRoom(1)
        r2 = factory.MakeRoom(2)
        theDoor = factory.MakeDoor(r1, r2)

        aMaze.AddRoom(r1)
        aMaze.AddRoom(r1)


        
        r1.SetSide(Sides.North, factory.MakeWall())
        r1.SetSide(Sides.East, theDoor)
        r1.SetSide(Sides.South, factory.MakeWall())
        r1.SetSide(Sides.West, factory.MakeWall())

        r2.SetSide(Sides.North, factory.MakeWall())
        r2.SetSide(Sides.East, theDoor)
        r2.SetSide(Sides.South, factory.MakeWall())
        r2.SetSide(Sides.West, factory.MakeWall())

        
        return aMaze
        


