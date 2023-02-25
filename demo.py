import os
import torch
import io
from PIL import Image


img_bytes = open(os.path.join("assets", "tv.jpg"), "rb")
img_bytes = img_bytes.read()
img = Image.open(io.BytesIO(img_bytes))
model = torch.hub.load('yolov5', model='custom', path='last2.pt', source='local', force_reload=True)
model.eval()
results = model([img])
print(results.pandas().xyxy[0].name.value_counts().values[0])
