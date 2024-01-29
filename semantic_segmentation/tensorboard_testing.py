import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import TensorBoard
model = load_model('unet_football.h5')
log_dir = 'logs/your_unet_visualization'
tensorboard_callback = TensorBoard(log_dir=log_dir)
