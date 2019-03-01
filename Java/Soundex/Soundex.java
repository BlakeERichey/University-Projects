//implements soundex algorithm on a word to generate a phonetic hash
public class Soundex {

  public static void main(String[] args) {
    common blake = new common();
    
    String word = common.Input("Word to be hashed?");
    String hash = "";
    if(word.length() > 0) { //first letter of hash
      hash = common.getLetter(word, 0);
    }
    
    for(int x = 1; x<word.length(); x++) { //remainder of char hashing
      char letter = Character.toLowerCase(word.charAt(x));
      if(common.contains("aeiouhwy", letter)) {
        hash += "0";
      }else if(common.contains("bfpv", letter)) {
        hash += "1";
      }else if(common.contains("cgjkqsxz", letter)) {
        hash += "2";
      }else if(common.contains("dt", letter)) {
        hash += "3";
      }else if(common.contains("l", letter)) {
        hash += "4";
      }else if(common.contains("mn", letter)) {
        hash += "5";
      }else if(common.contains("r", letter)) {
        hash += "6";
      }
    }
    
    //remove repeat characters
    hash = common.removeRepeats(hash);
    //remove 0s
    hash = common.removeZeros(hash);
    //ensure string is of length 4
    hash = common.padString(hash, 4, "0");
    //output hash
    common.Output("Hash: " + hash.substring(0,4));
  }

}
