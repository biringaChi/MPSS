// import java.io.IOException;
// import java.util.Map;
// import java.util.ArrayList;
// import java.util.LinkedHashMap;
// import java.util.List;

// import com.opencsv.exceptions.CsvValidationException;

// public class ASTNodeTypesTFIDF extends ASTs {
// 	/**
// 	 * Calculates the Term Frequency-Inverse Document Frequency (TF-IDF) of
// 	 * ASTsNodeTpes
// 	 */

// 	public List<Map<String, Double>> TF() throws CsvValidationException, IOException {
// 		List<Map<String, Double>> tfs = new ArrayList<>();
// 		for (Map.Entry<String, List<String>> entry : treeNodeTypes().entrySet()) {
// 			Map<String, Double> tf = new LinkedHashMap<>();
// 			if (entry.getValue() != null) {
// 				for (String nodeType : entry.getValue()) {
// 					tf.put(nodeType, tf.getOrDefault(nodeType, 0.0) + 1.0);
// 				}
// 				for (Map.Entry<String, Double> term : tf.entrySet()) {
// 					try {
// 						double frequency = term.getValue() / tf.size();
// 						tf.put(term.getKey(), frequency);
// 					} catch (ArithmeticException e) {
// 						tf.put(null, 0.0);
// 					}
// 				}
// 				tfs.add(tf);
// 			} else tfs.add(null);
// 		}
// 		return tfs;
// 	}

// 	public void IDF() throws CsvValidationException, IOException {	
// 	}
// }
