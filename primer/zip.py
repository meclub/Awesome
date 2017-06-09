from __future__ import print_function
import os
import zipfile


def zip_dir(dirname, zipfilename):
    filelist = []
    # Check input ...
    fulldirname = os.path.abspath(dirname)
    fullzipfilename = os.path.abspath(zipfilename)
    print("Start to zip %s to %s ..." % (fulldirname, fullzipfilename))
    if not os.path.exists(fulldirname):
        print("Dir/File %s is not exist, Press any key to quit..." % fulldirname)
        inputStr = raw_input()
        return
    if os.path.isdir(fullzipfilename):
        tmpbasename = os.path.basename(dirname)
        fullzipfilename = os.path.normpath(os.path.join(fullzipfilename, tmpbasename))
    if os.path.exists(fullzipfilename):
        print("%s has already exist, are you sure to modify it ? [Y/N]" % fullzipfilename)
        while 1:
            inputStr = raw_input()
            if inputStr == "N" or inputStr == "n":
                return
            else:
                if inputStr == "Y" or inputStr == "y":
                    print("Continue to zip files...")
                    break

                    # Get file(s) to zip ...
    if os.path.isfile(dirname):
        filelist.append(dirname)
        dirname = os.path.dirname(dirname)
    else:
        # get all file in directory
        for root, dirlist, files in os.walk(dirname):
            for filename in files:
                filelist.append(os.path.join(root, filename))

                # Start to zip file ...
    destZip = zipfile.ZipFile(fullzipfilename, "w")
    for eachfile in filelist:
        destfile = eachfile[len(dirname):]
        print("Zip file %s..." % destfile)
        destZip.write(eachfile, destfile)
    destZip.close()
    print("Zip folder succeed!")

