package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.FMProperty;
import myplugin.generator.fmmodel.strereotypes.interfaces.IUIElement;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Created by Jozef on 8/20/2016.
 */
public class UIProperty extends FMProperty implements IUIElement {

    public static String NAME = "UIProperty";
    //"max_length", "editable", "component", "nullable", "decimal_places", "max_digits", "defaultValue"

    // label not used.. for now
    protected UIElement uiElement;

    private Integer max_length;
    private Boolean editable;
    private Integer decimal_places;
    private String component;
    private Boolean nullable;
    private Integer max_digits;
    private String defaultValue;
    private List<String> propertiesKeyValue;

    public UIProperty() {
        super();
    }

    public UIProperty(String name, String type, String visibility, int lower, int upper) {
        super(name, type, visibility, lower, upper);
        uiElement = new UIElement();
    }

    public UIProperty(FMProperty property) {
        super(property.getName(), property.getType(), property.getVisibility(), property.getUpper(), property.getLower());
        uiElement = new UIElement();
    }

    public UIProperty(FMProperty fmProperty, Integer max_length, Boolean editable, Integer decimal_places,
                      String component, Boolean nullable, Integer max_digits, String defaultValue) {
        super(fmProperty.getName(), fmProperty.getType(), fmProperty.getVisibility(), fmProperty.getLower(), fmProperty.getUpper());
        this.max_length = max_length;
        this.editable = editable;
        this.decimal_places = decimal_places;
        setComponent(component);
        this.nullable = nullable;
        this.max_digits = max_digits;
        this.defaultValue = defaultValue;
        uiElement = new UIElement();
    }

    public Iterator<String> getPropertiesKeyValue() {
        if (propertiesKeyValue == null) {
            propertiesKeyValue = new ArrayList<>();
            addValueToPropertiesKeyValue("max_length = ", max_length);
            addValueToPropertiesKeyValue("editable = ", editable);
            addValueToPropertiesKeyValue("decimal_places = ", decimal_places);
            addValueToPropertiesKeyValue("null = ", nullable);
            addValueToPropertiesKeyValue("max_digits = ", max_digits);
            addValueToPropertiesKeyValue("default = ", defaultValue);

        }
        return propertiesKeyValue.iterator();

    }

    private void addValueToPropertiesKeyValue(String s, Object o) {
        if (o != null)
            propertiesKeyValue.add(s + o);
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

    public Integer getMax_length() {
        return max_length;
    }

    public void setMax_length(Integer max_length) {
        this.max_length = max_length;
    }

    public Integer getDecimal_places() {
        return decimal_places;
    }

    public void setDecimal_places(Integer decimal_places) {
        this.decimal_places = decimal_places;
    }

    public String getComponent() {
        return component;
    }

    public void setComponent(String component) {
        //"bigInteger" | "binary" | "boolean" | "char" | "commaSeparatedInteger" | "Date" | "dateTime" | "decimal" |
        // "duration" | "email" | "file" | "filePath" | "float" | "image" | "int" | "nullBoolean" | "positiveInteger" |
        // "positiveSmallInteger" | "slug" | "smallInteger" | "text" | "time" | "URL" | "UUID" | "foreignKey"|
        // "manyToMany" | "oneToOne"
        switch (component)
        {
            case "": this.component = "";break;
        }
        this.component = component;
    }

    public Boolean getNullable() {
        return nullable;
    }

    public void setNullable(Boolean nullable) {
        this.nullable = nullable;
    }

    public Boolean getEditable() {
        return editable;
    }

    public void setEditable(Boolean editable) {
        this.editable = editable;
    }

    public Integer getMax_digits() {
        return max_digits;
    }

    public void setMax_digits(Integer max_digits) {
        this.max_digits = max_digits;
    }

    public String getDefaultValue() {
        return defaultValue;
    }

    public void setDefaultValue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
}
