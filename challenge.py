#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request, os, requests, traceback, re

"""
    This is what the user types in the console
    Returns None if arguments passed is more than two or:
    Is not url='' format
    Is not depth = 1 .... n
"""
def pywget (url, depth):        
    try:
        if depth > 0:   #depth cannot be 0
            parsed_url (url, depth)
        else:
            print ("Command error. Invalid syntax. Can't have a depth of 0")
            return None
            
    except (Exception): #if some error occurs, print error msg
        print (traceback.format_exc())
        print ("Command error. Invalid syntax. Make sure you follow command conventions")
        return None

"""
    Fetches web page and ALL links in the ROOT of that web page
    This function will be called recursively until depth reaches 0
    Return None if error occurs or if url does not exist
"""
def parsed_url (address, depth):
    #recursion base case
    if depth > 0:
        #check if url exists
        if url_exist(address):      
            #fetch this web page to find images and links
            req = urllib.request.Request(address)
            resp = urllib.request.urlopen(req)
            data = resp.read()
            
            #find ALL images
            images = re.findall('img .*?src="(.*?)"', str(data))
            
            #find ALL links
            links = re.findall('a .*?href="(.*?)"', str(data))
    
            #get root of page
            #e.g. http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html 
            #will become http://homepages.ecs.vuw.ac.nz/~ian/nwen241/
            root = address.replace(os.path.basename(address), "")
            
            #get root directory of page
            #e.g. http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html 
            #will become homepages.ecs.vuw.ac.nz/~ian/nwen241/ if NOT exist.
            #IF it exists will become homepages.ecs.vuw.ac.nz.1/~ian/nwen241/
            root_dir = make_dir(root, os.path.basename(address))
            
            #fetch this web page and put it in a file
            get(root_dir, address)
            
            #go through ALL links
            for lnk in links:
                #absolute link
                if (root.startswith('http://') or root.startswith('https://')) and (lnk.startswith('http://') or lnk.startswith('https://')) and root in lnk:
                    #recall using this link with depth - 1
                    parsed_url(root+os.path.basename(lnk), depth-1)
                    
                    #fetch link
                    #link it to 'indexName' file
                    link_name = root_dir+os.path.basename(lnk)   #whole directory path including name
                    #path 'difference'
                    #e.g.root_dir as homepages.ecs.vuw.ac.nz/~ian/nwen241/ AND 
                    #link name as homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html
                    #so difference is index.html
                    link_name = link_name.replace(root_dir, "")
                    #link files
                    link_files(root_dir+os.path.basename(address), link_name, lnk)
                
                #relative link
                elif root.startswith('http://') and not lnk.startswith('http://') and not lnk.startswith('//'):
                    #recall using this link with depth - 1
                    #No need to relink as HTML markup is relative
                
                    #use root+lnk in get to make link absolute
                    parsed_url(root+lnk, depth-1)
            
            #go through ALL images
            for img in images:
                #if relative
                #e.g.GrumoyCat.jpg will become
                #homepages.ecs.vuw.ac.nz/~ian/nwen241/images/GrumoyCat.jpg
                #and then will be homepages.ecs.vuw.ac.nz/~ian/nwen241/images/
            
                #if absolute
                #e.g.homepages.ecs.vuw.ac.nz/~ian/nwen241/images/GrumoyCat.jpg
                #and then will be homepages.ecs.vuw.ac.nz/~ian/nwen241/images/
                
                #images linked in RELATIVE manner
                if not (root in img): 
                    image_root = (root+img).replace(os.path.basename(root+img), "")
                #images linked in ABSOLUTE manner
                else:
                    image_root = img.replace(os.path.basename(img), "")
                
                #make image directory as necessary
                img_dir = make_dir(image_root, os.path.basename(img))
                
                #images linked in RELATIVE manner
                if not (root in img):
                    #fetch image
                    #No need to relink as HTML markup is relative
                    
                    #use root+img in get to make link absolute
                    get (img_dir, root+img)
                    
                #images linked in ABSOLUTE manner
                else:
                    #fetch image
                    #link it to 'indexName' file
                    get (img_dir, img)
                    
                    #make link name relative
                    #e.g.img_dir as homepages.ecs.vuw.ac.nz/~ian/nwen241/images AND 
                    #image base name as GrumpyCat.jpg so
                    #link name is homepages.ecs.vuw.ac.nz/~ian/nwen241/images/GrumpyCat.jpg 
                    
                    link_name = img_dir+os.path.basename(img)   #whole directory path including name
                    link_name = link_name.replace(root_dir, "")
                    
                    #link files
                    link_files (root_dir+os.path.basename(address), link_name, img)           
        else:
            print ("Network error. URL/webpage does not exist")
            return None

"""
    Fetches a single web page
    Return None if error occurs or if url does not exist
"""
def get (directory,address):
    #check if url AND directory exists
    if url_exist(address) and directory is not None:
        #put address in HTML file with target as 'directory+baseName of address'
        #ASSUMES directory has already been checked for collisions
        return urllib.request.urlretrieve(address, directory+os.path.basename(address))
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
    Re-links absolute links to local links
    This modifies the 'index_name.html' file
    1. Find 'old_link_name' inside 'index_name.html' file
    2. Replace 'old_link_name' with 'new_link_name' which is the local name of file
"""   
def link_files (index_name, new_link_name, old_link_name):
    #The file to be modified must exist
    if os.path.exists(index_name):
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
"""
    Makes directory of folders until NOT exists
    Return None if error occurs
"""
def make_dir (root, file_name):
    #remove protocol identifiers
    if root.startswith('http:'):
        directory = root.replace("http://", "")
    elif root.startswith('https:'):
        directory = root.replace("https://", "")
    
    try:
        #if directory does NOT exist
        if not os.path.exists(directory):
            #make it and return that directory as string
            os.makedirs(directory)
            return directory
        #if it exists
        else:
            #split directory into list of dirs seperated by /
            folders = directory.split("/")
            directory = ""
            counter = 0
            suffix = "."+str(counter)
            
            #update counter while directory exists
            #e.g. if nwen241/images exists --> nwen241.1/images until it does not exist
            while os.path.exists("/".join(folders)+file_name):
                counter+=1
                suffix = "."+str(counter)                
                folders[0] = folders[0].replace("."+str(counter-1), "")+suffix
    
            directory = "/".join(folders)
            
            #if new directory does NOT exist
            if not os.path.exists(directory):
                #make it and return that directory as string
                os.makedirs(directory)
                
            return directory
    except (Exception): #if some error occurs, print error msg
        print (traceback.format_exc())
        print ("Directory write error")
        return None