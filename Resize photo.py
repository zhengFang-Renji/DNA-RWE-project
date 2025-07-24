from PIL import Image
import numpy as np
from skimage.filters import threshold_otsu

def load_and_preprocess_image(path, size=(12, 12)):
    img = Image.open(path).convert('L')  # 转灰度
    original = np.array(img)
    img_resized = img.resize(size, Image.BILINEAR)
    resized_np = np.array(img_resized) / 255.0
    return original, resized_np

def binarize_image(image, output_txt=None):
    thresh = threshold_otsu(image)
    binary = (image > thresh).astype(int)
    
    # 修正这里的缩进
    print("\n二值化结果预览：")  # 这里需要与上一行缩进对齐
    for row in binary:
        print("".join(str(x) for x in row))
    
    if output_txt:
        np.savetxt(output_txt, binary, fmt='%d', delimiter='')
        print(f"\n文件已保存至：{output_txt}")
    
    return binary

if __name__ == "__main__":
    _, processed_img = load_and_preprocess_image()
    binary_result = binarize_image(processed_img, output_txt=)