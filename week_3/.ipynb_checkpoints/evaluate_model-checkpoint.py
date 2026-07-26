import matplotlib.pyplot as plt
from ultralytics import YOLO


def load_model(model_name="yolov8n.pt"):
    """YOLO 모델을 불러오는 함수"""
    return YOLO(model_name)


def evaluate_model(model):
    """모델 성능(정확도 등)을 평가하는 함수"""
    metrics = model.val()
    return metrics


def plot_performance(metrics, save_path="model_performance.png"):
    """평가 결과를 그래프로 그려서 저장하는 함수"""
    labels = ["mAP50", "mAP50-95", "Precision", "Recall"]
    values = [
        metrics.box.map50,
        metrics.box.map,
        metrics.box.mp,
        metrics.box.mr,
    ]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color="skyblue")
    plt.ylim(0, 1)
    plt.title("YOLO Model Performance")
    plt.ylabel("Score")
    plt.savefig(save_path)
    print(f"완료! {save_path} 저장됨")


def main():
    """전체 과정을 실행하는 메인 함수"""
    model = load_model()
    metrics = evaluate_model(model)
    plot_performance(metrics)


if __name__ == "__main__":
    main()