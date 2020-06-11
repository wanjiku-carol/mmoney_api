import cv2
import numpy as np

def detect_faces_with_dnn(path_to_image):
  """
  """

  prototxt_path = "weights/deploy.prototxt.txt"
  model_path = "weights/res10_300x300_ssd_iter_140000_fp16.caffemodel"

  # load caffe model
  model = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
  
  # read image
  image = cv.imread(path_to_image)
  
  # get height and weight of image
  h, w = image.shape[:2]
  
  # preprocess the image: resize and performs mean subtraction
  blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
  
  # set the image into the input of the neural network
  model.setInput(blob)
  
  # perform inference and get the result
  output = np.squeeze(model.forward())
  
  font_scale = 1.0
  for i in range(0, output.shape[0]):
    # get the confidence
    confidence = output[i, 2]
    
    # if confidence is above 50%, then draw the surrounding box
    if confidence > 0.5:
      # get the surrounding box cordinates and upscale them to original image
      box = output[i, 3:7] * np.array([w,h,w,h])
      
      # convert to integers
      start_x, start_y, end_x, end_y = box.astype(np.int)
      
      # draw the rectangle surrounding the face
      cv2.rectangle(image, (start_x, start_y), (end_x, end_y), color=(255,0,0), thickness=2)
                    
      # draw text as well
      cv2.putText(
        image, f"{confidence*100:2f}%", (start_x, start_y-5), cv2.FONT_HERSHEY_SIMPLEX,
        font_scale, (255,0,0), 2
        )
  cv2.imshow("image", image)
  cv2.waitKey(0)
  
  # save the image with rectangles
  cv2.imwrite(f"detected_dnn_{path_to_image}", image)
  return image
  