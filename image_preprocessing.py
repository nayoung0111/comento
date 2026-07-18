#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install datasets pillow opencv-python numpy


# In[1]:


from datasets import load_dataset
import cv2
import numpy as np
import os
import itertools

# 스트리밍 방식: 전체 다운로드 없이 필요한 5장만 가져오기
dataset = load_dataset("ethz/food101", split="train", streaming=True)
samples = list(itertools.islice(dataset, 5))
print(f"{len(samples)}장 불러옴")

os.makedirs("preprocessed_samples", exist_ok=True)

def is_too_dark(image, threshold=50):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.mean(gray) < threshold

for i, item in enumerate(samples):
    pil_image = item['image'].convert('RGB')
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    # ① 크기 조정
    resized = cv2.resize(image, (224, 224))

    # ② Grayscale + Normalize
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    normalized = gray.astype(np.float32) / 255.0

    # ③ 노이즈 제거 (Blur)
    blurred = cv2.GaussianBlur(resized, (5, 5), 0)

    # ④ 데이터 증강
    flipped = cv2.flip(resized, 1)
    center = (112, 112)
    rotation_matrix = cv2.getRotationMatrix2D(center, 15, 1.0)
    rotated = cv2.warpAffine(resized, rotation_matrix, (224, 224))
    color_changed = cv2.convertScaleAbs(resized, alpha=1.2, beta=20)

    # 이상치 탐지: 너무 어두운 사진 제외
    if is_too_dark(resized):
        print(f"{i}번 사진: 너무 어두워서 제외함")
        continue

    cv2.imwrite(f"preprocessed_samples/sample_{i}_resized.png", resized)
    cv2.imwrite(f"preprocessed_samples/sample_{i}_gray.png", gray)
    cv2.imwrite(f"preprocessed_samples/sample_{i}_blurred.png", blurred)
    cv2.imwrite(f"preprocessed_samples/sample_{i}_flipped.png", flipped)
    cv2.imwrite(f"preprocessed_samples/sample_{i}_rotated.png", rotated)
    cv2.imwrite(f"preprocessed_samples/sample_{i}_colorchanged.png", color_changed)

print("전처리 완료! preprocessed_samples 폴더 확인해보세요.")


# In[ ]:




