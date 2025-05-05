class Settings():
    def __init__(self):
        """Initialize da Settings"""

        #sorting settings based on what they're related to
        self.screen_HEIGHT = 1000 #screen height
        self.screen_WIDTH = 1200 #screen width. What? Expected something funny?
        self.FPS = 60 #FPS modulator

        #Speed stat sorting
        self.player_SPEED = 3 #Damn, speed equaled 3
        self.big_boi_SPEED = self.player_SPEED/2 #original speed: HALF of player's speed
        self.speedy_boi_SPEED = self.player_SPEED * 2.75 #original: TRIPLE the player's speed
        self.blindBulb_SPEED = 1 #started as a third of player's speed
        self.zipper_SPEED = self.player_SPEED/4 #initially a QUARTER of the player's speed

        #Just some more sorting to find stats easier, did you expect more?
        self.bullet_SPEED = 25 #SPEED
        self.KNOCKBACK_AMOUNT = 20

        #even more sorting, is this getting old yet?
        self.ENEMY_FLASH_RATE = .01 #flashy flashy
        self.spawnrate = 0.8
        
        #more sorting? Ugh
        self.SCALE_FACTOR = 1 #Scale multiplier

        #Item stats
        self.medkit_HEAL = 25
        self.shield_SHIELD = 10