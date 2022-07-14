from z_example import *
from logger import *

from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt

def show_binary_pic(binary_pic):
    plt.figure()
    cm = plt.get_cmap('seismic')
    plt.imshow(binary_pic, cmap=cm, vmin=0, vmax=1)
    plt.show()


def visuailise_examples_in_pic(pic, zz_examples):
    plt.figure()
    plt.imshow(pic, cmap='gray_r', vmin=0, vmax=1)
    for example in zz_examples:
        head = example.get_z_point()
        plt.scatter(head.x, head.y, s=100, c='red', marker='o', alpha=0.4)
        for i in range(1, len(example.points)):
            plt.scatter(example.points[i].x, example.points[i].y, s=100, c='green', marker='o', alpha=0.4)
    plt.show()


def visualise_mass_pred(etalon_pic, zz_e1, m_pred, sample_zz, sample_, log, p_val):
    log.add_text("p_val="+str(p_val))
    log.add_text("sample_=" + str(sample_))
    log.add_text("sample_zz=" + str(sample_zz))
    fig, ax = plt.subplots()
    ax.imshow(etalon_pic, cmap='gray_r', )
    coord_center_x=zz_e1.get_z_point().x
    coord_center_y=zz_e1.get_z_point().y
    ax.plot(coord_center_x, coord_center_y , marker='o', markerfacecolor='blue', color='skyblue', linewidth=4)
    x=m_pred.top_left_coord.x+ coord_center_x
    y=m_pred.top_left_coord.y +coord_center_y
    w,h = m_pred.get_w_h()
    rect = Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    log.add_fig(fig)