package myplugin.analyzer.strategies;

import com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property;
import com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype;
import myplugin.analyzer.AnalyzeException;
import myplugin.generator.fmmodel.FMProperty;
import myplugin.generator.fmmodel.strereotypes.ForeignKey;

import java.util.List;

public class ForeignKeyStrategy implements IParsingStrategy<ForeignKey> {

    @Override
    public ForeignKey parseObject(Element element) throws AnalyzeException {
        throw new UnsupportedOperationException("This method is not implemented");
    }

    @Override
    public ForeignKey parseObject(Element element, String packageName) throws AnalyzeException {
        throw new UnsupportedOperationException("This method is not implemented");
    }

    @SuppressWarnings("rawtypes")
    @Override
    public ForeignKey parseObject(Element element, Element parent) throws AnalyzeException {
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

        ForeignKey foreignKey = new ForeignKey(new FMProperty(property.getName(), property.getType().getName(), property.getVisibility().toString(), lower, upper));

        Stereotype foreignKeyStereoType = StereotypesHelper.getAppliedStereotypeByString(property, "ForeignKey");

        //Attributes from UIProperty stereotype
        List lengthList = StereotypesHelper.getStereotypePropertyValue(property, foreignKeyStereoType, "length");
        if(lengthList.size() == 1)
            foreignKey.setMax_length((Integer) lengthList.get(0));


        List precisionList = StereotypesHelper.getStereotypePropertyValue(property, foreignKeyStereoType, "precision");
        if(precisionList.size() == 1)
            foreignKey.setDecimal_places((Integer) precisionList.get(0));


        List componentTypeList = StereotypesHelper.getStereotypePropertyValue(property, foreignKeyStereoType, "component");
        if(componentTypeList.size() == 1){
            String name = ((EnumerationLiteral)componentTypeList.get(0)).getName();
            foreignKey.setComponent(name);
        }

        List nullableList = StereotypesHelper.getStereotypePropertyValue(property, foreignKeyStereoType, "nullable");
        if(nullableList.size() == 1)
            foreignKey.setNullable((Boolean) nullableList.get(0));

        //Attributes from UIElement stereotype
        List labelList = StereotypesHelper.getStereotypePropertyValue(property, foreignKeyStereoType, "label");
        if(labelList.size() == 1)
            foreignKey.setLabel((String) labelList.get(0));

        return foreignKey;
    }

}
