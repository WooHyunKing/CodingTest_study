import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Truck{

    private int arrival;
    private int departure;

    public void setArrival(int arrival){
        this.arrival = arrival;
    }

    public int getArrival(){
        return this.arrival;
    }

    public void setDeparture(int departure){
        this.departure = departure;
    }

    public int getDeparture(){
        return this.departure;
    }


    public Truck(int arrival, int departure){
        this.arrival = arrival;
        this.departure = departure;
    }
    
}

class ParkingFeeCalculator{
    private int A;
    private int B;
    private int C;
    private int[] timeTable;

    public ParkingFeeCalculator(int A, int B, int C){
        this.A = A;
        this.B = B;
        this.C = C;
        this.timeTable = new int[101];
    }

    public void parkTruck(Truck truck){
        for(int i = truck.getArrival(); i < truck.getDeparture(); i++){
            timeTable[i] += 1;
        }
    }

    public int calculateTotalFee(){
        int totalFee = 0;

        for(int count : timeTable){
            if(count == 1)
                totalFee += (A*count);
            else if(count == 2)
                totalFee += (B*count);
            else if(count == 3)
                totalFee += (C*count);
        }

        return totalFee;
    }
    
}

public class Baekjoon2979 {
    public static void main(String[] args) throws Exception{

        // 한 대 주차할 때는 1분에 한 대당 A원을 내야 한다.
        // 두 대를 주차할 때는 1분에 한 대당 B원을 내야 한다.
        // 세 대를 주차할 때는 1분에 한 대당 C원을 내야 한다.

        // < Input >
        // 1. 주차 요금 A, B, C (1 ≤ C ≤ B ≤ A ≤ 100)
        // 2. 트럭이 주차장에 도착한 시간 / 주차장에서 떠난 시간(1 ≤ t ≤ 100)
        // (도착한 시간은 항상 떠난 시간보다 앞선다.)

        // < Output >
        // 상근이가 내야하는 주차 요금

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        ParkingFeeCalculator calculator = new ParkingFeeCalculator(A, B, C);

        int answer;

        for(int i = 0; i < 3; i++){

            st = new StringTokenizer(br.readLine());
            int arrival = Integer.parseInt(st.nextToken());
            int departure = Integer.parseInt(st.nextToken());

            Truck truck = new Truck(arrival, departure);

            calculator.parkTruck(truck);

        }

        answer = calculator.calculateTotalFee();

        System.out.println(answer);
        
    }
}
