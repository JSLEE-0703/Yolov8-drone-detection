import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# 加载训练好的最优模型
model = YOLO(r"D:\WY\runs\detect\train12\weights\best.pt")

# 设置页面标题
st.title("YOLOv8 Detection")

# 上传图片
uploaded_file = st.file_uploader("Update a file with drone", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 打开上传的图片
    image = Image.open(uploaded_file)

    # 进行目标检测
    results = model.predict(image)

    # 获取检测结果
    r = results[0]
    img_array = r.plot()

    # 将NumPy数组转换为PIL图像
    result_image = Image.fromarray(img_array)

    # 显示检测结果
    st.image(result_image, caption='result', use_column_width=True)
    