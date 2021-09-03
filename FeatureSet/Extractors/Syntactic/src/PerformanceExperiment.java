
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.junit.Test;
import com.opencsv.exceptions.CsvValidationException;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PerformanceExperiment extends ASTs {
	/* 
	Calculates the term frequency of tree nodes.
	Highlighting the access and manipulation of a linked hashmap.
	*/
	
	public List<Map<String, Double>> termFrequencyEntrySet() throws CsvValidationException, IOException {
		List<Map<String, Double>> tfs = new ArrayList<>();

		for (Map.Entry<String, List<String>> entry : treeNodeTypes().entrySet()) {
			Map<String, Double> tf = new LinkedHashMap<>();
			if (entry.getValue() != null) {
				for (String nodeType : entry.getValue()) {
					tf.put(nodeType, tf.getOrDefault(nodeType, 0.0) + 1.0);
				}
				for (Map.Entry<String, Double> term : tf.entrySet()) {
					try {
						double frequency = term.getValue() / tf.size();
						tf.put(term.getKey(), frequency);
					} catch (ArithmeticException e) {
						tf.put(null, 0.0);
					}
				}
				tfs.add(tf);
			} else tfs.add(null);
		}
		return tfs;
	}

	public List<Map<String, Double>> termFrequencyKeySet() throws CsvValidationException, IOException {
		List<Map<String, Double>> tfs = new ArrayList<>();

		for(String entry : treeNodeTypes().keySet())  {
			Map<String, Double> tf = new LinkedHashMap<>();
			if(treeNodeTypes().get(entry) != null) {
				for (String nodeType : treeNodeTypes().get(entry)) {
					tf.put(nodeType, tf.getOrDefault(nodeType, 0.0) + 1.0);
				}
				for (String term : tf.keySet()) {
					try {
						double frequency = tf.get(term) / tf.size();
						tf.put(term, frequency);
					} catch (ArithmeticException e) {
						tf.put(null, 0.0);
					}
				}
				tfs.add(tf);
			} else tfs.add(null);
		}
		return tfs;
	}

	@Test
	public void testTermFrequencyEntrySet() throws CsvValidationException, IOException {
		long start = System.nanoTime();
		assertEquals(termFrequencyEntrySet(), termFrequencyEntrySet());
		long end = System.nanoTime();
		System.out.println("Entry-set run-time: " + (end - start) / 1000000000 + " seconds");
	}

	@Test
	public void testTermFrequencyKeySet() throws CsvValidationException, IOException {
		long start = System.nanoTime();
		assertEquals(termFrequencyKeySet(), termFrequencyKeySet());
		long end = System.nanoTime();
		System.out.println("Key-set run-time: " + (end - start) / 1000000000 + " seconds");
	}

	public static void main(String[] args) throws CsvValidationException, IOException {
		PerformanceExperiment pe = new PerformanceExperiment();
		pe.testTermFrequencyEntrySet();
		pe.testTermFrequencyKeySet();
	}
}