#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:04:07 2022

@author: yuefanji
"""

import math
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def cycling_CCCV(file_name,cycle_num):
    df=pd.read_csv(file_name)
    charge=cycling_data_processing(df,cycle_num,'charge');
    discharge=cycling_data_processing(df,cycle_num,'discharge');
    
    plt.plot(charge['Capacity(Ah)'],charge['Voltage(V)'],label='charge')
    plt.plot(discharge['Capacity(Ah)'],discharge['Voltage(V)'],label='discharge')
    plt.legend()
    plt.xlabel('Capacity(Ah)')
    plt.ylabel('Voltage(V)')
    fig = plt.gcf()
    return(fig)

def diff_cap(file_name,cycle_num):
    df=pd.read_csv(file_name)
    charge=cycling_data_processing(df,cycle_num,'charge')
    discharge=cycling_data_processing(df,cycle_num,'discharge')
    charge_V=charge['Voltage(V)'][(charge['Voltage(V)']<4.18)]
    charge_cap=charge['Capacity(Ah)'][(charge['Voltage(V)']<4.18)]
    discharge_V=discharge['Voltage(V)'][(discharge['Voltage(V)']<4.18)]
    discharge_cap=discharge['Capacity(Ah)'][(discharge['Voltage(V)']<4.18)]
    
    dqdv_charge=np.diff(charge_cap)/np.diff(charge_V)

    N_charge=len(dqdv_charge)
    dqdv_discharge=np.diff(discharge_cap)/np.diff(discharge_V)
    N_discharge=len(dqdv_discharge)
    plt.plot(charge_V[0:N_charge],dqdv_charge,label='charge')
    plt.plot(discharge_V[0:N_discharge],dqdv_discharge,label='discharge')
    plt.legend()
    plt.xlabel('Voltage(V)')
    plt.ylabel('dQ/dV')
    fig = plt.gcf()
    return (fig)

def cycling_data_processing(df,cycle_num,data_type):
    
    if data_type == 'discharge':
        A=df[(df['Cyc#']==cycle_num)][(df['Current(A)']<0)]
    if data_type == 'charge':
        A=df[(df['Cyc#']==cycle_num)][(df['Current(A)']>0)]
    return (A)

def Capacity_voltage_extract(df):
    df_1=pd.DataFrame()
    df_1['Capacity(Ah)']=df['Capacity(Ah)']
    df_1['Voltage(V)']=df['Voltage(V)']
    return(df_1)
    

def impedance_data_processing(text_file):
    data=np.loadtxt(text_file,delimiter=",",skiprows=11)
    f=data[:,0]
    Z1=data[:,4]
    Z2=data[:,5]
    df=pd.DataFrame()
    df1=pd.DataFrame()
    df['frequency']=f
    df['Z1']=Z1
    df['Z2']=Z2
    df1=df.copy()
    df1=df1[(df1['Z2']<0)]
    df1.reset_index(inplace = True)
    return(df1)

def Nyquist_plot_UI(text_file):
    df=impedance_data_processing(text_file)
    return(Nyquist_plot(df))
    
def Nyquist_plot(df):
    
    plt.plot(df['Z1'],-df['Z2'])
    plt.xlabel('Z1')
    plt.ylabel('-Z1')
    fig = plt.gcf()
    return (fig)
    
def dis_cap(df,max_cycle):
    N=max_cycle+1
    cap=np.zeros(N)
    for i in range(0,N):
        discharge=cycling_data_processing(df,i,'discharge')

        cap[i]=discharge['Capacity(Ah)'].iloc[-1]

    return(cap[-1])

        
        
    
