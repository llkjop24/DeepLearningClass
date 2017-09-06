


import tensorflow as tf
tf.set_random_seed(777)

X = [1, 2, 3]
Y = [1, 2, 3] #correct answer

# a neuron
W = tf.Variable(tf.random_normal([1]))
hypothesis = W * X

cost_function = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.02)
gradient_descent = optimizer.minimize(cost_function)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Learning: find w
for step in range(100):
    sess.run(gradient_descent)

    w_val = sess.run(W)
    cost_val = sess.run(cost_function)
    print(step, 'W=', w_val, 'cost=', cost_val)

