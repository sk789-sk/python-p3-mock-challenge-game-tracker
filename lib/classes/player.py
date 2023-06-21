class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)
        
    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result,Result):
            self._results.append(new_result)
        return self._results
    
    def get_username(self):
        return self._username

    def set_username(self,name):
        if 2 <= len(name) <=16:
            self._username = name
        else:
            raise Exception

    username = property(get_username,set_username)


    
    def games_played(self, new_game=None):
        from classes.game import Game
        if isinstance(new_game,Game):
            self._games_played.append(new_game)
        return self._games_played
        

    
    def played_game(self, game): #Lets see if player has played this game
        #iterate over all the results and see where the game and self both exist
        if game in self._games_played:
            return True
        return False
    
    def num_times_played(self, game): #every game is 1 object every result is different
        #In every result see if the game matches the game we put in
        counter = 0
        for res_obj in self._results:
            if res_obj.game == game:
                counter +=1
        return counter
    
    @classmethod #return the player with highest average score in game
    def highest_scored(cls, game):
        #have average score for a player in a game with the average_score method in Game class
        #We have all the players in the all Player class var
        #pass all the players in the player method into the average_score method and see who comes out on top.
        score = 0
        top_player = None
        
        for player in Player.all:
            average = game.average_score(player)
            if average > score: #if u tie and are second to be seen sucks to suck
                score = average
                top_player = player
        return top_player
        
