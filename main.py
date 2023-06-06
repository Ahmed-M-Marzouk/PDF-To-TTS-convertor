import shutil
import os
import PyPDF2
from gtts import gTTS

src = input("Please enter the path of the PDF: ")
dit = "./PDFs/"

os.makedirs(dit, exist_ok=True)

for file_name in os.listdir(src):
    source = os.path.join(src, file_name)
    destination = os.path.join(dit, file_name)
    
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print("Copied " + file_name)
    else:
        print("Failed to copy " + file_name)


directory = "./PDFs"
Mp3s = "./Mp3"
files = os.listdir(directory)

os.makedirs(Mp3s, exist_ok=True)

for file_name in files:
    full_path = os.path.join(directory, file_name)
    
    if os.path.isfile(full_path):
        with open(full_path, 'rb') as pdfObj:
            reader = PyPDF2.PdfReader(pdfObj)
            print("The PDF you selected has " + str(reader.numPages) + " number of pages")
            
            desired = int(input("Which page do you want to hear: "))
            pageObj = reader.getPage(desired - 1)
            
            pageText = pageObj.extract_text()
            print(pageText)
            
            myText = pageText
            language = 'en'
            
            myMp3 = gTTS(text=myText, lang=language, slow=False)
            
            mp3_file_name = os.path.splitext(file_name)[0] + str(desired) + '.mp3'
            print(mp3_file_name)
            mp3_file_path = os.path.join(Mp3s, mp3_file_name)
            myMp3.save(mp3_file_path)
