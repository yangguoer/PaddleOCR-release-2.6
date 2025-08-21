
import os
import argparse
import json
from PIL import Image
import cv2

def gen_rec_label(input_path, out_path, lable):
    out_label = os.path.join(out_path,lable)
    input_txt = os.path.join(input_path,lable)
    with open(out_label, 'w+',encoding='utf-8') as out_file:
        with open(input_txt, 'r',encoding='utf-8') as f:
            for line in f.readlines():
                tmp = line.strip('\n').split('\t')
                img_name, des = tmp[0], tmp[1]
                img_path =  input_path + img_name
                print('img_path:{},des:{}',img_path,des)
                list = json.loads(des)
                print(type(list))
                i = 0
                for data in list:
                    point = data['points']
                    transcription = data["transcription"];
                    # 把相应的坐标转化为以左上角为原点的四个边框的位置，并把字符串转化为整数型
                    t2 = point[0]
                    t3 = point[2]
                    box = (t2[0], t2[1], t3[0], t3[1])
                    if box[2] < box[0] or box[3] < box[1]:
                        break
                    # 前两个坐标点是左上角坐标# 后两个坐标点是右下角坐标# width在前， height在后
                    try:
                        img = Image.open(img_path)
                        region = img.crop(box)
                        nn = img_name.split('.')[0]
                        name = nn + '_' + str(i) + '.jpg'
                        if region.width != 0 and region.height != 0:
                            region.save(out_path + name)
                            i += 1
                            trans = transcription.encode('utf-8')
                            s = str(trans, encoding="utf-8")
                            print(s)

                            out_file.write(name + '\t' + s + '\n')
                    except Exception as e:
                        print('异常：',e)
                        break



if __name__ == "__main__":
    # train
    input_path = './train_data/det/train/'
    output_path = './train_data/rec/train/'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    gen_rec_label(input_path, output_path, 'train.txt')
    input_path = './train_data/det/test/'
    output_path = './train_data/rec/test/'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    gen_rec_label(input_path, output_path,'test.txt')



