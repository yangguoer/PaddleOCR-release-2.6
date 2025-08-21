#!/bin/bash

# 定义两个Python文件路径
python_file1="split_data.py"
python_file2="gen_rec_data.py"

# 检查文件是否存在
if [ ! -f "$python_file1" ]; then
  echo "文件 '$python_file1' 不存在"
  exit 1
fi

if [ ! -f "$python_file2" ]; then
  echo "文件 '$python_file2' 不存在"
  exit 1
fi


echo "执行第一个Python文件: $python_file1"
# 使用系统中的Python 3解释器执行第一个文件
python_output1=$(D:/Virtualenv/PaddleOCR-release-2.6/Scripts/python.exe "$python_file1")
echo "第一个Python文件执行结果:"
echo "$python_output1"

echo "执行第二个Python文件: $python_file2"
# 执行完毕后，使用系统中的Python 3解释器执行第二个文件
python_output2=$(D:/Virtualenv/PaddleOCR-release-2.6/Scripts/python.exe "$python_file2")
echo "第二个Python文件执行结果:"
echo "$python_output2"
