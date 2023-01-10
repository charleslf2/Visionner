import numpy as np 
import cv2
import os
import matplotlib.pyplot as plt 
from rich.panel import Panel
from rich.console import Console

console=Console()



def display(dataset, dataset_shape, title):
        console.print(Panel.fit(f"{dataset_shape}", title=f"{title}", title_align="center"))

        plt.figure()
        for i in range(10):
            plt.subplot(2, 5, i + 1)
            plt.suptitle("10 first image in your dataset")
            plt.imshow(dataset[i])

        plt.show()



def DatasetImporter(path, size=(28, 28)):

    """
    This function take an image dataset directory and transform it into a numpy array

    Params
    ======
    path : a path that of your image dataset || should be a directory

    size : (28, 28) by default || specify the Width and the Heigh of your images  || should be a tuple 

    Usage
    =====
    ### import usefull package
    >>> from visionner import Vision
    >>> import matplotlib.pyplot as plt 

    ### basic usage
    >>> your_dataset=Vision("path/to/your/dataset/", size=(28, 28))

    ### visualize the first image
    >>> plt.imshow(your_dataset[0])
    >>> plt.show()

    """


    isDirectory = os.path.isdir(path)

    if isDirectory==False:
        raise TypeError("The path should be a directory")

    dataset=[]
        

    for file_name in os.listdir(path):
        img=cv2.imread(os.path.join(path, file_name))
        img=cv2.resize(img, size)
        dataset.append(img)

    dataset=np.array(dataset)

    dataset_shape=dataset.shape

    #display
    display(dataset, dataset_shape, title="Your dataset shape")

    return dataset
    

    


   

def DatasetNormalizer(dataset, dataset_shape):

    image_heigh_size=dataset_shape[1]

    image_chanel=dataset.shape[3]

    # reshape

    normalize_dataset=np.reshape(dataset, [-1, image_heigh_size, image_heigh_size, image_chanel])

    normalize_dataset=dataset.astype("float32")/250
        
    return normalize_dataset




def TrainTestSpliter(dataset, dataset_shape, test_size):
        
    x_test_number=(dataset_shape[0]*test_size)
    x_test=dataset[: x_test_number]
    x_train=dataset[x_test_number :]

    print("X_test number", x_test_number)
    return x_train,x_test
    

    