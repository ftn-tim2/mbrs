package myplugin.analyzer;

import com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.*;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package;
import com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype;
import myplugin.analyzer.parser.ObjectParser;
import myplugin.analyzer.strategies.*;
import myplugin.generator.fmmodel.FMClass;
import myplugin.generator.fmmodel.FMEnumeration;
import myplugin.generator.fmmodel.FMModel;
import myplugin.generator.fmmodel.FMProperty;
import myplugin.generator.fmmodel.strereotypes.*;

import java.util.Collection;
import java.util.Iterator;
import java.util.List;


/**
 * Model Analyzer takes necessary metadata from the MagicDraw model and puts it in
 * the intermediate data structure (@see myplugin.generator.fmmodel.FMModel) optimized
 * for code generation using freemarker. Model Analyzer now takes metadata only for ejb code
 * generation
 *
 * @ToDo: Enhance (or completely rewrite) myplugin.generator.fmmodel classes and
 * Model Analyzer methods in order to support GUI generation.
 */


public class ModelAnalyzer {
    //root model package
    private Package root;

    //java root package for generated code
    private String filePackage;

    public ModelAnalyzer(Package root, String filePackage) {
        super();
        this.root = root;
        this.filePackage = filePackage;
    }

    public Package getRoot() {
        return root;
    }

    public void prepareModel() throws AnalyzeException {
        FMModel.getInstance().getClasses().clear();
        FMModel.getInstance().getEnumerations().clear();
        processPackage(root, filePackage);
    }

    public void processPackage(Package pack, String packageOwner) throws AnalyzeException {
//		JOptionPane.showMessageDialog(null, "processPackage "+ pack.getName());
        if (pack.getName() == null)
            throw new AnalyzeException("Packages must have names!");

        String packageName = packageOwner;
        if (pack != root) {
//			JOptionPane.showMessageDialog(null, "NOT EQUAL");
            packageName += "." + pack.getName();
        }

        if (pack.hasOwnedElement()) {
//			JOptionPane.showMessageDialog(null, "HAS ELEMENT");
            for (Iterator<Element> it = pack.getOwnedElement().iterator(); it.hasNext(); ) {
                Element ownedElement = it.next();
//				JOptionPane.showMessageDialog(null, "found " + ownedElement.toString());
                if (ownedElement instanceof Class) {
                    Class cl = (Class) ownedElement;
//					JOptionPane.showMessageDialog(null, "class " + cl.toString());
                    System.out.println("Class detected: " + cl.getQualifiedName());
                    FMClass fmClass = getClassData(cl, packageName);
                    FMModel.getInstance().getClasses().add(fmClass);
                    continue;
                }

                if (ownedElement instanceof Enumeration) {
                    Enumeration en = (Enumeration) ownedElement;
//					JOptionPane.showMessageDialog(null, "enum " + en.toString());
                    System.out.println("Enumeration detected: " + en.getQualifiedName());
                    FMEnumeration fmEnumeration = getEnumerationData(en, packageName);
                    FMModel.getInstance().getEnumerations().add(fmEnumeration);
                    continue;
                }

                if (ownedElement instanceof Package) {
                    Package en = (Package) ownedElement;
//					JOptionPane.showMessageDialog(null, "Package " + en.toString());
                    System.out.println("Package detected: " + en.getQualifiedName());
                    //Temp hack
                    if (!en.getQualifiedName().contains("Profile")) {
                        processPackage(en, packageName);
                    }
                    continue;
                }

                if (ownedElement instanceof Comment) {
                    Comment comment = (Comment) ownedElement;
                    System.out.println("Comment detected: " + comment.getBody());
                    //Release
                    continue;
                }

                if (ownedElement instanceof Association) {
                    Association association = (Association) ownedElement;

                    Collection<Element> assocRoles = association.getRelatedElement();

                    if (assocRoles.size() == 1) {
                        System.out.println("Recursive association detected: " + ((Class) assocRoles.toArray()[0]).getQualifiedName());
                        continue;
                    }

                    if (assocRoles.size() == 2) {
                        System.out.println("Association detected: " + ((Class) assocRoles.toArray()[0]).getQualifiedName() + "||" + ((Class) assocRoles.toArray()[1]).getQualifiedName());
                        continue;
                    }

                    throw new AnalyzeException("N-ary association detected which is not supported in the current version of analyzer");

                    //Release
//					continue;
                }

                if (ownedElement instanceof Diagram) {
                    Diagram diagram = (Diagram) ownedElement;
                    System.out.println("Diagram detected: " + diagram.getQualifiedName());
                    //Release
                    continue;
                }

                if (ownedElement instanceof PackageImport)
                {
                    PackageImport packageImport = (PackageImport) ownedElement;
                    System.err.println("PackageImport type detected: " + packageImport.toString());
                    continue;
                }

                throw new AnalyzeException("Unidentified type detected: " + ownedElement.getClass());

            }
        }
    }

    public static FMClass getClassData(Class cl, String packageName) throws AnalyzeException {
        if (cl.getName() == null)
            throw new AnalyzeException("Classes must have names!");

        List<Stereotype> list = StereotypesHelper.getStereotypes(cl);
        if (list.isEmpty())
            throw new AnalyzeException("Classes must have at least one stereotype! Package Name :" + packageName + " Class : " + cl.getName());

        Stereotype standardStereotype = StereotypesHelper.getAppliedStereotypeByString(cl, "StandardPage");
        if (standardStereotype != null) {
            ObjectParser<StandardPage> parser = new ObjectParser<StandardPage>(new StandardPageStrategy());
            return parser.parse(cl, packageName);
        }

        Stereotype indexStereotype = StereotypesHelper.getAppliedStereotypeByString(cl, "IndexPage");
        if (indexStereotype != null) {
            ObjectParser<IndexPage> parser = new ObjectParser<IndexPage>(new IndexPageStrategy());
            return parser.parse(cl, packageName);
        }

        throw new AnalyzeException("Parser not available to that class: " + cl.getQualifiedName());
    }

    public static FMProperty getPropertyData(Property property, Class cclass) throws AnalyzeException {
        //	JOptionPane.showMessageDialog(null, "PropertyData!");
        Stereotype editableStereotype = StereotypesHelper.getAppliedStereotypeByString(property, "Editable");
        if (editableStereotype != null) {
            ObjectParser<Editable> parser = new ObjectParser<Editable>(new EditableStrategy());
            return parser.parse(property, cclass);
        }

        Stereotype readOnlyStereotype = StereotypesHelper.getAppliedStereotypeByString(property, "ReadOnly");
        if (readOnlyStereotype != null) {
            ObjectParser<ReadOnly> parser = new ObjectParser<ReadOnly>(new ReadOnlyStrategy());
            return parser.parse(property, cclass);
        }

        Stereotype nextStereotype = StereotypesHelper.getAppliedStereotypeByString(property, "Next");
        if (nextStereotype != null) {
            ObjectParser<Next> parser = new ObjectParser<Next>(new NextStrategy());
            return parser.parse(property, cclass);
        }

        Stereotype uiAssocEndStereotype = StereotypesHelper.getAppliedStereotypeByString(property, "UIAssocEnd");
        if (uiAssocEndStereotype != null) {
            ObjectParser<UIAssocEnd> parser = new ObjectParser<UIAssocEnd>(new UIAssocEndStrategy());
            return parser.parse(property, cclass);
        }

        ObjectParser<FMProperty> parser = new ObjectParser<FMProperty>(new FMPropertyStrategy());
        return parser.parse(property, cclass);

        //throw new IllegalArgumentException("Parser not available to that property");
    }

    private static FMEnumeration getEnumerationData(Enumeration enumeration, String packageName) throws AnalyzeException {
        ObjectParser<FMEnumeration> parser = new ObjectParser<FMEnumeration>(new EnumerationStrategy());
        return parser.parse(enumeration, packageName);
    }


}
