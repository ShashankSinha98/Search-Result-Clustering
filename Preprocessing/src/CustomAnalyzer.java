import java.io.IOException;
import java.io.StringReader;
import java.util.*;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.CharArraySet;
import org.apache.lucene.analysis.LowerCaseFilter;
import org.apache.lucene.analysis.StopFilter;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.Tokenizer;
import org.apache.lucene.analysis.en.EnglishAnalyzer;
import org.apache.lucene.analysis.en.PorterStemFilter;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.analysis.standard.StandardTokenizer;
import org.apache.lucene.analysis.tokenattributes.CharTermAttribute;

import com.optimaize.langdetect.*;
import com.optimaize.langdetect.i18n.LdLocale;
import com.optimaize.langdetect.ngram.NgramExtractors;
import com.optimaize.langdetect.profiles.LanguageProfile;
import com.optimaize.langdetect.profiles.LanguageProfileReader;
import com.optimaize.langdetect.text.CommonTextObjectFactories;
import com.optimaize.langdetect.text.TextObject;
import com.optimaize.langdetect.text.TextObjectFactory;

class CustomAnalyzer extends Analyzer {

	@Override
	protected TokenStreamComponents createComponents(String fieldName) {
		Tokenizer source = new StandardTokenizer();
		TokenStream result = new LowerCaseFilter(source);

		// Create a set of stop words
		Set<?> stopWordsSet = EnglishAnalyzer.ENGLISH_STOP_WORDS_SET;
        CharArraySet stopWords = new CharArraySet(stopWordsSet, true);
        result = new StopFilter(result, stopWords); // StopwordFilter
        result = new PorterStemFilter(result); // PorterStemmerFilter

        return new TokenStreamComponents(source, result);
	}

	public List<String> applyTokenization(String text) throws IOException {
		List<String> res = new ArrayList();
		Analyzer customAnalyzer = new CustomAnalyzer();
		TokenStream tokenStream  = customAnalyzer.tokenStream("fieldName", text);
		
		CharTermAttribute charTermAttribute = tokenStream.addAttribute(CharTermAttribute.class);
		
		try {
			tokenStream.reset();
			
			while(tokenStream.incrementToken()) {
				String term = charTermAttribute.toString();
				term = removePunctuation(term); // removing punctuation
				if(term.length() > 0) {
					res.add(term);
				}
			}
			
			tokenStream.end();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			tokenStream.close();
		}
		
		return res;
	}
	
	private static String removePunctuation(String text) {
		return text.replaceAll("[\\p{Punct}]", "");
    }
}