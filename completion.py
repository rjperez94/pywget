#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request, os, requests, traceback, re

"""
    This is what the user types in the console
    Returns None if arguments passed is more than one or is not url='' format
"""
def pywget (url):
    try:
        parsed_url (url)
    except (Exception): #if some error occurs, print error msg
        print ("Command error. Invalid syntax. Make sure you follow command conventions")
        return None

"""
    Fetches web page and ALL links in the ROOT of that web page
    Return None if error occurs or if url does not exist
"""
def parsed_url (address):
    #check if url exists
    if (url_exist(address)):
        #get root of page
        #e.g. http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html 
        #will become http://homepages.ecs.vuw.ac.nz/~ian/nwen241/
        root = address.replace(os.path.basename(address), "")       
        
        #fetch this web page to find images and links
        req = urllib.request.Request(address)
        resp = urllib.request.urlopen(req)
        data = resp.read()
        
        #find ALL images
        images = re.findall('img .*?src="(.*?)"', str(data))
        #find ALL links
        links = re.findall('a .*?href="(.*?)"', str(data))
        
        #check the 'would be' name of this web page if created
        index_name = check_new_name (address)
        
        #fetch this web page and put it in a file
        get(address)
        
        #go through ALL links
        for lnk in links:
            #absolute link
            if (root.startswith('http://') or root.startswith('https://')) and (lnk.startswith('http://') or lnk.startswith('https://')) and root in lnk:
                #check the 'would be' name of this web page if created
                linkName = check_new_name (lnk)
                #fetch link
                #if link fetch succesful link it to 'indexName' file
                if get (lnk) is not None:
                    link_files(index_name, linkName, lnk)
            
            #relative link
            elif root.startswith('http://') and not lnk.startswith('http://') and not lnk.startswith('//'):
                #check the 'would be' name of this web page if created
                linkName = check_new_name (root+lnk)  
                #fetch link
                #if link fetch succesful link it to 'indexName' file
                if get (root+lnk) is not None:
                    link_files(index_name, linkName, lnk)
        
        #go through ALL images
        for img in images:
            #check the 'would be' name of this image if created
            imageName = check_new_name (root+img)
            #fetch image
            #if image fetch succesful link it to 'indexName' file
            if get (root+img) is not None:
                link_files(index_name, imageName, img)

        
    else:
        #if this page not found
        print ("Network error. URL/webpage does not exist")
        return None

"""
    Fetches a single web page
    Return None if error occurs or if url does not exist
"""
def get (address):
    #check if url exists
    if url_exist(address):
        #if file already exist
        if os.path.exists(os.path.basename(address)) and os.path.isfile(os.path.basename(address)):
            #use the next permissible file name in 'sequence'
            return urllib.request.urlretrieve(address, file_does_exist (os.path.basename(address)))
        else:
            #else, use basename as file name
            return urllib.request.urlretrieve(address, os.path.basename(address))
    else:
        return None

"""
    Checks if url exist
    Retrurn True if it does, None if it doesn't
"""
def url_exist(path):
    try:
        r = requests.head(path)
        #return true if url 'path' exists i.e. the address
        return r.status_code == requests.codes.ok
    except (Exception): #if some error occurs, print stack trace
        print (traceback.format_exc())
        return None

"""
    Returns the 'next' permissible file name in pattern
    ASSUMES that file_name exists
    Return None if some error occurs
"""
def file_does_exist (file_name):
    try:
        counter = 1
        #actual file name
        name = os.path.splitext(os.path.basename(file_name))[0]
        #file name extension
        extension = os.path.splitext(os.path.basename(file_name))[1]
        
        #update counter while name exists
        #e.g. if name.1.jpg exists --> name.2.jpg until it does not exist
        while os.path.exists(name+"."+str(counter)+extension):
            counter+=1
        
        #return full file name
        return name+"."+str(counter)+extension
    except (Exception): #if some error occurs, print stack trace
        print (traceback.format_exc())
        return None

"""
    Returns the 'next' permissible file name in pattern
    DOES NOT assume that file exists
    Return None if some error occurs
"""
def check_new_name (address):
    if os.path.exists(os.path.basename(address)):
        return file_does_exist (os.path.basename(address))
    else:
        return os.path.basename(address)

"""
    Re-links absolute links to local links
    This modifies the 'index_name.html' file
    1. Find 'old_link_name' inside 'index_name.html' file
    2. Replace 'old_link_name' with 'new_link_name' which is the local name of file
"""   
def link_files (index_name, new_link_name, old_link_name):
    #The file to be modified must exist
    #The file to be 'targeted' must exist
    if os.path.exists(index_name) and os.path.exists(new_link_name):
        # this loads the entire file into a string
        oldF = open(index_name)
        content = oldF.read()
        oldF.close()
        
        #replace occurance of 'old_link_name' as 'new_link_name'
        content = content.replace(old_link_name, new_link_name)
        
        #rewrite index_name and put modified 'content' into it
        newF = open(index_name, "w")
        newF.write(content)
        newF.close()
    else:
        return None