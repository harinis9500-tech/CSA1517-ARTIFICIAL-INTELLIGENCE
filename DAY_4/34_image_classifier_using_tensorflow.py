# 34 TensorFlow image classifier on Fashion-MNIST
import tensorflow as tf
(x,y),(xt,yt)=tf.keras.datasets.fashion_mnist.load_data()
x=x/255.;xt=xt/255.
m=tf.keras.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),tf.keras.layers.Dense(128,activation="relu"),tf.keras.layers.Dense(10,activation="softmax")])
m.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
m.fit(x,y,epochs=3,validation_split=.1);print(m.evaluate(xt,yt))