import sys
import dnnlib
import dnnlib.tflib as tflib
from training import training_loop
from metrics import metric_main
import tensorflow as tf

sys.path.append('models/stylegan2')

def train_stylegan2():
    # Check if GPU is available
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    if len(physical_devices) > 0:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        print(f"Using GPU: {physical_devices[0]}")
    else:
        print("No GPU found. Exiting.")
        return

    # Initialize TensorFlow
    tflib.init_tf()

    # Define training parameters
    config = dnnlib.EasyDict()
    config.num_gpus = 1  # Adjust this to match the number of GPUs available
    config.total_kimg = 25000
    config.mirror_augment = True
    config.result_dir = 'results'
    
    # Dataset and model paths
    config.data_dir = 'data/processed/stylegan2'
    config.network_snapshot_ticks = 10
    config.network_pkl = None  # Path to pre-trained model or None for training from scratch

    # Launch training
    training_loop.training_loop(config)
    print('Training complete.')

if __name__ == '__main__':
    train_stylegan2()
