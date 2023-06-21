class Result:

    all = []

    def __init__(self, player, game, score): #do i need to import and set ?
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    #player and game both need results so lets have this as ssot point and define relationships here

        self.player.results(self)   #add this result for the player
        self.player.games_played(self.game) #add this game as a game that the player plays
        self.game.results(self)  #add this result for the game
        self.game.players(self.player) #add this player as a player of this game

        #not imported so the method isnt known to exist?


    def get_score(self):
        return self._score

    def set_score(self,score):
        if 1<=score<=5000:
            self._score = score
        else:
            raise Exception
    
    score = property(get_score,set_score)

    def get_player(self):
        return self._player


    def set_player(self,player):
        from classes.player import Player 
        if isinstance(player,Player):
            self._player = player
        else:
            raise Exception

    player = property(get_player,set_player)

    def get_game(self):
        return self._game #if these are truly ment to be private then here it would be not under and in the top it is 

    def set_game(self,game):
        from classes.game import Game
        if isinstance(game,Game):
            self._game = game
        else:
            raise Exception

    game = property(get_game,set_game)