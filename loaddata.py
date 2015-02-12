# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 14:32:43 2015

@author: Nate
"""

import pandas as pd

def loaddata():
    qb = pd.read_csv('qb-fantasy-stats-2008-2014.csv', header=False)
    rb = pd.read_csv('rb-fantasy-stats-2008-2014.csv', header=False)
    wr = pd.read_csv('wr-fantasy-stats-2008-2014.csv', header=False)

    qb_stats = {}
    rb_stats = {}
    wr_stats = {}
    
    for row in qb.iterrows():
        qb_name = row[1][0]
        
        season = row[1][3]
        week = row[1][2]
        game_id = '{}-{}'.format(season, week)
        
        passAtt = row[1][4]
        passYds = row[1][5]
        passInt = row[1][7]
        passTDs = row[1][8]
        rushAtt = row[1][9]
        rushYds = row[1][10]
        rushTDs = row[1][11]
        fumLost = row[1][12]

        if qb_name not in qb_stats:
            qb_stats[qb_name] = {}

        qb_stats[qb_name][game_id] = {
            'passAtt': passAtt,
            'passYds': passYds,
            'passInt': passInt,
            'passTDs': passTDs,
            'rushAtt': rushAtt,
            'rushYds': rushYds,
            'rushTDs': rushTDs,
            'fumLost': fumLost,
        }
        
    for row in rb.iterrows():
        rb_name = row[1][0]
        
        season = row[1][3]
        week = row[1][2]
        game_id = '{}-{}'.format(season, week)
        
        rushAtt = row[1][4]
        rushYds = row[1][5]
        rushTDs = row[1][7]
        receptions = row[1][8]
        recYds = row[1][9]
        recTDs = row[1][11]
        fumLost = row[1][12]
        
        if rb_name not in rb_stats:
            rb_stats[rb_name] = {}
        
        rb_stats[rb_name][game_id] = {
            'rushAtt': rushAtt,
            'rushYds': rushYds,
            'rushTDs': rushTDs,
            'receptions': receptions,
            'recYds': recYds,
            'recTDs': recTDs,
            'fumLost': fumLost,
        }
    
    for row in wr.iterrows():
        wr_name = row[1][0]
        
        season = row[1][3]
        week = row[1][2]
        game_id = '{}-{}'.format(season, week)
        
        receptions = row[1][4]
        targets = row[1][5]
        recYds = row[1][6]
        recTDs = row[1][8]
        returnTDs = row[1][9] + row[1][10]
        fumLost = row[1][11]
        
        if wr_name not in wr_stats:
            wr_stats[wr_name] = {}
        
        wr_stats[wr_name][game_id] = {
            'receptions': receptions,
            'targets': targets,
            'recYds': recYds,
            'recTDs': recTDs,
            'returnTDs': returnTDs,
            'fumLost': fumLost,
        }

    return (qb_stats, rb_stats, wr_stats)