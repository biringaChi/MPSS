import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.lang.Math;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.stmt.Statement;
import com.opencsv.exceptions.CsvValidationException;

public class ASTLoops extends ASTPrep {
	/**
	 * Extracts frequency of Loop Statements Types: for, ForEach and while
	 */

	public List<Double> getLoopStmts() throws IOException, CsvValidationException {
		List<Double> loopsFreq = new ArrayList<>();
		Iterator<CompilationUnit> getASTs = getASTs().iterator();
		while (getASTs.hasNext()) {
			try {
				double count = 0.0;
				List<Statement> stmts = getASTs.next().findAll(Statement.class);
				for (Statement stmt : stmts) {
					if (stmt.isForStmt() || stmt.isForEachStmt() || stmt.isWhileStmt()) count++;
				}
				loopsFreq.add(count);
			} catch(NullPointerException e) {
				loopsFreq.add(0.0);
			}
		}
		return loopsFreq;
	}

	public List<Double> extractLoopFeatures() throws IOException, CsvValidationException {
		List<Double> loops = new ArrayList<>();
		Iterator<Double> getCharFreq = getCharFreq().iterator();
		Iterator<Double> getLoopStmts = getLoopStmts().iterator();
		while (getCharFreq.hasNext() && getLoopStmts.hasNext()) {
			loops.add(Math.log10(getCharFreq.next() / getLoopStmts.next()));
		}
		return loops;
	}
}