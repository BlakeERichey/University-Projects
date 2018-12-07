class Traversal
{
  public void preOrder(BTNode n, int k)
  {
    if (n != null)
    {
      process(n, k);
      preOrder(n.getLeft(), k+1);
      preOrder(n.getRight(), k+1);
    }
    else
    {
      // error(k);
    }
  }


  public void inOrder(BTNode n, int k)
  {
    if (n != null)
    {
      inOrder(n.getLeft(), k+1);
      process(n, k);
      inOrder(n.getRight(), k+1);
    }
    else
    {
      //error(k);
    }
  }



  public void postOrder(BTNode n, int k)
  {
    if (n != null)
    {
      postOrder(n.getLeft(), k+1);
      postOrder(n.getRight(), k+1);
      process(n, k);
    }
    else
    {
      //error(k);
    }
  }


  private void process (BTNode n, int k)
  {
    for (int i=0; i<k; i++)
    {
      System.out.print("  ");
    }
    System.out.println(n.getData());
  }


  private void error(int k)
  {
    for (int i=0; i<k; i++)
    {
      System.out.print("  ");
    }
    System.out.println("<null>");
  }
}