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
### Note
The detection model predicts front and back of the ID, however I wasn't able to find a dataset to detect the text on the back of the ID,
therefore we are only using prediction of front side to feed to the segmentation model
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

| Model            | mAP50                     | Recall | Precision |
|-----------------|----------------------------|--------|-----------|
| <b> yolov9c_detection </b> | 0.995           |   1    |  0.998    |
| <b> yolov9c_segmentation </b> | 0.975       | 0.929   |  0.95     |

### Detect and correct allignment 
#### I used pytesract to detect the orientation of the text on the card then rotating the image by the predicted angle
