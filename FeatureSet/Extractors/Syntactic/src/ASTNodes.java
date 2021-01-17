import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Iterator;

import com.github.javaparser.ast.CompilationUnit;
import com.opencsv.exceptions.CsvValidationException;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.Node.PreOrderIterator;
import com.google.common.collect.Iterators;

public class ASTNodes extends ASTPrep {
	/**
	 * Extracts frequency of Nodes
	 */ 

	public List<Double> getNodeFreqs() throws CsvValidationException, IOException {
		List<Double> nodes = new ArrayList<>();
		for (CompilationUnit ast : getASTs()) {
			if (ast != null) {
				PreOrderIterator iterator = new Node.PreOrderIterator(ast);
				double size = Iterators.size(iterator);
				nodes.add(size);
			} else nodes.add(0.0);
		}
		return nodes;
	}

	public List<Double> extractNodeFeatures() throws IOException, CsvValidationException {
		List<Double> nodes = new ArrayList<>();
		Iterator<Double> getCharFreqs = getCharFreqs().iterator();
		Iterator<Double> getNodeFreqs = getNodeFreqs().iterator();
		while (getCharFreqs.hasNext() && getNodeFreqs.hasNext()) {
			nodes.add(Math.log10(getCharFreqs.next() / getNodeFreqs.next()));
		}
		Collections.replaceAll(nodes, Double.POSITIVE_INFINITY, 0.0);
		return nodes;
	}
}