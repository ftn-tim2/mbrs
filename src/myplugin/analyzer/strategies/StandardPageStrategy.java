package myplugin.analyzer.strategies;

import com.nomagic.uml2.ext.jmi.helpers.ModelHelper;
import com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property;
import com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype;
import myplugin.analyzer.AnalyzeException;
import myplugin.analyzer.ModelAnalyzer;
import myplugin.generator.fmmodel.FMClass;
import myplugin.generator.fmmodel.strereotypes.StandardPage;

import java.util.Iterator;


public class StandardPageStrategy implements IParsingStrategy<StandardPage>{

	@Override
	public StandardPage parseObject(Element element, String packageName) throws AnalyzeException {

		Class cclass = (Class) element;
		StandardPage standardPage = new StandardPage(new FMClass(cclass.getName(), packageName, cclass.getVisibility().toString()));
		Stereotype standardStereotype = StereotypesHelper.getAppliedStereotypeByString(cclass, "StandardPage");

		//Standard page stereotype
		standardPage.setCreate((Boolean) StereotypesHelper.getStereotypePropertyValue(cclass, standardStereotype, "create").get(0));
		standardPage.setRead((Boolean) StereotypesHelper.getStereotypePropertyValue(cclass, standardStereotype, "read").get(0));
		standardPage.setDelete((Boolean) StereotypesHelper.getStereotypePropertyValue(cclass, standardStereotype, "delete").get(0));
		standardPage.setUpdate((Boolean) StereotypesHelper.getStereotypePropertyValue(cclass, standardStereotype, "update").get(0));
		
		//UIElement stereotype
		standardPage.setLabel((String) StereotypesHelper.getStereotypePropertyValue(cclass, standardStereotype, "label").get(0));

		Iterator<Property> it = ModelHelper.attributes(cclass);
		while (it.hasNext()) {
			Property property = it.next();
			standardPage.addProperty(ModelAnalyzer.getPropertyData(property, cclass));	
		}
		
		return standardPage;
	}

	@Override
	public StandardPage parseObject(Element element) {
		throw new UnsupportedOperationException("This method is not implemented");
	}

	@Override
	public StandardPage parseObject(Element element, Element parent) throws AnalyzeException {
		throw new UnsupportedOperationException("This method is not implemented");
	}

}
