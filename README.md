# Computer Vision at UFSC

Computer Vision course at UFSC using Python, OpenCV, Numpy, Matplotlib and Tensorflow.


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
| [Google Colab](https://colab.research.google.com/) | Environment |
| [tensorflow](https://github.com/tensorflow/tensorflow) | Model library |
| [matplotlib](https://github.com/matplotlib/matplotlib) | Graphics |

## Structure
| Folder |  Description |
| --- | --- |
| neural_net/ | part II: python code and books for NNs |
| data/img/ | part I: images |
| image_processing/ | part I: python code for image manipulation |