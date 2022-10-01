

from Player.Player import Player


class PlayerManager:
    def __init__(self,typeOfPlayer):
        self.players = []
        self.currentPlayer = None
        self.playerType = typeOfPlayer
        
    def InitOnePlayer(self):
        self.players.append(Player())
        self.currentPlayer = self.players[0]
        
    def InitTwoPlayer(self):
        self.players.append(Player())
        self.players.append(Player())
        self.currentPlayer = self.players[0]
        
    def HitPlayer(self,pos : tuple):
        pass
    def RemovePlayer(self,player:Player):
        self.players.remove(player)
        
    def SwitchPlayer(self):
        index = self.players.index(self.currentPlayer)
        if index < self.players.size():
            self.currentPlayer = self.players[index + 1] 
        else:
            self.currentPlayer = self.players[0]
            
        
    