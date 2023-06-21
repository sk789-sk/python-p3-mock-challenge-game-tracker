class Game:
    def __init__(self, title):
        if type(title) == str and len(title)>0:
            self.title = title
        else:
            raise Exception
        self._results = []
        self._players = []
    
    def get_title(self):
        return self._title
    
    def set_title(self,title): #how to make this unchangable? make it so if there is a title we raise an exception? that seems janky. Set title to none by default and then see if it equals none?  
        if type(title) == str and not hasattr(self, 'title'):
            self._title = title
        else:
            raise Exception

    title = property(get_title,set_title)



    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result,Result):
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if isinstance(new_player,Player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player): #return the average score on the game by a player
        #every result has a game score and player
        #the game has a list of results 
        #go through the list of results pick out the ones with the player is the same average the value

        p_count = 0
        score = 0
        for res_obj in self._results:
            if res_obj.player == player:
                p_count +=1
                score += res_obj.score 
        if p_count == 0:
            return 0
        else:
            return (score/p_count)

