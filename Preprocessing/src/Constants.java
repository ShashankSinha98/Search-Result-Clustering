
public class Constants {
	
	public static final String DATASET_FOLDER = "big_dataset";
	public static final String ORIGINAL_DOC_JSON_FILE = "original_docs.json";
	public static final String PROCESSED_DOC_JSON_FILE = "processed_docs.json";
	public static final String CWD = Utils.getCWD();
	
	public static final String datasetFolderPath = Utils.concat(CWD, "\\", DATASET_FOLDER);
	public static final String originalDocFilePath = Utils.concat(CWD, "\\", ORIGINAL_DOC_JSON_FILE);
	public static final String processedDocFilePath = Utils.concat(CWD, "\\", PROCESSED_DOC_JSON_FILE);
	
}
