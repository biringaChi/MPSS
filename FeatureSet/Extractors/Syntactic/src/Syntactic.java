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
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.Node.PreOrderIterator;
import com.google.common.collect.Iterators;


class ASTConditionals extends ASTPrep {
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

class ASTLiterals extends ASTPrep {
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


class ASTLoops extends ASTPrep {
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


class ASTNodes extends ASTPrep {
	/**
	 * Extracts frequency of Nodes
	 */ 

	public List<Double> getNodeFreqs() throws CsvValidationException, IOException {
		List<Double> nodes = new ArrayList<>();
		for (CompilationUnit ast : getASTs()) {
			if (ast != null) {
				PreOrderIterator iterator = new Node.PreOrderIterator(ast);
				double size = Iterators.size(iterator);
				nodes.add(size);
			} else nodes.add(0.0);
		}
		return nodes;
	}

	public List<Double> extractNodeFeatures() throws IOException, CsvValidationException {
		List<Double> nodes = new ArrayList<>();
		Iterator<Double> getCharFreqs = getCharFreqs().iterator();
		Iterator<Double> getNodeFreqs = getNodeFreqs().iterator();
		while (getCharFreqs.hasNext() && getNodeFreqs.hasNext()) {
			nodes.add(Math.log10(getCharFreqs.next() / getNodeFreqs.next()));
		}
		Collections.replaceAll(nodes, Double.POSITIVE_INFINITY, 0.0);
		return nodes;
	}
}
