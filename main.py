import shutil
import os
import PyPDF2
from gtts import gTTS

src = input("Please enter the path of the PDF: ")
dit = r"D:\work\dody\python\PDF-TTS\PDFs\\"

for file_name in os.listdir(src):
    source = os.path.join(src, file_name)
    distenation = os.path.join(dit, file_name)
    
    if os.path.isfile(source):
        shutil.copy(source, distenation)
        print("copied " + file_name)
    else:
        print("failed to copy " + file_name)


directory = "./PDFs"
Mp3s = "./Mp3"
files = os.listdir(directory)

for file_name in files:
    full_path = os.path.join(directory, file_name)
    
    if os.path.isfile(full_path):
        pdfObj = open(full_path, 'rb')
        
        reader = PyPDF2.PdfReader(pdfObj)
        print("The PDF you selected have " + str(reader.pages) + " number of pages")
        
        desired = int(input("Which page do you want to hear: "))
        pageObj = reader.getPage(desired - 1)
        
        pageText = pageObj.extract_text()
        print(pageText)
#Thanks for reading my code if you have any suggestions please commit
        
        myText = pageText
        language = 'en'
        
        myMp3 = gTTS(text=myText, lang=language, slow=False)
        
        myMp3.save(os.path.join(Mp3s, file_name + '.mp3'))
