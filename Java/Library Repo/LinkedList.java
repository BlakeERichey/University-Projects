public class LinkedList {
  
  private Node head;
  private Node tail;
  private int  length;
  
  public LinkedList() {
    head = null;
    tail = null;
    length = 0;
  }
  
  public LinkedList(String data) {
    Node head = new Node(data);
    tail = head;
    length = 1;
  }
  
  public void addNode(String data) {
    if(length == 0) { //empty list
      head = new Node(data);
      tail = head;
      length = 1;
    }else if(length == 1) {
      Node tempNode = new Node(data);
      tail = tempNode;
      head.setNext(tail);
      tail.setPrevious(head);
      length++;
    }else {
      Node tempNode = new Node(data);
      tail.setNext(tempNode);
      tempNode.setPrevious(tail);
      tail = tempNode;
      length++;
    }
  }
  
  //returns node that contains the same data as is queried if it exist
  public Boolean isInList(String data) {
    Node currentNode = head;
    if(length != 0) {
      while(currentNode.getNext() != null) {
        if(currentNode.getData().toString().equals(data.toString())) {
          return true;
        }
        currentNode = currentNode.getNext();
      }
      
      //test last node
      if(currentNode.getData().toString().equals(data.toString())) {
        return true;
      }
    }
    return false;
  }
  
  public int getLength() {
    return length;
  }
  
  public String[] getList() {
    String[] list = new String[length];
    
    Node currentNode = head;
    int index = 0;
    //add items from linked list into an array
    while(currentNode.getNext() != null) {
      list[index++] = currentNode.getData();
      currentNode = currentNode.getNext();
    }
    
    //add last node
    list[length-1] = currentNode.getData();
    
    return list;
  }
}
