import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.Node.PreOrderIterator;
import com.github.javaparser.printer.DotPrinter;
import com.github.javaparser.printer.YamlPrinter;
import com.google.common.collect.Iterators;
import com.opencsv.exceptions.CsvValidationException;

public class ASTs extends ASTPrep {

	public List<String> viewASTs() throws CsvValidationException, IOException {
		YamlPrinter printer = new YamlPrinter(true);
		List<String> ASTs = new ArrayList<>();
		for (CompilationUnit ast : getASTs()) {
			if (ast != null)
				ASTs.add(printer.output(ast).toString());
			else ASTs.add(null);
		}
		return ASTs;
	}

	public void graphASTs(int idx) throws IOException, CsvValidationException {
		String path = "FeatureEng/Extractors/Syntactic/src/Graphs/";
		DotPrinter printer = new DotPrinter(true);
		CompilationUnit ast = getASTs().get(idx);
		if (ast != null) {
			try (FileWriter fileWriter = new FileWriter(path + idx + "-" + "ast.dot");
					PrintWriter printWriter = new PrintWriter(fileWriter)) {
				printWriter.print(printer.output(ast));
			}
		} else System.err.println("Please provide a valid compilation unit idx");
	}

	public List<Integer> numNodes() throws CsvValidationException, IOException {
		List<Integer> nodes = new ArrayList<>();
		for (CompilationUnit ast : getASTs()) {
			if (ast != null) {
				PreOrderIterator iterator = new Node.PreOrderIterator(ast);
				int size = Iterators.size(iterator);
				nodes.add(size);
			} else nodes.add(0);
		}
		return nodes;
	}

	public int maxDepth() throws CsvValidationException, IOException {
		CompilationUnit ast = getASTs().get(0);
		List<List<String>> result = new ArrayList<>();
		Node root = ast.findRootNode();
		if(root == null) return 0;
		Queue<Node> queue = new LinkedList<>();
		queue.offer(root);
		int depth = 0;
		while(!queue.isEmpty()) {
			List<String> level = new ArrayList<>();
			int size = queue.size();
			for(int i = 0; i < size; i++) {
				Node currentNode = queue.poll();
				level.add(currentNode.getRange().toString());
				if(currentNode.getChildNodes() != null) queue.add(currentNode.getChildNodes().get(0));
				if(currentNode.getChildNodes().get(1) != null) queue.add(currentNode.getChildNodes().get(1));
			}
			depth++;
			result.add(level);
		}
		return depth;
	}

	public HashMap<String, List<String>> nodeType() throws CsvValidationException, IOException {
		List<String> temp = new ArrayList<>();
		HashMap<String, List<String>> nodeTypes = new HashMap<>(); 
		String d = "doc";
		Integer idx = 0;
		for(String doc : viewASTs()) {
			if(doc != null) {
				String[] words = doc.split("\\s+");
				for(String word : words) {
					if(word.indexOf("Type=") != -1) {
						temp.add(word.substring(word.indexOf('=') + 1, word.indexOf(')')));
					}
				}
				nodeTypes.put(d + idx, temp);
			} else nodeTypes.put(d + idx, null);
			idx++;
		}
		return nodeTypes;
	}

	public void nodeTypeTF() {
	}

	public void nodeTypeTFIDF() {
	}
}