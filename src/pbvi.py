'''
This part is the core code of PBVI algorithm. It will include some utilities from other files

Notice (About My Code Design):
PBVI is a subclass of 'Solver'
all the algorithm will be included in the super class 'Solver'.
'''

class PBVI(Solver):
    def __init__(self, modelEnv):
        Solver.__init__(self, modelEnv)
        self.solved = False

    
    def solveHorizonT(self, T):
        mEnv = self.modelEnv
        if self.solved:
            return
        # every step the alpha-vector will be updated
        for step in range(T):
            # step 1: create projection
            gammaIntermediate = self.createProjection()
            # step 2: cross-sum operation
            gammaActionBelief = self.computeCrossSum(gammaIntermediate)
            # step 3: find best action for each belief point
            self.alphaVectors = self.findBestAction(gammaActionBelief)
        
        self.solved = True
