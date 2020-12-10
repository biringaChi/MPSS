import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.opencsv.exceptions.CsvValidationException;

public class ProcessFeatures {
	/**
	 * Collects feature extractors and builds dataset
	 */
	
	private static final String DATA_DIR = "/Users/Gabriel/Documents/Research/Experimentation/Models/processed_data.csv";

	public List<List<Double>> featureExtractor() throws CsvValidationException, IOException {
		List<List<Double>> features = new ArrayList<>();
		ASTConditionals ac = new ASTConditionals();
		ASTLiterals al = new ASTLiterals();
		ASTLoops aloops = new ASTLoops();
		ASTNodes an = new ASTNodes();
		features.add(ac.extractConditionalFeatures());
		features.add(al.extractLiteralFeatures());
		features.add(aloops.extractLoopFeatures());
		features.add(an.extractNodeFeatures());
		return features;
	}

	public void buildDataset() throws CsvValidationException, IOException {
		FileWriter fw = new FileWriter(DATA_DIR, true);
		for(List<Double> extractor : featureExtractor()) {
			fw.write(extractor.toString().replace("[", "").replace("]", "") + System.lineSeparator());
		}
		fw.close();
	}
}
