package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.FMClass;

/**
 * Created by Jozef on 8/20/2016.
 */
public class IndexPage extends StandardPage{
	
	private String projectName;
	
	public IndexPage(String name, String classPackage, String visibility, String projectName) {
		super(name, classPackage, visibility);
		this.projectName = projectName;
	}
	
	public IndexPage(FMClass fmClass){
		super(fmClass.getName(), fmClass.getTypePackage(), fmClass.getVisibility());
	}

	public String getProjectName() {
		return projectName;
	}

	public void setProjectName(String projectName) {
		this.projectName = projectName;
	}

}
