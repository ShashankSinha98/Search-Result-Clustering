import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.ByteBuffersDirectory;
import org.apache.lucene.store.Directory;
import org.apache.lucene.document.Field;
import org.apache.lucene.store.RAMDirectory;

import com.google.gson.Gson;

import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.search.similarities.BM25Similarity;

public class QueryDocuments {
	
	private List<String> preprocessedDocuments;
	private Map<Integer, Doc> idDocMap;
	private Gson gson;
	private List<Doc> retrievedDocs;
	
	public QueryDocuments() {
		retrievedDocs = new ArrayList<>();
		preprocessedDocuments = new ArrayList<>();
		idDocMap = new HashMap<>();
		gson = new Gson();
		
		List<Doc> docs = ReadDocuments.getDocuments();
		for(Doc doc: docs) {
			idDocMap.put(doc.getDocId(), doc);
			List<String> tokens = DocumentPreprocessor.preprocess(doc.getContent());
			if(tokens==null) {
				System.out.println("Null Tokens, something went wrong. Aborting!");
				return;
			}
			String tokenStr = Utils.concat(tokens, " ");
			preprocessedDocuments.add(tokenStr);
		}
	}
	

	public String query(String query, int expectedResultSize) throws IOException, ParseException {
		System.out.println("Received query request: "+query);
		
		// At max RELEVANT_DOCS_LIMIT no of docs will be retrieved 
		// irrespective of user demand
		if(expectedResultSize > Constants.RELEVANT_DOCS_LIMIT) {
			expectedResultSize = Constants.RELEVANT_DOCS_LIMIT;
		}
		
		Directory directory = createIndex(preprocessedDocuments);
		Query q = parseQuery(query, new StandardAnalyzer());
		TopDocs topDocs = searchIndex(directory, q, expectedResultSize);
		DirectoryReader directoryReader = DirectoryReader.open(directory);
	    IndexSearcher searcher = new IndexSearcher(directoryReader);
	    
		for (ScoreDoc scoreDoc : topDocs.scoreDocs) {
	        Document doc = searcher.doc(scoreDoc.doc);
	        retrievedDocs.add(idDocMap.get(Integer.valueOf(scoreDoc.doc)));
	    }
		
		System.out.println("Retrieved size: "+retrievedDocs.size());
		return gson.toJson(retrievedDocs);
	}
	
	
	
	public static Directory createIndex(List<String> documents) {
		try {
		    Directory directory = new ByteBuffersDirectory();
		    StandardAnalyzer analyzer = new StandardAnalyzer();
		    IndexWriterConfig config = new IndexWriterConfig(analyzer);
		    
		    config.setSimilarity(new BM25Similarity());
		    
		    IndexWriter indexWriter = new IndexWriter(directory, config);
	
		    for (String text : documents) {
		        Document doc = new Document();
		        doc.add(new TextField("content", text, Field.Store.YES));
		        indexWriter.addDocument(doc);
		    }
		    indexWriter.close();
		    return directory;
		} catch(Exception e) {
			System.out.println("Exception in creating index: "+e.getMessage());
			e.printStackTrace();
			return null;
		}
	}
	
	
	public static Query parseQuery(String queryString, StandardAnalyzer analyzer) throws ParseException {
	    QueryParser parser = new QueryParser("content", analyzer);
	    return parser.parse(queryString);
	}
	
	
	public static TopDocs searchIndex(Directory directory, Query query, int expectedResultSize) throws IOException {
	    DirectoryReader directoryReader = DirectoryReader.open(directory);
	    IndexSearcher searcher = new IndexSearcher(directoryReader);
	    TopDocs hits = searcher.search(query, expectedResultSize); 
	    directoryReader.close();
	    return hits;
	}

}
