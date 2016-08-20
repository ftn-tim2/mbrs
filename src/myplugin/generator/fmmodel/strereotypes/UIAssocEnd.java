package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.FMProperty;

/**
 * Created by Jozef on 8/20/2016.
 */
public class UIAssocEnd extends UIProperty{

	public UIAssocEnd(String name, String type, String visibility, int lower, int upper) {
		super(name, type, visibility, lower, upper);
		uiElement = new UIElement();
	}
	
	public UIAssocEnd(FMProperty fmProperty, Integer length, Integer precision, ComponentType componentType, Boolean nullable){
		super(fmProperty.getName(), fmProperty.getType(), fmProperty.getVisibility(), fmProperty.getLower(), fmProperty.getUpper());
		uiElement = new UIElement();
	}
	
	public UIAssocEnd(FMProperty property){
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
	
}
