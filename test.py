import tensorflow as tf
from tensorflow.keras.applications import ResNet50V2
from tensorflow.keras.utils import plot_model

# 创建ResNet18_vd模型
resnet18_vd_model = ResNet50V2(weights='imagenet', include_top=True)

# 可视化网络结构并保存为图片
plot_model(resnet18_vd_model, to_file='resnet18_vd_model.png', show_shapes=True)
