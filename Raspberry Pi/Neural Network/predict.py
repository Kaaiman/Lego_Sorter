from tensorflow.keras.models import load_model
from keras.preprocessing import image
import numpy as np
import natsort

model_path = 
images_path = 

numb_classes = 9
classes = [2357, 2456, 3001, 3002, 3003, 3004, 3008, 3009, 3010]

model = load_model(model_path)

for part in classes:
    image_path = os.path.join(images_path, str(part) + '.jpg')
    test_image = image.load_img(image_path, target_size=(64, 64)) 
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)

    result = model.predict(test_image)
    percentages = result[0]
    percentages_list = []
    i = 0
    while i < numb_classes:
        percentages_list.append(percentages[i])
        i += 1

    percentages_sorted = natsort.natsorted(percentages_list)
    highest_percentage = percentages_sorted[-1]
    numb = percentages_list.index(highest_percentage)
    part_number = classes[numb]
    print(part_number)
