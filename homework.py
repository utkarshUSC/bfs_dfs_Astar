import heapq
import math

x = [1, -1, 0, 0, 0, 0, 1, 1, -1, -1, 1, 1, -1, -1, 0, 0, 0, 0]
y = [0, 0, 1, -1, 0, 0, 1, -1, 1, -1, 0, 0, 0, 0, 1, 1, -1, -1]
z = [0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 1, -1, 1, -1, 1, -1, 1, -1]


def check_valid(point_to_check, matrix_size):
    return (point_to_check[0] >= 0) and (point_to_check[1] >= 0) and (point_to_check[2] >= 0) and (
            point_to_check[0] < matrix_size[0]) and (point_to_check[1] < matrix_size[1]) and (
                   point_to_check[2] < matrix_size[2])


def convert_into_point(each_line_arr):
    point = (int(each_line_arr[0]), int(each_line_arr[1]), int(each_line_arr[2]))
    return point


def get_heuristic_value(point, final_point):
    dist = 0
    for i, _ in enumerate(point):
        dist = dist + (final_point[i] - point[i])*(final_point[i] - point[i])
    return round(math.sqrt(dist), 1)


def get_updated_point(curr_point, move):
    updated_x = curr_point[0] + x[move - 1]
    updated_y = curr_point[1] + y[move - 1]
    updated_z = curr_point[2] + z[move - 1]
    updated_point = (updated_x, updated_y, updated_z)
    return updated_point


def compare_two_point(point1, point2):
    return (point1[0] == point2[0]) and (point1[1] == point2[1]) and (point1[2] == point2[2])


def get_distance(method, curr_point, coordinates):
    dist = abs(coordinates[0] - curr_point[0]) + abs(coordinates[1] - curr_point[1]) + abs(coordinates[2] - curr_point[2])
    if method == "BFS":
        if dist == 0:
            return 0
        else:
            return 1
    if dist == 1:
        return 10
    elif dist == 2:
        return 14
    else:
        return 0


def print_path(method, parent_dict, initial_point, final_point):
    points = []
    curr_point = final_point
    points.append(final_point)
    while True:
        if compare_two_point(curr_point, initial_point):
            break
        curr_point = parent_dict.get(curr_point)
        points.append(curr_point)

    f = open("output.txt", "a")
    length = len(points)
    curr_point = initial_point
    cost = 0
    lines = []
    print(points)
    for i in range(0, length):
        coordinates = points[length - 1 - i]
        curr_cost = get_distance(method, curr_point, coordinates)
        cost = cost + curr_cost
        curr_point = coordinates
        line = str(coordinates[0]) + " " + str(coordinates[1]) + " " + str(coordinates[2])+" "+str(curr_cost)
        lines.append(line)
    f.write(str(cost))
    f.write("\n" + str(length))
    for line in lines:
        f.write("\n"+line)
    f.close()


def bfs(method, matrix, initial_point, final_point, points_to_consider_dict):
    queue = [initial_point]
    visited_dict = dict()
    parent_dict = dict()
    found_answer = False
    visited_dict[initial_point] = True
    while queue:
        curr_point = queue.pop(0)
        movements = points_to_consider_dict[curr_point]
        for move in movements:
            updated_point = get_updated_point(curr_point, move)
            if (visited_dict.get(updated_point) is None) and check_valid(updated_point, matrix):
                parent_dict[updated_point] = curr_point
                if compare_two_point(updated_point, final_point):
                    found_answer = True
                    break
                queue.append(updated_point)
                visited_dict[curr_point] = True
    if found_answer:
        print_path(method, parent_dict, initial_point, final_point)
    else:
        f = open("output.txt", "a")
        f.write("FAIL")
        f.close()


def search_space(method, matrix, initial_point, final_point, points_to_consider_dict):
    queue = []
    heapq.heappush(queue, (0, initial_point))
    distance_dict = dict()
    parent_dict = dict()
    found_answer = False
    distance_dict[initial_point] = 0
    while queue:
        if found_answer:
            break
        cost_curr_point = heapq.heappop(queue)
        curr_point = cost_curr_point[1]
        movements = points_to_consider_dict[curr_point]
        for move in movements:
            updated_point = get_updated_point(curr_point, move)
            prev_cost = distance_dict.get(curr_point)
            eval_cost = get_distance(method, curr_point, updated_point)
            curr_cost = prev_cost + eval_cost
            if ((distance_dict.get(updated_point) is None) or (distance_dict.get(updated_point) > curr_cost)) and \
                    check_valid(updated_point, matrix):
                parent_dict[updated_point] = curr_point
                distance_dict[updated_point] = curr_cost
                if compare_two_point(updated_point, final_point):
                    found_answer = True
                    break
                cost_value_for_checking = curr_cost
                if method == "A*":
                    cost_value_for_checking = cost_value_for_checking + get_heuristic_value(updated_point, final_point)
                heapq.heappush(queue, (cost_value_for_checking, updated_point))
    if found_answer:
        print_path(method, parent_dict, initial_point, final_point)
    else:
        f = open("output.txt", "a")
        f.write("FAIL")
        f.close()


def input_func():
    method = ""
    matrix_size = (0, 0, 0)
    initial_point = (0, 0, 0)
    final_point = (0, 0, 0)
    points_to_consider_dict = dict()

    line_num = 0
    point_number = 0
    input_file = open("input.txt", "r")

    for each_line in input_file:
        line_num = line_num + 1
        each_line = each_line.replace('\n', '', -1)
        each_line_arr = each_line.split(" ")
        if line_num == 1:
            method = each_line_arr[0]
        elif line_num == 2:
            matrix_size = (convert_into_point(each_line_arr))
        elif line_num == 3:
            initial_point = (convert_into_point(each_line_arr))
        elif line_num == 4:
            final_point = (convert_into_point(each_line_arr))
        elif line_num == 5:
            number_of_points_to_consider = int(each_line_arr[0])
        elif point_number < number_of_points_to_consider:
            point_number = point_number + 1
            movement_allowed = [int(movement_number) for movement_number in each_line_arr[3:]]
            point = (convert_into_point(each_line_arr))
            points_to_consider_dict[point] = movement_allowed
    input_file.close()
    return method, initial_point, final_point, matrix_size, points_to_consider_dict


if __name__ == '__main__':
    method, initial_point, final_point, matrix_size, points_to_consider_dict = input_func()
    if method == "BFS":
        bfs(method, matrix_size, initial_point, final_point, points_to_consider_dict)
    else:
        search_space(method, matrix_size, initial_point, final_point, points_to_consider_dict)
