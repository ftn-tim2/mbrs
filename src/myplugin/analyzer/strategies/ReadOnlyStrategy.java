package myplugin.analyzer.strategies;

import java.util.List;

import myplugin.analyzer.AnalyzeException;
import myplugin.generator.fmmodel.FMProperty;
import myplugin.generator.fmmodel.strereotypes.ComponentType;
import myplugin.generator.fmmodel.strereotypes.ReadOnly;

import com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property;
import com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype;

public class ReadOnlyStrategy implements IParsingStrategy<ReadOnly> {

	@Override
	public ReadOnly parseObject(Element element) throws AnalyzeException {
		throw new UnsupportedOperationException("This method is not implemented");
	}

	@Override
	public ReadOnly parseObject(Element element, String packageName) throws AnalyzeException {
		throw new UnsupportedOperationException("This method is not implemented");
	}

	@SuppressWarnings("rawtypes")
	@Override
	public ReadOnly parseObject(Element element, Element parent) throws AnalyzeException {
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

		ReadOnly readOnly = new ReadOnly(new FMProperty(property.getName(), property.getType().getName(), property.getVisibility().toString(), lower, upper));
		
		Stereotype readOnlyStereotype = StereotypesHelper.getAppliedStereotypeByString(property, "ReadOnly");
		
		//Attributes from UIProperty stereotype
				List lengthList = StereotypesHelper.getStereotypePropertyValue(property, readOnlyStereotype, "length");
				if(lengthList.size() == 1)
					readOnly.setLength((Integer) lengthList.get(0)); 
					
				
				List precisionList = StereotypesHelper.getStereotypePropertyValue(property, readOnlyStereotype, "precision");
				if(precisionList.size() == 1)
					readOnly.setPrecision((Integer) precisionList.get(0));
				
				
				List componentTypeList = StereotypesHelper.getStereotypePropertyValue(property, readOnlyStereotype, "component");
				if(componentTypeList.size() == 1){
					readOnly.setComponentType(ComponentType.getComponentNumberByName(((EnumerationLiteral)componentTypeList.get(0)).getName()));
				}
				
				List nullableList = StereotypesHelper.getStereotypePropertyValue(property, readOnlyStereotype, "nullable");
				if(nullableList.size() == 1)
					readOnly.setNullable((Boolean) nullableList.get(0));
				
				//Attributes from UIElement stereotype
				List labelList = StereotypesHelper.getStereotypePropertyValue(property, readOnlyStereotype, "label");
				if(labelList.size() == 1)
					readOnly.setLabel((String) labelList.get(0));

		return readOnly;		
	}

}
