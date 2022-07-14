from z_rule import *
from z_example import *
from utils import *
from visualisation import *
from mass_prediction import *
from stata import *
from logger import *

from random import choice

def apply_zz_rule_to_img(binary_pic, z_rule, zz_rule):
    z_examples = find_all_z_ezamples_on_pic(binary_pic, z_rule, min_len=3)
    binary_pic_z = place_examples_to_binary_img(binary_pic.shape, z_examples)
    zz_examples = find_all_z_ezamples_on_pic(binary_pic_z, zz_rule, min_len=3)
    return zz_examples

def get_z_zz_rules(binary_etalon):
    # show_binary_pic(binary_etalon)
    z_rule = ZRule(mean_u=Point(x=0, y=-1), max_rad=1, len_of_seq=3)
    z_examples = find_all_z_ezamples_on_pic(binary_etalon, z_rule, min_len=3)
    binary_etalon_z = place_examples_to_binary_img(binary_etalon.shape, z_examples)
    # show_binary_pic(binary_etalon_z)
    zz_rule = create_z_rule(binary_etalon_z, max_rad=3, min_len=3)
    zz_examples = find_all_z_ezamples_on_pic(binary_etalon_z, zz_rule, min_len=3)
    #visuailise_examples_in_pic(etalon_pic, zz_examples)
    return z_rule, zz_rule

def get_strongest_example(zz_examples):
    index = 0
    best_len = 0
    for i in range(len(zz_examples)):
        curr_len = len(zz_examples[i].points)
        if curr_len>best_len:
            best_len = curr_len
            index = i
    return zz_examples[index]

def collect_train_situations_NO_RANGE(train_pics, z_rule, zz_rule):
    binary_pics = []
    points = []
    for binary_pic in train_pics:
        zz_examples = apply_zz_rule_to_img(binary_pic, z_rule, zz_rule)
        for zz_ex in zz_examples:
            binary_pics.append(binary_pic)
            points.append(zz_ex.get_z_point())
        if len(zz_examples)==0:
            print("PROBLEM - no Z-points in TRAIN PIC!")
    return binary_pics, points

if __name__ == '__main__':
    log = HtmlLogger("NAIVE_SELECTION_MASS_PRED")
    train_pics, test_pics, contrast = get_train_test_contrast_BIN(class_num=45) #F=45, две закорюки и точка = 56, самый простой значок = 9, 29 и 32
    etalon_pic = choice(train_pics)

    z_rule, zz_rule = get_z_zz_rules(etalon_pic)
    zz_examples = apply_zz_rule_to_img(etalon_pic, z_rule, zz_rule)
    visuailise_examples_in_pic(etalon_pic, zz_examples)

    zz_e1 = get_strongest_example(zz_examples)
    #  выбор предсказаний относительно zz_e1
    m_pred = MassPrediction(u=Point(x=-10, y=10),
                            top_left_coord=Point(x=3, y=3),
                            bottow_right_coord=Point(x=-5, y=-3))

    situation_pics, situation_points = collect_train_situations_NO_RANGE(train_pics, z_rule, zz_rule)
    sample_zz = m_pred.sample_by_situation_generator(situation_pics, situation_points)
    sample_ = m_pred.sample_from_generlal_population(train_pics)
    p_val = get_p_value_for_two_samples(sample_, sample_zz)
    visualise_mass_pred(etalon_pic, zz_e1, m_pred, sample_zz, sample_, log, p_val)
    print(p_val)
    log.close()













