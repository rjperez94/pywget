#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request, os, requests, traceback

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
    Fetches a single web page
    Return None if error occurs or if url does not exist
"""
def parsed_url (address):
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
        #if this address not found
        print ("Network error. URL/webpage does not exist")
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