public class LexPermutations{
    
    public static void main(String[] args){
        String chars = "0123456789";
        long index = 1000000;
        
        String answer = chars;
        
        for(int i = 0; i < answer.length() - 1; i++){
            long fact = factorial(answer.length() - (i + 1) );
            
            int replaceIndex = (index % fact == 0) ? (int)(index / fact) - 1 : (int)(index / fact);
            System.out.println( index + "/" + fact + " = " + replaceIndex);
            index = index - (replaceIndex * fact);
            
            // organizing answer so far
            String str = "";
            for(int j = 0; j < i; j++){
                str = str + answer.charAt(j);
            }
            str = str + answer.charAt(i + replaceIndex);
            for(int j = i; j < answer.length(); j++){
                str = str + (j != replaceIndex + i ? answer.charAt(j) : "");
            }
            
            answer = str;
            System.out.println(answer);
        }
        
    }
    
    // factorial function
    public static long factorial(int n){
        int answer = 1;
        
        for(int i = 2; i <= n; i++){
            answer *= i;
        }
        
        return answer;
    }
}