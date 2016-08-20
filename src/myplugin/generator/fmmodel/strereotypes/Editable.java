package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.FMProperty;

/**
 * Created by Jozef on 8/20/2016.
 */
public class Editable extends UIProperty{

	public Editable(String name, String type, String visibility, int lower, int upper) {
		super(name, type, visibility, lower, upper);
	}
	
	public Editable(FMProperty property){
		super(property.getName(), property.getType(), property.getVisibility(), property.getUpper(), property.getLower());
	}
	
	@Override
	public String toString() {
		return "Editable : "  + super.getLabel() ;
	}
}
