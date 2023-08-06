import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean as dis
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


class DivisiveAnalysis:
    #Class which implements the DIANA (Divisive Analysis) algorithm and provides an interface for using the implementation.
    def __init__(self,no_clusters):
      self.no_clusters = no_clusters
      self.labels = []
      self.clusters = [0]
    
    def initializeToZero(self,X):
      # Given a dataframe
      # Makes a list of zeros which are the initial labels
      return [0 for i in range(X.shape[0])]

    def cluster_list(self,X,c):
      # Given a dataframe, their respective labels and a single label
      # Returns a list of points which have label 'c' and their respective index
      list = []
      for i,p in enumerate(X):
        if self.labels[i] == c:
          list.append([p[k] for k in range(len(p))] + [i])
      return np.array(list)

    def diameterOfCluster(self, x):
      # Given a dataframe
      # Returns the maximum distance between two points in it
      distances = [0] # Initialized with a zero for clusters of 1 point that won´t enter the loop below
      for i in range(x.shape[0]):
        for j in range(i+1,x.shape[0]):
          distances.append(dis(x[i],x[j]))
      return max(distances)


    def largest_cluster(self, X):
      # Given a dataframe, its labels, and a list of unique labels contained in labels
      # Returns the label of the biggest cluster (the one with the biggest diameter)
      max_val = 0
      max_cluster = 0
      for c in self.clusters:
        diam = self.diameterOfCluster(self.cluster_list(X,c))
        if diam > max_val:
          max_val = diam
          max_cluster = c
      return max_cluster
    
    def get_clusters(self):
      return self.clusters

    def The_average_point(self,p,x):
      # Given a point and a dataframe
      # Returns the mean distance between the point and each point in the dataframe
      point_in_cluster = False

      sum_distances = 0
      for point in x:
        for i in range(len(p)):
          if point[i] == p[i]:
            point_in_cluster = True
        sum_distances += dis(p,point)

      if point_in_cluster:
        if len(x) == 1:  
              return 0
        else:
          return sum_distances/(len(x) - 1)  # we subtract 1 p is part of x 
      else:
        return sum_distances/(len(x)) 

    def splinter(self,x_i):
      # Given a dataframe with (x,y,z...,i) where i is the index
      # Returns the index of the point in the dataframe which in average is furthest apart from the rest
      splinter = 0
      max_avg = 0
      
      for point in x_i:
        The_average = self.The_average_point(point[:-1],x_i[:,:-1])
        if The_average > max_avg:
          max_avg = The_average
          splinter = point[len(point)-1]
      return int(splinter)

    def a_splinter(self,p,U,D):
      # Given a point, the father dataframe and the splinter dataframe
      # Returns True if the point should be in the splinter dataframe using the average distance
      if self.The_average_point(p,D) < self.The_average_point(p,U):
        return True
      else:
        return False


    def create_dendrogram(self,X):
      #Function to create the dendrogram using the linkage matrix and save it to a file.
      fig = plt.figure(figsize=(18, 8))
      plt.title("Dendrogram - Divisive Clustering")
      Z = linkage(X, 'ward')
      dendrogram(Z, orientation='top', labels=self.labels)
      fig.savefig('DIANA\dendrograms\dendrogram.png')
      plt.show()

    def fit(self,X): 
      if X.shape[0] < self.no_clusters:
        import warnings
        warnings.warn("The number of clusters can't be larger than number of points in the dataframe")
        return None

      X = np.array(X)

      self.labels = self.initializeToZero(X)

      for z in range(self.no_clusters-1):

        # Get the largest cluster
        majorClusterLabel = self.largest_cluster(X)
        majorClusterList = self.cluster_list(X,majorClusterLabel)

        # Get the splinter that makes your new cluster
        disi = self.splinter(majorClusterList)
        self.clusters.append(self.clusters[-1]+1) 
        self.labels[disi] = self.clusters[-1]
        newClusterList = self.cluster_list(X,self.clusters[-1])
        m = newClusterList.copy()
        M = majorClusterList.copy()


        # pass the points to the splinter cluster
        changed = True
        max_changes = X.shape[0]*4
        changes = 0
        while changed == True and changes != max_changes:
          changed = False
          for i in range(len(majorClusterList)):
            if self.labels[int(majorClusterList[i][-1])] == majorClusterLabel:
              if self.a_splinter(majorClusterList[i][:-1],M[:,:-1],m[:,:-1]):
                changed = True
                self.labels[int(majorClusterList[i][-1])] = self.clusters[-1]
                M = self.cluster_list(X,majorClusterLabel)
                m = self.cluster_list(X,self.clusters[-1])
            else:
              if not self.a_splinter(majorClusterList[i][:-1],M[:,:-1],m[:,:-1]):
                changed = True
                self.labels[int(majorClusterList[i][-1])] = majorClusterLabel
                M = self.cluster_list(X,majorClusterLabel)
                m = self.cluster_list(X,self.clusters[-1])
                changes += 1

      return(list(self.labels))



if __name__ == '__main__':
    pass
