import java.io.*;
import java.util.*;

public class Baekjoon2606 {

    static List<List<Integer>> graph;
    static boolean[] visited;
    static int count = -1;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        visited = new boolean[n+1];

        graph = new ArrayList<>();

        for(int i=0; i<n+1; i++){
            graph.add(new ArrayList<>());
        }

        for(int i=0; i<m; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph.get(x).add(y);
            graph.get(y).add(x);
        }

        // dfs(1);
        bfs(1);
        System.out.println(count);
        
    }

    public static void dfs(int start){

        visited[start] = true;
        count++;

        for(int i : graph.get(start)){
            if(!visited[i])
                dfs(i);
        }
    }

    public static void bfs(int start){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;

        count++;

        while(!queue.isEmpty()){
            int node = queue.poll();

            for(int i : graph.get(node)){
                if(!visited[i]){
                    visited[i] = true;
                    count++;
                    queue.add(i);
                }
            }
        }
    }
}
