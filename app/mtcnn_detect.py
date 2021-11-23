from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
import cv2
 
def draw_image_with_boxes(filename, result_list):
	data = pyplot.imread(filename)
	pyplot.imshow(data)

	ax = pyplot.gca()

	for result in result_list:
		x, y, width, height = result['box']
		# negyzetek megrajzolasa az arcok kore
		rect = Rectangle((x, y), width, height, fill=False, color='red')

		ax.add_patch(rect)
		# pontok kijelolese
		for key, value in result['keypoints'].items():
			# szemek, orr es szaj detektalasa
			dot = Circle(value, radius=2, color='red')
			ax.add_patch(dot)
    #kirajzolas
	pyplot.show()



def mtcnn_detect(image):
	image_local = image.copy()
	detector = MTCNN()
	results = detector.detect_faces(image_local)
	for face in results:
		bounding_box = face['box']
		rect = cv2.rectangle(image_local,
							 (bounding_box[0], bounding_box[1]),
							 (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
							 (255, 0, 0), 2)
	return image_local, len(results)



'''
filename = 'picture_02.jpg'

pixels = pyplot.imread(filename)
# detektor alkalmazasa
detector = MTCNN()
# arcok detektalasa
faces = detector.detect_faces(pixels)
# arcok bejelolese
draw_image_with_boxes(filename, faces)
'''