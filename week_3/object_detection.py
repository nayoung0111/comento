import cv2
from ultralytics import YOLO


def load_trained_model(weights_path="best.pt"):
    """학습된 YOLO 모델을 불러오는 함수"""
    return YOLO(weights_path)


def detect_objects(model, image_path):
    """이미지에서 객체를 탐지하는 함수"""
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"이미지를 불러올 수 없습니다: {image_path}")

    results = model(image)
    return image, results


def draw_boxes(image, results):
    """탐지된 객체에 박스와 이름을 그리는 함수"""
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = result.names[int(box.cls[0])]
            confidence = box.conf[0]

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                image, f"{label} ({confidence:.2f})", (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2
            )
    return image


def save_result(image, output_path="kids_detected.png"):
    """결과 이미지를 저장하는 함수"""
    cv2.imwrite(output_path, image)
    print(f"완료! {output_path} 저장됨")


def main():
    """전체 과정을 실행하는 메인 함수"""
    model = load_trained_model("best.pt")
    image, results = detect_objects(model, "kids.png")
    image_with_boxes = draw_boxes(image, results)
    save_result(image_with_boxes)


if __name__ == "__main__":
    main()
