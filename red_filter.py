#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np

# 이미지 로드
image = cv2.imread('kids.png')


# In[3]:


# 이미지가 제대로 불러와졌는지 확인
if image is None:
    print("이미지를 불러올 수 없습니다. 파일 이름과 위치를 확인하세요.")
else:
    # BGR에서 HSV 색상 공간으로 변환
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 빨간색 범위 지정 (빨간색은 색상환 양쪽 끝에 걸쳐 있어서 범위 2개 필요)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # 마스크 생성 (빨간색인 부분만 흰색, 나머지는 검은색인 흑백 이미지)
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # 원본 이미지에서 빨간색 부분만 추출
    result = cv2.bitwise_and(image, image, mask=mask)

    # 결과 이미지 출력
    cv2.imshow('Original', image)
    cv2.imshow('Red Filtered', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 결과 이미지 파일로 저장
    cv2.imwrite('kids_red_filtered.png', result)
    print("완료! kids_red_filtered.png 파일로 저장됐어요.")


# In[ ]:




