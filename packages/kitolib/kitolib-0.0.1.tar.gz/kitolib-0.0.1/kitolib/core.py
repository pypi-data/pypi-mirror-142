import matplotlib.pyplot as plt
import numpy as np

def plot_scatter(X, y=None, centroids=None, title=None):
    d_size = 3
    c_size = 30    
    plt.figure(figsize=(5, 5))
    
    if y is not None:
        y_unq = np.unique(y)
        for label in y_unq:
            plt.scatter(X[y == label, 0], X[y == label, 1], label=label, s=d_size)
    else:
        plt.scatter(X[:, 0], X[:, 1], s=d_size)
        
    if centroids is not None:
        plt.scatter(centroids[:, 0] , centroids[:, 1] , s=c_size, c='black')        
        
    plt.title(title)
        
    plt.show()


class KMeans:
    def __init__(self, k, max_iterations=100):
        self._k = k
        self._max_iterations = max_iterations
        
    def init_clusters(self, X):
        return np.random.permutation(X)[:self._k]
    
    def calculate_distances(self, X, centroids):
        distances = np.zeros((X.shape[0], self._k))
        for c in range(self._k):
            distances[:, c] = np.square(np.linalg.norm(X - centroids[c], axis=1))        
        return distances
    
    def find_closest_cluster(self, distances):
        return np.argmin(distances, axis=1)
    
    def adjust_centroids(self, X, y):
        new_centroids = np.zeros((self._k, X.shape[1]))
        for c in range(self._k):
            new_centroids[c] = np.mean(X[y == c], axis=0)
        return new_centroids
        
    def fit(self, X, plot_2d_conv=False):
        centroids = self.init_clusters(X)
        
        for i in range(self._max_iterations):
            old_centroids = centroids
            distances = self.calculate_distances(X, old_centroids)
            y = self.find_closest_cluster(distances)
            
            if plot_2d_conv:
                plot_scatter(X, y, old_centroids, title=f"Iteration {i + 1}")
            
            centroids = self.adjust_centroids(X, y)           
            
            if (old_centroids == centroids).all():
                print(f"Converged with {i + 1} iterations")
                break
        self._centroids = centroids
                
    def predict(self, X):
        distances = self.calculate_distances(X, self._centroids)
        return self.find_closest_cluster(distances)