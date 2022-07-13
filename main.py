from z_rule import *
from z_example import *
from utils import *
from visualisation import *
from random import choice

def apply_zz_rule_to_img(img, z_rule, zz_rule):
    binary_pic = binarise_img(img)
    z_examples = find_all_z_ezamples_on_pic(binary_pic, z_rule, min_len=3)
    binary_pic_z = place_examples_to_binary_img(binary_pic.shape, z_examples)
    zz_examples = find_all_z_ezamples_on_pic(binary_pic_z, zz_rule, min_len=3)
    visuailise_examples_in_pic(img, zz_examples)

def get_rules(etalon_pic):
    binary_etalon = binarise_img(etalon_pic)
    # show_binary_pic(binary_etalon)
    z_rule = ZRule(mean_u=Point(x=0, y=-1), max_rad=1, len_of_seq=3)
    z_examples = find_all_z_ezamples_on_pic(binary_etalon, z_rule, min_len=3)
    binary_etalon_z = place_examples_to_binary_img(binary_etalon.shape, z_examples)
    # show_binary_pic(binary_etalon_z)
    zz_rule = create_z_rule(binary_etalon_z, max_rad=3, min_len=3)
    zz_examples = find_all_z_ezamples_on_pic(binary_etalon_z, zz_rule, min_len=3)
    #visuailise_examples_in_pic(etalon_pic, zz_examples)
    return z_rule, zz_rule

if __name__ == '__main__':
    train_pics, test_pics, contrast = get_train_test_contrast(class_num=45) #F=45, две закорюки и точка = 56, самый простой значок = 9, 29 и 32
    etalon_pic = choice(train_pics)

    z_rule, zz_rule = get_rules(etalon_pic)
    apply_zz_rule_to_img(etalon_pic, z_rule, zz_rule)
    apply_zz_rule_to_img(test_pics[0], z_rule, zz_rule)










