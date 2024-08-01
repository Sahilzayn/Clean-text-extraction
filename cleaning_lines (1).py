import nltk
import re
import os
stopwords = nltk.corpus.stopwords.words('english')
import glob

nltk.download('stopwords')
nltk.download('punkt')

"""doc = " ".join([i for i in doc if i not in stopwords])"""

def clean_text():
    path = "C:/Users/SHARP/OneDrive - Victorian Institute of Technology/Desktop/txt_data" + "/*.txt"
    # print(path)
    li = glob.glob(path)
    for a in li:
        with open(a) as file:
            lines = file.readlines()
            for l in lines:
                doc = re.sub("\s+"," ", l) #remove spaces and next lines
                doc = doc.lower()# lower cases
                doc = re.sub("[^A-Za-z)(0-9\/.-]"," ", doc) # removing punctuations
                doc = nltk.tokenize.word_tokenize(doc)
                doc = [i for i in doc if i not in stopwords]
                #ps = nltk.PorterStemmer()
                #doc = [ps.stem(word) for word in doc]
                #ss = nltk.SnowballStemmer(language = 'english')
                #doc = [ss.stem(word) for word in doc]
                doc = " ".join([i for i in doc])
                file_name = os.path.basename(a)
                # print(file_name)
                with open("C:/Users/SHARP/OneDrive - Victorian Institute of Technology/Desktop/cleaned_data/" + file_name, 'a',encoding='utf-8') as f:
                    f.write(doc + "\n")
                # print(doc)
    return(doc)

nltk.download('punkt')

# with open('C:/Users/shyam/Downloads/s3rawtextfiles/AadityaKAMARAJU-BachelorsProvisionalCertificate.txt') as f:
#   lines = f.read()
#   clean_text(lines)

clean_text()