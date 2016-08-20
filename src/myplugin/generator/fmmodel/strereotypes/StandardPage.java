package myplugin.generator.fmmodel.strereotypes;

import myplugin.generator.fmmodel.FMClass;

/**
 * Created by Jozef on 8/20/2016.
 */
public class StandardPage extends UIClass {
	
	private boolean create;
	private boolean delete;
	private boolean update;
	private boolean read;
	
	public StandardPage(String name, String classPackage, String visibility) {
		super(name, classPackage, visibility);
		this.create = true;
		this.delete = true;
		this.update = true;
		this.read = false;
	}
	
	public StandardPage(FMClass fmClass, String label, boolean create, boolean delete, boolean update, boolean read) {
		super(fmClass.getName(), fmClass.getTypePackage(), fmClass.getVisibility());
		this.create = create;
		this.delete = delete;
		this.update = update;
		this.read = read;
	}
	
	public StandardPage(FMClass fmClass){
		super(fmClass.getName(), fmClass.getTypePackage(), fmClass.getVisibility());
		this.create = true;
		this.delete = true;
		this.update = true;
		this.read = false;
	}

	public boolean isCreate() {
		return create;
	}

	public void setCreate(boolean create) {
		this.create = create;
	}

	public boolean isDelete() {
		return delete;
	}

	public void setDelete(boolean delete) {
		this.delete = delete;
	}

	public boolean isUpdate() {
		return update;
	}

	public void setUpdate(boolean update) {
		this.update = update;
	}

	public boolean isRead() {
		return read;
	}

	public void setRead(boolean read) {
		this.read = read;
	}
	
	@Override
	public String toString() {
		return "StandardPage : "  + super.getLabel() ;
	}
	
}
