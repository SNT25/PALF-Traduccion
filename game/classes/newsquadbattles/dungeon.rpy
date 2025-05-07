init python:
    class Dungeon:
        def __init__(self, palette, name, party, moblist, winlabel, loselabel, maxprogress, dungeonlevel, dungeoncutscenefunc=None, fudgerollfunc=None, eventfunc=None, generateitems=None):
            global activedungeon 
            activedungeon = self
            self.Palette = palette
            self.Name = name
            self.Progress = 0
            self.MaxProgress = maxprogress
            self.CurrentFloor = 1
            self.History = []
            self.Party = party
            self.CurrentEvent = None
            self.WinLabel = winlabel
            self.LoseLabel = loselabel
            self.DungeonWon = False
            self.DungeonLost = False
            self.TileSize = 96
            self.DungeonWidth = 20
            self.DungeonHeight = 12
            self.DungeonLevel = dungeonlevel
            self.ShownScenes = []
            self.DungeonCutsceneFunc = dungeoncutscenefunc
            self.FudgeRollFunc = fudgerollfunc
            self.EventFunc = eventfunc
            self.GenerateItems = generateitems
            if (self.GenerateItems == None):
                self.GenerateItems = []

            self.LastBattler = None

            self.BattleHistory = []
            self.HandledBattleHistory = []
            self.ItemHistory = dict()
            self.Bridges = []
            self.CreateMapDict()

        def IsOverlapping(self, room1, room2):
            x1, y1, width1, height1 = room1.GetDimensions()
            x2, y2, width2, height2 = room2.GetDimensions()

            right1 = x1 + width1
            bottom1 = y1 + height1
            right2 = x2 + width2
            bottom2 = y2 + height2

            return x1 < right2 and x2 < right1 and y1 < bottom2 and y2 < bottom1

        def GetDungeonWon(self):
            if (not hasattr(self, 'DungeonWon')):
                self.DungeonWon = False
            return self.DungeonWon

        def GetDungeonLost(self):
            if (not hasattr(self, 'DungeonLost')):
                self.DungeonLost = False
            return self.DungeonLost

        #don't laugh at me, I just forget what these functions are called.
        def IsOver(self):
            return self.Finished()
        def IsFinished(self):
            return self.Finished()
        def Finished(self):
            return self.GetDungeonWon() or self.GetDungeonLost()

        def GetPalette(self):
            return self.Palette

        def GetMapDict(self):
            return self.MapDict

        def GetMaxProgress(self):
            return self.MaxProgress

        def GetProgress(self):
            return self.Progress

        def AlterProgress(self, val=1):
            self.Progress += val

        def GetName(self):
            return self.Name

        def GetCurrentEvent(self):
            return self.CurrentEvent

        def SetLastBattler(self, squadder):
            self.LastBattler = squadder

        def GetLastBattler(self):
            return self.LastBattler

        def ValidEvent(self, eventtag):
            try:
                if (eventtag == None or eventtag in self.History or (ReturnEventTag("ExcludeFunction", eventtag) != None and ReturnEventTag("ExcludeFunction", eventtag)(self))):
                    return False
            except:
                return False
            return True

        def GetSquadder(self, name):
            for squadder in self.Party:
                if squadder.GetFormatName() == name:
                    return squadder

        def GetLastBattledFoe(self):
            if (len(self.BattleHistory) == 0):
                return None
            return self.BattleHistory[-1][1]

        def GetLastBattledRound(self):
            if (len(self.BattleHistory) == 0):
                return None
            return self.BattleHistory[-1][0]

        def WonlastFight(self):
            lastfoe = self.GetLastBattledFoe()
            if (lastfoe == None or lastfoe.Health > 0 and not (lastfoe in box or lastfoe in playerparty)):
                return False
            else:
                return True

        def GenerateEvent(self):
            randevent = None 
            if (self.EventFunc):
                randevent = self.EventFunc(self)
            else:
                while (not self.ValidEvent(randevent)):
                    randevent = RandomChoice(GenericEventNames())
            self.CurrentEvent = randevent
            return randevent

        def CreateMapDict(self):
            RoomCount = RandInt(2, 5)
            Rooms = set()
            Bridges = set()

            for i in range(RoomCount):
                roomWidth = RandInt(3, max(4, math.floor((self.DungeonWidth - 2) * RandomUniform(0.1, 0.6))))
                roomHeight = RandInt(3, max(4, math.floor((self.DungeonHeight - 2) * RandomUniform(0.1, 0.6))))
                Rooms.add(Room(self.DungeonWidth, self.DungeonHeight, roomWidth, roomHeight, False, False))

            for room in Rooms:
                for otherroom in Rooms:
                    if (room != otherroom and self.IsOverlapping(room, otherroom)):
                        room.Overlaps.add(otherroom)
                        otherroom.Overlaps.add(room)
                        otherroom.Connected = True
                        room.Connected = True

            for room in Rooms:
                for otherroom in Rooms:
                    if (room != otherroom and room not in otherroom.Overlaps and room not in otherroom.Bridged):
                        if (len(room.Bridged) == 0 or Random() < 1.0 / RoomCount):
                            Bridges.add(Bridge(self.DungeonWidth, self.DungeonHeight, room, otherroom))
                            room.Bridged.add(otherroom)
                            otherroom.Bridged.add(room)

            self.MapDict = {}

            for x in range(self.DungeonWidth):
                for y in range(self.DungeonHeight):
                    coords = (x, y)
                    iswall = True
                    if (not (x == 0 or y == 0 or x == self.DungeonWidth - 1 or y == self.DungeonHeight - 1)):
                        for room in Rooms:
                            if room.InRoom(coords):
                                iswall = False
                                break
                        for bridge in Bridges:
                            for room in bridge.MiniRooms:
                                if room.InRoom(coords):
                                    iswall = False
                                    break
                    self.MapDict[(x, y)] = iswall

            imagedict = {}
            for key in self.MapDict.keys():
                imagedict[key] = self.ComputeTile(self.MapDict, key)

            self.MapDict = imagedict

        def TallyMorale(self):
            moralecount = 0
            for squadder in self.Party:
                moralecount += squadder.GetMotivation()
            return moralecount

        def MaxMorale(self):
            return len(self.Party) * 5

        def GetBlockedWalls(self, mapdict, coords):
            blockedwalls = []
            x = coords[0]
            y = coords[1]
            if (self.IsWall(mapdict, (x - 1, y - 1))):
                blockedwalls.append("TL")
            if (self.IsWall(mapdict, (x, y - 1))):
                blockedwalls.append("T")
            if (self.IsWall(mapdict, (x + 1, y - 1))):
                blockedwalls.append("TR")
            if (self.IsWall(mapdict, (x - 1, y))):
                blockedwalls.append("L")
            if (self.IsWall(mapdict, (x + 1, y))):
                blockedwalls.append("R")
            if (self.IsWall(mapdict, (x - 1, y + 1))):
                blockedwalls.append("BL")
            if (self.IsWall(mapdict, (x, y + 1))):
                blockedwalls.append("B")
            if (self.IsWall(mapdict, (x + 1, y + 1))):
                blockedwalls.append("BR")
            return blockedwalls

        def IsWall(self, mapdict, coords):
            if (coords[0] < 0 or coords[0] >= self.DungeonWidth or coords[1] < 0 or coords[1] >= self.DungeonHeight):
                return True
            return mapdict[coords]

        def ComputeTile(self, mapdict, coords):
            ts = self.TileSize
            finaltile = Null()
            blockedwalls = self.GetBlockedWalls(mapdict, coords)

            if (blockedwalls == ["TL", "T", "TR", "L", "R", "BL", "B", "BR"]):
                sheetcoords = RandomChoice([(1, 1), (1, 1), (1, 1), (4, 1), (7, 1)], True, coords)                    
            
            elif (blockedwalls == ["T", "L", "R", "B"]):
                sheetcoords = (1, 7)

            elif (blockedwalls == ["TL", "T", "TR", "L", "R", "B"]):
                sheetcoords = (1, 12)
            elif (blockedwalls == ["TL", "T", "L", "R", "BL", "B"]):
                sheetcoords = (0, 13)
            elif (blockedwalls == ["T", "TR", "L", "R", "B", "BR"]):
                sheetcoords = (2, 13)
            elif (blockedwalls == ["T", "L", "R", "BL", "B", "BR"]):
                sheetcoords = (1, 14)

            elif (blockedwalls == ["TL", "T", "TR", "L", "R", "BL", "B"]):
                sheetcoords = (0, 15)
            elif (blockedwalls == ["TL", "T", "TR", "L", "R", "B", "BR"]):
                sheetcoords = (1, 15)
            elif (blockedwalls == ["TL", "T", "L", "R", "BL", "B", "BR"]):
                sheetcoords = (0, 16)
            elif (blockedwalls == ["T", "TR", "L", "R", "BL", "B", "BR"]):
                sheetcoords = (1, 16)

            elif (blockedwalls == ["L", "R", "BL", "B"]):
                sheetcoords = (0, 19)
            elif (blockedwalls == ["L", "R", "B", "BR"]):
                sheetcoords = (1, 19)
            elif (blockedwalls == ["TL", "T", "L", "R"]):
                if (self.IsWall(mapdict, coords) and self.GetPalette() == "forest"):
                    sheetcoords = RandomChoice([(0, 20), (3, 20)], True, coords)
                else:
                    sheetcoords = (0, 20)
            elif (blockedwalls == ["T", "TR", "L", "R"]):
                if (self.IsWall(mapdict, coords) and self.GetPalette() == "forest"):
                    sheetcoords = RandomChoice([(1, 20), (4, 20)], True, coords)
                else:
                    sheetcoords = (1, 20)

            elif (blockedwalls == ["T", "L", "R", "B", "BR"]):
                sheetcoords = (0, 21)
            elif (blockedwalls == ["T", "L", "R", "BL", "B"]):
                sheetcoords = (1, 21)
            elif (blockedwalls == ["T", "TR", "L", "R", "B"]):
                sheetcoords = (0, 22)
            elif (blockedwalls == ["TL", "T", "L", "R", "B"]):
                sheetcoords = (1, 22)

            elif (blockedwalls == ["T", "TR", "L", "R", "BL", "B"]):
                sheetcoords = (0, 23)
            elif (blockedwalls == ["TL", "T", "L", "R", "B", "BR"]):
                sheetcoords = (1, 23)       

            #C-Blocks #5
            elif (all(elem in blockedwalls for elem in ["L", "R", "BL", "B", "BR"])):
                if (self.IsWall(mapdict, coords) and self.GetPalette() == "forest"):
                    sheetcoords = RandomChoice([(1, 0), (4, 0), (7, 0)], True, coords)
                else:
                    sheetcoords = (1, 0)
            elif (all(elem in blockedwalls for elem in ["T", "TR", "R", "B", "BR"])):
                if (self.IsWall(mapdict, coords) and self.GetPalette() == "forest"):
                    sheetcoords = RandomChoice([(0, 1), (3, 1), (6, 1)], True, coords)
                else:
                    sheetcoords = (0, 1)
            elif (all(elem in blockedwalls for elem in ["TL", "T", "L", "BL", "B"])):
                if (self.IsWall(mapdict, coords) and self.GetPalette() == "forest"):
                    sheetcoords = RandomChoice([(2, 1), (5, 1), (8, 1)], True, coords)
                else:
                    sheetcoords = (2, 1)
            elif (all(elem in blockedwalls for elem in ["TL", "T", "TR", "L", "R"])):
                if (self.IsWall(mapdict, coords) and self.GetPalette() == "forest"):
                    sheetcoords = RandomChoice([(1, 2), (4, 2), (7, 2)], True, coords)
                else:
                    sheetcoords = (1, 2)

            #thumbs-up blocks #4
            elif (all(elem in blockedwalls for elem in ["T", "TR", "R", "B"])):
                sheetcoords = (0, 17)
            elif (all(elem in blockedwalls for elem in ["TL", "T", "L", "B"])):
                sheetcoords = (1, 17)
            elif (all(elem in blockedwalls for elem in ["T", "R", "B", "BR"])):
                sheetcoords = (0, 18)
            elif (all(elem in blockedwalls for elem in ["T", "L", "BL", "B"])):
                if (self.IsWall(mapdict, coords) and self.GetPalette() == "forest"):
                    sheetcoords = RandomChoice([(1, 18), (4, 18)], True, coords)
                else:
                    sheetcoords = (1, 18)

            # L-Blocks #3
            elif (all(elem in blockedwalls for elem in ["R", "B", "BR"])):
                sheetcoords = (0, 0)
            elif (all(elem in blockedwalls for elem in ["L", "BL", "B"])):
                sheetcoords = (2, 0)
            elif (all(elem in blockedwalls for elem in ["T", "TR", "R"])):
                sheetcoords = (0, 2)
            elif (all(elem in blockedwalls for elem in ["TL", "T", "L"])):
                sheetcoords = (2, 2)

            #T-Blocks #3
            elif (all(elem in blockedwalls for elem in ["L", "R", "B"])):
                sheetcoords = (1, 9)
            elif (all(elem in blockedwalls for elem in ["T", "R", "B"])):
                sheetcoords = (0, 10)
            elif (all(elem in blockedwalls for elem in ["T", "L", "B"])):
                sheetcoords = (2, 10)
            elif (all(elem in blockedwalls for elem in ["T", "L", "R"])):
                if (self.IsWall(mapdict, coords) and self.GetPalette() == "forest"):
                    sheetcoords = RandomChoice([(1, 11), (4, 11)], True, coords)
                else:
                    sheetcoords = (1, 11)

            #straight and right angle blocks #2
            elif (all(elem in blockedwalls for elem in ["R", "B"])):
                sheetcoords = (0, 3)
            elif (all(elem in blockedwalls for elem in ["L", "R"])):
                sheetcoords = (1, 3)
            elif (all(elem in blockedwalls for elem in ["L", "B"])):
                sheetcoords = (2, 3)
            elif (all(elem in blockedwalls for elem in ["T", "B"])):
                sheetcoords = (0, 4)
            elif (all(elem in blockedwalls for elem in ["T", "R"])):
                sheetcoords = (0, 5)
            elif (all(elem in blockedwalls for elem in ["T", "L"])):
                sheetcoords = (2, 5)

            #Single Blocks #1
            elif ("B" in blockedwalls):
                sheetcoords = (1, 6)
            elif ("R" in blockedwalls):
                sheetcoords = (0, 7)
            elif ("L" in blockedwalls):
                sheetcoords = (2, 7)
            elif ("T" in blockedwalls):
                sheetcoords = (1, 8)
            else:
                sheetcoords = (1, 4)
                
            if (self.IsWall(mapdict, coords)):
                finaltile = Transform("images/sprites/maps/{}.webp".format(self.GetPalette()), crop=(336 + sheetcoords[0] * 100, 652 + sheetcoords[1] * 100, 96, 96))
            else:
                finaltile = Transform("images/sprites/maps/{}.webp".format(self.GetPalette()), crop=(336 + (sheetcoords[0] + 9) * 100, 652 + sheetcoords[1] * 100, 96, 96))

            return finaltile

    class Room:
        def __init__(self, floorwidth, floorheight, roomWidth, roomHeight, presetorigin=None, bridge=None):
            self.Height = roomHeight
            self.Width = roomWidth
            self.Bridge = bridge
            leftcornerx = RandInt(1, floorwidth - self.Width - 1)
            leftcornery = RandInt(1, floorheight - self.Height - 1)
            self.Origin = (leftcornerx, leftcornery)
            self.Overlaps = set()
            self.Bridged = set()
            self.Connected = True
            self.Walls = set()

        def GetDimensions(self):
            return (self.Origin[0], self.Origin[1], self.Width, self.Height)

        def GetRandPoint(self):
            return (RandInt(self.Origin[0], self.Origin[0] + self.Width - 1), RandInt(self.Origin[1], self.Origin[1] + self.Height - 1))

        def InRoom(self, coords):
            x, y = coords
            return x >= self.Origin[0] and x < self.Origin[0] + self.Width and y >= self.Origin[1] and y < self.Origin[1] + self.Height

    class Bridge:
        def __init__(self, floorwidth, floorheight, firstroom, secondroom):
            self.FirstRoom = firstroom
            self.SecondRoom = secondroom
            self.Rooms = { firstroom, secondroom }
            self.MiniRooms = set()
            self.Width = RandInt(1, 3)

            firstpoint = firstroom.GetRandPoint()
            secondpoint = secondroom.GetRandPoint()
            midpoint = (0, 0)
            pointdirections = {}
            verticalfirst = RandomChoice([True, False])

            if (not verticalfirst):
                midpoint = (firstpoint[0], secondpoint[1])
                pointdirections = { firstpoint: "Horizontal", midpoint: "Vertical"}
            else:
                midpoint = (secondpoint[0], firstpoint[1])
                pointdirections = { firstpoint: "Vertical", midpoint: "Horizontal"}

            self.Points = [firstpoint, midpoint, secondpoint]

            for i in range(len(self.Points) - 1):
                point = self.Points[i]
                nextpoint = self.Points[i + 1]
                origin = (min(point[0], nextpoint[0]), min(point[1], nextpoint[1]))
                if (pointdirections[point] == "Horizontal"):
                    self.MiniRooms.add(Room(floorwidth, floorheight, 1, max(nextpoint[1] - point[1], point[1] - nextpoint[1] + 1), origin, self))
                elif (pointdirections[point] == "Vertical"):
                    self.MiniRooms.add(Room(floorwidth, floorheight, max(nextpoint[0] - point[0], point[0] - nextpoint[0] + 1), 1, origin, self))