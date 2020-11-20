import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.lang.Math;
import java.util.Iterator;

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
		List<Double> condFreq = new ArrayList<>();
		Iterator<CompilationUnit> getASTs = getASTs().iterator();
		while (getASTs.hasNext()) {
			try {
				double count = 0.0;
				List<Statement> stmts = getASTs.next().findAll(Statement.class);
				List<Expression> exps = getASTs.next().findAll(Expression.class);
				for (Statement stmt : stmts) {
					if (stmt.isIfStmt() || stmt.isSwitchStmt() || stmt.isTryStmt()) count++;
				}
				for (Expression exp : exps) {
					if (exp.isConditionalExpr()) count++;
				}
				condFreq.add(count);
			} catch(NullPointerException e) {
				condFreq.add(0.0);
			}
		}
		return condFreq;
	}

	public List<Double> extractConditionalFeatures() throws IOException, CsvValidationException {
		List<Double> conditionals = new ArrayList<>();
		Iterator<Double> getCharFreq = getCharFreq().iterator();
		Iterator<Double> getCondStmts = getCondStmts().iterator();
		while (getCharFreq.hasNext() && getCondStmts.hasNext()) {
			conditionals.add(Math.log10(getCharFreq.next() / getCondStmts.next()));
		}
		return conditionals;
	}
}
