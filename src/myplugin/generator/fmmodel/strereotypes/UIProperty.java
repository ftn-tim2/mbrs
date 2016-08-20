package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.FMProperty;
import myplugin.generator.fmmodel.strereotypes.interfaces.IUIElement;

/**
 * Created by Jozef on 8/20/2016.
 */
public class UIProperty extends FMProperty implements IUIElement{
	
	protected UIElement uiElement;
	
	private Integer length;
	private Integer precision;
	private ComponentType componentType;
	private Boolean nullable;

	public UIProperty(String name, String type, String visibility, int lower, int upper) {
		super(name, type, visibility, lower, upper);
		uiElement = new UIElement();
	}
	
	public UIProperty(FMProperty fmProperty, Integer length, Integer precision, ComponentType componentType, Boolean nullable){
		super(fmProperty.getName(), fmProperty.getType(), fmProperty.getVisibility(), fmProperty.getLower(), fmProperty.getUpper());
		this.length = length;
		this.precision = precision;
		this.componentType = componentType;
		this.nullable = nullable;
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

	public Integer getLength() {
		return length;
	}

	public void setLength(Integer length) {
		this.length = length;
	}

	public Integer getPrecision() {
		return precision;
	}

	public void setPrecision(Integer precision) {
		this.precision = precision;
	}

	public ComponentType getComponentType() {
		return componentType;
	}

	public void setComponentType(ComponentType componentType) {
		this.componentType = componentType;
	}

	public Boolean getNullable() {
		return nullable;
	}

	public void setNullable(Boolean nullable) {
		this.nullable = nullable;
	}

}
