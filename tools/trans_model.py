import paddle

paddle_name = './output/rec_ppocr_v3/best_accuracy'
params = paddle.load(paddle_name + '.pdparams')
new_state_dict = {}
for k1 in params.keys():
    if 'Student.' in k1:
        new_state_dict[k1.replace('Student.','')] = params[k1]
        # print(k1)
paddle.save(new_state_dict, paddle_name+'_new.pdparams')