import cv2
import numpy as np


def load_image(path):
    """이미지 파일을 불러오는 함수"""
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"이미지를 불러올 수 없습니다: {path}")
    return image


def generate_depth_map(image):
    """이미지를 흑백으로 바꾼 뒤 밝기 기반 깊이 맵(컬러맵)을 생성하는 함수"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    depth_map = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    return gray, depth_map


def generate_point_cloud(gray):
    """흑백 이미지의 밝기 값을 깊이(Z)로 사용해 (X, Y, Z) 3D 좌표를 생성하는 함수"""
    h, w = gray.shape[:2]
    X, Y = np.meshgrid(np.arange(w), np.arange(h))
    Z = gray.astype(np.float32)  # 밝기 값을 깊이(Z축)로 사용
    points_3d = np.dstack((X, Y, Z))
    return points_3d


def save_results(depth_map, points_3d, depth_path="kids_depth_map.png", points_path="points_3d.npy"):
    """깊이 맵 이미지와 3D 좌표 데이터를 각각 저장하는 함수"""
    cv2.imwrite(depth_path, depth_map)
    print(f"완료! {depth_path} 저장됨")

    np.save(points_path, points_3d)
    print(f"3D 좌표 저장 완료! 형태: {points_3d.shape} → {points_path}")

    # 참고용으로 일부 좌표값 출력 (X, Y, Z)
    print("샘플 좌표 (0,0) 위치의 (X, Y, Z):", points_3d[0, 0])
    print("샘플 좌표 (중앙) 위치의 (X, Y, Z):", points_3d[points_3d.shape[0] // 2, points_3d.shape[1] // 2])


def main():
    """전체 과정을 실행하는 메인 함수"""
    image = load_image('kids.png')
    gray, depth_map = generate_depth_map(image)
    points_3d = generate_point_cloud(gray)
    save_results(depth_map, points_3d)


if __name__ == "__main__":
    main()
