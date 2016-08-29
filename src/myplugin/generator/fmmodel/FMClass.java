package myplugin.generator.fmmodel;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;


public class FMClass extends FMType {	
	
	private String visibility;
	

	//Class properties
	private List<FMProperty> FMProperties = new ArrayList<>();
	
	//list of packages (for import declarations) 
	private List<String> importedPackages = new ArrayList<>();
	
	/** @ToDo: add list of methods */
	private List<String> methods = new ArrayList<>();

	public FMClass(){
		super();
	}
	
	public FMClass(String name, String classPackage, String visibility) {
		super(name, classPackage);		
		this.visibility = visibility;
	}	
	
	public List<String> getMethods() {
		return methods;
	}

	public List<FMProperty> getProperties(){
		return FMProperties;
	}
	
	public Iterator<String> getMethodsIterator(){
		return methods.iterator();
	}
	
	public void addMethod(String method){
		methods.add(method);
	}
	
	public int getMethodsCount(){
		return methods.size();
	}
	
	public Iterator<FMProperty> getPropertyIterator(){
		return FMProperties.iterator();
	}
	
	public void addProperty(FMProperty property){
		FMProperties.add(property);		
	}
	
	public int getPropertyCount(){
		return FMProperties.size();
	}
	
	public List<String> getImportedPackages(){
		return importedPackages;
	}

	public Iterator<String> getImportedIterator(){
		return importedPackages.iterator();
	}
	
	public void addImportedPackage(String importedPackage){
		importedPackages.add(importedPackage);		
	}
	
	public int getImportedCount(){
		return FMProperties.size();
	}
	
	public String getVisibility() {
		return visibility;
	}

	public void setVisibility(String visibility) {
		this.visibility = visibility;
	}	

	
	
}
