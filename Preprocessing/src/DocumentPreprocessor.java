import java.io.IOException;
import java.util.List;

public class DocumentPreprocessor {
	
	private static CustomAnalyzer analyzer;
	
	static {
		analyzer = new CustomAnalyzer();
	}
	
	public static List<String> preprocess(String document) {
		try {
			return analyzer.applyTokenization(document);
		} catch (IOException e) {
			System.out.println("Exception in DocumentPreprocessor: "+e.getMessage());
			e.printStackTrace();
			return null;
		}
	}

}
