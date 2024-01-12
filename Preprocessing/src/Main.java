import java.io.IOException;
import java.util.Scanner;

import org.apache.lucene.queryparser.classic.ParseException;

import com.google.gson.Gson;

public class Main {

	public static void main(String[] args) throws IOException, ParseException {
		Scanner sc = new Scanner(System.in);
		QueryDocuments qd = new QueryDocuments();
		System.out.print("Enter Query: ");
		String query = sc.nextLine();
		String res = qd.query(query, 10);
		System.out.println(res); // not display if result is v large
	}

}
