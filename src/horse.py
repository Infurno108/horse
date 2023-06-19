from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
from PIL import Image
from numpy import asarray

detector = MTCNN()

url = "photos/test2.jpg"

def extractFace(imagePath, requiredSize=(224, 224,)):
    image = plt.imread(imagePath)
    detector = MTCNN()
    faces = detector.detect_faces(image)

    faceImages = []

    for face in faces:
        x1, y1, width, height = face['box']
        x2, y2 = x1 + width, y1 + height

        faceBoundary = image[y1:y2, x1:x2]

        faceImage = Image.fromarray(faceBoundary)
        faceImage = faceImage.resize(requiredSize)
        faceArray = asarray(faceImage)
        faceImages.append(faceArray)
    return faceImages

def displayFaces(image_path, faces):
    image = plt.imread(image_path)
    plt.imshow(image)

    ax = plt.gca()

    for face in faces:
        x, y, width, height = face['box']
        face_rect = Rectangle((x, y), width, height, fill=False, color='red')

        ax.add_patch(face_rect)
    plt.show()

image = plt.imread(url)
faces = detector.detect_faces(image) #this is just the raw data of the boxes within the faces, nothing else
extractedFace = extractFace(url) #This is the array that contains individual faces

displayFaces(url, faces) 

for i in range (0, len(extractedFace)):
    plt.imshow(extractedFace[i])
    plt.show()



