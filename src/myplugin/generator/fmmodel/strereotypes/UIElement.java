package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.strereotypes.interfaces.IUIElement;

/**
 * Created by Jozef on 8/20/2016.
 */
public class UIElement implements IUIElement{
	
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
