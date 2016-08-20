package myplugin.generator.fmmodel.strereotypes;

/**
 * Created by Jozef on 8/20/2016.
 */
public enum ComponentType {
	TEXT_FIELD(1, "textField"), 
	TEXT_AREA(2, "textArea"),
    INTEGER_FILED(9, "integerField"),
	//COMBOBOX(3, "combobox"),
	CHECKBOX(4, "checkbox"), 
	DATEPICKER(5, "datePicker"),
	RADIO_BUTTON(7, "radioButton"),
	FLOAT_FIELD(8, "floatField"),
	;

	private int id;
	private String name;
	
	private ComponentType(int id, String name) {
		this.id = id;
		this.name = name;
	}
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	
	public static ComponentType getComponentNumberById(int id){
		for (ComponentType component : ComponentType.values()) {
			if(component.getId() == id)
				return component;
		}
		throw new IllegalArgumentException("No day found with day number: " + id);
	}

	public static ComponentType getComponentNumberByName(String componentName){
		for (ComponentType component : ComponentType.values()) {
			if(component.getName().equalsIgnoreCase(componentName))
				return component;
		}
		throw new IllegalArgumentException("No day found with name: " + componentName);
	}
	
	
}
