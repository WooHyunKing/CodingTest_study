import java.util.*;

class Fish {
    int x, y, size, distance; // 거리 필드를 추가

    // 물고기의 좌표, 크기, 거리 초기화하는 생성자
    public Fish(int x, int y, int size, int distance) {
        this.x = x;
        this.y = y;
        this.size = size;
        this.distance = distance; // 거리 정보 추가
    }
}

class Shark extends Fish {
    int eatenFish; // 상어가 먹은 물고기의 수

    // 상어 객체를 초기화하는 생성자
    public Shark(int x, int y, int size) {
        super(x, y, size, 0); // 부모 클래스(Fish)의 생성자를 호출, 거리 정보는 필요 없음
        this.eatenFish = 0; // 처음에는 먹은 물고기 수를 0으로 설정
    }

    // 물고기를 일정 수만큼 먹었을 때 상어가 성장하는 메서드
    public void grow() {
        this.size++; // 상어 크기를 1 증가
        this.eatenFish = 0; // 먹은 물고기 수를 초기화
    }
}

public class BabyShark {
    static int n; // 맵의 크기
    static int[][] area; // 바다 맵
    static int[] dx = {-1, 1, 0, 0}; // 상하좌우 이동 방향 (행 변화량)
    static int[] dy = {0, 0, -1, 1}; // 상하좌우 이동 방향 (열 변화량)

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // 사용자 입력을 받기 위한 Scanner 객체
        n = scanner.nextInt(); // 맵의 크기 입력
        area = new int[n][n]; // 바다 맵 초기화

        Shark shark = null; // 상어 객체를 초기화

        // 바다 맵을 입력받으며 상어의 초기 위치를 찾음
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                area[i][j] = scanner.nextInt(); // 맵의 각 칸 값을 입력받음
                if (area[i][j] == 9) { // 상어의 초기 위치
                    shark = new Shark(i, j, 2); // 상어 객체 생성 (크기는 2로 시작)
                    area[i][j] = 0; // 상어의 초기 위치를 맵에서 0으로 변경
                }
            }
        }

        int totalTime = 0; // 상어가 움직이고 물고기를 먹는 데 걸린 총 시간

        while (true) {
            Fish targetFish = findNearestFish(shark); // 상어가 먹을 수 있는 가장 가까운 물고기를 찾음

            if (targetFish == null) {
                break; // 더 이상 먹을 수 있는 물고기가 없으면 종료
            }

            totalTime += moveShark(shark, targetFish); // 상어를 이동시키고 시간 추가
            shark.eatenFish++; // 먹은 물고기 수를 증가

            if (shark.eatenFish == shark.size) { // 상어가 자신의 크기만큼 물고기를 먹었다면
                shark.grow(); // 상어가 성장
            }
        }

        System.out.println(totalTime); // 총 시간을 출력
    }

    // 상어가 먹을 수 있는 가장 가까운 물고기를 찾는 메서드
    private static Fish findNearestFish(Shark shark) {
        boolean[][] visited = new boolean[n][n]; // 방문 여부를 기록하는 배열
        int[][] distance = new int[n][n]; // 각 칸까지의 거리를 기록하는 배열

        Queue<int[]> queue = new LinkedList<>(); // BFS를 위한 큐
        PriorityQueue<Fish> fishes = new PriorityQueue<>((a, b) -> {
            // 물고기를 거리, 행, 열 순서로 정렬
            if (a.distance != b.distance) return Integer.compare(a.distance, b.distance); // 거리 우선
            if (a.x != b.x) return Integer.compare(a.x, b.x); // 행 우선
            return Integer.compare(a.y, b.y); // 열 우선
        });

        queue.offer(new int[]{shark.x, shark.y}); // BFS의 시작 위치는 상어의 현재 위치
        visited[shark.x][shark.y] = true; // 시작 위치를 방문 처리

        while (!queue.isEmpty()) {
            int[] current = queue.poll(); // 현재 위치를 큐에서 꺼냄
            int cx = current[0]; // 현재 행
            int cy = current[1]; // 현재 열

            for (int i = 0; i < 4; i++) { // 4방향 탐색
                int nx = cx + dx[i]; // 다음 행
                int ny = cy + dy[i]; // 다음 열

                if (nx >= 0 && ny >= 0 && nx < n && ny < n && !visited[nx][ny] && area[nx][ny] <= shark.size) {
                    // 맵 범위 내, 방문하지 않음, 상어 크기 이하인 경우만 이동 가능
                    visited[nx][ny] = true; // 방문 처리
                    distance[nx][ny] = distance[cx][cy] + 1; // 거리를 현재 거리 +1로 설정
                    queue.offer(new int[]{nx, ny}); // 다음 위치를 큐에 추가

                    if (area[nx][ny] > 0 && area[nx][ny] < shark.size) {
                        // 물고기가 있고, 상어 크기보다 작은 경우
                        fishes.offer(new Fish(nx, ny, area[nx][ny], distance[nx][ny])); // 거리 정보를 포함하여 우선순위 큐에 추가
                    }
                }
            }
        }

        return fishes.isEmpty() ? null : fishes.poll(); // 우선순위 큐에서 가장 가까운 물고기를 반환 (없으면 null)
    }

    // 상어를 목표 물고기 위치로 이동시키고 맵을 갱신하는 메서드
    private static int moveShark(Shark shark, Fish fish) {
        int time = fish.distance; // 물고기까지의 거리(시간)
        shark.x = fish.x; // 상어의 행 위치를 물고기의 행으로 갱신
        shark.y = fish.y; // 상어의 열 위치를 물고기의 열로 갱신
        area[fish.x][fish.y] = 0; // 물고기를 먹었으므로 해당 칸을 0으로 설정
        return time; // 이동에 걸린 시간을 반환
    }
}