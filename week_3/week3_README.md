# 3차 과제 — AI 기반 데이터 모델링 및 OpenCV 결과 시각화

YOLOv8 모델을 coco128 데이터셋으로 직접 학습시키고, 학습된 모델로 이미지 속 객체를 탐지·시각화하는 코드입니다. (모델 학습 및 평가는 Google Colab의 GPU 환경에서 진행)

## 파일 구조

|파일|역할|
|-|-|
|`colab\\\_train\\\_evaluate.py`|(Colab에서 실행) YOLOv8n 모델을 coco128 데이터셋으로 학습시키고, 성능을 평가·시각화하는 코드|
|`object\\\_detection.py`|학습된 모델(`best.pt`)로 이미지에서 객체를 탐지하고 박스를 그리는 코드 (로컬 환경 실행). `load\\\_trained\\\_model`, `detect\\\_objects`, `draw\\\_boxes`, `save\\\_result` 함수로 구성|
|`best.pt`|Colab에서 학습 완료된 YOLO 모델 가중치 파일|
|`kids.png`|원본 테스트 이미지|
|`kids\\\_detected.png`|객체 탐지 결과 이미지 (박스 및 라벨 표시)|
|`model\\\_performance.png`|모델 성능 지표(Precision, Recall, mAP50, mAP50-95) 시각화 그래프|

## 실행 방법

### 1\. 모델 학습 및 평가 (Google Colab, GPU 환경 권장)

`colab\\\_train\\\_evaluate.py`의 코드를 Colab 노트북 셀에 붙여넣어 실행합니다.

```python
!pip install ultralytics
```

학습 완료 후 `runs/detect/train/weights/best.pt` 파일과 `model\\\_performance.png`를 다운로드하여 본 폴더에 저장합니다.

### 2\. 객체 탐지 (로컬 환경)

```bash
pip install opencv-python ultralytics
python object\\\_detection.py
```

## 성능 평가 결과

|지표|값|
|-|-|
|Precision|0.752|
|Recall|0.645|
|mAP50|0.728|
|mAP50-95|0.561|

## 참고 사항

* 학습·평가는 GPU 연산이 필요해 로컬 대신 Google Colab에서 진행했습니다.
* coco128은 YOLO 공식 튜토리얼에서 제공하는 소규모(128장) 벤치마크 데이터셋으로, person/car/dog 등 80종의 일반 객체 클래스를 포함합니다.
* 학습 과정에서 생성된 데이터셋 원본(`datasets/`), 학습 로그(`runs/`), 학습 전 기본 모델(`yolov8n.pt`)은 용량 및 관리 편의를 위해 저장소에서 제외했습니다.

