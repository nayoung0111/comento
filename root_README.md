# 코멘토 직무부트캠프 — Computer Vision 팀 업무 과제

이 저장소는 코멘토 직무부트캠프에서 진행한 Computer Vision 실무 과제 모음입니다. 매주 하나씩 실무 시나리오 기반 과제를 수행하며, Git 협업 → 이미지 처리 → 코드 검증 → AI 모델링까지 단계적으로 실습했습니다.

## 폴더 구조

| 폴더 | 과제 주제 | 핵심 내용 |
|---|---|---|
| [`week_1/`](./week_1) | Git 활용 및 이미지 처리 | Git 브랜치/PR 워크플로우, OpenCV 빨간색 픽셀 필터링, Hugging Face 데이터셋 전처리 |
| [`week_2/`](./week_2) | Unit Test 및 2D→3D 변환 | pytest 기반 함수 검증, 깊이 맵(Depth Map) 생성 및 3D 포인트 클라우드 좌표 변환 |
| [`week_3/`](./week_3) | AI 모델링 및 결과 시각화 | YOLOv8 모델 학습(Google Colab), 객체 탐지, 성능 지표 시각화 |

각 폴더에는 실행 방법과 파일 구조를 설명하는 자체 README.md가 있습니다. 자세한 내용은 위 링크를 참고해주세요.

## 전체 기술 스택

- **언어/환경**: Python 3.x, Jupyter Notebook, Google Colab
- **이미지 처리**: OpenCV, NumPy
- **AI/딥러닝**: Ultralytics YOLOv8
- **테스트**: pytest
- **데이터셋**: Hugging Face Datasets (`ethz/food101`), coco128
- **버전 관리**: Git, GitHub (Branch → PR → Merge 워크플로우)

## 공통 작업 방식

- 매 과제마다 `feature/*` 브랜치를 생성해 작업 후 Pull Request를 통해 `master`로 병합
- 과제별로 폴더를 분리하고, 재사용 가능한 함수 단위로 코드를 구성
- 폴더별 README에 실행 방법과 결과물을 문서화하여, 코드를 직접 열어보지 않아도 구조를 파악할 수 있도록 정리
