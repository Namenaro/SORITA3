from utils import *

class ZRule:
    def __init__(self, mean_u, max_rad, len_of_seq):
        self.mean_u = mean_u
        self.max_rad = max_rad
        self.len = len_of_seq
        self.u = Point(round(mean_u.x), round(mean_u.y))


def create_z_rule(binary_img, max_rad, min_len):
    while True:
        start_point = get_random_coord_of_1(binary_img)
        points_list = try_grow_seq_of_points_unknown_u(start_point, binary_img, max_rad)
        if len(points_list) < min_len:
            print("Too short points list to create rule")
            continue

        z_rule = create_z_rule_by_list(points_list, max_rad)
        print("Rule was found!")
        return z_rule

def try_grow_seq_of_points_unknown_u(start_point, binary_img, max_rad):
    if sense_1(start_point, binary_img) is False:
        return []
    second_p = find_nearest_1(start_point, binary_img, max_rad)
    u = Point(second_p.x - start_point.x, second_p.y - start_point.y)
    return try_qrow_seq_of_points_with_u(start_point, binary_img, u, max_rad)

def try_qrow_seq_of_points_with_u(start_point, binary_img, u, max_rad):
    if sense_1(start_point, binary_img) is False:
        return []
    seq_of_points = [start_point]
    last_point = start_point
    while True:
        next_expected_point = Point(x=last_point.x + u.x, y=last_point.y + u.y)
        next_real_point = find_nearest_1_with_exclusions(next_expected_point, binary_img, max_rad, exclusions=seq_of_points)
        if next_real_point is None:
            break
        seq_of_points.append(next_real_point)
        last_point = next_real_point
    # обратный проход
    u = get_backward_dir(u)
    last_point = seq_of_points[0]
    while True:
        next_expected_point = Point(x=last_point.x + u.x, y=last_point.y + u.y)
        next_real_point = find_nearest_1_with_exclusions(next_expected_point, binary_img, max_rad, exclusions=seq_of_points)
        if next_real_point is None:
            break
        seq_of_points.insert(0, next_real_point)
        last_point = next_real_point
    return seq_of_points

def create_z_rule_by_list(points_list, max_rad):
    mean_u = get_mean_u(points_list)
    z_rule = ZRule(mean_u, max_rad, len_of_seq=len(points_list))
    return z_rule

def try_zrule_from_start_point(binary_img, start, z_rule, min_len):
    points = try_qrow_seq_of_points_with_u(start, binary_img, z_rule.u, z_rule.max_rad)
    if len(points) >= min_len:
        if points[0] == start:
            return points
    return []
