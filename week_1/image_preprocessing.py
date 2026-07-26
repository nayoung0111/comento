from datasets import load_dataset
import cv2
import numpy as np
import os
import itertools


def load_sample_images(dataset_name="ethz/food101", n=5):
    """Hugging Face 데이터셋에서 이미지 n장을 스트리밍 방식으로 불러오는 함수"""
    dataset = load_dataset(dataset_name, split="train", streaming=True)
    samples = list(itertools.islice(dataset, n))
    print(f"{len(samples)}장 불러옴")
    return samples


def to_cv2_image(pil_image):
    """PIL 이미지를 OpenCV(numpy) 형식으로 변환하는 함수"""
    pil_image = pil_image.convert('RGB')
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)


def resize_image(image, size=(224, 224)):
    """이미지 크기를 통일하는 함수"""
    return cv2.resize(image, size)


def to_grayscale_normalized(image):
    """흑백 변환 및 0~1 정규화하는 함수"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    normalized = gray.astype(np.float32) / 255.0
    return gray, normalized


def remove_noise(image):
    """블러 필터로 노이즈를 제거하는 함수"""
    return cv2.GaussianBlur(image, (5, 5), 0)


def augment_image(image):
    """데이터 증강(반전, 회전, 색상 변화)을 적용하는 함수"""
    flipped = cv2.flip(image, 1)

    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 15, 1.0)
    rotated = cv2.warpAffine(image, rotation_matrix, (w, h))

    color_changed = cv2.convertScaleAbs(image, alpha=1.2, beta=20)

    return flipped, rotated, color_changed


def is_too_dark(image, threshold=50):
    """평균 밝기가 너무 낮으면(너무 어두운 사진) True 반환하는 함수"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.mean(gray) < threshold


def process_and_save(samples, output_dir="preprocessed_samples"):
    """전체 전처리 파이프라인을 실행하고 결과를 저장하는 함수"""
    os.makedirs(output_dir, exist_ok=True)

    for i, item in enumerate(samples):
        image = to_cv2_image(item['image'])
        resized = resize_image(image)

        if is_too_dark(resized):
            print(f"{i}번 사진: 너무 어두워서 제외함")
            continue

        gray, normalized = to_grayscale_normalized(resized)
        blurred = remove_noise(resized)
        flipped, rotated, color_changed = augment_image(resized)

        cv2.imwrite(f"{output_dir}/sample_{i}_resized.png", resized)
        cv2.imwrite(f"{output_dir}/sample_{i}_gray.png", gray)
        cv2.imwrite(f"{output_dir}/sample_{i}_blurred.png", blurred)
        cv2.imwrite(f"{output_dir}/sample_{i}_flipped.png", flipped)
        cv2.imwrite(f"{output_dir}/sample_{i}_rotated.png", rotated)
        cv2.imwrite(f"{output_dir}/sample_{i}_colorchanged.png", color_changed)

    print(f"전처리 완료! {output_dir} 폴더 확인해보세요.")


def main():
    """전체 과정을 실행하는 메인 함수"""
    samples = load_sample_images()
    process_and_save(samples)


if __name__ == "__main__":
    main()
