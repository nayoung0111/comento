import numpy as np
import cv2
import pytest


def generate_depth_map(image):
    """사진을 받아서 깊이감 있는 이미지(depth map)로 바꿔주는 함수"""
    if image is None:
        raise ValueError("입력된 이미지가 없습니다.")
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    depth_map = cv2.applyColorMap(grayscale, cv2.COLORMAP_JET)
    return depth_map


def test_generate_depth_map_shape():
    """결과 이미지 크기가 원본이랑 같은지 확인"""
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    depth_map = generate_depth_map(image)
    assert depth_map.shape == image.shape, "출력 크기가 입력 크기와 다릅니다."


def test_generate_depth_map_type():
    """결과가 numpy 배열 형태로 잘 나오는지 확인"""
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    depth_map = generate_depth_map(image)
    assert isinstance(depth_map, np.ndarray), "출력 데이터 타입이 ndarray가 아닙니다."


def test_generate_depth_map_none_input():
    """이미지가 없을 때(None) 에러를 잘 내는지 확인"""
    with pytest.raises(ValueError):
        generate_depth_map(None)