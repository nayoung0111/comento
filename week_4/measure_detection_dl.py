import cv2
from ultralytics import YOLO


def load_trained_model(weights_path="best.pt"):
    """학습된 마디 탐지 YOLO 모델을 불러오는 함수"""
    return YOLO(weights_path)


def detect_measures(model, image_path, conf=0.015, imgsz=1024):
    """이미지에서 마디를 탐지하는 함수.

    conf=0.015: 여러 차례 튜닝을 통해 실제 마디 수에 가장 근접하다고 확인된 신뢰도 기준.
    imgsz=1024: 학습 시 사용한 해상도와 동일하게 맞춰야 탐지가 안정적임 (더 키우면 중복 탐지 발생).
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"이미지를 불러올 수 없습니다: {image_path}")

    results = model(image, conf=conf, imgsz=imgsz, verbose=False)
    return image, results


def draw_measure_boxes(image, results):
    """탐지된 마디에 번호와 박스를 그리는 함수"""
    result_image = image.copy()
    for result in results:
        for i, box in enumerate(result.boxes):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = box.conf[0]

            cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                result_image, f"#{i + 1}", (x1 + 4, y1 + 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2
            )
    return result_image


def count_measures(results):
    """탐지된 마디 개수를 세는 함수"""
    return sum(len(result.boxes) for result in results)


def save_result(image, output_path):
    """결과 이미지를 jpg로 저장하는 함수"""
    cv2.imwrite(output_path, image, [cv2.IMWRITE_JPEG_QUALITY, 95])
    print(f"완료! {output_path} 저장됨")


def analyze_sheet(model, image_path, output_path, conf=0.015):
    """전체 과정을 실행하는 함수: 마디 탐지 -> 박스 표시 -> jpg 저장"""
    image, results = detect_measures(model, image_path, conf=conf)
    result_image = draw_measure_boxes(image, results)
    save_result(result_image, output_path)

    measure_count = count_measures(results)
    print(f"{image_path}: 감지된 마디 수 = {measure_count}개 (conf={conf})")
    return measure_count


def main():
    """학습된 모델(best.pt)로 실제 악보 샘플들을 최종 설정(conf=0.015)으로 분석"""
    model = load_trained_model("best.pt")
    analyze_sheet(model, "sheet_sample_01.jpg", "sheet_sample_01_final.jpg")
    analyze_sheet(model, "sheet_sample_02.jpg", "sheet_sample_02_final.jpg")


if __name__ == "__main__":
    main()
