import java.io.*;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;

public class ReadDocuments {
	
	
	public static List<Doc> getDocuments() {
		File folder = new File(Constants.datasetFolderPath);
		List<Doc> documents = new ArrayList<>();
		
        File[] files = folder.listFiles(txtFileFilter);
        int count = 0;
		 if (files != null) {
			 System.out.println("Reading "+files.length+" documents, please wait!");
			 for (int i=0; i<files.length; i++) {
				 File file = files[i];
				 String content = readFile(file);
				 if(content==null || content.length()==0)
					 continue;
				 
				 int docId = count++;
				 String fileName = file.getName();
				 Doc doc = new Doc(docId, fileName, content);
				 documents.add(doc);
			 } 
		 }		
		return documents;
	}
	
	public static List<Doc> getDummyDocuments() {
		String[] dummyDocs = Constants.dummyDocs;
		List<Doc> docs = new ArrayList<>();
		for(int i=0; i<dummyDocs.length; i++) {
			Doc d = new Doc(i, String.valueOf(i), dummyDocs[i]);
			docs.add(d);
		}
		
		return docs;
	}

	public static void convertTextDocumentsToJson(List<Doc> documents) throws IOException {
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
	
	
    private static String readFile(File file) {
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
