import java.io.*;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;

public class ReadDocuments {

	public static void convertTextDocumentsToJson() throws IOException {

		File folder = new File(Constants.datasetFolderPath);
		List<Document> documents = new ArrayList<>();
		
        File[] files = folder.listFiles(txtFileFilter);
        int count = 0;
		 if (files != null) { 
			 for (int i=0; i<files.length; i++) {
				 if(i%100==0) {
					 System.out.println("Processing "+i+" file");
				 }
				 File file = files[i];
				 String content = processFile(file);
				 if(content==null || content.length()==0)
					 continue;
				 
				 int docId = count++;
				 String fileName = file.getName();
				 Document doc = new Document(docId, fileName, content);
				 documents.add(doc);
			 } 
		 }
		 
		// Convert to Json
		Gson gson = new Gson();
		String docJsonStr = gson.toJson(documents);

		File jsonFile = new File(Constants.originalDocFilePath);
		
		if(!jsonFile.exists()) {
			jsonFile.createNewFile();
		}
		
		Utils.writeToFile(docJsonStr, Constants.originalDocFilePath);
	}
	
    
	private static FilenameFilter txtFileFilter = new FilenameFilter() {
        @Override
        public boolean accept(File dir, String name) {
            return name.endsWith(".txt");
        }
    };
	
	
    private static String processFile(File file) {
        try {
            // Read the file
            StringBuilder content = new StringBuilder();
            try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    content.append(line).append(System.lineSeparator());
                }
            }
            return content.toString();

        } catch (IOException e) {
        	e.printStackTrace();
        	return null;
        }
    }
 }
