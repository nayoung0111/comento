# 1차 과제 — Git 활용 및 이미지 처리
OpenCV로 이미지에서 빨간색 픽셀을 감지·필터링하고, Hugging Face 데이터셋을 AI 학습용으로 전처리하는 코드입니다.

## 파일 구조
| 파일/폴더 | 역할 |
|---|---|
| `red_filter.py` | 빨간색 필터링 코드. `load_image`(이미지 로드), `filter_red`(HSV 마스킹으로 빨간색 추출), `save_image`(결과 저장) 함수로 구성 |
| `image_preprocessing.py` | Hugging Face 이미지 전처리 코드. 크기 조정, 흑백/정규화, 블러, 데이터 증강, 어두운 이미지 필터링 함수로 구성 |
| `kids.png` | 원본 테스트 이미지 |
| `kids_red_filtered.png` | `red_filter.py` 실행 결과 (빨간색만 추출된 이미지) |
| `preprocessed_samples/` | `image_preprocessing.py` 실행 결과 (이미지 5장 × 6종 변형) |

## 실행 방법
```bash
pip install opencv-python numpy datasets pillow

python red_filter.py
python image_preprocessing.py
```

## 핵심 로직
- **빨간색 필터링**: BGR → HSV 색공간 변환 후, 빨간색이 걸쳐있는 두 범위(0~10°, 170~180°)를 각각 마스킹하여 합산, 원본과 합성(`bitwise_and`)
- **데이터 전처리**: 224×224 크기 통일 → Grayscale/Normalize → GaussianBlur → 반전/회전/색상 변화 증강 → 평균 밝기 기준 이상치(너무 어두운 이미지) 제거
