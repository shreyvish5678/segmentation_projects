import tensorflowjs as tfjs
import tensorflow as tf
model = tf.keras.models.load_model('unet_football.h5')
tfjs.converters.save_keras_model(model, "")