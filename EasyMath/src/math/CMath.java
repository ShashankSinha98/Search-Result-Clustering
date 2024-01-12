package math;
public class CMath {
	
	public static int square(int x) throws InterruptedException {
		System.out.println("square called: "+x);
		Thread.sleep(2000);
		return x*x;
	}
}
