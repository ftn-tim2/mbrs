package myplugin.analyzer.strategies;

import java.util.List;

import myplugin.analyzer.AnalyzeException;
import myplugin.generator.fmmodel.FMProperty;
import myplugin.generator.fmmodel.strereotypes.ComponentType;
import myplugin.generator.fmmodel.strereotypes.Next;

import com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property;
import com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype;

public class NextStrategy implements IParsingStrategy<Next> {

	@Override
	public Next parseObject(Element element) throws AnalyzeException {
		throw new UnsupportedOperationException("This method is not implemented");
	}

	@Override
	public Next parseObject(Element element, String packageName) throws AnalyzeException {
		throw new UnsupportedOperationException("This method is not implemented");
	}

	@SuppressWarnings("rawtypes")
	@Override
	public Next parseObject(Element element, Element parent) throws AnalyzeException {
		Property property = (Property) element;
		Class cclass = (Class) parent;

		//Attributes from property
		if (property.getName() == null) 
			throw new AnalyzeException("Properties of the class: " + cclass.getName() + " must have names!");

		if (property.getType() == null)
			throw new AnalyzeException("Property " + cclass.getName() + "." + property.getName() + " must have type!");

		if (property.getType().getName() == null)
			throw new AnalyzeException("Type ot the property " + cclass.getName() + "." + property.getName() + " must have name!");		

		int lower = property.getLower();
		int upper = property.getUpper();

		Next next = new Next(new FMProperty(property.getName(), property.getType().getName(), property.getVisibility().toString(), lower, upper));
		
		Stereotype nextStereotype = StereotypesHelper.getAppliedStereotypeByString(property, "Next");
		
		//Attributes from UIProperty stereotype
		List lengthList = StereotypesHelper.getStereotypePropertyValue(property, nextStereotype, "length");
		if(lengthList.size() == 1)
			next.setMax_length((Integer) lengthList.get(0));


		List precisionList = StereotypesHelper.getStereotypePropertyValue(property, nextStereotype, "precision");
		if(precisionList.size() == 1)
			next.setDecimal_places((Integer) precisionList.get(0));


		List componentTypeList = StereotypesHelper.getStereotypePropertyValue(property, nextStereotype, "component");
		if(componentTypeList.size() == 1){
			next.setComponent(ComponentType.getComponentNumberByName(((EnumerationLiteral)componentTypeList.get(0)).getName()));
		}

		List nullableList = StereotypesHelper.getStereotypePropertyValue(property, nextStereotype, "nullable");
		if(nullableList.size() == 1)
			next.setNullable((Boolean) nullableList.get(0));
		
		//Attributes from UIElement stereotype
		List labelList = StereotypesHelper.getStereotypePropertyValue(property, nextStereotype, "label");
		if(labelList.size() == 1)
			next.setLabel((String) labelList.get(0)); 
		
		return next;		
	}

}
