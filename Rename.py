import shutil
import os

folder = 'Mammals_Image/'
count = 1

for filename in os.listdir(folder):
    source = folder + filename
    destination = folder + "Mammal_" + str(count)+ ".jpg"
    os.rename(source, destination)
    count+=1
    
print("The Task is done")