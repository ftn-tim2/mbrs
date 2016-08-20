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
import myplugin.generator.fmmodel.strereotypes.Editable;

import java.util.List;

public class EditableStrategy implements IParsingStrategy<Editable> {

    @Override
    public Editable parseObject(Element element) throws AnalyzeException {
        throw new UnsupportedOperationException("This method is not implemented");
    }

    @Override
    public Editable parseObject(Element element, String packageName) throws AnalyzeException {
        throw new UnsupportedOperationException("This method is not implemented");
    }

    @SuppressWarnings("rawtypes")
    @Override
    public Editable parseObject(Element element, Element parent) throws AnalyzeException {
        Property property = (Property) element;
        Class cclass = (Class) parent;

        //Attributes from property
        if (property.getName() == null)
            throw new AnalyzeException("Properties of the class: " + cclass.getName() + " must have names!");

        if (property.getType() == null)
            throw new AnalyzeException("Property " + cclass.getName() + "." + property.getName() + " must have type!");

        if (property.getType().getName() == null)
            throw new AnalyzeException("Type ot the property " + cclass.getName() + "." + property.getName() + " must have name!");

        Editable editable = new Editable(new FMProperty(property.getName(), property.getType().getName(), property.getVisibility().toString(), property.getLower(), property.getUpper()));

        Stereotype editableStereotype = StereotypesHelper.getAppliedStereotypeByString(property, "Editable");

        //Attributes from UIProperty stereotype
        List lengthList = StereotypesHelper.getStereotypePropertyValue(property, editableStereotype, "length");
        if (lengthList.size() == 1)
            editable.setLength((Integer) lengthList.get(0));


        List precisionList = StereotypesHelper.getStereotypePropertyValue(property, editableStereotype, "precision");
        if (precisionList.size() == 1)
            editable.setPrecision((Integer) precisionList.get(0));


        List componentTypeList = StereotypesHelper.getStereotypePropertyValue(property, editableStereotype, "component");
        if (componentTypeList.size() == 1) {
            editable.setComponentType(ComponentType.getComponentNumberByName(((EnumerationLiteral) componentTypeList.get(0)).getName()));
        }

        List nullableList = StereotypesHelper.getStereotypePropertyValue(property, editableStereotype, "nullable");
        if (nullableList.size() == 1)
            editable.setNullable((Boolean) nullableList.get(0));

        //Attributes from UIElement stereotype
        List labelList = StereotypesHelper.getStereotypePropertyValue(property, editableStereotype, "label");
        if (labelList.size() == 1)
            editable.setLabel((String) labelList.get(0));

        return editable;
    }

}
