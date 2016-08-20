package myplugin.analyzer.strategies;

import java.util.Iterator;

import myplugin.analyzer.AnalyzeException;
import myplugin.analyzer.ModelAnalyzer;
import myplugin.generator.fmmodel.FMClass;
import myplugin.generator.fmmodel.strereotypes.IndexPage;

import com.nomagic.uml2.ext.jmi.helpers.ModelHelper;
import com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property;
import com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype;

public class IndexPageStrategy implements IParsingStrategy<IndexPage> {

	@Override
	public IndexPage parseObject(Element element) {
		throw new UnsupportedOperationException("This method is not implemented");
	}

	@Override
	public IndexPage parseObject(Element element, String packageName) throws AnalyzeException {
		Class cclass = (Class) element;
		
		IndexPage indexPage = new IndexPage(new FMClass(cclass.getName(), packageName, cclass.getVisibility().toString()));
		Stereotype indexStereotype = StereotypesHelper.getAppliedStereotypeByString(cclass, "IndexPage");
		
		indexPage.setLabel((String) StereotypesHelper.getStereotypePropertyValue(cclass, indexStereotype, "label").get(0));
		indexPage.setProjectName((String) StereotypesHelper.getStereotypePropertyValue(cclass, indexStereotype, "projectName").get(0));
		
		Iterator<Property> it = ModelHelper.attributes(cclass);
		while (it.hasNext()) {
			Property property = it.next();
			indexPage.addProperty(ModelAnalyzer.getPropertyData(property, cclass));	
		}
		
		return indexPage;
	}

	@Override
	public IndexPage parseObject(Element element, Element parent){
		throw new UnsupportedOperationException("This method is not implemented");
	}

}
