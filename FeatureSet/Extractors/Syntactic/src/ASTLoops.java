import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Iterator;

import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.stmt.Statement;
import com.opencsv.exceptions.CsvValidationException;


public class ASTLoops extends ASTPrep {
	/**
	 * Extracts frequency of Loop Statements 
	 * Types: for, ForEach and while
	 */

	public List<Double> getLoopStmts() throws IOException, CsvValidationException {
		List<Double> loopFreqs = new ArrayList<>();
		Iterator<String> getSourcecode = getSourcecode().iterator();
		while(getSourcecode.hasNext()) {
			try {
				CompilationUnit compilationUnit = StaticJavaParser.parse(getSourcecode.next());
				double count = 0.0;
				List<Statement> stmts = compilationUnit.findAll(Statement.class);
				for (Statement stmt : stmts) {
					if (stmt.isForStmt() || stmt.isForEachStmt() || stmt.isWhileStmt()) {
						count++;
					} 
				}
				loopFreqs.add(count);
			} catch (Exception e) {
				loopFreqs.add(0.0);
			}
		}
		return loopFreqs;
	}

	public List<Double> extractLoopFeatures() throws IOException, CsvValidationException {
		List<Double> loops = new ArrayList<>();
		Iterator<Double> getCharFreqs = getCharFreqs().iterator();
		Iterator<Double> getLoopStmts = getLoopStmts().iterator();
		while (getCharFreqs.hasNext() && getLoopStmts.hasNext()) {
			loops.add(Math.log10(getCharFreqs.next() / getLoopStmts.next()));
		}
		Collections.replaceAll(loops, Double.POSITIVE_INFINITY, 0.0);
		return loops;
	}
}