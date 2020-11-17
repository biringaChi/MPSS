import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;
import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;


public class ASTPrep {
	/**
	 * Preprocesses dataset
	 * Generates Compilation Units for ASTs
	 */

	private static final String DATA_DIR = "/Users/Gabriel/Documents";

	public String getDir() throws IOException {
		try (Stream<Path> walk = Files.walk(Paths.get(DATA_DIR))) {
			List<String> dataDir = walk.map(x -> x.toString())
					.filter(x -> x.endsWith(".csv"))
					.collect(Collectors.toList());
			return dataDir.get(1);
		} 
	} 

	public List<List<String>> readData() throws IOException, CsvValidationException {
		List<List<String>> data = new ArrayList<>();
		try(CSVReader reader = new CSVReader(new FileReader(getDir()));) {
			String[] row;
			while ((row = reader.readNext()) != null) {
				data.add(Arrays.asList(row));
			}
		}
		return data;
	}

	public List<String> getSourcecode() throws IOException, CsvValidationException {
		List<String> sourcecode = new ArrayList<>();
		for(List<String> row : readData()) {
			for(int col = 2; col < row.size(); col += 4) {
				sourcecode.add(row.get(col));
			}
		}
		sourcecode.remove(0);
		return sourcecode;
	}
	
	public List<Integer> getCharFrequency() throws IOException, CsvValidationException {
		List<Integer> charFreq = new ArrayList<>();
		for(String file : getSourcecode()) {
			charFreq.add(file.length());
		}
		return charFreq;
	}

	public List<Integer> getCodewordFrequency() throws IOException, CsvValidationException {
		List<Integer> codewordFreq = new ArrayList<>();
		for(String file : getSourcecode()) {
			String[] string = file.split("\\s+");
			codewordFreq.add(string.length);
		}
		return codewordFreq;
	}

	public List<CompilationUnit> getASTs() throws IOException, CsvValidationException {
		Integer idx = 0;
		List<CompilationUnit> compilationUnits = new ArrayList<>();
		HashMap<Integer, String> uncompiled = new HashMap<>();
		for(String file : getSourcecode()) {
			try {
				CompilationUnit compilationUnit = StaticJavaParser.parse(file);
				compilationUnits.add(compilationUnit);
			} catch (Exception e) {
				uncompiled.put(idx, file);
				compilationUnits.add(null);
			}
			idx++;
		}
		return compilationUnits;
	}
}