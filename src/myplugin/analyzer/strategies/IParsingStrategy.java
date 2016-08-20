package myplugin.analyzer.strategies;

import myplugin.analyzer.AnalyzeException;

import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;

public interface IParsingStrategy<E> {
	public E parseObject(Element element) throws AnalyzeException;
	public E parseObject(Element element, String packageName) throws AnalyzeException;
	public E parseObject(Element element, Element parent) throws AnalyzeException;
}
