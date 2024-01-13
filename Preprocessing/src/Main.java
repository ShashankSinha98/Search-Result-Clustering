import java.io.File;
import java.io.IOException;
import java.io.StringReader;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.en.EnglishAnalyzer;
import org.apache.lucene.analysis.synonym.SynonymMap;
import org.apache.lucene.analysis.synonym.WordnetSynonymParser;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.util.Version;

import com.google.gson.Gson;


public class Main {

	public static void main(String[] args) throws IOException, ParseException {
		Scanner sc = new Scanner(System.in);
		QueryDocuments qd = new QueryDocuments();
		int userInp = 1;
		while(userInp !=0) {			
			System.out.print("Enter Query: ");
			String query = sc.nextLine();
			if(query.length()==0) {
				System.out.println("Input valid input");
				continue;
			}
			String res = qd.query(query, 50);
			System.out.println(res); // not display if result is v large
			
			System.out.print("Do you want to continue (1/0)? ");
			userInp = sc.nextInt();
		}
	}

}
