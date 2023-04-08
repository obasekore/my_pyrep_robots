from pyrep.robots.arms.arm import Arm


#class BaxterLeft(Arm):

#    def __init__(self, count: int = 0):
#        super().__init__(count, 'Baxter_leftArm', 7, base_name='Baxter')


#class BaxterRight(Arm):

#    def __init__(self, count: int = 0):
#        super().__init__(count, 'Baxter_rightArm', 7, base_name='Baxter')

class NAOLeft(Arm):

    def __init__(self, count: int = 0):
        super().__init__(count, 'NAO_leftArm', 5, base_name='NAO')

class NAORight(Arm):

    def __init__(self, count: int = 0):
        super().__init__(count, 'NAO_rightArm', 5, base_name='NAO')


class NAOLeftLeg(Arm):

    def __init__(self, count: int = 0):
        super().__init__(count, 'NAO_leftLeg', 6, base_name='NAO')

class NAORightLeg(Arm):

    def __init__(self, count: int = 0):
        super().__init__(count, 'NAO_rightLeg', 6, base_name='NAO')
