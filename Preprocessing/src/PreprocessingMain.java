import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import  java.lang.reflect.Type;

public class PreprocessingMain {

	private static Gson gson = new Gson();
	private static List<Doc> documents;
	private static List<Doc> preprocessedDocuments;
	
	public static void main(String[] args) throws IOException {
		File originalDocJson = new File(Constants.originalDocFilePath);
		
		// If original docs json doesn't exist - create one
		if(!originalDocJson.exists()) {
			List<Doc> documents = ReadDocuments.getDocuments();
			ReadDocuments.convertTextDocumentsToJson(documents);
		}
		
		
		// read json and save docs in list
		Reader reader = new FileReader(Constants.originalDocFilePath);
		Type listType = new TypeToken<List<Doc>>(){}.getType();
        documents = gson.fromJson(reader, listType);
        
        
        // preprocess docs and save result
        preprocessedDocuments = new ArrayList<>();
        
        if(documents!=null && documents.size() > 0) {
        	for(int i=0; i<documents.size(); i++) {
        		if(i%100==0) {
        			System.out.println(i+"/"+documents.size()+" docs processed...");
        		}
        		Doc doc = documents.get(i);
        		List<String> tokens = DocumentPreprocessor.preprocess(doc.getContent());
        		Doc processedDoc = new Doc(
        				doc.getDocId(), doc.getFileName(), 
        				Utils.concat(tokens, " "));
        		
        		preprocessedDocuments.add(processedDoc);
        	}
        	
        String processedDocsJson = gson.toJson(preprocessedDocuments);
        
        File jsonFile = new File(Constants.processedDocFilePath);
		
		if(!jsonFile.exists()) {
			jsonFile.createNewFile();
		}
		
		Utils.writeToFile(processedDocsJson, Constants.processedDocFilePath);
        	
        } else {
        	System.out.println("Null/Empty Documents");
        }        
	}

}
