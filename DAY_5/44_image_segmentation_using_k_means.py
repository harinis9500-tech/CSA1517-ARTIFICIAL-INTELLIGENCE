# 44 K-Means image segmentation. Provide sample_image.jpg.
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
im=np.array(Image.open("sample_image.jpg").convert("RGB").resize((200,200)))
X=im.reshape(-1,3);m=KMeans(n_clusters=4,random_state=1,n_init=5).fit(X)
seg=m.cluster_centers_[m.labels_].reshape(im.shape).astype("uint8")
plt.imshow(seg);plt.axis("off");plt.show()