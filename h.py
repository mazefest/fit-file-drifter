import os
import glob
import shutil
import zipfile


print("Fit File Drifter")
print("----------------")

#Display prompt
print("v - View last downloaded .zip files\nd - delete all unzipped files\nu - unzip X last downloaded .zip files\nvu - view unzipped files\ne - exit FFD")


selection = 'v'

while selection != 'e':
    #Load downloads file into arrTwo
    path = './../../../Downloads'
    files = glob.glob/:path + "/*.zip")   
    files.sort(key=os.path.getmtime)
    arrTwo = os.listdir(path)
    
    #Destination path
    path = './zip'
    arr = os.listdir(path)

    selection = input(">>")

    if selection == 'e':
        break

    elif selection == 'd':
        filelist = glob.glob(os.path.join('./zip', "*"))
        for f in filelist:
            try:
                os.remove(f)
            except:
                shutil.rmtree(f)
        filelist = glob.glob(os.path.join('./unzipped', "*"))
        for f in filelist:
            try:
                os.remove(f)
            except:
                shutil.rmtree(f)
        print("v - View all File contents\nd - delete all data\nu - unzip all files\ne - exit FFD")

    elif selection == 'v':
        print("Enter Number Of Recent Download You Would Like To See \n >>")
        recentCount = input()
        recentCount = int(recentCount)
        for x in range(recentCount):
            print( files[x] )
        print("v - View all File contents\nd - delete all data\nu - unzip all files\ne - exit FFD")
    
    elif selection == 'u': #stage files
        print("Enter Number Of Recent Downloads you would like to unzip \n >>")
        recentCount = input()
        recentCount = int(recentCount)
        for x in range(recentCount):
            print( "Staging - " + files[x] )
            fname = str(x)
            shutil.move(files[x], "./zip/" + fname + ".zip")
            with zipfile.ZipFile('./zip/'+ fname + ".zip", 'r') as zip_ref:
                print("unzipping " + files[x] + " and moving to ./unzipped")
                zip_ref.extractall('./unzipped')

        
        print("\n>> To view all unzipped files press vu\n>>")
    elif selection == 'vu':
        unzippedArr = os.listdir('./unzipped')
        size = len(unzippedArr)
        for x in range(size):
            print(unzippedArr[x])
        print("v - View all File contents\nd - delete all data\nu - unzip all files\ne - exit FFD")

    else:#define last downloaded#move
        print("Invalid Statement")
        print("v - View all File contents\nd - delete all data\nu - unzip all files\ne - exit FFD")


