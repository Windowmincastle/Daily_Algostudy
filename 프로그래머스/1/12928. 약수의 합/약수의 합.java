class Solution {
    
    public int solution(int n) {
        
        int total = 0;
        
        for(int i=1; i <= n; i++){
            
            if( n % i == 0 ){
                total += i;
            }
            
        }
        
        int answer = total;
        
        return answer;
    }
    
    
}