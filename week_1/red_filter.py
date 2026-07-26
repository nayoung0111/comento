import cv2
import numpy as np


def load_image(path):
    """이미지 파일을 불러오는 함수"""
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"이미지를 불러올 수 없습니다: {path}")
    return image


def filter_red(image):
    """이미지에서 빨간색 영역만 필터링하는 함수"""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    result = cv2.bitwise_and(image, image, mask=mask)
    return result


def save_image(image, path):
    """결과 이미지를 저장하는 함수"""
    cv2.imwrite(path, image)
    print(f"완료! {path} 파일로 저장됐어요.")


def main():
    """전체 과정을 실행하는 메인 함수"""
    image = load_image('kids.png')
    result = filter_red(image)
    save_image(result, 'kids_red_filtered.png')


if __name__ == "__main__":
    main()
