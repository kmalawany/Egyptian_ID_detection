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
<ul>
<li> The detection model predicts front and back of the ID, however I wasn't able to find a dataset to detect the text on the back of the ID,
therefore we are only using prediction of front side to feed to the segmentation model </li>
<li> For better results take a good quality image of the card with good lighting </li>
</ul>

### Models
<ul>
<li> trained yolov9c-detection on 420 images of Egyptian IDs with 2 classes; front side and back side  </li>
<li> I used pytesract to detect the orientation of the text on the card then rotating the image by the predicted angle </li>
<li> trained yolov9c-segmentation on 368 images of Egyptian IDs with 7 classes; Code, city, family name, name, neighborhood, number, state  </li>
</ul>

### Training scripts  
<ul>
  <li> ID detection Model: ( https://colab.research.google.com/drive/14MT7JPbMQXcBrJqedGgD80ly9kEh6kB2?usp=sharing ) </li>
  <li> ID segmantation Model: ( https://colab.research.google.com/drive/1tDKYR0OPQ858JLPrQGSDLxi6gMw840Kg?usp=sharing ) </li>
</ul>

### Datasets
<ul>
  <li> ID detection Dataset: ( https://universe.roboflow.com/shalaby/detect-egyptian-national-id ) </li>
  <li> ID segmantation Dataset: ( https://drive.google.com/drive/folders/1FkWQxFynWlztyEGKPxrt00HmJt4ddqdl?usp=sharing ) </li>
</ul>

### Metrics

| Model            | mAP50                     | Recall | Precision |
|-----------------|----------------------------|--------|-----------|
| <b> yolov9c_detection </b> | 0.995           |   1    |  0.998    |
| <b> yolov9c_segmentation </b> | 0.975       | 0.929   |  0.95     |


