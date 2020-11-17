import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.expr.Expression;
import com.github.javaparser.ast.stmt.Statement;
import com.opencsv.exceptions.CsvValidationException;


public class ASTConditionals extends ASTPrep {
	/**
	 * Extracts frequency of Conditional Statements
	 * Types: If, Switch, Try-Catch and Ternary 
	 */ 
	public List<Integer> getCondStmts() throws IOException, CsvValidationException {
		List<Integer> condFrequency = new ArrayList<>();
		for(CompilationUnit ast : getASTs()) {
			if(ast != null) {
				List<Statement> stmts = ast.findAll(Statement.class);
				List<Expression> exps = ast.findAll(Expression.class);
				int count = 0;
				for(Statement stmt : stmts) {
					if(stmt.isIfStmt() || stmt.isSwitchStmt() || stmt.isTryStmt()) count++;
				}
				for(Expression exp : exps) {
					if(exp.isConditionalExpr()) count++;
				}
				condFrequency.add(count);
			} else condFrequency.add(0);
		}
		return condFrequency;
	}

	public List<Double> extractConditionalFeatures() throws IOException, CsvValidationException {
		List<Double> conditionalFeatures = new ArrayList<>();
		for(int i = 0; i < getCharFrequency().size(); i++) {
			try {
				double temp = Math.log10(getCharFrequency().get(i) / getCondStmts().get(i));
				conditionalFeatures.add((double) (Math.round(temp * 100.0) / 100.0));
			} catch (ArithmeticException e) {
				conditionalFeatures.add((double) 0);
			}
		}
		return conditionalFeatures;
	}
}
