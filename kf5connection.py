import json
import warnings

import requests


class kf5connection:
    """Handle connections to the KF5 API"""

    def __init__(self,baseUrl,username,password):
        self.valid = False;
        if baseUrl[-1:] != '/':
            warnings.warn('Adding / to baseUrl',RuntimeWarning)
            baseUrl = baseUrl + '/'
        auth = requests.post(baseUrl + 'rest/account/userLogin', data={'userName': username, 'password': password})
        if auth.status_code == 200:
            self.valid = True;
            self.baseUrl = baseUrl
            self.username = username
            self.password = password
            self.cookies = auth.cookies
            self.json = json.loads(auth.text)
            self.sectionTitleById = {}
            self.sectionIdByTitle = {}
            for e in self.json:
                self.sectionTitleById[e['sectionId']] = e['sectionTitle']
                self.sectionIdByTitle[e['sectionTitle']] = e['sectionId']
            self.postsBySectionId = {}

    def is_valid(self):
        """ Is the connection valid? """
        return self.valid;

    def get_section_ids(self):
        """ Return the user's section IDs. """
        return self.sectionTitleById.keys()

    def get_section_id_by_title(self,sectionTitle):
        """ Return the ID of a section given its title. """
        return self.sectionIdByTitle.get(sectionTitle)
    
    def get_section_posts_by_id(self,sectionId):
        """ Return the posts in a section given the section's ID.  Some memoization is used. """
        if sectionId not in self.postsBySectionId:
            posts = requests.get(self.baseUrl + 'rest/content/getSectionPosts/%s' %  sectionId,cookies=self.cookies)
            self.postsBySectionId[sectionId] = json.loads(posts.text)
        return self.postsBySectionId[sectionId]

    def get_section_posts_by_title(self,sectionTitle):
        """ Return the posts in a section given the section's title. """
        return self.getSectionPostsById(self.getSectionIdByTitle(sectionTitle))

