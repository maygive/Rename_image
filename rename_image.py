from PIL import Image
import glob
import random
def rotate(image_path, degrees_to_rotate, saved_location):
    """
    Rotate the given photo the amount of given degreesk, show it and save it
    @param image_path: The path to the image to edit
    @param degrees_to_rotate: The number of degrees to rotate the image
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(saved_location)
if __name__ == '__main__':
    
    list_img= glob.glob("D:\\India\\image_test\\mosquito2\\Anopheles\\*.jpg")
    print(len(list_img))
    j=0
    for i in range (len(list_img)):
        name="anopheles"+str(j)
        rotate(list_img[i], 0, name+'.jpg')
        j+=1
