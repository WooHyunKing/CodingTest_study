import java.io.*;
import java.util.*;
import java.awt.Point;

public class Baekjoon2178 {

    static int[][] area;
    static int[][] distance;
    static boolean[][] visited;

    static int N;
    static int M;

    static int[] dx = {0,0,-1,1};
    static int[] dy = {-1,1,0,0};
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        area = new int[N][M];
        visited = new boolean[N][M];
        distance = new int[N][M];

        for(int i=0; i<N; i++){
            String s = br.readLine();
            for(int j=0; j<M; j++){
                area[i][j] = s.charAt(j)-'0';
            }
        }

        bfs(0,0);

        System.out.print(distance[N-1][M-1]);
    }

    public static void bfs(int x, int y){
        Queue<Point> queue = new LinkedList<>();

        queue.add(new Point(x,y));

        visited[x][y] = true;
        distance[x][y] = 1;

        while(!queue.isEmpty()){
            Point p = queue.poll();
            for(int i=0; i<4; i++){
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];

                if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny] && area[nx][ny] == 1){
                    visited[nx][ny] = true;
                    queue.add(new Point(nx,ny));
                    distance[nx][ny] = distance[p.x][p.y] + 1;
                }
            }
        }
    }
}
