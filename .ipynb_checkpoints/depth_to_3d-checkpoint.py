import cv2
import numpy as np

# 이미지 로드 (kids.png 사용)
image = cv2.imread('kids.png')

if image is None:
    print("이미지를 불러올 수 없습니다.")
else:
    # 그레이스케일 변환 (밝기 정보만 남기기 → 이걸 "깊이"로 씀)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 깊이 맵 생성 (밝기에 따라 색을 입혀서 입체감 표현)
    depth_map = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    # 결과 저장
    cv2.imwrite('kids_depth_map.png', depth_map)
    print("완료! kids_depth_map.png 저장됨")

    # --- 심화: 3D 포인트 클라우드 좌표 생성 ---
    h, w = depth_map.shape[:2]
    X, Y = np.meshgrid(np.arange(w), np.arange(h))
    Z = gray.astype(np.float32)  # 밝기 값을 깊이(Z축)로 사용

    points_3d = np.dstack((X, Y, Z))
    print(f"3D 좌표 생성 완료! 형태: {points_3d.shape}")