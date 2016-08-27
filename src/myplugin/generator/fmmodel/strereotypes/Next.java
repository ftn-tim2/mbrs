package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.FMProperty;

/**
 * Created by Jozef on 8/20/2016.
 */
public class Next extends UIAssocEnd {

	@Override
	public String toString() {
		return "Next : "  + super.getLabel() ;
	}

	public Next(){
		super();
	}

	public Next(String name, String type, String visibility, int lower, int upper) {
		super(name, type, visibility, lower, upper);
	}
	
	public Next(FMProperty property){
		super(property.getName(), property.getType(), property.getVisibility(), property.getUpper(), property.getLower());
	}
	
}
