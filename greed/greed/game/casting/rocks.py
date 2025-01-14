from game.casting.actor import Actor


class Rock(Actor):
    """
    A rock (o) that the user will try to avoid. 
    
    The responsibility of a Rock is to provide something for the user to try
    to avoid and to loose points if caught.

    Attributes:
        None.
    """
    def __init__(self):
        super().__init__()
        
    def update_score(self, score):
        """
        Subract 100 points everytime a rock (o) is caught by the user.
        Arg:
            (self): An instance of the Rock class.
            (score): subtract from the score
        """
        score.deduct_points()