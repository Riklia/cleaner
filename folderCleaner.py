import os, shutil
from transliterate import transliteration as mytr
try:
    import patoolib
except ModuleNotFoundError:
    pass

def printAllFiles(direct):
    for file in os.listdir(direct):
        print(file)
        
def printAllExtF(direct):
    ext = input("Which extension? ")
    for file in os.listdir(direct):
        if file.endswith("."+ext):
            print(file)

def printCategory(direct, cat=""):
    if cat == "":
        cat = input("Which category (images/videos/text/audio/programs/unknown)? ")
    categories = {
        "text":[".txt", ".doc", ".docx", ".tex", ".wpd", ".rtf", ".odt", ".pdf", ".ods", ".xls", ".xlsm", ".xlsx"],
        "images":[".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff"],
        "programs":[".exe", ".c", ".cgi", ".pl", ".class", ".cpp", ".cs", ".h", ".java", ".php", ".py", ".sh", ".swift", ".vb"],
        "videos":[".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv"],
        "audio":[".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"],        
        "archives":[".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip"],
          }
    if cat != "unknown":
        for file in os.listdir(direct):
            if os.path.splitext(file)[1] in categories[cat]:
                print(file)
            elif os.path.splitext(file)[1] == "":
                printCategory(os.path.join(direct, file), cat)
    elif cat == "unknown":
        for file in os.lestdir(direct):
            if os.path.splitext(file)[1] not in categories:
                print(file)
            elif os.path.splitext(file)[1] == "":
                printCategory(os.path.join(direct, file), cat)
    else:
        print("Error. Try again.")
        
def clearDir(direct):
    print("Enter \"Clean all\" for deleting all files from this directory")
    string = input()
    if string == "Clean all":
        for file in os.listdir(direct):
            os.remove(os.path.join(direct, file))
            print("Cleaned!")

def printFilesWithSize(direct):
    print("Example >= 50mb (you can enter size in b, kb, mb and gb")
    sizeStr = input()
    size = float(''.join(x for x in sizeStr if x.isdigit()))
    if sizeStr[-2:] == "kb":
        div = 1000
    elif sizeStr[-2:] == "mb":
        div = 10**6
    elif sizeStr[-2:] == "gb":
        div = 10**9
    else:
        print("Error!")
        return 0
    print(sizeStr[-2:])
    if ">=" in sizeStr:
        for file in os.listdir(direct):
            if os.path.getsize(os.path.join(direct, file))/div >= size:
                print(file)
    elif "<=" in sizeStr:
        for file in os.listdir(direct):
            if os.path.getsize(file)/div <= size:
                print(file)   

def searchByValue(dictionary, value):
    val_list = list(dictionary.values())
    for i in range(len(val_list)):
        for j in range(len(val_list[i])):
            if val_list[i][j] == value:
                return i
    
def archiveFunc(direct):
    ext = ["7z", "arj", "deb", "pkg", "rar", "rpm", "tar.gz", "z", "zip"]
    ok = 1
    for file in os.listdir(direct):
        name = os.path.splitext(file)[0]
        fext = os.path.splitext(file)[1][1:]
        if fext in ext:
            os.makedirs(os.path.join(direct, name))
            extractDir = os.path.join(direct, name)
            try:
                patoolib.extract_archive(os.path.join(direct, file), outdir=extractDir)
            except NameError:
                print("You should install pytool. Zip-archives only were unpacked.")
                if fext == "zip":
                    shutil.unpack_archive(os.path.join(direct, file), extractDir, fext)
                    os.remove(os.path.join(direct, file))
            else: 
               os.remove(os.path.join(direct, file))                
    normalize(direct)
    
def normalize(direct):
    for file in os.listdir(direct):
        if os.path.isdir(os.path.join(direct, file)):
            oldName = os.path.join(direct, file)
            newName = os.path.join(direct, mytr(file))
            os.rename(oldName, newName)
            normalize(os.path.join(direct, file))
        else:
            oldName = os.path.join(direct, file)
            newName = os.path.join(direct, mytr(file))
            os.rename(oldName, newName)
    
def sortByFolders(direct, recDir=""):
    normalize(direct)
    if recDir == "":
        recDir = direct
    categories = {
        "documents":[".txt", ".doc", ".docx", ".tex", ".wpd", ".rtf", ".odt", ".pdf", ".ods", ".xls", ".xlsm", ".xlsx"],
        "images":[".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff"],
        "programs":[".exe", ".c", ".cgi", ".pl", ".class", ".cpp", ".cs", ".h", ".java", ".php", ".py", ".sh", ".swift", ".vb"],
        "video":[".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv"],
        "audio":[".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"],        
        "archives":[".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip"],
        "unknown":["none"]       
        }
    key_list = list(categories.keys())
    if os.path.isdir(recDir):
        for file in os.listdir(recDir):
            if any(os.path.splitext(file)[1] in inner_list for inner_list in categories.values()):
                position = searchByValue(categories, os.path.splitext(file)[1])
                newDir = os.path.join(direct, key_list[position])
                if not os.path.exists(newDir):
                    os.makedirs(newDir)
                    os.replace(os.path.join(direct, file), os.path.join(newDir, file))
                else:
                    os.replace(os.path.join(recDir, file), os.path.join(newDir, file))
            elif os.path.splitext(file)[1] == "":
                if file not in categories.keys():
                    sortByFolders(direct, os.path.join(recDir, file))
            elif not any(os.path.splitext(file)[1] in inner_list for inner_list in categories.values()) or direct != recDir:
                newDir = os.path.join(direct, "unknown")
                if not os.path.exists(newDir):
                    os.makedirs(newDir)
                    os.replace(os.path.join(direct, file), os.path.join(newDir, file))
                else:
                    os.replace(os.path.join(direct, file), os.path.join(newDir, file))
    for dirpath, dirnames, filenames in os.walk(direct, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)
    if os.path.isdir(os.path.join(direct, "archives")):        
        archiveFunc(os.path.join(direct, "archives"))
         
MENU = {"1": printAllFiles,
        "2": printAllExtF,
        "3": printFilesWithSize,
        "4": printCategory,
        "5": sortByFolders,
        "6": clearDir,
        }
    
def main():
    print("CleanerForFolder started")
    direct = input("Enter the path of your folder: ")
    while os.path.isdir(direct) == False:
        direct = input("This folder doesn't exist. Enter the path of your folder: ")
    textMenu = """Enter:
1 - for printing all files in a current folder
2 - for printing all files with specific extension in a current folder
3 - for printing all files with size >= <= than given (in a current folder)
4 - for printing all files from given category
5 - for sorting ALL files by category folders
6 - for deleting all files in a current folder
7 - change the current folder
8 - exit"""
    print(textMenu)
    choice = input("Your choice: ")
    while choice != "8":
        if choice == "7":
            direct = input("Enter the path of your folder: ")
            while os.path.isdir(direct) == False:
                direct = input("This folder doesn't exist. Enter the path of your folder: ")
        else:
            try:
                MENU[choice](direct)
            except KeyError:
                print("There's no such option. Try again.")
        print(textMenu)
        choice = input("Your choice: ")    
        
main()
