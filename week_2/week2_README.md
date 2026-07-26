# 2차 과제 — Unit Test 및 2D → 3D 변환

## 무엇을 하는 폴더인가요?
pytest로 깊이 맵 생성 함수를 검증하고, 2D 이미지를 깊이감 있는 3D 좌표 데이터(포인트 클라우드)로 변환하는 코드입니다.

## 파일 구조
| 파일 | 역할 |
|---|---|
| `depth_to_3d.py` | 2D→3D 변환 코드. `load_image`(이미지 로드), `generate_depth_map`(흑백+컬러맵 깊이 맵 생성), `generate_point_cloud`(픽셀별 X,Y,Z 좌표 생성), `save_results`(결과 저장) 함수로 구성 |
| `unittest_3d.py` | `depth_to_3d.py`의 `generate_depth_map` 함수에 대한 Unit Test 3종 (출력 크기 / 타입 / 예외 처리 검증) |
| `kids.png` | 원본 테스트 이미지 |
| `kids_depth_map.png` | 깊이 맵 생성 결과 이미지 |
| `points_3d.npy` | 픽셀별 (X, Y, Z) 3D 좌표 데이터 (numpy 배열 저장 파일) |

## 실행 방법
```bash
pip install pytest opencv-python numpy

pytest unittest_3d.py -v
python depth_to_3d.py
```

## 핵심 로직 및 한계
- **깊이 맵**: 이미지를 흑백 변환 후, 밝기 값에 컬러맵(JET)을 입혀 깊이감을 시각적으로 표현
- **3D 포인트 클라우드**: 각 픽셀에 (X, Y, 밝기) 좌표를 부여해 3D 좌표 데이터 생성. 단, 이때 Z값은 실제 센서로 측정한 깊이가 아니라 **밝기 값을 깊이로 가정한 간이(pseudo) 방식**임 — 실제 서비스에서는 스테레오 카메라나 딥러닝 기반 깊이 추정 모델(MiDaS 등) 사용 필요
- **Unit Test**: 함수 단위로 크기/타입/예외 처리를 개별 테스트로 분리하여 실패 지점을 정확히 파악할 수 있도록 구성
