class Solution {
    public int reverse(int x) {
        int y = x;
       if(x < 0){
        x *=-1;
       }
        String temp = Integer.toString(x);
        char [] str = temp.toCharArray();
        char [] reversedx = new char[str.length];
        int j = 0;
        for ( int i = str.length-1 ; i >=0 ; i --){
            reversedx [j] = str [i];
            j++; 

        }
        temp = String.valueOf(reversedx);
        try{
        int result = Integer.parseInt(temp);
        if(y<0){
            result*=-1;
            
        }
        return result;
        } 
        catch(Exception e){
            return 0;
        }
        
    }
    
}