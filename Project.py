import os
import shutil


current_path = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(current_path):

    if filename.endswith((".jpg", '.jpeg' , '.png' , '.PSD')):
        if not os.path.exists("Images"):
            os.mkdir('Images')
        shutil.copy(filename, 'Images')
        os.remove(filename)
        print("Images done..")

    if filename.endswith((".webm", ".mp4")):
        if not os.path.exists("Videos"):
            os.mkdir('Videos')
        shutil.copy(filename, 'Videos')
        os.remove(filename)
        print("Videos done..")   

    if filename.endswith((".m4a", ".mp3", ".wav", ".aac")):
        if not os.path.exists("Audio"):
            os.mkdir('Audio')
        shutil.copy(filename, 'Audio')
        os.remove(filename)
        print("Audio done..")    

    if filename.endswith((".doc", ".docx", ".odt",".pdf")):
        if not os.path.exists("Document"):
            os.mkdir('Document')
        shutil.copy(filename, 'Document')
        os.remove(filename)
        print("Document done..")    