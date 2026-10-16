class Controller:
    #using a class here is better than a module by itself, because it preserves the previous error value
    #defines the fixed values thare are set at the start
    def __init__(self):
        self.Kp = 0.15
        self.Kd = 0.6
        self.previous_error = 0
        #e[-1] = 0 as we have been told

    def calculate(self, reference, obs):
        error = reference - obs

        action = self.Kp * error + self.Kd * ( #as specified in the document, PD control form
            error - self.previous_error
        )

        #maintains the previous error object in a simpler manner
        self.previous_error = error

        return action

    
    def reset(self):
        self.previous_error = 0


    
       
    
