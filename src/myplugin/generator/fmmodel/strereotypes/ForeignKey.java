package myplugin.generator.fmmodel.strereotypes;

import myplugin.analyzer.AnalyzeException;
import myplugin.generator.fmmodel.FMProperty;
import org.apache.commons.collections.IteratorUtils;

import java.util.Iterator;
import java.util.List;

/**
 * Created by Jozef on 8/20/2016.
 */
public class ForeignKey extends UIProperty {

    public ForeignKey() {
        super();
    }

    public ForeignKey(String name, String type, String visibility, int lower, int upper) {
        super(name, type, visibility, lower, upper);
        uiElement = new UIElement();
    }

    public ForeignKey(FMProperty fmProperty, Integer length, Integer precision, Boolean nullable) {
        super(fmProperty.getName(), fmProperty.getType(), fmProperty.getVisibility(), fmProperty.getLower(), fmProperty.getUpper());
        uiElement = new UIElement();
    }

    public ForeignKey(FMProperty property) {
        super(property.getName(), property.getType(), property.getVisibility(), property.getUpper(), property.getLower());
        uiElement = new UIElement();
    }

    public String getLabel() {
        return uiElement.getLabel();
    }

    public void setLabel(String label) {
        uiElement.setLabel(label);
    }

    public UIElement getUiElement() {
        return uiElement;
    }

    public void setUiElement(UIElement uiElement) {
        this.uiElement = uiElement;
    }

    @Override
    public Iterator<String> getPropertiesKeyValue() throws AnalyzeException {
        List result = IteratorUtils.toList(super.getPropertiesKeyValue());
        result.add("to = " + "\"" + this.getType() + "\"");
        return result.iterator();
    }

}
