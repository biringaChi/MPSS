import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.stmt.Statement;
import com.opencsv.exceptions.CsvValidationException;


public class ASTLoops extends ASTPrep {
	/**
	 * Extracts frequency of Loop Statements Types: for, ForEach and while
	 */

	public List<Integer> getLoopStmts() throws IOException, CsvValidationException {
		List<Integer> loopFrequency = new ArrayList<>();
		for(CompilationUnit ast : getASTs()) {
			if(ast != null) {
				List<Statement> stmts = ast.findAll(Statement.class);
				int count = 0;
				for(Statement stmt : stmts) {
					if(stmt.isForStmt() || stmt.isForEachStmt() || stmt.isWhileStmt()) count++;
				}
				loopFrequency.add(count);
			} else loopFrequency.add(0);
		}
		return loopFrequency;
	}

	public List<Double> extractLoopFeatures() throws IOException, CsvValidationException {
		List<Double> loopFeatures = new ArrayList<>();
		for(int i = 0; i < getCharFrequency().size(); i++) {
			try {
				double temp = Math.log10(getCharFrequency().get(i) / getLoopStmts().get(i));
				loopFeatures.add((double) (Math.round(temp * 100.0) / 100.0));
			} catch (ArithmeticException e) {
				loopFeatures.add((double) 0);
			}
		}
		return loopFeatures;
	}
}