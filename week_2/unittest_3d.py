import numpy as np
import pytest
from depth_to_3d import generate_depth_map


def test_generate_depth_map_shape():
    """결과 이미지 크기가 원본이랑 같은지 확인"""
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    gray, depth_map = generate_depth_map(image)
    assert depth_map.shape == image.shape, "출력 크기가 입력 크기와 다릅니다."


def test_generate_depth_map_type():
    """결과가 numpy 배열 형태로 잘 나오는지 확인"""
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    gray, depth_map = generate_depth_map(image)
    assert isinstance(depth_map, np.ndarray), "출력 데이터 타입이 ndarray가 아닙니다."


def test_generate_depth_map_none_input():
    """이미지가 없을 때(None) 에러를 잘 내는지 확인"""
    with pytest.raises(Exception):
        generate_depth_map(None)
