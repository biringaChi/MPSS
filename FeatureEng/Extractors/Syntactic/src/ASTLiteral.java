import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.expr.Expression;
import com.opencsv.exceptions.CsvValidationException;


public class ASTLiteral extends ASTPrep {
	/**
	 * Extracts frequency of Literal Expressions
	 * Types: number(int, double, float), character, string, boolean, null, etc.
	 */ 
	public List<Integer> getLiteralExps() throws IOException, CsvValidationException {
		List<Integer> literalFrequency = new ArrayList<>();
		for (CompilationUnit ast : getASTs()) {
			if (ast != null) {
				List<Expression> exps = ast.findAll(Expression.class);
				int count = 0;
				for (Expression exp : exps) {
					if (exp.isLiteralExpr() || exp.isIntegerLiteralExpr() 
					|| exp.isDoubleLiteralExpr() || exp.isCharLiteralExpr() 
					|| exp.isTextBlockLiteralExpr() || exp.isNormalAnnotationExpr()) count++;
				}
				literalFrequency.add(count);
			} else literalFrequency.add(0);
		}
		return literalFrequency;
	}

	public List<Double> extractLiteralFeatures() throws IOException, CsvValidationException {
		List<Double> conditionalFeatures = new ArrayList<>();
		for (int i = 0; i < getCharFrequency().size(); i++) {
			try {
				double temp = Math.log10(getCharFrequency().get(i) / getLiteralExps().get(i));
				System.out.println(temp);
				conditionalFeatures.add((double) (Math.round(temp * 100.0) / 100.0));
			} catch (ArithmeticException e) {
				conditionalFeatures.add((double) 0);
			}
		}
		return conditionalFeatures;
	}
}