# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 17:14:59 2015

@author: Nate
"""

def calculate_score(playerData, weights):
    score = 0
    
    for key in weights:
        if key in playerData:
            score += weights[key]*playerData[key]
            
    return score

def standard(playerData):
    weights = {
        'passYds': 0.04,
        'passTDs': 4,
        'passInt': -1,
        'rushYds': 0.1,
        'rushTDs': 6,
        'receptions': 0,
        'recYds': 0.1,
        'recTDs': 6,
        'returnTDs': 6,
        'fumLost': -2,
    }
    
    return calculate_score(playerData, weights)
    
def ppr(playerData):
    weights = {
        'passYds': 0.04,
        'passTDs': 4,
        'passInt': -1,
        'rushYds': 0.1,
        'rushTDs': 6,
        'receptions': 1,
        'recYds': 0.1,
        'recTDs': 6,
        'returnTDs': 6,
        'fumLost': -2,
    }
    
    return calculate_score(playerData, weights)

def half_ppr(playerData):
    weights = {
        'passYds': 0.04,
        'passTDs': 4,
        'passInt': -1,
        'rushYds': 0.1,
        'rushTDs': 6,
        'receptions': 0.5,
        'recYds': 0.1,
        'recTDs': 6,
        'returnTDs': 6,
        'fumLost': -2,
    }
    
    return calculate_score(playerData, weights)    