//Bidirectional Node Class
class Node
{
  private String data;
  private Node next;
  private Node previous;

  public Node()
  {
    data = "";
    next = null;
  }

  public Node(String x)
  {
    data = x;
    next = null;
  }

  public String getData()
  {
    return data;
  }

  public Node getNext()
  {
    return next;
  }

  public void setData(String x)
  {
    data = x;
  }

  public void setNext(Node n)
  {
    next = n;
  }
  
  public void setPrevious(Node n) {
    previous = n;
  }
  
  public Node getPrevious() {
    return previous;
  }
}