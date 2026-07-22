# Computer Vision

## Computer Vision course at UFSC
 
 A computer vision course taught during the first semester of 2026 at the Universidade Federal de Santa Catarina (UFSC), covering the study of neural networks and image processing using Python, OpenCV, NumPy, Matplotlib, TensorFlow, and YOLO.

## Fire and Smoke Project

Research of fire and smoke detection at the VISIA Computer Vision Laboratory (UFSC).

>model: https://huggingface.co/weslleyskah/fire_smoke_detection_box

>dataset: https://huggingface.co/datasets/weslleyskah/fire_smoke_dataset_fasdd_cv

### Detections

#### **Bounding Box**

>name: fire_smoke_box | model: yolo26n.pt | best map50 (box): 0.772 | dataset: fasdd_cv [article 1] [total:95k, fire(only):12.5k, smoke(only):23.3k, fire+smoke:20.1k, null:39.1k]

>parameters: epochs=100, imgsz=640, batch=256, workers=12, patience=30

| Original | Output |
| --- | --- |
| ![original](models/fire_smoke_box/fire_smoke_box-detections/notredame3_original.gif) | ![output](models/fire_smoke_box/fire_smoke_box-detections/notredame3.gif) |
| ![original](models/fire_smoke_box/fire_smoke_box-detections/notredame_original.gif) | ![output](models/fire_smoke_box/fire_smoke_box-detections/notredame.gif) |
| ![original](models/fire_smoke_box/fire_smoke_box-detections/wildfire_videos_0_original.gif) | ![output](models/fire_smoke_box/fire_smoke_box-detections/wildfire_videos_0.gif) |
| ![original](models/fire_smoke_box/fire_smoke_box-detections/wildfire_videos_1_original.gif) | ![output](models/fire_smoke_box/fire_smoke_box-detections/wildfire_videos_1.gif) |
| ![original](models/fire_smoke_box/fire_smoke_box-detections/wildfire_videos_2_original.gif) | ![output](models/fire_smoke_box/fire_smoke_box-detections/wildfire_videos_2.gif) |
| ![original](models/fire_smoke_box/fire_smoke_box-detections/wildfire_videos_3_original.gif) | ![output](models/fire_smoke_box/fire_smoke_box-detections/wildfire_videos_3.gif) |
| ![original](models/fire_smoke_box/fire_smoke_box-detections/urban_fire_0_original.jpg) | ![output](models/fire_smoke_box/fire_smoke_box-detections/urban_fire_0.jpg) |
| ![original](models/fire_smoke_box/fire_smoke_box-detections/urban_fire_1_original.jpg) | ![output](models/fire_smoke_box/fire_smoke_box-detections/urban_fire_1.jpg) |
| ![original](models/fire_smoke_box/fire_smoke_box-detections/urban_fire_2_original.jpg) | ![output](models/fire_smoke_box/fire_smoke_box-detections/urban_fire_2.jpg) |

#### **Segmentation**

>name: fire_smoke_seg | model:yolo26n-seg.pt | best map50 (box): 0.697, best map50 (mask): 0.595 | dataset: [article 2 + sam3]

>parameters: epochs=300, imgsz=640, batch=32, lr0=0.0005, lrf=0.01, cos_lr=True, warmup_epochs=1.0, mixup=0.15, copy_paste=0.3, mosaic=1.0 | roboflow aug: grayscale 15%, brightness: 10% 

| Original | Output |
| --- | --- |
| ![original](models/fire_smoke_seg/fire_smoke_seg-detections/notredame3_original.gif) | ![output](models/fire_smoke_seg/fire_smoke_seg-detections/notredame3.gif) |
| ![original](models/fire_smoke_seg/fire_smoke_seg-detections/notredame_original.gif) | ![output](models/fire_smoke_seg/fire_smoke_seg-detections/notredame.gif) |
| ![original](models/fire_smoke_seg/fire_smoke_seg-detections/wildfire_videos_0_original.gif) | ![output](models/fire_smoke_seg/fire_smoke_seg-detections/wildfire_videos_0.gif) |
| ![original](models/fire_smoke_seg/fire_smoke_seg-detections/wildfire_videos_1_original.gif) | ![output](models/fire_smoke_seg/fire_smoke_seg-detections/wildfire_videos_1.gif) |
| ![original](models/fire_smoke_seg/fire_smoke_seg-detections/wildfire_videos_2_original.gif) | ![output](models/fire_smoke_seg/fire_smoke_seg-detections/wildfire_videos_2.gif) |
| ![original](models/fire_smoke_seg/fire_smoke_seg-detections/wildfire_videos_3_original.gif) | ![output](models/fire_smoke_seg/fire_smoke_seg-detections/wildfire_videos_3.gif) |

## Articles

"An open flame and smoke detection dataset for deep learning in remote sensing based fire detection"

>[document](articles/An%20open%20flame%20and%20smoke%20detection%20dataset%20for%20deep%20learning%20in%20remote%20sensing%20based%20fire%20detection.pdf), [dataset](https://universe.roboflow.com/forestfiresmoke/fasdd_cv-dx83j)

"The Wildfire Dataset Enhancing Deep Learning-Based Forest Fire Detection" 

>[document](articles/Wildfire%20Dataset%20Enhancing%20Deep%20Learning-Based%20Forest%20Fire%20Detection.pdf), [dataset](https://www.kaggle.com/datasets/elmadafri/the-wildfire-dataset)

## Notes

> Use reliable datasets from articles with a balanced number of classes for fire, smoke and null images.

> Improve training with augmentations, parameters, and null-imgs.

> SAM3 / NVIDIA LocateAnything auto-label annotations are causing problems and false metrics.

**Dependencies**: uv, ultralytics yolo, google colab, tensorflow, opencv

**Datasets**: [roboflow](https://roboflow.com/), [open images v7](https://storage.googleapis.com/openimages/web/index.html), [aws open data](https://registry.opendata.aws/), [huggingface](https://huggingface.co/datasets)

**Annotations**: [CVAT](https://app.cvat.ai), roboflow

**Scripts**

>transform videos to gif
```bash
FOR %a IN (*.mp4 *.avi) DO ffmpeg -i "%a" -vf "fps=8,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=64[p];[s1][p]paletteuse=dither=none" -loop 0 "%~na.gif"
```

>push model and dataset to huggingface
```python
# uv venv
# uv pip install huggingface_hub
# uv run main.py
from huggingface_hub import login, upload_file, upload_folder

# Login
login()

# Push dataset
"""
upload_file(
    path_or_fileobj="FASDD_CV.zip",      # Your local file path
    path_in_repo="FASDD_CV.zip",         # The name the file will have on the Hub
    repo_id="weslleyskah/fasdd_cv",      # Your target repository
    repo_type="dataset"                  # Flagging it as a dataset repo
)
"""

# Push model
upload_folder(
    folder_path="fire_smoke_box", 
    repo_id="weslleyskah/fire_smoke_box", 
    repo_type="model"
)
```

---

## Structure
| Folder |  Description |
| --- | --- |
| neural_net/ | python code and books for NNs |
| image_processing/ | python code for image manipulation |
| models/ | trained models for fire and smoke detection |