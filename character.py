class Character:
    def __init__(self, level=1, xp=0):
        self.level = level
        self.xp = xp

    def gain_xp(self, xp_earned):
        self.xp += xp_earned
        self.check_level_up()

    def check_level_up(self):
        xp_needed = self.calculate_xp_needed()
        if self.xp >= xp_needed:
            self.level += 1
            self.xp -= xp_needed

    def calculate_xp_needed(self):
        return (self.level * 100) + ((self.level - 1) * 50)
