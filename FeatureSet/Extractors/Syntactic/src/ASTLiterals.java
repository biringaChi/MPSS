import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.expr.Expression;
import com.opencsv.exceptions.CsvValidationException;


public class ASTLiterals extends ASTPrep {
	/**
	 * Extracts frequency of Literal Expressions
	 * Types: number(int, double, float), character, string, boolean, null, etc.
	 */
	 
	public List<Double> getLiteralExps() throws IOException, CsvValidationException {
		List<Double> literalFreqs = new ArrayList<>();
		Iterator<String> getSourcecode = getSourcecode().iterator();
		while(getSourcecode.hasNext()) {
			try {
				CompilationUnit compilationUnit = StaticJavaParser.parse(getSourcecode.next());
				double count = 0.0;
				List<Expression> exps = compilationUnit.findAll(Expression.class);
				for (Expression exp : exps) {
					if (exp.isLiteralExpr() || exp.isIntegerLiteralExpr() 
					|| exp.isDoubleLiteralExpr() || exp.isCharLiteralExpr() 
					|| exp.isTextBlockLiteralExpr() || exp.isNormalAnnotationExpr()) count++;
				}
				literalFreqs.add(count);
			} catch (Exception e) {
				literalFreqs.add(0.0);
			}
		}
		return literalFreqs;
	}

	public List<Double> extractLiteralFeatures() throws IOException, CsvValidationException {
		List<Double> literals = new ArrayList<>();
		Iterator<Double> getCharFreqs = getCharFreqs().iterator();
		Iterator<Double> getLiteralExps = getLiteralExps().iterator();
		while (getCharFreqs.hasNext() && getLiteralExps.hasNext()) {
			literals.add(Math.log10(getCharFreqs.next() / getLiteralExps.next()));
		}
		Collections.replaceAll(literals, Double.POSITIVE_INFINITY, 0.0);
		return literals;
	}
}