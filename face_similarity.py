import face_recognition
from glob import glob
import csv

csv_file = open('similarity.csv', mode='w')
csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(['image','similarity'])

folder_path = 'big_images/'

similarity_list = []
count = 0
for image_name in sorted(glob(folder_path + "*.jpg")):
    image = face_recognition.load_image_file(image_name)
    face_encodings = face_recognition.face_encodings(image)

    if len(face_encodings) == 2:
        sim_score = face_recognition.face_distance([face_encodings[0]], face_encodings[1])[0]
        similarity_list.append({ "name" : image_name, "similarity" : sim_score })

    count += 1
    if count % 20 == 0:
        print ("Processed ", count, " images")
sorted_similarity = sorted(similarity_list, key = lambda img : img['similarity'])

print ("===Most Similar===")
for imgdata in sorted_similarity[:10]:
    print (imgdata['name'], imgdata['similarity'])

print ("\n\n===Least Similar===")
for imgdata in sorted_similarity[-10:]:
    print (imgdata['name'], imgdata['similarity'])

for imgdata in sorted_similarity:
    csv_writer.writerow([imgdata['name'], imgdata['similarity']])
