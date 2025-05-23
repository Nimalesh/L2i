BATCH_SIZE = 4
DIM_Z = 512  # used only for setting default arg value
resolution = 256
# resolution = 128
useGPU = True
NUM_CHANNELS = 3

## Regressor - Scene
# reg_json = None
# reg_path = '/path/500_dict.model'
## StyleGAN2 - scene
# g_path = '/path/checkpoint/190000.pt'

## Regressor - ffhq
reg_json = None
reg_path = '/content/drive/MyDrive/utils/latent2image/003_dict.model'
## StyleGAN2 - ffhq
g_path = '/content/drive/MyDrive/utils/latent2image/550000.pt'

"""
If use a WGAN-GP loss (not used in the end)
"""
# CRITIC_ITERS = 5 # For WGAN and WGAN-GP, number of critic iters per gen iter
# LAMBDA = 10 # Gradient penalty lambda hyperparameter
# ITERS = 200000 # How many generator iterations to train for
