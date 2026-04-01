# WGU Package Delivery System
###  Created by Connor Natiuk


## A) Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the package ID as input and inserts each of the following data components into the hash table:
The solution to this is located in the Hash_Table class along with the Data_Retrieval class, as the Hash_Table class sets up the table, hash key method, etc, as the Data_Retrieval class creates Package objects and inserts the Package into the hash table (along with its ID as the key), including the components outlined in the step A.

## B) Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:
The solution to this is located in the Hash_Table class starting at line 37.

## C) Write an original program that will deliver all packages and meet all requirements using the attached supporting documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and “WGUPS Package File.”
The solution to this is found in main.py, and the data used for the program is found in the Data folder (Distances.csv, Packages.csv, Locations.csv).

Comments in the code are found throughout the project and each class is documented thoroughly.

## D) Provide an intuitive interface for the user to view the delivery status (including the delivery time) of any package at any time and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
The solution to this is found in the Screenshots folder, and the UI is found in User_Interface.py.

## E) Provide screenshots showing successful completion of the code that includes the total mileage traveled by all trucks.
The solution to this is the Final Delivery Logs.png and Mileage Info.png inside of the Screenshots folder.

## F) Justify the package delivery algorithm used in the solution as written in the original program by doing the following:
1.) One strength of this algorithm is that it is self-adjusting and keeps track of which locations it has already visited, rather than trying to find the best possible path to every package each iteration (this would be O(n!)). Because of this, it operates at O(N^2) time complexity. A second strength is that it is adaptable to certain constraints. If locations update, distances change, or another package is added, it can easily adapt since it makes decisions on the spot rather than in advance.

2.) The algorithm does indeed meet ALL requirements and constraints outlined in the task.

3.) An algorithm that could have been used could be the 2-Opt Algorithm. This algorithm iterates on a path where the distances of each edge are already known. It swaps or combines paths to calculate the most optimal route, or until a certain "cost" has been reached (Davis, 2022). This would work since the distances between each location are already known and a graph can be made to implement this algorithm. A difference however between each of these algorithms is that the nearest-neighbor algorithm is local and only cares about the locations that are connected to it. It constructs a path based on the nodes nearest to its current node, where as the 2-opt algorithm creates an optimal route based on the global scope of the graph and updates after an initial optimal final route has been created.

Another algorithm that could have been used is the Clarke-Wright Savings Algorithm. The algorithm takes two routes, from the hub to a certain location and back to the hub (H -> L1 -> H), (H -> L2 -> H), and figures out how much cost it would save by merging the two trips (H -> L1 -> L2 -> H) (Odedra, 2025). It does this repeatedly, calculating and merging pairs of nodes that result in the most optimal route. This would work for this task because the locations and distances are already known from the hub to any other location, and locations can be merged to find the most optimal route. This differs from the nearest-neighbor algorithm in that instead of finding the nearest location in real time, it calculates the savings of a route before making a decision, and uses a global scope rather than a local scope.

## G) Describe what you would do differently, other than the two algorithms identified in part F3, if you did this project again, including details of the modifications that would be made.

Looking back, I probably could have made a more robust system to handle the special notes of each package. For instance, I would have made a UI that could take the special notes given to it and assign certain delivery constraints to the package (maybe a code ID for a "late package" or a "wrong address", etc). I also think I could have created an entirely separate class for the loading of the trucks rather than doing it all manually inside of main.py, essentially making it more readable.

## H) Verify that the data structure used in the solution meets all requirements in the scenario.
The data structure used in this assignments affirms ALL requirements for the scenario. It allows packages to be loaded and delivered, with O(1) access time to needed information about packages and locations.

Another data structure that could have been used is a balanced binary search tree. Essentially all packages would be stored in nodes, with smaller ID's to the left and larger ID's to the right. This allows for an O(log N) time complexity for accessing the package and location information, and is more memory efficient than a hash table The difference between the data structures is that while the hash table will use a mathematical function to find the location of a bucket in the table, the BST will "search" comparatively through the list to find the location of the desired data. It will still meet all the requirements in this assignment.

Lastly you could create an adjacency list (although it would have to be from scratch as most adjacency lists use built in dictionaries and that would be against the requirements). You could create a list of packages and their locations, with nested lists of their adjacent locations, distances, etc. to solve for all requirements. Unlike a hash table, the While the time complexity of data access is larger O(V + E), the memory overhead may be more efficient, since inefficient bucket usage and collisions can increase memory usage, but this is not always the case. Once again, the hash table uses a hash function to find the location of a bucket and its data, while the adjacency list will search through the graph by traversal, resulting in far slower lookup times. It will still meet all the requirements in the assignment.

### SOURCES

Davis, A. (2022, May 18). Traveling salesman problem with the 2-opt algorithm. Medium. https://slowandsteadybrain.medium.com/traveling-salesman-problem-ce78187cf1f3

Odedra, R. (2025, November 10). Clarke Wright algorithm for EV routing research. Medium. https://medium.com/@ranjitodedra/clarke-wright-algorithm-for-ev-routing-research-2771473bcab8

