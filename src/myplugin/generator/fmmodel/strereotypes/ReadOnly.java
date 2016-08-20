package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.FMProperty;

/**
 * Created by Jozef on 8/20/2016.
 */
public class ReadOnly extends UIProperty {

	public ReadOnly(String name, String type, String visibility, int lower, int upper) {
		super(name, type, visibility, lower, upper);
	}
	
	public ReadOnly(FMProperty property){
		super(property.getName(), property.getType(), property.getVisibility(), property.getUpper(), property.getLower());
	}
	
	@Override
	public String toString() {
		return "ReadOnly : "  + super.getLabel() ;
	}

}
