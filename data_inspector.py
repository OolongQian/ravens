import os
import pickle
import cv2


if __name__ == '__main__':
    folder = './rearrangement-train/color/000001-2.pkl'
    with open(folder, 'rb') as f:
        tmp = pickle.load(f)
    for i in range(3):
        img = tmp[i, 0, ...]
        cv2.imshow('haha', img)
        cv2.waitKey(0)
