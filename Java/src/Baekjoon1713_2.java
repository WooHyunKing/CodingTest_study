import java.io.*;
import java.util.*;

public class Baekjoon1713_2 {
    
    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        Student [] students = new Student[101];
        List<Student> photos = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0; i<M; i++){
            
            int num = Integer.parseInt(st.nextToken());

            if(students[num] != null){
                students[num].count++;
            }
            else{

                Collections.sort(photos);

                if(photos.size() == N){
                    Student delete = photos.remove(N-1);
                    students[delete.num] = null;
                }

                students[num] = new Student(num,1,i);
                photos.add(students[num]);
            }
        }

        Collections.sort(photos, (s1,s2)->s1.num-s2.num);

        for(Student s : photos){
            System.out.print(s.num + " ");
        }

        br.close();

    }
}

class Student implements Comparable<Student>{

    int num;
    int count;
    int timeStamp;

    public Student(int num, int count, int timeStamp){
        super();
        this.num = num;
        this.count = count;
        this.timeStamp = timeStamp;
    }

    
    @Override
    public int compareTo(Student s){

        if(this.count == s.count){
            return s.timeStamp - this.timeStamp;
        }
        else{
            return s.count - this.count;
        }
    }
}