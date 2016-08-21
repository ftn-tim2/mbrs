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
import myplugin.generator.fmmodel.strereotypes.UIProperty;

import java.util.List;

public class UIPropertyStrategy implements IParsingStrategy<UIProperty> {

    @Override
    public UIProperty parseObject(Element element) throws AnalyzeException {
        throw new UnsupportedOperationException("This method is not implemented");
    }

    @Override
    public UIProperty parseObject(Element element, String packageName) throws AnalyzeException {
        throw new UnsupportedOperationException("This method is not implemented");
    }

    @SuppressWarnings("rawtypes")
    @Override
    public UIProperty parseObject(Element element, Element parent) throws AnalyzeException {
        Property property = (Property) element;
        Class _class = (Class) parent;

        //Attributes from property
        if (property.getName() == null)
            throw new AnalyzeException("Properties of the class: " + _class.getName() + " must have names!");

        if (property.getType() == null)
            throw new AnalyzeException("Property " + _class.getName() + "." + property.getName() + " must have type!");

        if (property.getType().getName() == null)
            throw new AnalyzeException("Type ot the property " + _class.getName() + "." + property.getName() + " must have name!");

        int lower = property.getLower();
        int upper = property.getUpper();

        UIProperty uiProperty = new UIProperty(new FMProperty(property.getName(), property.getType().getName(), property.getVisibility().toString(), lower, upper));

        Stereotype uiPropertyStereotype = StereotypesHelper.getAppliedStereotypeByString(property, UIProperty.NAME);

        //"max_length", "editable", "component", "nullable", "decimal_places", "max_digits", "defaultValue"
        Object valueFromStereotype = extractValueFromStereotype(property, uiPropertyStereotype, "max_length");
        uiProperty.setMax_length((Integer) valueFromStereotype);

        valueFromStereotype = extractValueFromStereotype(property, uiPropertyStereotype, "editable");
        uiProperty.setEditable((Boolean) valueFromStereotype);

        valueFromStereotype = extractValueFromStereotype(property, uiPropertyStereotype, "component");
        if (valueFromStereotype!=null)
            uiProperty.setComponent(ComponentType.getComponentNumberByName(((EnumerationLiteral) valueFromStereotype).getName()));

        valueFromStereotype = extractValueFromStereotype(property, uiPropertyStereotype, "nullable");
        uiProperty.setNullable((Boolean) valueFromStereotype);

        valueFromStereotype = extractValueFromStereotype(property, uiPropertyStereotype, "decimal_places");
        uiProperty.setDecimal_places((Integer) valueFromStereotype);

        valueFromStereotype = extractValueFromStereotype(property, uiPropertyStereotype, "max_digits");
        uiProperty.setMax_digits((Integer) valueFromStereotype);

        valueFromStereotype = extractValueFromStereotype(property, uiPropertyStereotype, "defaultValue");
        uiProperty.setDefaultValue((String) valueFromStereotype);

        return uiProperty;
    }

    private Object extractValueFromStereotype(Element element, Stereotype stereotype, String s) {
        List lengthList = StereotypesHelper.getStereotypePropertyValue(element, stereotype, s);
        if (lengthList.size() == 1)
            return lengthList.get(0);
        else
            return null;
    }
}
