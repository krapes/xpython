class Bowl:
    def __init__(self):
        self.tally = 0
        self.frame = 0
        self.previous_pins = 0
        self.strike_flag = 0
        self.spare_flag = 0
        self.error = None

    def roll(self,pins):
        '''
        print("")
        print("Pins: {}".format(pins))
        print("strike flag: {}".format(self.strike_flag))
        print("spare_flage: {}".format(self.spare_flag))
        print("Frame: {}".format(self.frame))
        print("Tally: {}".format(self.tally))
        print("Previous_pins: {}".format(self.previous_pins))
        '''

        #Determine if this is a legal roll
        if pins < 0:
            self.error = "error: Negative roll is invalid"
            print(error)
            return
        elif pins + self.previous_pins > 10:
            self.error = "error: Pin count exceeds pins on the lane"
            print(error)
            return
        if self.frame >= 10 and self.strike_flag == 0 and self.spare_flag == 0:
            self.error = "error: Cannot roll after game is over"
            print(self.error)
            return

        #Determine if this is a normal frame or bonus frame
        in_game_frame = 1 if self.frame < 10 else 0
        
        #Calculate the multiple for added strike bonus points
        if self.strike_flag - 1 <= 0:
            strike = self.strike_flag
        else:
            strike = self.strike_flag - 1
            
        #Sum tally
        self.tally += (pins*(in_game_frame) 
                      + pins*strike
                      + pins*self.spare_flag)
        
        #Deprecate strike and spare flags
        self.strike_flag = max(0, self.strike_flag - max(1, strike))
        self.spare_flag = max(0, self.spare_flag - 1)
        
        #Determine if the next roll is a new frame
        new_frame = False if (self.frame - int(self.frame)) == 0.0 else True

        #Add flags for this roll's results
        if pins + self.previous_pins >= 10 and self.frame < 10:
            if new_frame == False:
                self.strike_flag += 2
            else:
                self.spare_flag += 1

        #Update frame
        if pins == 10:
            self.frame += 1.0
            new_frame = True
        else:
            self.frame += 0.5

        #Update previous_pins
        self.previous_pins = pins if new_frame == False else 0

    def score(self):
        if self.error != None:
            print(self.error)
            return 
        elif self.frame < 10 or self.strike_flag > 0 or self.spare_flag > 0:
            print("error: Score cannot be taken until the end of the game")
            return
        else:        
            return self.tally

game = Bowl()
scores =  [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for pin in scores:
    game.roll(pin)
print(game.score())
