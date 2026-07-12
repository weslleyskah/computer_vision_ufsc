# Computer Vision

### [Fire detection](#fire-detection-1)

Research of fire and smoke detection at the VISIA Computer Vision Laboratory (UFSC).

### [Computer Vision course at UFSC](#computer-vision-course-at-ufsc-1)
 
 A computer vision course taught during the first semester of 2026 at the Universidade Federal de Santa Catarina (UFSC), covering the study of neural networks and image processing using Python, OpenCV, NumPy, Matplotlib, TensorFlow, and YOLO.

## Fire Detection

### Detections

| Original | Output |
| --- | --- |
| ![Wildfire Detection Model](data/slides/detections/wildfire_original_video_0.gif) | ![Wildfire Detection Model](data/slides/detections/wildfire_video_0.gif) |
| ![Wildfire Detection Model](data/slides/detections/wildfire_original_video_1.gif) | ![Wildfire Detection Model](data/slides/detections/wildfire_video_1.gif) |
| ![Wildfire Detection Model](data/slides/detections/wildfire_original_video_2.gif) | ![Wildfire Detection Model](data/slides/detections/wildfire_video_2.gif) |

>fireseg_v3.pt

### Datasets

> Combine datasets (fire+smoke) and annotate smokes so the model won't forget.

> Improve training with nofire environments without labels on the background.

**Datasets**: [dataset I](https://universe.roboflow.com/roboflow-universe-projects/fire-and-smoke-segmentation), [dataset II](https://universe.roboflow.com/uzai-kha-s-workspace/forest_fire-aggsg), [dataset III](https://etsin.fairdata.fi/dataset/1dce1023-493a-4d63-a906-f2a44f831898/data)

**Articles**

The Wildfire Dataset Enhancing Deep Learning-Based Forest Fire Detection: [article](https://www.mdpi.com/1999-4907/14/9/1697),  [document](articles/Wildfire%20Dataset%20Enhancing%20Deep%20Learning-Based%20Forest%20Fire%20Detection.pdf), [dataset](https://www.kaggle.com/datasets/elmadafri/the-wildfire-dataset)

A Small Target Forest Fire Detection Model Based on YOLOv5 Improvement: [article](https://www.mdpi.com/1999-4907/13/8/1332)

A Small-Target Forest Fire Smoke Detection Model Based on Deformable Transformer for End-to-End Object Detection: [article](https://www.mdpi.com/1999-4907/14/1/162)

---

### Notes

**Dependencies**: [uv](https://github.com/astral-sh/uv), [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html), ultralytics

**Dataset sites**: [roboflow](https://roboflow.com/), [open images v7](https://storage.googleapis.com/openimages/web/index.html), [aws open data](https://registry.opendata.aws/), [huggingface](https://huggingface.co/datasets)

**Annotations**: [CVAT](https://app.cvat.ai), roboflow

---

### Setup

```bash
uv venv
uv pip install ultralytics
uv run src/main.py
```

## Computer Vision course at UFSC

## Part I: Images

### Setup

```bash
cd project_folder
uv venv
uv pip install -r requirements.txt
uv run main.py
```

**Dependencies**: [uv](https://github.com/astral-sh/uv), [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html), [numpy](https://github.com/numpy/numpy)

---

## Part II: Neural Nets

**Datasets**: [roboflow](https://roboflow.com/), [open images v7](https://storage.googleapis.com/openimages/web/index.html), [aws open data](https://registry.opendata.aws/), [huggingface](https://huggingface.co/datasets), [fashion-mnist](https://github.com/zalandoresearch/fashion-mnist)

**Dependencies**: [google colab](https://colab.research.google.com/), [tensorflow](https://github.com/tensorflow/tensorflow), [matplotlib](https://github.com/matplotlib/matplotlib)

## Structure
| Folder |  Description |
| --- | --- |
| neural_net/ | part II: python code and books for NNs |
| image_processing/ | part I: python code for image manipulation |
| train/ | models, datasets and notebooks |