import urllib
import re,os

def getImages(myurl):
    imgSum = 0
    badImg = 0
    urlStr = urllib.urlopen(myurl).read()

    #hrefCmp = re.compile("""<img src=".*?" .*?>""")
    #hrefCmp = re.compile("""<.*? src="(.*?)" .*?>""")
    #hrefCmp = re.compile("""<img src="(.*?)"(.*?)>""")
    hrefCmp = re.compile("""<img.*?src="(.*?)".*?>""")  #ok
    hreflist = hrefCmp.findall(urlStr)

    drive = "/home/tom/pyt"
    if not os.path.exists(drive):
        os.mkdir(drive)

    for href in hreflist:
        #print href
        if href.find("""http://""")==0: # must start with http
            imageName = href[href.rindex("/")+1:]
            try:
                urllib.urlretrieve(href, os.path.join(drive,imageName))
                imgSum += 1
                print imageName + "    OK"
            except :    #default
                print "cannot download this image: "+imageName
                #print href
        else:
            badImg += 1
            print href
    print "Success: ",imgSum,"    Failed: ",badImg

if __name__ == "__main__":
    imgurl = raw_input("url -> ")
    getImages(imgurl)