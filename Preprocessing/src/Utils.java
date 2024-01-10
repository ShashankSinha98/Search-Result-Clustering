import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class Utils {
	
	public static String getCWD() {
		return System. getProperty("user.dir");
	}
	
	public static String concat(String... strings) {
		
		StringBuilder sb = new StringBuilder();
		for(String s: strings) {
			sb.append(s);
		}
		
		return sb.toString();
	}
	
	public static String concat(List<String> strings, String divider) {
		
		StringBuilder sb = new StringBuilder();
		for(String s: strings) {
			sb.append(s);
			sb.append(divider);
		}
		
		return sb.toString();
	}
	
	public static void writeToFile(String text, String filePath) {

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(text);
            System.out.println("Docs saved to "+filePath+" successfully");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
   }

}
