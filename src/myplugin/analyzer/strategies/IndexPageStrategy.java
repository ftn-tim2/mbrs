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
import myplugin.generator.fmmodel.strereotypes.IndexPage;

import java.util.Iterator;

public class IndexPageStrategy implements IParsingStrategy<IndexPage> {

    @Override
    public IndexPage parseObject(Element element) {
        throw new UnsupportedOperationException("This method is not implemented");
    }

    @Override
    public IndexPage parseObject(Element element, String packageName) throws AnalyzeException {
        Class _class = (Class) element;

        IndexPage indexPage = new IndexPage(new FMClass(_class.getName(), packageName, _class.getVisibility().toString()));
        Stereotype indexStereotype = StereotypesHelper.getAppliedStereotypeByString(_class, "IndexPage");

        indexPage.setLabel((String) StereotypesHelper.getStereotypePropertyValue(_class, indexStereotype, "label").get(0));
        indexPage.setProjectName((String) StereotypesHelper.getStereotypePropertyValue(_class, indexStereotype, "projectName").get(0));

        Iterator<Property> it = ModelHelper.attributes(_class);
        while (it.hasNext()) {
            Property property = it.next();
            indexPage.addProperty(ModelAnalyzer.getPropertyData(property, _class));
        }

        return indexPage;
    }

    @Override
    public IndexPage parseObject(Element element, Element parent) {
        throw new UnsupportedOperationException("This method is not implemented");
    }

}
