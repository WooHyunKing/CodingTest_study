import java.io.*;
import java.util.*;

public class Backjoon1260 {

    static List<List<Integer>> graph;
    static boolean[] visited_dfs;
    static boolean[] visited_bfs;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();

        for(int i=0; i<N+1; i++){
            graph.add(new ArrayList<>());
        }

        visited_dfs = new boolean[N+1];
        visited_bfs = new boolean[N+1];

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph.get(x).add(y);
            graph.get(y).add(x);
        }

        for(List<Integer> edges : graph){
            Collections.sort(edges);
        }

        dfs(V);

        System.out.println();
        
        bfs(V);

    }

    public static void dfs(int start){
        visited_dfs[start] = true;

        System.out.print(start+" ");

        for(int i : graph.get(start)){
            if(!visited_dfs[i]){
                dfs(i);
            }
        }
    }

    public static void bfs(int start){
        Queue<Integer> queue = new LinkedList<>();

        visited_bfs[start] = true;

        queue.add(start);

        while(!queue.isEmpty()){
            int node = queue.poll();
            System.out.print(node + " ");

            for (int i : graph.get(node)){
                if (!visited_bfs[i]){
                    visited_bfs[i] = true;
                    queue.add(i);
                }
            }
        }
    }
}
