from sympy import shape, Matrix, symbols, cos, sin, simplify, pi, pprint, diff
from numpy import linspace, meshgrid, ones_like
import matplotlib.pyplot as plt
import time
from test import cal_base_to_end_transformation, transform

samples = 40 
dt = 5.0/samples 
theta1, theta2, theta3, theta4, theta5, theta6, theta7 = symbols('theta1, theta2, theta3, theta4, theta5, theta6, theta7')

T_01, T_02, T_04, T_05, T_06, T_07 = cal_base_to_end_transformation()

Z00 = simplify(Matrix([0,0,1,0]))
Z01 = simplify(T_01[:,2])
Z02 = simplify(T_02[:,2])
Z04 = simplify(T_04[:,2])
Z05 = simplify(T_05[:,2])
Z06 = simplify(T_06[:,2])

X0p = simplify(T_07[:,3])
Jv1 = simplify(diff(X0p, theta1))
Jv2 = simplify(diff(X0p, theta2))
Jv4 = simplify(diff(X0p, theta4))
Jv5 = simplify(diff(X0p, theta5))
Jv6 = simplify(diff(X0p, theta6))
Jv7 = simplify(diff(X0p, theta7))

upper_jacobian_matrix = Jv1.row_join(Jv2).row_join(Jv4).row_join(Jv5).row_join(Jv6).row_join(Jv7)
upper_jacobian_matrix = upper_jacobian_matrix.row_del(3)

lower_jacobian_matrix = Z00.row_join(Z01).row_join(Z02).row_join(Z04).row_join(Z05).row_join(Z06)
lower_jacobian_matrix = lower_jacobian_matrix.row_del(3)

jacobian = upper_jacobian_matrix.col_join(lower_jacobian_matrix)
pprint("jacobian_matrix is")
pprint(jacobian)

def cal_theta_dot(th, theta_joint):
    y_dot = 4.0*pi*sin(th)
    z_dot = 4.0*pi*cos(th)
    X_dot = Matrix([0.0, y_dot, z_dot, 0.0, 0.0, 0.0]) 
    jacobian_inv = jacobian.evalf(3,subs={theta1: theta_joint[0],theta2: theta_joint[1], theta4: theta_joint[2], theta5:
    theta_joint[3], theta6: theta_joint[4], theta7: theta_joint[5]}).inv()
    theta_dot = jacobian_inv * X_dot 
    theta_joint = theta_joint + theta_dot*dt
    return theta_joint

def update_joint_angle(theta, theta_dot):
    theta = theta + theta_dot*dt
    return theta
def forward_position_kinematics(theta):
    T = T_07.evalf(subs={theta1: theta[0], theta2: theta[1], theta4: theta[2], theta5: theta[3], theta6: theta[4], theta7:
    theta[5]})
    return (T[0,3].round(4),T[1,3].round(4),T[2,3].round(4))
if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.axes.set_xlim(left=-10, right=90)
    ax.axes.set_ylim(bottom=-30, top=55)
    ax.axes.set_zlim(bottom=0, top=85)
    ax.set_xlabel('X_axis')
    ax.set_ylabel('Y_axis')
    ax.set_zlabel('Z_axis')
    theta_joint = Matrix([0.0, 0.0, float(pi/2), 0.0, float(pi), 0.0]) 
    for theta in linspace(float(pi/2), float((5*pi)/2), num=samples):
        theta_joint = cal_theta_dot(theta, theta_joint)
        (x_0p, y_0p, z_0p) = forward_position_kinematics(theta_joint)
        print("for theta:",theta,"X pose is:",x_0p,"Y pose is:",y_0p,"Z pose is:",z_0p)
        ax.scatter(x_0p,y_0p,z_0p)
        plt.pause(dt)
    plt.show()