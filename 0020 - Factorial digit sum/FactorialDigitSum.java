import java.math.BigInteger;

/*
 * Project Euler 20
 * @date 06.04.2019
 */

public class FactorialDigitSum{
    public static void main(String[] args){
        // Number that we are going to get the factorial of it
        int number = 100;
        
        // Calculating the factorial
        BigInteger fact = new BigInteger("1");
        for(int i = 1; i <= 100; i++){
            fact = fact.multiply( BigInteger.valueOf(i));
        }
        
        // calculating sum of the numbers
        String factStr = fact.toString();
        int sum = 0;
        for(int i = 0; i < factStr.length(); i++){
            sum = sum + Character.getNumericValue( factStr.charAt(i) );
        }
        
        // prompting the answer
        System.out.println(sum);
    }
    
}