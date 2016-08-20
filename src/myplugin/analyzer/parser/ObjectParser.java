package myplugin.analyzer.parser;

import myplugin.analyzer.AnalyzeException;
import myplugin.analyzer.strategies.IParsingStrategy;

import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;

public class ObjectParser<E> {

    private IParsingStrategy<E> strategy;

    public ObjectParser(IParsingStrategy<E> strategy) {
        super();
        this.strategy = strategy;
    }

    public E parse(Element element) throws AnalyzeException {
        return strategy.parseObject(element);
    }

    public E parse(Element element, String packageName) throws AnalyzeException {
        return strategy.parseObject(element, packageName);
    }

    public E parse(Element element, Element parent) throws AnalyzeException {
        return strategy.parseObject(element, parent);
    }

}
