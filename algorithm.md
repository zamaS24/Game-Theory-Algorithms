### General algorithm
```bash
# This is the pseudo algorithm of our approach
Generate random data clusters #(let it be 4)
initialize random centroids and assignation of points


for each point in the dataset

    initialize payoff_matrix
    calculate cost for each combination of cluster-point strategies
    call nash-equilibrium

    based-on nash-equilibrium
        update the point assigned centroid
        update centroid positions 

    if(converged) # Number of epochs or criteria satisfied or positions aren't changed
        quitt
```


### about cost functions
given a combination of a strategies (profile in the payoff matrix)
let it be (C1,S1), meaning that A point chooses C1 (cluster1 to be assigned to), and Centroid chooses S1 strategy let it be the mean of cluster points.

we will evaluate the point based on the distance to this cluster when : 
    the cluster chooses the mean strategy and the point chooses cluster1
    based on the 1/distance of the point to this cluster

we will evaluate the centroid based on the sum of distances to every point that belong the cluster associated to this centroid when : 
    this cluster contains point1 and chooses mean strategy 
    based on the 1/(sum of distances of points from this cluster / number of points of the cluster)

```bash 
    
```