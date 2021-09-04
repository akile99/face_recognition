from PIL import Image
import face_recognition

pic_of_me = 'faces/me.png'
unknown_pic = 'faces/emma_me.png'
def get_faces(file_name):
    image = face_recognition.load_image_file(file_name)
    face_locations = face_recognition.face_locations(image)

    show_faces(face_locations, image)

def convert_jpeg_to_png(fname):

    im1 = Image.open(fr'{fname}')
    im1 = im1.rotate(90*3)
    im1.save(fr'faces/{fname}.png')

def compare_picture(known_pic, unknown_pic):

    picture_of_me = face_recognition.load_image_file(known_pic)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

    unknown_picture = face_recognition.load_image_file(unknown_pic)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[1]

    # Now we can see the two face encodings are of the same person with `compare_faces`!

    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)


    if results[0] == True:
        print("It's a picture of me!")
    else:
        print("It's not a picture of me!")


def show_faces(face_locations, image):

    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location
        # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()
# convert_jpeg_to_png('IMG_5015.JPG')
compare_picture(r"faces/me.png", r'faces/emma_me.png')

get_faces(unknown_pic)