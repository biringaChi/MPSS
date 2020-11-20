import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.Node.PreOrderIterator;
import com.github.javaparser.printer.DotPrinter;
import com.github.javaparser.printer.YamlPrinter;
import com.google.common.collect.Iterators;
import com.opencsv.exceptions.CsvValidationException;

public class ASTs extends ASTPrep {
	/**
	 * Processes ASTs and generates additional features
	 * Examples: Graphs, number of nodes and node types
	*/

	public List<String> viewASTs() throws CsvValidationException, IOException {
		YamlPrinter printer = new YamlPrinter(true);
		List<String> ASTs = new ArrayList<>();
		for (CompilationUnit ast : getASTs()) {
			if (ast != null) ASTs.add(printer.output(ast).toString());
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

	public List<Double> numNodes() throws CsvValidationException, IOException {
		List<Double> nodes = new ArrayList<>();
		for (CompilationUnit ast : getASTs()) {
			if (ast != null) {
				PreOrderIterator iterator = new Node.PreOrderIterator(ast);
				int size = Iterators.size(iterator);
				nodes.add((double) (Math.round(Math.log10(size) * 100.0) / 100.0));
			} else nodes.add((double) 0);
		}
		return nodes;
	}

	public int maxDepth() throws CsvValidationException, IOException {
		CompilationUnit ast = getASTs().get(0);
		List<List<String>> levels = new ArrayList<>();
		Node root = ast.findRootNode();
		if (root == null) return 0;
		Queue<Node> queue = new LinkedList<>();
		queue.offer(root);
		int depth = 0;
		while (!queue.isEmpty()) {
			List<String> level = new ArrayList<>();
			int size = queue.size();
			for (int i = 0; i < size; i++) {
				Node currentNode = queue.poll();
				level.add(currentNode.getRange().toString());
				if (currentNode.getChildNodes() != null) queue.add(currentNode.getChildNodes().get(0));
				if (currentNode.getChildNodes().get(1) != null) queue.add(currentNode.getChildNodes().get(1));
			}
			depth++;
			levels.add(level);
		}
		return depth;
	}

	public Map<String, List<String>> treeNodeTypes() throws CsvValidationException, IOException {
		Integer idx = 0;
		String docId = "doc", typeId = "Type="; 
		Map<String, List<String>> treeNodeType = new LinkedHashMap<>(); 
		for(String docNode : viewASTs()) {
			List<String> temp = new ArrayList<>();
			if (docNode != null) {
				String[] nodes = docNode.split("\\s+");
				for (String node : nodes) {
					if (node.indexOf(typeId) != -1) {
						temp.add(node.substring(node.indexOf('=') + 1, node.indexOf(')')));
					}
				}
				if (!treeNodeType.containsKey(docId + idx)) treeNodeType.put(docId + idx, temp);
			} else treeNodeType.put(docId + idx, null);
			idx++;
		}
		return treeNodeType;
	}
}