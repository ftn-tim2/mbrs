package myplugin.analyzer.strategies;

import java.util.List;

import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Enumeration;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral;

import myplugin.analyzer.AnalyzeException;
import myplugin.generator.fmmodel.FMEnumeration;

public class EnumerationStrategy implements IParsingStrategy<FMEnumeration> {

	@Override
	public FMEnumeration parseObject(Element element) {
		throw new UnsupportedOperationException("This method is not implemented");
	}

	@Override
	public FMEnumeration parseObject(Element element, String packageName) throws AnalyzeException {
		Enumeration enumeration = (Enumeration) element;
		
		FMEnumeration fmEnum = new FMEnumeration(enumeration.getName(), packageName);
		List<EnumerationLiteral> list = enumeration.getOwnedLiteral();
		for (int i = 0; i < list.size(); i++) {
			EnumerationLiteral literal = list.get(i);
			if (literal.getName() == null)  
				throw new AnalyzeException("Items of the enumeration " + enumeration.getName() + " must have names!");
			fmEnum.addValue(literal.getName());
		}
		return fmEnum;
	}

	@Override
	public FMEnumeration parseObject(Element element, Element parent) throws AnalyzeException {
		throw new UnsupportedOperationException("This method is not implemented");
	}

}
