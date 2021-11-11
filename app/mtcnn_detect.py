from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
 
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
 
filename = 'picture_02.jpg'

pixels = pyplot.imread(filename)
# detektor alkalmazasa
detector = MTCNN()
# arcok detektalasa
faces = detector.detect_faces(pixels)
# arcok bejelolese
draw_image_with_boxes(filename, faces)