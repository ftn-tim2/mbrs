package myplugin.generator.fmmodel;

import java.util.ArrayList;
import java.util.List;

public class FMMethod extends FMElement{
	
	private List<String> parameters = new ArrayList<>();
	
	public FMMethod(){
		
	}

	public FMMethod(List<String> parameters) {
		super();
		this.parameters = parameters;
	}

	public List<String> getParameters() {
		return parameters;
	}

	public void setParameters(List<String> parameters) {
		this.parameters = parameters;
	}
	
	

}
