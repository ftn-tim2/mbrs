package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.FMClass;
import myplugin.generator.fmmodel.strereotypes.interfaces.IUIElement;

/**
 * Created by Jozef on 8/20/2016.
 */
public abstract class UIClass extends FMClass implements IUIElement{
	
	private UIElement uiElement;

	public UIClass(){
		super();
	}

	public UIClass(String name, String classPackage, String visibility) {
		super(name, classPackage, visibility);
		uiElement = new UIElement();
	}
	
	public String getLabel() {
		return uiElement.getLabel();
	}

	public void setLabel(String label) {
		uiElement.setLabel(label);
	}

}
