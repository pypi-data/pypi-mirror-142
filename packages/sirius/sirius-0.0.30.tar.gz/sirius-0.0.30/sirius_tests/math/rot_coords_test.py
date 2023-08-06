import numpy as np
from sirius._sirius_utils._math_utils import mat_dis
from sirius._sirius_utils._coord_transforms import _compute_rot_coords, _rot_coord

def test_mat_dis():
    A = np.array([np.linspace(0, 4, 4), np.linspace(0, 4, 4)])
    B = np.array([np.linspace(0, 4, 4)+1, np.linspace(0, 4, 4)+1])
    assert np.allclose(np.sum(np.abs(A-B)), mat_dis(A, B))
    
def test_rot_coord():
    assert np.allclose(_rot_coord(1, 2, 2), (1.402448017104221, -1.7415910999199666))
    
def test_compute_rot_coords():
    assert np.allclose((np.array([[-1.97260236, -0.15400751,  1.66458735,  3.4831822 ,  5.30177705],
        [-2.80489603, -0.98630118,  0.83229367,  2.65088853,  4.46948338],
        [-3.63718971, -1.81859485,  0.        ,  1.81859485,  3.63718971],
        [-4.46948338, -2.65088853, -0.83229367,  0.98630118,  2.80489603],
        [-5.30177705, -3.4831822 , -1.66458735,  0.15400751,  1.97260236]]),
 np.array([[ 5.30177705,  4.46948338,  3.63718971,  2.80489603,  1.97260236],
        [ 3.4831822 ,  2.65088853,  1.81859485,  0.98630118,  0.15400751],
        [ 1.66458735,  0.83229367, -0.        , -0.83229367, -1.66458735],
        [-0.15400751, -0.98630118, -1.81859485, -2.65088853, -3.4831822 ],
        [-1.97260236, -2.80489603, -3.63718971, -4.46948338, -5.30177705]])), _compute_rot_coords(np.array([5, 5]), np.array([2, 2]), 2))

