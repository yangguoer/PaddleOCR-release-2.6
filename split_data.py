from sklearn.model_selection import train_test_split
import os
import shutil

if __name__ == "__main__":
    path = './data/Label.txt'
    train_path = './train_data/det/train/'
    test_path = './train_data/det/test/'
    if not os.path.exists(train_path):
        os.makedirs(train_path)
    if not os.path.exists(test_path):
        os.makedirs(test_path)
    train_lable_path = './train_data/det/train/train.txt'
    test_lable_path = './train_data/det/test/test.txt'

    arr = []
    with open(path, 'r',encoding='utf-8') as f:
        for line in f.readlines():
            tmp = line.strip('\n').split('\t')
            img_name, des = tmp[0], tmp[1]
            # img_name = img_path.split('/')[1]
            arr.append(img_name)

    train,test = train_test_split(arr, test_size=0.2, random_state=42)
    print('x_train:',train)
    print('x_train:', test)
    for train_img in train:
        src = os.path.join('./', train_img)
        print('src:' + src + ' result_path:' + train_path)
        # 复制图像
        shutil.copy(src, train_path)
    for test_img in test:
        src = os.path.join('./', test_img)
        print('src:' + src + ' result_path:' + test_path)
        # 复制图像
        shutil.copy(src, test_path)
    with open(train_lable_path, 'w', encoding='utf-8') as train_lable_f:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                tmp = line.strip('\n').split('\t')
                img_name, des = tmp[0], tmp[1]
                if img_name in train:
                    img_name1 = img_name.split('/')[1]
                    train_lable_f.write(img_name1+'\t'+des+'\n')
    with open(test_lable_path, 'w', encoding='utf-8') as test_lable_f:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                tmp = line.strip('\n').split('\t')
                img_name, des = tmp[0], tmp[1]
                if img_name in test:
                    img_name1 = img_name.split('/')[1]
                    test_lable_f.write(img_name1+'\t'+des+'\n')

