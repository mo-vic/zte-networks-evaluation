# -*- coding:utf8 -*-
import os
import numpy as np


def remove_file(one_data):
    result_file = os.path.join(one_data, "result.txt")
    if os.path.exists(result_file):
        os.remove(result_file)


def fetch_data(one_data):
    result_list = []
    result_file = os.path.join(one_data, "result.txt")

    with open(result_file, "r") as f:
        for line in f:
            path, value = line.split(':')
            value = int(value.strip())
            result_list.append(value)

    return result_list


def evaluate():
    data_path = "../data"
    gt_path = "../gt"

    data_list = os.listdir(data_path)
    gt_list = os.listdir(gt_path)

    result_list = []
    for one_data, one_gt in zip(data_list, gt_list):
        assert one_data.replace("data", "gt") == one_gt
        path_result = fetch_data(os.path.join(data_path, one_data))
        gt_result = fetch_data(os.path.join(gt_path, one_gt))

        gt_result = np.array(gt_result)
        path_result = np.array(path_result)

        ret = np.mean(np.maximum(0, 1.0 - np.abs(path_result - gt_result) / np.maximum(1e-4, gt_result)))
        result_list.append(ret.item())

    print("Your score is: ", np.mean(result_list).item())


def main():
    data_path = "../data"
    data_list = os.listdir(data_path)
    for one_data in data_list:
        remove_file(os.path.join(data_path, one_data))

    os.system("python main.py")

    evaluate()


if __name__ == "__main__":
    main()
