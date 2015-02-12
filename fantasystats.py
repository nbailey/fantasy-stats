# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 17:03:28 2015

@author: Nate
"""

def calculate_fantasy_performance(playerData, scoringMethod):
    fantasyPerformance = []
    for week in playerData:
        fantasyPerformance.append(scoringMethod(playerData[week]))
    
    return fantasyPerformance

def bootstrap_fantasy_performance(playerData, metric):
    return 0