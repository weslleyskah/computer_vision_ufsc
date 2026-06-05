# Computer Vision

### [Fire detection](#fire-detection)

Researching fire and smoke detection methods at the VISIA Computer Vision Laboratory (UFSC).

### [Computer Vision course at UFSC](#computer-vision-course-at-ufsc)
 
 A computer vision course taught during the first semester of 2026 at the Universidade Federal de Santa Catarina (UFSC), covering the study of neural networks and image processing using Python, OpenCV, NumPy, Matplotlib, TensorFlow, and YOLO.

## Fire Detection

### Detections

Version 2

![Wildfire Detection Model](train/data/output/fire_dataset/v2/wildfire_video_60.gif)

![Wildfire Detection Model](train/data/output/fire_dataset/v2/wildfire_video_61.gif)

![Wildfire Detection Model](train/data/output/fire_dataset/v2/wildfire_video_63.gif)

![Wildfire Detection Model](train/data/output/fire_dataset/v2/wildfire_video_67.gif)

![Wildfire Detection Model](train/data/output/fire_dataset/v2/wildfire_video_76.gif)

![Wildfire Detection Model](train/data/output/fire_dataset/v2/wildfire_video_58.gif)

Version 3

![Wildfire Detection Model](train/data/output/fire_dataset/v3/wildfire_video_60.gif)

### Datasets

>Combine datasets (fire+smoke) and annotate smokes so the model won't forget. 

- Wildfire Images: [dataset I](https://universe.roboflow.com/roboflow-universe-projects/fire-and-smoke-segmentation), [dataset II](https://universe.roboflow.com/uzai-kha-s-workspace/forest_fire-aggsg)

- Wildfire Videos: [dataset I](https://www.kaggle.com/datasets/weslleyskah/wildfire-dataset)

### Notes

| Dependencies |  |
| --- | --- |
| [uv](https://github.com/astral-sh/uv) | Python package manager |
| [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) | Image manipulation |
| ultralytics | Detection with YOLO |

| Datasets |  |
| --- | --- |
| Sites | [roboflow](https://roboflow.com/), [open images v7](https://storage.googleapis.com/openimages/web/index.html), [aws open data](https://registry.opendata.aws/), [huggingface](https://huggingface.co/datasets), kaggle, flickr |
| Annotations | [CVAT](https://app.cvat.ai) |

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
uv pip install -r requirements.txt # uv pip sync requirements.txt
uv run main.py
```

| Dependencies |  |
| --- | --- |
| [uv](https://github.com/astral-sh/uv) | Python package manager |
| [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) | Image manipulation |
| [numpy](https://github.com/numpy/numpy) | Array manipulation |

## Part II: Neural Nets

| Datasets |  |
| --- | --- |
| Sites | [roboflow](https://roboflow.com/), [open images v7](https://storage.googleapis.com/openimages/web/index.html), [aws open data](https://registry.opendata.aws/), [huggingface](https://huggingface.co/datasets) |
| Dataset I | [fashion-mnist](https://github.com/zalandoresearch/fashion-mnist) |

| Dependencies |  |
| --- | --- |
| [google colab](https://colab.research.google.com/) | Environment |
| [tensorflow](https://github.com/tensorflow/tensorflow) | Model library |
| [matplotlib](https://github.com/matplotlib/matplotlib) | Graphics |

## Structure
| Folder |  Description |
| --- | --- |
| neural_net/ | part II: python code and books for NNs |
| image_processing/ | part I: python code for image manipulation |
| train/ | models, datasets and notebooks |