# 1차 과제: Git 활용 및 이미지 처리

## 개발 환경
- Python 3.x

## 설치 방법

아래 명령어로 필요한 패키지를 설치하세요.

```bash
pip install opencv-python numpy datasets pillow
```

## 실행 방법

### 1. 빨간색 픽셀 필터링
```bash
python red_filter.py
```
- `kids.png` 이미지에서 빨간색 영역만 감지해 필터링합니다.
- 실행 결과: `kids_red_filtered.png` 파일이 생성됩니다.

### 2. Hugging Face 데이터셋 전처리
```bash
python image_preprocessing.py
```
- Hugging Face의 `ethz/food101` 데이터셋에서 이미지 5장을 스트리밍 방식으로 불러와 전처리합니다.
- 전처리 내용: 크기 조정(224x224), Grayscale/Normalize, Blur, 데이터 증강(반전/회전/색상 변화), 어두운 이미지 필터링
- 실행 결과: `preprocessed_samples/` 폴더에 처리된 이미지들이 저장됩니다.

## 결과물
| 파일/폴더 | 설명 |
|---|---|
| `red_filter.py` | 빨간색 픽셀 필터링 코드 |
| `kids_red_filtered.png` | 필터링 결과 이미지 |
| `image_preprocessing.py` | Hugging Face 데이터셋 전처리 코드 |
| `preprocessed_samples/` | 전처리된 이미지 결과 (5장 × 6종 변형) |



# 2차 과제: Unit Test 및 2D → 3D 변환

## 실행 방법
```bash
pytest unittest_3d.py -v
python depth_to_3d.py
```

## 결과물
| 파일 | 설명 |
|---|---|
| `unittest_3d.py` | 깊이 맵 생성 함수에 대한 Unit Test (3개 테스트) |
| `depth_to_3d.py` | 2D 이미지를 깊이 맵(3D 느낌)으로 변환하는 코드 |
| `kids_depth_map.png` | 변환 결과 이미지 |
