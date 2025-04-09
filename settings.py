class Settings():
    def __init__(self):
        """Initialize da Settings"""

        #sorting settings based on what they're related to
        self.screen_HEIGHT = 800 #screen width
        self.screen_WIDTH = 1000 #screen height, what? Expected something funny?
        self.FPS = 60 #FPS modulator

        #more setting sorting
        self.player_SPEED = 3 #Damn, speed
        self.big_boi_SPEED = self.player_SPEED/2

        #Just some more sorting to find stats easier, did you expect more?
        self.bullet_SPEED = 20 #SPEED

        #even more sorting, is this getting old yet?
        self.ENEMY_FLASH_RATE = .01 #flashy flashy

        #more sorting? Ugh
        self.SCALE_FACTOR = 1 #Scale multiplier