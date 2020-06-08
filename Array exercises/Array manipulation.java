static long arrayManipulation(int n, int[][] queries) {
        long [] outputarray = new long[n+2];

        for(int i=0;i<queries.length;i++){
            int a = queries[i][0];
            int b = queries[i][1];
            int k = queries[i][2];
            outputarray[a] += k;
            outputarray[b+1] -= k;
        }
        long max = getMax(outputarray);
        return max;


    }

    private static long getMax(long[] inputarray){
        long max = Long.MIN_VALUE;
        long sum = 0;

        for(int i=0;i<inputarray.length;i++){
            sum += inputarray[i];
            max = Math.max(max,sum);
        }
        return max;
    }
