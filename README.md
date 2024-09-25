# Egyption ID detection and segmentation 


### How to use
```
git clone https://github.com/kmalawany/Egyptian_ID_detection.git
cd Egyptian_ID_detection
pip install -r requirements.txt
```
### testing

```
python predict.py [img_dir]
```

### Training scripts
<ul>
  <li> ID detection Model: ( https://colab.research.google.com/drive/14MT7JPbMQXcBrJqedGgD80ly9kEh6kB2?usp=sharing ) </li>
  <li> ID segmantation Model: ( https://colab.research.google.com/drive/1tDKYR0OPQ858JLPrQGSDLxi6gMw840Kg?usp=sharing ) </li>
</ul>

### Datasets
<ul>
  <li> ID detection Dataset: ( https://universe.roboflow.com/shalaby/detect-egyptian-national-id ) </li>
  <li> ID segmantation Dataset: ( https://universe.roboflow.com/omartamer0/egyptian-id-detectr ) </li>
</ul>

### Metrics

| Model         | Description                        | Default Value |
|-----------------|------------------------------------|---------------|
| yolov9c_detection| Path to the input file             | `None`        |
| `--output`      | Path to save the output file       | `results/`    |
| `--model`       | Model to use for processing        | `resnet50`    |
| `--gpu`         | Enable GPU usage (0 for CPU, 1 for GPU) | `0`       |
