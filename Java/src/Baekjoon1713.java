import java.io.*;
import java.util.*;

public class Baekjoon1713 {
	
	static HashMap<Integer,Integer> hash = new HashMap<Integer,Integer>();
	
	static class Student implements Comparable<Student>{
		int id;
		int postingCount;
		
		public Student(int id, int postingCount) {
			this.id = id;
			this.postingCount = postingCount;
		}

		@Override
		public int compareTo(Student target) {

			if(hash.get(this.id) > hash.get(target.id))
				return 1;
			else if (hash.get(this.id) == hash.get(target.id)) {
				if(this.postingCount > target.postingCount)
					return 1;
				else
					return -1;
			}
			else
				return -1;
		}
		
	}

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		PriorityQueue<Student> pq = new PriorityQueue<>();

		int postingCount = 0;
		
		int [] result = new int[N];
		int resultIndex = 0;
		
		for(int i=0; i<M; i++) {
		
			int studentId = Integer.parseInt(st.nextToken());
			
			// 사진틀이 꽉찬 경우
			if(pq.size() >= N) { 
				
				// 1) 해당 학생 이미 큐에 존재하는 경우
				if(hash.get(studentId) != null && hash.get(studentId) > 0) {
					// 추천수 + 1	
					hash.put(studentId, hash.get(studentId)+1);
					
					PriorityQueue<Student> new_q = new PriorityQueue<>();
					
					for(Student s : pq) {
						new_q.offer(new Student(s.id,s.postingCount));			
					}
					
					pq = new_q;
					
				}
				
				// 2) 해당 학생이 큐에 존재하지 않는 경우
				else {
					// 큐에서 우선순위가 가장 적은 원소를 제거하고 
					Student removed = pq.poll();
					hash.put(removed.id, 0);
					
					// 새로운 학생 추가
					hash.put(studentId, 1);
					Student added = new Student(studentId,++postingCount);
					pq.offer(added);
				}
				
			}
			// 사진틀이 남아있는 경우
			else {
				// 1) 해당 학생 이미 큐에 존재하는 경우
				if(hash.get(studentId) != null && hash.get(studentId) > 0) {
					// 추천수 + 1
					hash.put(studentId, hash.get(studentId)+1);
					
					PriorityQueue<Student> new_q = new PriorityQueue<>();
					
					for(Student s : pq) {
						new_q.offer(new Student(s.id,s.postingCount));			
					}
					
					pq = new_q;
				}
				else { // 2) 해당 학생이 큐에 존재하지 않는 경우
					// 새로운 학생 추가
					hash.put(studentId, 1);
					Student added = new Student(studentId,++postingCount);
					pq.offer(added);
				}
			}

		}
		
		while(!pq.isEmpty()) {
			result[resultIndex] = pq.poll().id;
			resultIndex++;
		}
		
		Arrays.sort(result);
		
		for(int i=0; i<result.length; i++) {
			if(result[i] != 0)
				System.out.print(result[i] + " ");
		}
		
	}

}
