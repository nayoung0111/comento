# 1차 업무 과제

## 1. Git 활용
- GitHub 저장소 생성 및 로컬 환경 연동
- `feature/image-processing` 브랜치 생성 후 작업
- 커밋 및 푸시 후 Pull Request 생성

## 2. 픽셀 단위 이미지 처리 (red_filter.py)
- OpenCV를 사용해 `kids.png` 이미지에서 빨간색 영역만 감지 및 필터링
- HSV 색상 공간으로 변환 후 빨간색 범위를 마스킹하여 추출
- 결과: `kids_red_filtered.png`로 저장

## 3. Hugging Face 데이터셋 전처리 (추가 요청)
- `ethz/food101` 데이터셋에서 이미지 5장을 스트리밍 방식으로 불러옴
- 전처리 내용:
  - 크기 조정 (224x224)
  - Grayscale 변환 및 Normalize
  - Blur 필터로 노이즈 제거
  - 데이터 증강 (좌우 반전, 회전, 색상 변화)
  - 심화: 평균 밝기가 너무 낮은(어두운) 이미지는 제외 처리
- 결과: `preprocessed_samples/`