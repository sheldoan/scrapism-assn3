import face_recognition
from glob import glob

folder_path = 'big_images/'

similarity_list = []
for image_name in sorted(glob(folder_path + "*.jpg")):
    image = face_recognition.load_image_file(image_name)
    face_encodings = face_recognition.face_encodings(image)

    if len(face_encodings) == 2:
        sim_score = face_recognition.face_distance([face_encodings[0]], face_encodings[1])[0]
        similarity_list.append({ "name" : image_name, "similarity" : sim_score })

sorted_similarity = sorted(similarity_list, key = lambda img : img['similarity'])

for imgdata in sorted_similarity[:20]:
    print (imgdata['name'], sim_score)
