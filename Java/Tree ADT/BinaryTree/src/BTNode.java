class BTNode
{
  private String data;
  private BTNode left, right;

  public BTNode(String s)
  {
    data = s;
    left = null;
    right = null;
  }

  public String getData()
  {
    return data;
  }

  public void setData(String s)
  {
    data = s;
  }

  public BTNode getLeft()
  {
    return left;
  }

  public void setLeft(BTNode n)
  {
    left = n;
  }

  public BTNode getRight()
  {
    return right;
  }

  public void setRight(BTNode n)
  {
    right = n;
  }

}