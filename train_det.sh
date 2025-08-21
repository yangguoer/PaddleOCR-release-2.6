#!/bin/bash

# 定义两个Python文件路径
python_file1="tools/train.py"

python_file2="tools/export_model.py"

# 检查文件是否存在
if [ ! -f "$python_file1" ]; then
  echo "文件 '$python_file1' 不存在"
  exit 1
fi

if [ ! -f "$python_file2" ]; then
  echo "文件 '$python_file2' 不存在"
  exit 1
fi
# 提取除了第一个参数之外的所有参数
shift
python_args1="-c configs/det/det_res18_db_v2.0.yml -o Global.pretrained_model=./pretrain_models/ResNet18_vd_pretrained"

shift
python_args2="-c configs/det/det_res18_db_v2.0.yml -o Global.pretrained_model="./output/ch_db_res18/best_accuracy" Global.save_inference_dir="./output/det_inference/""

echo "执行ocr目标检测训练文件: $python_file1"
echo "传递的参数: $python_args1"
# 使用系统中的Python 3解释器执行第一个文件
python_output1=$(D:/Virtualenv/PaddleOCR-release-2.6/Scripts/python.exe "$python_file1" $python_args1)
echo "ocr目标检测训练文件执行结果:"
echo "$python_output1"

echo "执行ocr目标检测模型导出文件: $python_file2"
echo "传递的参数: $python_args2"
# 执行完毕后，使用系统中的Python 3解释器执行第二个文件
python_output2=$(D:/Virtualenv/PaddleOCR-release-2.6/Scripts/python.exe "$python_file2" $python_args2)
echo "ocr目标检测模型导出文件执行结果:"
echo "$python_output2"
