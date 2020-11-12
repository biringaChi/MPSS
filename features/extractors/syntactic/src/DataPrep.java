import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;


public class DataPrep {
	// Processes data from dataset file

	private static final String data_dir = "/Users/Gabriel/Documents/research/experimentation";

	public String getDir() throws IOException {
		try (Stream<Path> walk = Files.walk(Paths.get(data_dir))) {
			List<String> data_dir = walk.map(x -> x.toString())
					.filter(x -> x.endsWith(".csv"))
					.collect(Collectors.toList());
			return data_dir.get(1);
		} 
	} 

	public List<List<String>> readData() throws IOException, CsvValidationException{
		List<List<String>> data = new ArrayList<>();
		try(CSVReader csvReader = new CSVReader(new FileReader(getDir()));){
			String[] row;
			while ((row = csvReader.readNext()) != null) {
				data.add(Arrays.asList(row));
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return data;
	}

	public List<String> getSourcecode() throws IOException, CsvValidationException {
		List<String> sourcecode = new ArrayList<>();
		for(List<String> line : readData()) {
			for(int i = 2; i < line.size(); i += 4) {
				sourcecode.add(line.get(i));
			}
		}
		sourcecode.remove(0);
		return sourcecode;
	}
}