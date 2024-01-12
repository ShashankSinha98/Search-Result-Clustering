
public class Doc {
	
	private int docId = -1;
	private String docName;
	private String content;
	
	
	public Doc(int docId, String fileName, String content) {
		this.docId = docId;
		this.docName = fileName;
		this.content = content;
	}
	
	public int getDocId() {
		return docId;
	}
	
	public String getFileName() {
		return docName;
	}
	
	public String getContent() {
		return content;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "ID: "+this.docId+"\nDocName: "+this.docName+"\nContent: "+this.content;
	}

}
