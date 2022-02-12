class Player():
    def __init__(self, name, start=False, ai_switch=False):
        self.ai = ai_switch
        self.values = {0:.5}
        self.name = name
        self.turn = start
        self.epsilon = 1
