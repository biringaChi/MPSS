import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
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
	public List<Double> getLiteralExps() throws IOException, CsvValidationException {
		List<Double> literalFreq = new ArrayList<>();
		Iterator<CompilationUnit> getASTs = getASTs().iterator();
		while (getASTs.hasNext()) {
			try {
				double count = 0.0;
				List<Expression> exps = getASTs.next().findAll(Expression.class);
				for (Expression exp : exps) {
					if (exp.isLiteralExpr() || exp.isIntegerLiteralExpr() 
					|| exp.isDoubleLiteralExpr() || exp.isCharLiteralExpr() 
					|| exp.isTextBlockLiteralExpr() || exp.isNormalAnnotationExpr()) count++;
				}
				literalFreq.add(count);
			} catch(NullPointerException e) {
				literalFreq.add(0.0);
			}
		}
		return literalFreq;
	}

	public List<Double> extractLiteralFeatures() throws IOException, CsvValidationException {
		List<Double> literals = new ArrayList<>();
		Iterator<Double> getCharFreq = getCharFreq().iterator();
		Iterator<Double> getLiteralExps = getLiteralExps().iterator();
		while (getCharFreq.hasNext() && getLiteralExps.hasNext()) {
			literals.add(Math.log10(getCharFreq.next() / getLiteralExps.next()));
		}
		return literals;
	}
}