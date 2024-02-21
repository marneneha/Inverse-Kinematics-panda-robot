from sympy import Matrix, symbols, cos, sin, simplify, pi, pprint, diff, shape, transpose
from numpy import array

def transform(a, theta, alfa, d):
    Ai = Matrix([[cos(theta), -sin(theta)*cos(alfa), sin(theta)*sin(alfa), a*cos(theta)],
        [sin(theta), cos(theta)*cos(alfa), -cos(theta)*sin(alfa), a*sin(theta)],
        [0, sin(alfa), cos(alfa), d],
        [0, 0, 0, 1]])
    return Ai

def cal_base_to_end_transformation():
    theta1, theta2, theta4, theta5, theta6, theta7 = symbols('theta1, theta2, theta4, theta5, theta6, theta7')
    a = 8.8
    d1=33.3
    d2=0
    d3=31.6
    d4=0
    d5=38.4
    d6=0
    d7=-20.7
    alfa1 = pi/2
    alfa2 = -pi/2
    alfa3 = -pi/2
    alfa4 = pi/2
    alfa5 = pi/2
    alfa6 = -pi/2
    alfa7 = 0
    DH_Table = array([[ 0,theta1, pi/2, d1], 
    [0,theta2, -pi/2, d2],
    [a,0, -pi/2, d3],
    [-a,theta4, pi/2, d4],
    [0,theta5, pi/2, d5], 
    [a,theta6, -pi/2, d6], 
    [0,theta7, 0, d7]])
    pprint("DH Parameters are")
    pprint(DH_Table)

    T_01 = transform(DH_Table[0][0],DH_Table[0][1], DH_Table[0][2], DH_Table[0][3])
    T_12 = transform(DH_Table[1][0],DH_Table[1][1], DH_Table[1][2], DH_Table[1][3])
    T_23 = transform(DH_Table[2][0],DH_Table[2][1], DH_Table[2][2], DH_Table[2][3])
    T_34 = transform(DH_Table[3][0],DH_Table[3][1], DH_Table[3][2], DH_Table[3][3])
    T_45 = transform(DH_Table[4][0],DH_Table[4][1], DH_Table[4][2], DH_Table[4][3])
    T_56 = transform(DH_Table[5][0],DH_Table[5][1], DH_Table[5][2], DH_Table[5][3])
    T_67 = transform(DH_Table[6][0],DH_Table[6][1], DH_Table[6][2], DH_Table[6][3])

    T_02 = T_01 * T_12
    T_04 = T_02 * T_23 * T_34
    # T_04 = T_03 * 
    T_05 = T_04 * T_45
    T_06 = T_05 * T_56
    T_07 = T_06 * T_67
    return T_01, T_02, T_04, T_05, T_06, T_07
