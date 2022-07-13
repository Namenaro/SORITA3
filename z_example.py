from utils import *
from z_rule import *

class ZExample:
    def __init__(self, rule, points):
        self.rule = rule
        self.points = points

    def get_z_point(self):
        return self.points[0]

def find_all_z_ezamples_on_pic(binary_img, z_rule, min_len):
    print("find_all_z_ezamples_on_pic")
    examples = []
    for x in range(binary_img.shape[1]):
        for y in range(binary_img.shape[0]):
            start = Point(x, y)
            if start.x==25 and start.y==22:
                print("ghghghg")
            points = try_zrule_from_start_point(binary_img, start, z_rule, min_len)
            if len(points) < min_len:
                continue
            z_example = ZExample(z_rule, points)
            examples.append(z_example)

    return examples

def place_examples_to_binary_img(shape, examples):
    new_img = np.zeros(shape)
    for example in examples:
        point = example.get_z_point()
        new_img[point.y, point.x] = 1
    return new_img


