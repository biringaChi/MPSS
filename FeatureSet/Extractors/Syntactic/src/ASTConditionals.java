import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Iterator;

import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.expr.Expression;
import com.github.javaparser.ast.stmt.Statement;
import com.opencsv.exceptions.CsvValidationException;


public class ASTConditionals extends ASTPrep {
	/**
	 * Extracts frequency of Conditional Statements
	 * Types: If, Switch, Try-Catch and Ternary 
	 */ 

	public List<Double> getCondStmts() throws IOException, CsvValidationException {
		List<Double> condFreqs = new ArrayList<>();
		Iterator<String> getSourcecode = getSourcecode().iterator();
		while(getSourcecode.hasNext()) {
			try {
				CompilationUnit compilationUnit = StaticJavaParser.parse(getSourcecode.next());
				double count = 0.0;
				List<Statement> stmts = compilationUnit.findAll(Statement.class);
				List<Expression> exps = compilationUnit.findAll(Expression.class);
				for (Statement stmt : stmts) {
					if (stmt.isIfStmt() || stmt.isSwitchStmt() || stmt.isTryStmt()) {
						count++;
					} 
				}
				for (Expression exp : exps) {
					if (exp.isConditionalExpr()) {
						count++;
					} 
				}
				condFreqs.add(count);
			} catch (Exception e) {
				condFreqs.add(0.0);
			}
		}
		return condFreqs;
	}

	public List<Double> extractConditionalFeatures() throws IOException, CsvValidationException {
		List<Double> conditionals = new ArrayList<>();
		Iterator<Double> getCharFreqs = getCharFreqs().iterator();
		Iterator<Double> getCondStmts = getCondStmts().iterator();
		while (getCharFreqs.hasNext() && getCondStmts.hasNext()) {
			conditionals.add(Math.log10(getCharFreqs.next() / getCondStmts.next()));
		}
		Collections.replaceAll(conditionals, Double.POSITIVE_INFINITY, 0.0);
		return conditionals;
	}
}
