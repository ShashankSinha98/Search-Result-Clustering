
public class Constants {
	
	public static final String DATASET_FOLDER = "big_dataset";
	public static final String ORIGINAL_DOC_JSON_FILE = "original_docs.json";
	public static final String PROCESSED_DOC_JSON_FILE = "processed_docs.json";
	public static final String CWD = Utils.getCWD();
	
	public static final String datasetFolderPath = Utils.concat(CWD, "\\", DATASET_FOLDER);
	public static final String originalDocFilePath = Utils.concat(CWD, "\\", ORIGINAL_DOC_JSON_FILE);
	public static final String processedDocFilePath = Utils.concat(CWD, "\\", PROCESSED_DOC_JSON_FILE);
	
	public static final int RELEVANT_DOCS_LIMIT = 100;
	
	public static final String[] dummyDocs = new String[] {"the young french men crowned world champions",
            "Google Translate app is getting more intelligent everyday",
            "Facebook face recognition is driving me crazy",
            "who is going to win the Golden Ball title this year",
            "these camera apps are funny",
            "Croacian team made a brilliant world cup campaign reaching the final match",
            "Google Chrome extensions are useful.",
            "Social Media apps leveraging AI incredibly",
            "Qatar 2022 FIFA world cup is played in winter",
            "The cat is on the mat.",
			"The kitty lies on the mat."};
}
