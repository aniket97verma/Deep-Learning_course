# Make_a_neural_network
This is the code for the "Make a Neural Network" - Intro to Deep Learning #2 by Siraj Raval on Youtube

##Overview

This is the code for [this](https://youtu.be/p69khggr1Jo) video by Siraj Raval on Youtube. This is a [simple](http://computing.dcu.ie/~humphrys/Notes/Neural/single.neural.html) single layer feedforward neural network (perceptron). We use binary digits as our inputs and expect binary digits as our outputs. We'll use [backpropagation](http://neuralnetworksanddeeplearning.com/chap2.html) via gradient descent to train our network and make our prediction as accurate as possible.


##Dependencies

None! Just numpy.

##Usage

Run ``python demo.py`` in terminal to see it train, then predict.

##Challenge

The challenge for this video is to create a 3 layer feedforward neural network using only numpy as your dependency. By doing this, you'll understand exactly how backpropagation works and develop an intuitive understanding of neural networks, which will be useful for more the more complex nets we build in the future. Backpropagation usually involves recursively taking derivatives, but in our 1 layer demo there was no recursion so was a trivial case of backpropagation. In this challenge, there will be. Use a small binary dataset, you can define one programmatically like in this example.

## Backpropagation Algorithm
Backpropagation is the process of tuning a neural network’s weights to better the prediction accuracy. There are two directions in which information flows in a neural network.

    Forward propagation — also called inference — is when data goes into the neural network and out pops a prediction.
    Backpropagation — the process of adjusting the weights by looking at the difference between prediction and the actual result.
    
Below are the steps involved in Backpropagation:

    Step – 1: Forward Propagation
    Step – 2: Backward Propagation 
    Step – 3: Putting all the values together and calculating the updated weight value
 

**Bonus -- use a larger, more interesting dataset**

##Credits

The credits for this code go to [Milo Harper](https://github.com/miloharper). I've merely created a wrapper to get people started.
