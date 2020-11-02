"""
You can Replace Use_CenterNet() with Following Functions:
	
	Use_RetinaNet()
	Use_YOLOv4()
	Use_TinyYOLOv4()
"""


from xtreme_vision.Detection import Object_Detection

model = Object_Detection()
model.Use_CenterNet()
model.Detect_From_Image(input_path='kite.jpg',
                        output_path='./centernet.jpg')

from PIL import Image
Image.open('centernet.jpg')