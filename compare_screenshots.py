import abc
import numpy as np
import cv2
import PIL
from MakeScreenshot import MakeScreenshot
from skimage.metrics import structural_similarity as ssim

class ACompareImages(abc.ABC):
    def __init__(self):
        pass
    @abc.abstractmethod
    def load_images(self, image_1, image_2):
        pass
    def compare_images(self):
        pass    
    @abc.abstractmethod
    def calculate_mean_square_diff(self):
        pass    
    def calculate_structural_similarity_index(self):
        pass

class ISL(ACompareImages):
    def __init__(self):
        self._similarity     = 0
        self._list_of_images = []    
    def load_images(self,image_list):        
        if len(image_list) < 2 : return "Need at least 2 images to compare"        
        for images in image_list:            
            if isinstance(images, str): self.load_to_memory(images)
            else:                       self._list_of_images.append(images)
    def convert_pil_to_cv(self,link_to_image):
        pil_image = PIL.Image.open(link_to_image).convert('RGB')
        open_cv_image = np.array(pil_image)        
        return open_cv_image
    def load_to_memory(self, link_to_image):
        self._list_of_images.append(self.convert_pil_to_cv(link_to_image))
    def get_differences(self,calculation_method = "MSE"):
        if len(self._list_of_images) < 2 or len(self._list_of_images) % 2 == 1: return "Need at least 2 images to compare"
        for num_of_image in range(len(self._list_of_images)):
            if num_of_image % 2 == 1: continue
            image_A = self._list_of_images[num_of_image]
            image_B = self._list_of_images[num_of_image+1]
            value = None
            if calculation_method == "MSE":
                value = self.calculate_mean_square_diff(image_A,image_B)
            if calculation_method == "SSI":
                value = self.calculate_structural_similarity_index(image_A,image_B)
            return value
    def calculate_mean_square_diff(self, image_A, image_B, compare_each_image = False):
        err = np.sum((image_A.astype("float") - image_B.astype("float")) ** 2)
        err /= float(image_A.shape[0] * image_A.shape[1])
        return err
    def calculate_structural_similarity_index(self, image_A, image_B):
        return ssim(image_A, image_B,multichannel=True)