import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;  

//Example use:
//Columns test = new Columns();
//test.addLine("One", "Two", "Three", "Four");
//test.addLine("1", "2", "3", "4");
//test.print();
//System.out.println(test.toString());
//Displays: 
//One Two Three Four 
//1   2   3     4  
//credit @ candied_orange
public class Columns {

    List<List<String>> lines = new ArrayList<>();
    List<Integer> maxLengths = new ArrayList<>();
    int numColumns = -1;

    public Columns addLine(String... line) {

        if (numColumns == -1){
            numColumns = line.length;
            for(int column = 0; column < numColumns; column++) {
                maxLengths.add(0);
            }
        }

        if (numColumns != line.length) {
            throw new IllegalArgumentException();
        }

        for(int column = 0; column < numColumns; column++) {
            int length = Math
                .max( 
                    maxLengths.get(column), 
                    line[column].length() 
                )
            ;
            maxLengths.set( column, length );
        }

        lines.add( Arrays.asList(line) );

        return this;
    }

    public void print(){
        System.out.println( toString() );
    }

    public String toString(){
        String result = "";
        for(List<String> line : lines) {
            for(int i = 0; i < numColumns; i++) {
                result += pad( line.get(i), maxLengths.get(i) + 1 );                
            }
            result += System.lineSeparator();
        }
        return result;
    }

    private String pad(String word, int newLength){
        if(newLength < 40) {
          newLength = 40;
        }
        while (word.length() < newLength) {
            word += " ";            
        }       
        return word;
    }
}