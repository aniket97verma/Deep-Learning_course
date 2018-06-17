
from numpy import *

def compute_error(b, m, points):
    totalError = 0
    for i in range(0,len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) **2
    return totalError / float(len(points))

def step_gradient(current_b, current_m, points, learning_rate):
    #gradient descent working
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - (current_m * x + current_b))
        m_gradient += -(2/N) * x * (y-(current_m * x + current_b))
    new_b = current_b - (learning_rate * b_gradient)
    new_m = current_m - (learning_rate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations):
    b = initial_b
    m = initial_m

    for i in range(num_iterations):
        b, m  = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def run():
    points = genfromtxt('data.csv',delimiter=',')
    #hyperparameters
    learning_rate = 0.0001
    #y = mx + b initial line
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print("optimal b: " + str(b))
    print("optimal m: " + str(m))
    print(compute_error(b, m, points))

if __name__ == '__main__':
    run()
