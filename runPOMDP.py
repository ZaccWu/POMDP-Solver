from src.tigermodel import TigerModel
from src.pbvi import PBVI

from tools.sampleUtility import generateInitBeliefPoints, generateUniformBeliefs

from visualization.visualizeTiger import VisualizedTiger

def main():
    execParams = {
        'model_name': 'Tiger',
        'max_play': 100,
        'print_process': True,
    }
    algoParams = {
        'algo':'pbvi',
        'T': 2,
        'expendN': 5,
        'step_size': 0.01,
    }
    envParams = {
        'env_name': 'Tiger_env',
        'discount': 0.75,
        'reward_param': {
            'open_correct_reward': 10.,
            'open_incorrect_cost': -100.,
            'listen_cost': -1.,
        },
        'observation_param': {
            'obs_correct_prob': 0.85,
            'obs_incorrect_prob': 0.15,
        }
    }


    modelEnv = TigerModel()
    modelEnv.specifyEnvironmentArguments(envParams)
    visualizer= VisualizedTiger()
    solver = PBVI(modelEnv)

    beliefPoints = generateInitBeliefPoints(modelEnv.states, algoParams['step_size'])
    solver.specifyAlgorithmArguments(beliefPoints,algoParams['expendN'])

    # 5. choose your visualization part
    #visualizer.visualizeBeliefPoint(beliefPoints)


    # start playing
    totalRewards = 0
    belief = generateUniformBeliefs(modelEnv.states)    # for model evaluation
    print('''Initial State: {} || Initial Belief: {} || Time Horizon: {} || Max Play: {}
        '''.format(modelEnv.currentState,belief,algoParams['T'],execParams['max_play']))

    for i in range(execParams['max_play']):
        # this is a general framework of solving POMDP problems
        solver.planningHorizon(algoParams['T'])                               # planning
        action = solver.getBestPlanningAction(belief)                        # get best action
        nextState, observation, reward = modelEnv.envFeedback(action)  # receive environment feedback
        belief = modelEnv.updateBelief(belief, action, observation)    # update the belief
        totalRewards += reward
        # for every trial, print the result
        if execParams['print_process']:
            print("Play Times: {} || Action Chosen: {} || Observation: {} || Reward: {} || New State: {} || New Belief: {}".format(i,action,observation,reward,nextState,belief))
    print("Total reward:{}".format(totalRewards))



if __name__ == '__main__':
    main()
