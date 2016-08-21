package myplugin.analyzer.strategies;

import com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property;
import com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype;
import myplugin.analyzer.AnalyzeException;
import myplugin.generator.fmmodel.FMProperty;
import myplugin.generator.fmmodel.strereotypes.ComponentType;
import myplugin.generator.fmmodel.strereotypes.UIAssocEnd;

import java.util.List;

public class UIAssocEndStrategy implements IParsingStrategy<UIAssocEnd> {

    @Override
    public UIAssocEnd parseObject(Element element) throws AnalyzeException {
        throw new UnsupportedOperationException("This method is not implemented");
    }

    @Override
    public UIAssocEnd parseObject(Element element, String packageName) throws AnalyzeException {
        throw new UnsupportedOperationException("This method is not implemented");
    }

    @SuppressWarnings("rawtypes")
    @Override
    public UIAssocEnd parseObject(Element element, Element parent) throws AnalyzeException {
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

        UIAssocEnd uiAssocEnd = new UIAssocEnd(new FMProperty(property.getName(), property.getType().getName(), property.getVisibility().toString(), lower, upper));

        Stereotype uiAssocEndStereotype = StereotypesHelper.getAppliedStereotypeByString(property, "UIAssocEnd");

        //Attributes from UIProperty stereotype
        List lengthList = StereotypesHelper.getStereotypePropertyValue(property, uiAssocEndStereotype, "length");
        if (lengthList.size() == 1)
            uiAssocEnd.setMax_length((Integer) lengthList.get(0));


        List precisionList = StereotypesHelper.getStereotypePropertyValue(property, uiAssocEndStereotype, "precision");
        if (precisionList.size() == 1)
            uiAssocEnd.setDecimal_places((Integer) precisionList.get(0));


        List componentTypeList = StereotypesHelper.getStereotypePropertyValue(property, uiAssocEndStereotype, "component");
        if (componentTypeList.size() == 1) {
            uiAssocEnd.setComponent(ComponentType.getComponentNumberByName(((EnumerationLiteral) componentTypeList.get(0)).getName()));
        }

        List nullableList = StereotypesHelper.getStereotypePropertyValue(property, uiAssocEndStereotype, "nullable");
        if (nullableList.size() == 1)
            uiAssocEnd.setNullable((Boolean) nullableList.get(0));

        //Attributes from UIElement stereotype
        List labelList = StereotypesHelper.getStereotypePropertyValue(property, uiAssocEndStereotype, "label");
        if (labelList.size() == 1)
            uiAssocEnd.setLabel((String) labelList.get(0));

        return uiAssocEnd;
    }

}
