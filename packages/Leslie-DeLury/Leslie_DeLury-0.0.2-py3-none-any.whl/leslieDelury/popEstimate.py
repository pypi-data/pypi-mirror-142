from scipy.stats import linregress
import numpy as np

def LDEstimate(catch, effort):
    if len(catch) != len(effort):
        raise ValueError('catch and effort must be same length')
    
    if len(catch) == 0 or len(effort) == 0:
        raise ValueError('catch and effort must be non-empty')

    catch, effort = np.array(catch), np.array(effort)
        
    catch_effort = catch / effort

    K = np.cumsum(catch) - catch

    linModel = linregress(K, catch_effort)

    q_hat = -linModel.slope
    N0_hat = linModel.intercept / q_hat

    return N0_hat, q_hat