import java.io.*;
import java.util.*;
import java.awt.*;

class Fish {
    int x, y, size, distance;

    public Fish(int x, int y, int size, int distance){
        this.x = x;
        this.y = y;
        this.size = size;
        this.distance = distance;
    }
}

class Shark extends Fish{

    int eatenFish;

    public Shark(int x, int y, int size){
        super(x,y,size,0);
        this.eatenFish = 0;
    }

    public void grow(){
        this.eatenFish = 0;
        this.size++;
    }
}

public class Baekjoon16236 {

    static int N;
    static int[][] area;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        area = new int[N][N];

        int answer = 0;

        Shark shark = null;

        for(int i=0; i<N; i++){

            StringTokenizer st = new StringTokenizer(br.readLine());

            for(int j=0; j<N; j++){
                area[i][j] = Integer.parseInt(st.nextToken());

                if(area[i][j] == 9){
                    shark = new Shark(i,j,2);
                    area[i][j] = 0;
                }
            }
        }

        while(true){

            Fish nextFish = findNearestFish(shark);

            if(nextFish == null)
                break;

            moveShark(shark, nextFish);

            answer += nextFish.distance;

            shark.eatenFish ++;
            
            if(shark.eatenFish == shark.size)
                shark.grow();

        }

        System.out.println(answer); 
        
    }

    public static Fish findNearestFish(Shark s){
        boolean [][] visited = new boolean[N][N];
        int [][] distance = new int[N][N];

        Queue<Point> queue = new LinkedList<>();
        PriorityQueue<Fish> fishes = new PriorityQueue<>((a,b)->{
            if(a.distance != b.distance) return Integer.compare(a.distance, b.distance);
            if(a.x != b.x) return Integer.compare(a.x, b.x);
            return Integer.compare(a.y, b.y);
        });

        queue.offer(new Point(s.x,s.y));
        visited[s.x][s.y] = true;

        while(!queue.isEmpty()){
            Point current = queue.poll();
            int cx = current.x;
            int cy = current.y;

            for(int i=0; i<4; i++){
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if(0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny] && area[nx][ny] <= s.size){

                    visited[nx][ny] = true;
                    distance[nx][ny] = distance[cx][cy] + 1;
                    queue.offer(new Point(nx,ny));

                    if(area[nx][ny] > 0 && area[nx][ny] < s.size){
                        fishes.offer(new Fish(nx,ny,area[nx][ny],distance[nx][ny]));
                    }

                }
            }
        }

        return fishes.isEmpty() ? null : fishes.poll();

    }

    public static void moveShark(Shark s, Fish f){
        s.x = f.x;
        s.y = f.y;
        area[f.x][f.y] = 0;
    }

    
}
