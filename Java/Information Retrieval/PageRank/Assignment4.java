//Blake Richey
//COSC 4315 Information Knowledge Management
//Dr. Leanard Brown
//This program is designed to find the page rank of 6 nodes given a probability matrix.
//The program take input from the user as to how many iterations to perform PageRanking
//The program then outputs the PageRank//probability of being at each node

public class Assignment4 {

  public static void main(String[] args) {
    double alpha = .25;
    int numNodes = 6;
    
    double probMatrix[][] = {
        {0,         1,     0,     0, 0,     0},
        {0,         0,     0, 1/2.0, 0, 1/2.0},
        {1/3.0, 1/3.0,     0, 1/3.0, 0,     0},
        {0,         0,     0,     0, 0,     1},
        {1/4.0,     0, 1/4.0, 1/4.0, 0, 1/4.0},
        {0,         0,     0,     0, 0,     0},
    };
    
    double probLocation[] = common.initArray(numNodes, 1/6.0);  //holds prob of being at Node
    
    int numIterations = -1000000;       //return value if error is caught by stringToInt
    while (numIterations == -1000000) { //Request number of iterations
      numIterations = common.stringToInt(common.Input("Enter number of Iterations"));
      if(numIterations == -1000000) { common.Alert("Invalid entry. Type must be an Int"); }
    }
    
    for(int iteration = 0; iteration < numIterations; iteration++) {        //number of iterations
     
      double newProbLocation[] = common.initArray(numNodes, 0);
      for(int i = 0; i < numNodes; i++) { //for every node in probLocation
        double sum = 0;
        for(int index = 0; index < numNodes; index++) { //find sum to multiple (1-alpha)
          sum += probMatrix[index][i]*probLocation[index];
        }
        newProbLocation[i] = alpha/numNodes + (1-alpha) * sum;
      }
      
      for(int index = 0; index < numNodes; index++) {   //assign new prob of being at Node
        probLocation[index] = newProbLocation[index];
      }
    }
    
    common.Alert(common.arrayToString(probLocation, ",\n"));

  }

}
