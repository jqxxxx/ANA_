from dataSetGenerator import *

data = np.load("./negative_img_dataTest.npy")
labels = np.load("./negative_img_labelsTest.npy")
classes = np.load("./negative_img_classes.npy")

picShow(data,labels,classes,just=1,predict=None,autoClose = False, Save_as = "pic", save_to = "images")