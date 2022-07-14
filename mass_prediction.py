from utils import *
from random import choice, randrange

class MassPrediction:
    def __init__(self, u, top_left_coord, bottow_right_coord):
        self.u = u
        self.top_left_coord = top_left_coord
        self.bottow_right_coord=bottow_right_coord

    def run(self, start, binary_img):
        abs_center = Point(x=start.x+self.u.x, y=start.y+self.u.y)
        min_x = self.top_left_coord.x
        max_x = self.bottow_right_coord.x
        min_y = self.top_left_coord.y
        max_y = self.bottow_right_coord.y

        mass = 0
        for local_x in range(min_x, max_x):
            for local_y in range(min_y, max_y):
                abs_point = Point(x=abs_center.x+local_x, y=abs_center.y+local_y)
                mass += sense_1(abs_point, binary_img)
        return mass

    def sample_from_generlal_population(self, binary_pics):
        sample = []
        for i in range(300):
            random_pic = choice(binary_pics)
            random_x = randrange(0, random_pic.shape[1])
            random_y = randrange(0, random_pic.shape[0])
            point = Point(random_x, random_y)
            sample.append(self.run(point,random_pic))
        return sample

    def sample_by_situation_generator(self, binary_pics, points):
        sample = []
        for i in range(len(binary_pics)):
            pic = binary_pics[i]
            point = points[i]
            sample.append(self.run(point, pic))
        return sample

    def get_w_h(self):
        min_x = self.top_left_coord.x
        max_x = self.bottow_right_coord.x
        min_y = self.top_left_coord.y
        max_y = self.bottow_right_coord.y

        w = max_x-min_x
        h = max_y-min_y
        return w,h





