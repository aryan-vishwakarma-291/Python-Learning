# import tensorflow as tf
# from tensorflow import keras
# import numpy as np
# import matplotlib.pyplot as plt

# # load MNIST 70000 handwritten digit images
# (X_train , y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()
# print(f'Traning: {X_train.shape} | Test: {X_test.shape}')

# #visulize samples
# plt.figure(figsize=(12,2))
# for i in range(12):
#     plt.subplot(1,12,i+1)
#     plt.imshow(X_train[i],cmap='gray'); plt.axis('off')
#     plt.title(str(y_train[i]), fontsize=8)
# plt.suptitle('Sample MNIST Digits'); plt.show()

# #Normalise
# X_train = X_train / 255.0
# X_test = X_test / 255.0

# #Flaatten 
# X_train = X_train.reshape(-1,784)
# X_test = X_test.reshape(-1,784)

# model = keras.Sequential([
#     keras.layers.Dense(512,activation='relu' , input_shape=(784,)),
#     keras.layers.Dense(0.2),
#     keras.layers.Dense(256,activation='relu'),
#     keras.layers.Dense(0.2),
#     keras.layers.Dense(10, activation='softmax')
# ])

# model.summary()

# model.compile(
#     optimizer='adam',
#     loss='sparse_categorical_crossentropy',
#     metrics=['accuracy']
# )

# #Train the model
# history = model.fit(
#     X_train , y_train,
#     epochs=10,
#     batch_size=128,
#     validation_split=0.1,
#     callbacks=[keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)]
# )

# #Evaluate
# test_loss,test_acc = model.evaluate(X_test,y_test,verbose=0)
# print(f'Test accuracy: {test_acc*100:.2f}')

# #plot training history
# fig,axes = plt.subplots(1,2,figsize=(12,4))
# axes[0].plot(history.history['accuracy'], label='Train')
# axes[0].plot(history.history['val_accuracy'] , label='Validation')
# axes[0].set_title('Accuracy'); axes[0].legend()
# axes[1].plot(history.history['loss'],  label='Train')
# axes[1].plot(history.history['val_loss'], label='validation')
# axes[1].set_title('Loss'); axes[1].legend()
# plt.tight_layout(); plt.show()


# #see prediction on test images
# predictions = model.predict(X_test[:15])
# pred_classes = np.argmax(predictions, axis=1)

# plt.figure(figsize=(15,3))
# for i in range(15):
#     plt.subplot(1,15,i+1)
#     plt.imshow(X_test[i].reshape(28,28),cmap='gray')
#     correct = pred_classes[i]==y_test[i]
#     plt.title(str(pred_classes[i]),color='green' if correct else 'red' , fontsizr=8)
#     plt.axis('off')
# plt.suptitle('Green=correct Red=Wrong'); 
# plt.show()
