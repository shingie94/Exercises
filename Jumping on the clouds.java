public static int jumpingOnClouds(int[] c) {
        int n = c.length;
        int total_jumps = 0;

        int i=0;
        while(i<n-1){
            if(i+2 < n && c[i+2] != 1){
                total_jumps++;
                i=i+2;
            }
            else{
                total_jumps++;
                i++;
            }
        }
    return total_jumps;
}
