package myplugin.analyzer.strategies;

import myplugin.analyzer.AnalyzeException;
import myplugin.generator.fmmodel.FMProperty;

import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property;

public class FMPropertyStrategy implements IParsingStrategy<FMProperty> {

	@Override
	public FMProperty parseObject(Element element) throws AnalyzeException {
		throw new UnsupportedOperationException("This method is not implemented");
	}

	@Override
	public FMProperty parseObject(Element element, String packageName) throws AnalyzeException {
		throw new UnsupportedOperationException("This method is not implemented");
	}

	@Override
	public FMProperty parseObject(Element element, Element parent) throws AnalyzeException {
		Property property = (Property) element;
		Class cclass = (Class) parent;

		if (property.getName() == null) 
			throw new AnalyzeException("Properties of the class: " + cclass.getName() + " must have names!");

		if (property.getType() == null)
			throw new AnalyzeException("Property " + cclass.getName() + "." + property.getName() + " must have type!");

		if (property.getType().getName() == null)
			throw new AnalyzeException("Type ot the property " + cclass.getName() + "." + property.getName() + " must have name!");		

		int lower = property.getLower();
		int upper = property.getUpper();

		return new FMProperty(property.getName(), property.getType().getName(), property.getVisibility().toString(), lower, upper);
	}

}
