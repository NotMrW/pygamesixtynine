class Settings():
    def __init__(self):
        """Initialize da Settings"""



        #sorting settings based on what they're related to
        self.screen_HEIGHT = 1000 #screen height
        self.screen_WIDTH = 1200 #screen width. What? Expected something funny?
        self.FPS = 60 #FPS modulator



        #Speed stat sorting
        self.speed_mod = 1


        self.player_SPEED = 3 #Damn, speed equaled 3
        self.enemy_SPEED = 2 * self.speed_mod
        self.big_boi_SPEED = 1.5 * self.speed_mod #original speed: HALF of player's speed
        self.speedy_boi_SPEED = 8.25 * self.speed_mod #original: 2.75x player speed
        self.blindBulb_SPEED = 1 * self.speed_mod #started as a third of player's speed
        self.zipper_SPEED = 0.75 * self.speed_mod #initially a QUARTER of the player's speed



        #Just some more sorting to find stats easier, did you expect more?
        self.bullet_SPEED = 33 #SPEED
        self.bullet_SPREAD = 0.3
        self.KNOCKBACK_AMOUNT = 20



        #even more sorting, is this getting old yet?
        self.ENEMY_FLASH_RATE = .01 #flashy flashy
        self.spawnrate = 0.001
        
        

        
        #more sorting? Ugh
        self.SCALE_FACTOR = 1 #Scale multiplier



        #Item stats
        self.medkit_HEAL = 25
        self.shield_SHIELD = 10