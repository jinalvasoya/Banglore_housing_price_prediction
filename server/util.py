# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:12:05 2022

@author: dell
"""

import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None
__area_type= None

def get_estimated_price(area,location,sqft,bhk,bath,balcony):
    #print(__data_columns)
    
    try:
        loc_index = [x.replace(' ','') for x in __data_columns ].index(location.lower().replace(' ',''))
        area_index=[x.replace(' ','') for x in __data_columns ].index(area.lower().replace(' ',''))
    except:
        loc_index = -1
        area_index=-1
    print(loc_index,area_index)
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[3] = bhk
    x[2]=  balcony
    if loc_index>=0:
        x[loc_index] = 1
    if area_index>=0:
        x[area_index] = 1
    

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations
    global __area_type

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[8:] # first 3 columns are sqft, bath, bhk
        __area_type= __data_columns[4:8]

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations
def get_area_type():
    return __area_type

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(__data_columns)
    #print(get_location_names())
    #print(get_area_type())
    print(get_estimated_price('area_type_Built-up  Area','location_1st Block Jayanagar',1000,2,2,2))
    #print(get_estimated_price('area_type_Built-up  Area','location_1st Phase JP Nagar', 1000, 2,3, 2))
    # print(get_estimated_price('location_Kalhalli', 1000, 2, 2)) # other location
    # print(get_estimated_price('location_Ejipura', 1000, 2, 3))  # other location