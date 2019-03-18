import java.util.*;


public class Assignment1 {

   public static void main (String[] args) {
      Scanner scan = new Scanner(System.in);
      System.out.println("Enter a positive integer for x");
      int x = scan.nextInt();
      System.out.println("Enter a positive integer for y");
      int y = scan.nextInt();

      VeryLargeInteger v1 = new VeryLargeInteger(x);
      VeryLargeInteger v2 = new VeryLargeInteger(x);

      System.out.println(v1.getString());
      System.out.println(v1.length());
      System.out.println(v1.numTrailZero());
      System.out.println(v1.lastNonZero());
      v1.multiply(3);
      System.out.println(v1.getString());
      
      /*
      // Compute x!
      for (int i=x-1; i>1; i--) {
         v1.multiply(i);
      }
      System.out.println("Factorial is " + v1.getString());

      // Compute x^y
      for (int i=1; i<y; i++) {
         v2.multiply(x);
      }
      System.out.println("Power is " + v2.getString());

      // Compute stats
      System.out.println();
      System.out.println();
      System.out.println("Factorial");
      System.out.println("Length: " + v1.length());
      System.out.println("Zeros:  " + v1.numTrailZero());
      System.out.println("Ending: " + v1.lastNonZero());

      System.out.println();
      System.out.println("Power");
      System.out.println("Length: " + v2.length());
      System.out.println("Zeros:  " + v2.numTrailZero());
      System.out.println("Ending: " + v2.lastNonZero());
      */
   }
}

