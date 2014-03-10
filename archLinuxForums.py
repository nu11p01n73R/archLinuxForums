#!/usr/bin/python2

import urllib2
from bs4 import BeautifulSoup
import re

class ArchLinuxForums:
    def __init__(self,noPosts):
        self.url = "https://bbs.archlinux.org/viewforum.php?id="
        self.forumHead = {23:'Newbie Corner',17:'Installation',8:'Networking, Server and Protection',50:'System Administration'}
        self.forumId = (23,17,8,50)
        self.noSticky = {23:6,17:0,8:1,50:1}
        self.output = {}
        self.noPosts = noPosts
        self.getAllPages()
        self.printPosts()
    
    def getAllPages(self):
        for Id in self.forumId:
            page = self.getPage(Id)
            self.output[Id] = self.parsePage(page)


    def getPage(self,Id):
       request = urllib2.Request(self.url+str(Id))
       response = urllib2.urlopen(request)
       page = response.read()
       return page
    
    def parsePage(self,page):
        soup = BeautifulSoup(page)
        tags = soup.find_all('div') 
        posts = []
        for tag in tags:
            try:
                if tag['class'] == ['tclcon']:
                    posts.append(tag.a.string)      
            except KeyError:
                pass
        return posts

    def printPosts(self):
        for Id in self.forumId:
            print
            print self.forumHead[Id]
            print 
            posts = self.output[Id]
            for post in posts[self.noSticky[Id]:self.noSticky[Id]+self.noPosts+1]:
                print post

forum = ArchLinuxForums(10)
