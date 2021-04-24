#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:41:33 2021

@author: Clement
"""
import pandas 

def create_json ():
    df = pandas.DataFrame(index=[],
                          columns=['Nom', 'Lat', 'Long'])
    
    df = df.set_index('Nom')
    df.loc['Agriculteur 1'] = [43.831961, 3.874051]
    
    print(df)
    df.to_json('donnes_agri.json', orient='table', indent=4)
    
create_json()