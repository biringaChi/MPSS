// // traverse tree and get all node types 
// // put it in a list
// // calculate the term frequency of each element in the list


// import java.io.IOException;
// import java.util.ArrayList;
// import java.util.List;
// import java.lang.Math;

// import com.github.javaparser.ast.CompilationUnit;
// import com.github.javaparser.ast.stmt.Statement;
// import com.opencsv.exceptions.CsvValidationException;


// public class ASTNodes extends ASTPrep {
// 	/**
// 	 * Traverses ASTs and retrieves information
// 	 * Types: MaxDepth,  
// 	 */
	
// 	public List<Integer> maxDepth() throws IOException {
// 		List<Integer> loopFrequency = new ArrayList<>();
// 		// try {
// 		// 	for(CompilationUnit cu : getCompilationUnits()) {
// 		// 		if(cu != null) {
// 		// 			List<Statement> stmts = cu.findAll(Statement.class);
// 		// 			int count = 0;
// 		// 			for(Statement stmt : stmts) {
// 		// 				if(stmt.isForStmt() || stmt.isForEachStmt() || stmt.isWhileStmt()) count++;
// 		// 			}
// 		// 			loopFrequency.add(count);
// 		// 		} else loopFrequency.add(0);
// 		// 	}
// 		// } catch (CsvValidationException e) {e.printStackTrace();}

// 		getCompilationUnits().get(0).walk(Node.TreeTraversal.PREORDER, node -> System.out.println("New Node" + node));
// 		return null;
// 	}

// 	public static void main(String[] args) throws IOException {
// 		ASTNodes an = new ASTNodes();
// 		System.out.println(an.maxDepth());
// 	}
// }