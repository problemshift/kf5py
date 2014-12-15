#Requires kf5py.py, matplotlib, numpy
#Version 0.01 by Fernando Diaz del Castillo
#Count contributions by a user or group of users
#Inspired by the "Contribution" Analytic Tool in KF 4.x by WILLIAM SHAKESPEARE)

from datetime import datetime
from kf5py import connection
from matplotlib import pyplot
import numpy


class ContributionCount:
    """Contribution count for a view.
    start_date, end_date str("YYYY-MM-DD")
    """
    
    def __init__(self, baseURL, username, password, sectionIds, start_date='', end_date=''):
        self.kf_connection = connection(baseURL, username, password)
        self.post_count = {}
        try:
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
            #print(self.start_date)
        except ValueError:
            self.start_date = datetime.strptime("1900-01-01", "%Y-%m-%d")
        try:
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
            #print(self.end_date)
        except ValueError:
            self.end_date = datetime.now()

        if self.kf_connection.is_valid():
            for section in sectionIds:
                for post in self.kf_connection.get_posts_by_sectionid(section):
                    created_date = datetime.strptime(post['created'], "%b %j, %Y %I:%M:%S %p")
                    if created_date < self.end_date and created_date > self.start_date: 
                        for author in post['authors']:
                            if author['guid'] in self.post_count:
                                self.post_count[author['guid']] += 1
                            else:
                                self.post_count[author['guid']] = 1
    
    def get_post_count(self):
        """Return the number of posts by each user.
        post_count = {user_id: number_of_posts}"""
        return self.post_count
    
    def plot_post_count(self):
        print(self.post_count.keys())
        index = numpy.arange(len(self.get_post_count().keys()))
        contribution_counts = self.get_post_count().values()
        bar_width = 0.4
        bar_graph = pyplot.subplot()
        rect = bar_graph.bar(index, contribution_counts, bar_width)
        
        # add some text for labels, title and axes ticks
        bar_graph.set_ylabel('Number of contributions')
        bar_graph.set_title('Contributions by author')
        bar_graph.set_xticks(index+bar_width)
        bar_graph.set_xticklabels(self.get_post_count().keys())
             
             
        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                bar_graph.text(rect.get_x()+rect.get_width()/2., 1.3*height, '%d'%int(height),
                        ha='center', va='bottom')
        
        autolabel(rect)
        pyplot.show()
        #print(contribution_counts)
        ##return self.num_data_points
        