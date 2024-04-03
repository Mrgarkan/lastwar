import streamlit as st
import numpy as np

level_exp = [0,100,200,300,400, #1-5
            500,600,700,800,900, #6-10
            1000,1100,1200,1300,1400, #11-15
            1500,1600,1700,1800,1900, #16-20
            2000,2100,2300,2700, #21-25
            3200,3900,4600,5500,6600, #26-30
            8000,9500,12000,14000,17000,20000, #31-35
            24000,29000,35000,41000,49000, #36-40
            59000,71000,85000,110000,130000, #41-45
            150000,180000,220000,310000,  #46-50
            370000,440000,530000,630000,760000, #51-55
            910000,1100000,1400000,1600000,1900000, #56-60
            2100000,2300000,2500000,2800000,3100000, #61-65
            3400000,3700000,4100000,4500000,4900000, #66-70
            5400000,5900000,6500000,7200000,7900000, #71-75
            8700000,9500000,11000000,12000000,13000000, #76-80
            13000000,14000000,14000000,15000000,16000000, #81-85
            17000000,18000000,19000000,20000000,21000000, #86-90
            22000000,23000000,24000000,25000000,26000000, #91-95
            27000000,28000000,30000000,31000000,33000000, #96-100
            35000000,37000000,39000000,41000000,33000000, #101-105
            45000000,47000000,49000000,51000000,53000000, #106-110
            55000000,57000000,59000000,61000000,63000000, #111-115
            65000000,67000000,69000000,71000000,73000000, #116-120
            75000000,77000000,79000000,81000000,83000000, #121-125
            85000000,87000000,89000000,91000000,93000000, #126-130
            95000000,97000000,100000000,105000000,110000000, #131-135
            115000000,120000000,125000000,130000000,135000000, #136-140
            140000000,145000000,150000000,155000000,160000000, #141-145
            165000000,170000000,175000000,180000000,185000000 #146-150
            ]

st.markdown('## Hero Experience Calculator')

current_level = st.selectbox(
    'Current Hero Level',
    np.arange(1,151))


target_level = st.selectbox(
    'Target Hero Level',
    np.arange(1,151))


st.write('Going from level ', int(current_level), ' to level ', target_level)

req_exp = sum(level_exp[current_level-1:target_level])


def numformat(num):
    fn = 0
    if num > 999999999:
        if not num % 1000000000:
            fn = f'{num // 1000000000}G'
        else:
            fn = f'{round(num / 1000000000, 1)}G'

    elif num > 999999:
        if not num % 1000000:
            fn = f'{num // 1000000}M'
        else:
            fn = f'{round(num / 1000000, 1)}M'

    elif num > 999:
        if not num % 1000:
            fn = f'{num // 1000}K'
        else:
            fn = f'{round(num / 1000, 1)}K'

    if fn == 0: 
        return ''
    else: 
        return f'{fn}' 


if numformat(req_exp) != '':
    st.write('Required Experience: ', numformat(req_exp), '({:0,})'.format(req_exp))
else:
    st.write('Required Experience: ', '{:0,}'.format(req_exp))


st.markdown('## VS Hero Day Points Calculator')
vs_event = st.selectbox(
    'VS reward per 660xp points:',
    [1,2])


st.write( '{:0,}'.format(int(req_exp/660)*vs_event) )

#660 = 2pts