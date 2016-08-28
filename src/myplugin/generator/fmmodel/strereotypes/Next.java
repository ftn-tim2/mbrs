package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.FMProperty;
import org.apache.commons.collections.IteratorUtils;

import java.util.Iterator;
import java.util.List;

/**
 * Created by Jozef on 8/20/2016.
 */
public class Next extends UIAssocEnd {

    @Override
    public String toString() {
        return "Next : " + super.getLabel();
    }

    public Next() {
        super();
    }

    public Next(String name, String type, String visibility, int lower, int upper) {
        super(name, type, visibility, lower, upper);
    }

    public Next(FMProperty property) {
        super(property.getName(), property.getType(), property.getVisibility(), property.getUpper(), property.getLower());
    }

    @Override
    public Iterator<String> getPropertiesKeyValue() {
        List result = IteratorUtils.toList(super.getPropertiesKeyValue());
        result.add("to = " + "\"" + this.getType() + "\"");
        return result.iterator();
    }

}
