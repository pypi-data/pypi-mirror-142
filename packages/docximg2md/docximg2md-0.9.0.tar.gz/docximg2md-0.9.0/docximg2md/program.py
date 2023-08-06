import zipfile
from mdutils.mdutils import MdUtils
from PIL import Image
import os
import sys


def create_unique_folder(i: int, foldername: str, original_foldername: str):
    if (os.path.isdir(os.path.abspath(foldername))):
        i += 1
        foldername = create_unique_folder(i, "{}{}".format(original_foldername, i), original_foldername)
    else:
        os.mkdir(foldername)
    
    return foldername


def extract_images(document: str, folder: str):
    '''
    Code from: 
    https://stackoverflow.com/questions/60201419/extract-all-the-images-in-a-docx-file-using-python
    '''
    try:
        archive = zipfile.ZipFile(document)
    except FileNotFoundError:
        print("Can't find the file {}".format(document))
        exit()
    except:
        print('Error: {} when trying to open the document {} as a zipfile. (line 24)'.format(sys.exc_info()[0], document))
        exit()

    for file in archive.filelist:
        if file.filename.startswith('word/media/'):
            archive.extract(file, path=os.path.abspath(folder))



def convert_if_emf(foldername: str, filename: str):
    try:
        folder_list = os.listdir("{}\word\media".format(foldername))
    except FileNotFoundError:
        print("There's no images in the word document {}".format(filename))
        exit()

    for file_name in folder_list:
        if file_name.endswith('.emf') or file_name.endswith('.wmf'):
            name = file_name[:-4]
            img = Image.open("{}\word\media\{}".format(foldername, file_name))
            img.save("{}\word\media\{}.png".format(foldername, name))
            os.remove("{}\word\media\{}".format(foldername, file_name))



def write_markdown(markdownname: str, foldername: str):
    mdFile = MdUtils(file_name=markdownname)
 
    for image_file in os.listdir(foldername):
        mdFile.write('![](word\media\{})\n'.format(image_file))

    mdFile.create_md_file()

def main():
    if (len(sys.argv) == 1):
        print('version 0.9.0  (c) 2022 Isabel Sandstrom Hermit AS\n\n\
Python command line program that takes in a word document and transfers the images to a markdown file.\
\nUsage:\n\ndocximg2md inputdocument markdownfile\n\n\
where the inputdocumnet is the word document with the images, and the markdownfile is the name of the markdownfile you want to create containing the images.')
        exit()

    elif (len(sys.argv) < 3):
        print('Usage:\n\ndocximg2md inputdocument markdownfile\n\n\
where the inputdocumnet is the word document with the images, and the markdownfile is the name of the markdownfile you want to create containing the images.')
        exit()

    filename = sys.argv[1]

    if (filename.endswith('.docx') == False):
        print('First argument has to be a word document of type .docx')
        exit()

    foldername = "{}-folder".format(filename)

    foldername = create_unique_folder(0, foldername, foldername)

    extract_images(filename, foldername)
    convert_if_emf(foldername, filename)
    write_markdown("{}/{}".format(foldername, sys.argv[2]), "{}\word\media".format(foldername))


if __name__ == "__main__":
    main()