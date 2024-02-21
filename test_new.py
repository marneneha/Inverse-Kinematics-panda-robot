from sympy import Matrix, symbols, cos, sin, simplify, pi, pprint, diff, shape, transpose
from numpy import array

def transform(a, theta, alfa, d):
    Ai = Matrix([[cos(theta), -sin(theta)*cos(alfa), sin(theta)*sin(alfa), a*cos(theta)],
                 [sin(theta), cos(theta)*cos(alfa), -cos(theta)*sin(alfa), a*sin(theta)],
                 [0,          sin(alfa),             cos(alfa),            d],
                 [0,            0,                      0,                 1]])
    return Ai

def cal_base_to_end_transformation():
    theta1, theta2, theta3 = symbols('theta1, theta2, theta3')
    d1 = 0.2
    d2 = 1.0
    d3 = 0.0
    d4 = 0.0
    a1=0.0
    a2=0.0
    a3=1.0
    a4=1.0
    DH_Table = Matrix([[a1,theta1, 0.0,    d1], 
                       [a2,theta2, pi/2,   d2],
                       [a3,theta3, 0.0,    d3],
                       [a4, 0.0,   0.0,    d4]])
    pprint("DH Parameters are")
    pprint(DH_Table)

    T_01 = transform(DH_Table[0,0],DH_Table[0,1], DH_Table[0,2], DH_Table[0,3])
    T_12 = transform(DH_Table[1,0],DH_Table[1,1], DH_Table[1,2], DH_Table[1,3])
    T_23 = transform(DH_Table[2,0],DH_Table[2,1], DH_Table[2,2], DH_Table[2,3])
    T_34 = transform(DH_Table[3,0],DH_Table[3,1], DH_Table[3,2], DH_Table[3,3])

    # print("T_01 is")
    # pprint(T_01)
    # print("T_12 is")
    # pprint(T_12)
    # print("T_23 is")
    # pprint(T_23)
    # print("T_34 is")
    # pprint(T_34)
    T_02 = T_01 * T_12
    T_03 = T_02 * T_23
    T_04 = T_03 * T_34
    return T_01, T_02, T_03, T_04