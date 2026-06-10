# Computer Vision

### [Fire detection](#fire-detection-1)

Research of fire and smoke detection at the VISIA Computer Vision Laboratory (UFSC).

### [Computer Vision course at UFSC](#computer-vision-course-at-ufsc-1)
 
 A computer vision course taught during the first semester of 2026 at the Universidade Federal de Santa Catarina (UFSC), covering the study of neural networks and image processing using Python, OpenCV, NumPy, Matplotlib, TensorFlow, and YOLO.

## Fire Detection

### Detections

Version 2

| | |
| --- | --- |
| ![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_original_video_60.gif) | ![Wildfire Detection Model](train/data/output/fire_dataset/v2/wildfire_video_60.gif) |
| ![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_original_video_61.gif) | ![Wildfire Detection Model](train/data/output/fire_dataset/v2/wildfire_video_61.gif) |

Version 3
>Only fire, the model forgot the smoke!

| | |
| --- | --- |
| ![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_original_video_4.gif) | ![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_video_4.gif) |
| ![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_original_video_26.gif) | ![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_video_26.gif) |
| ![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_original_video_24.gif) | ![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_video_24.gif) |
| ![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_original_video_76.gif) | ![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_video_76.gif) |

### Datasets

> Combine datasets (fire+smoke) and annotate smokes so the model won't forget.

> Improve training with nofire environments without labels on the background.

**Wildfire Images** — [dataset I](https://universe.roboflow.com/roboflow-universe-projects/fire-and-smoke-segmentation) · [dataset II](https://universe.roboflow.com/uzai-kha-s-workspace/forest_fire-aggsg)

---

### Notes

**Dependencies** — [uv](https://github.com/astral-sh/uv) · [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) · ultralytics

**Dataset sites** — [roboflow](https://roboflow.com/) · [open images v7](https://storage.googleapis.com/openimages/web/index.html) · [aws open data](https://registry.opendata.aws/) · [huggingface](https://huggingface.co/datasets)

**Annotations** — [CVAT](https://app.cvat.ai), roboflow

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

**Dependencies** — [uv](https://github.com/astral-sh/uv) · [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) · [numpy](https://github.com/numpy/numpy)

---

## Part II: Neural Nets

**Datasets** — [roboflow](https://roboflow.com/) · [open images v7](https://storage.googleapis.com/openimages/web/index.html) · [aws open data](https://registry.opendata.aws/) · [huggingface](https://huggingface.co/datasets) · [fashion-mnist](https://github.com/zalandoresearch/fashion-mnist)

**Dependencies** — [google colab](https://colab.research.google.com/) · [tensorflow](https://github.com/tensorflow/tensorflow) · [matplotlib](https://github.com/matplotlib/matplotlib)

## Structure
| Folder |  Description |
| --- | --- |
| neural_net/ | part II: python code and books for NNs |
| image_processing/ | part I: python code for image manipulation |
| train/ | models, datasets and notebooks |