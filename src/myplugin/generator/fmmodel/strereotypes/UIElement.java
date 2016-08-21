package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.strereotypes.interfaces.IUIElement;

public class UIElement implements IUIElement {

    public static String NAME = "UIElement";

    private String label;

    public UIElement() {
        label = "";
    }

    public UIElement(String label) {
        super();
        this.label = label;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}
