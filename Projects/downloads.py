import os 
file_path = '/Users/victorbertels/Downloads/ezgif.com-webp-to-png (1).png'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File succesfully delete")

else:
    print("File does not exist")