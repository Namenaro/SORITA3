from utils import *
from random import choice, randrange

class MassPrediction:
    def __init__(self, u, top_left_coord, bottow_right_coord):
        self.u = u
        self.top_left_coord = top_left_coord
        self.bottow_right_coord=bottow_right_coord

    def run(self, start, binary_img):
        coord_center_x = start.x + self.u.x
        coord_center_y = start.y - self.u.y
        x_min = coord_center_x + self.top_left_coord.x
        y_min = coord_center_y - self.top_left_coord.y
        w, h = self.get_w_h()

        mass = 0
        for dx in range(w):
            for dy in range(h):
                abs_point = Point(x=x_min+dx, y=y_min+dy)
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
        w = self.bottow_right_coord.x- self.top_left_coord.x
        h = self.top_left_coord.y - self.bottow_right_coord.y
        return w,h





