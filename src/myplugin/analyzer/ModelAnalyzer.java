package myplugin.analyzer;

import com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.*;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class;
import com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package;
import com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype;
import myplugin.GlobalLogger;
import myplugin.analyzer.parser.ObjectParser;
import myplugin.analyzer.strategies.*;
import myplugin.generator.fmmodel.FMClass;
import myplugin.generator.fmmodel.FMEnumeration;
import myplugin.generator.fmmodel.FMModel;
import myplugin.generator.fmmodel.FMProperty;
import myplugin.generator.fmmodel.strereotypes.*;

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
    private Package _root;

    //java root package for generated code
    private String _filePackage;

    private FMModel _model;

    public ModelAnalyzer(Package root, String filePackage, FMModel model) {
        super();
        _root = root;
        _filePackage = filePackage;
        _model = model;
    }

    public Package getRoot() {
        return _root;
    }

    public void prepareModel() throws AnalyzeException {
        processPackage(_root, _filePackage);
        postProcessPackage();
    }

    private void processPackage(Package pack, String packageOwner) throws AnalyzeException {
        if (pack.getName() == null)
            throw new AnalyzeException("Packages must have names!");

        String packageName = packageOwner;
        if (pack != _root) {
            packageName += "." + pack.getName();
        }

        if (pack.hasOwnedElement()) {
            for (Iterator<Element> it = pack.getOwnedElement().iterator(); it.hasNext(); ) {
                Element ownedElement = it.next();

                //Package
                if (ownedElement instanceof Package) {
                    Package en = (Package) ownedElement;
                    GlobalLogger.Log("Package detected: " + en.getQualifiedName());
                    Stereotype stereoType = StereotypesHelper.getAppliedStereotypeByString(en, ToGenerate.NAME);
                    if (stereoType != null) {
                        GlobalLogger.Log("Package detected: " + en.getQualifiedName() + " -- " + ToGenerate.NAME);
                        processPackage(en, packageName);
                    }
                    continue;
                }

                //Class
                if (ownedElement instanceof Class) {
                    Class cl = (Class) ownedElement;
                    GlobalLogger.Log("Class detected: " + cl.getQualifiedName());
                    _model.getClasses().add(getClassData(cl, packageName));
                    continue;
                }

                //Enumeration
                if (ownedElement instanceof Enumeration) {
                    Enumeration en = (Enumeration) ownedElement;
                    GlobalLogger.Log("Enumeration detected: " + en.getQualifiedName());
                    _model.getEnumerations().add(getEnumerationData(en, packageName));
                    continue;
                }

                //Association
                //disabled
                /*if (ownedElement instanceof Association) {
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

                }*/

                //Continue
                if (ownedElement instanceof Comment ||
                        ownedElement instanceof Diagram ||
                        ownedElement instanceof PackageImport ||
                        ownedElement instanceof Association ||
                        ownedElement instanceof InstanceSpecification) {

                    //Release
                    continue;
                }

                throw new AnalyzeException("Unidentified type detected: " + ownedElement.getClass());
            }
        }
    }

    private void postProcessPackage() throws AnalyzeException {
        // search for the proper enumeration for the DropDown UIProperty
        for (FMClass fmClass : _model.getClasses()) {
            for (FMProperty fmProperty : fmClass.getProperties()) {
                if (fmProperty.getClass() == UIProperty.class) {
                    UIProperty tempProp = (UIProperty) fmProperty;
                    if (tempProp.isDropDownFlag()) {
                        for (FMEnumeration fmEnumeration : _model.getEnumerations()) {
                            if (fmEnumeration.getName().equals(tempProp.getType())) {
                                tempProp.setEnumerations(fmEnumeration);
                            }
                        }
                        if (tempProp.getEnumeration() == null) {
                            throw new AnalyzeException("Unidentified enumeration detected: " + tempProp.getName());
                        }
                    }

                }
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
            ObjectParser<StandardPage> parser = new ObjectParser<>(new StandardPageStrategy());
            return parser.parse(cl, packageName);
        }

        Stereotype indexStereotype = StereotypesHelper.getAppliedStereotypeByString(cl, "IndexPage");
        if (indexStereotype != null) {
            ObjectParser<IndexPage> parser = new ObjectParser<>(new IndexPageStrategy());
            return parser.parse(cl, packageName);
        }

        throw new AnalyzeException("Parser not available to that class: " + cl.getQualifiedName());
    }

    public static FMProperty getPropertyData(Property property, Class _class) throws AnalyzeException {

        Stereotype readOnlyStereotype = StereotypesHelper.getAppliedStereotypeByString(property, UIProperty.NAME);
        if (readOnlyStereotype != null) {
            ObjectParser<UIProperty> parser = new ObjectParser<>(new UIPropertyStrategy());
            return parser.parse(property, _class);
        }

        Stereotype nextStereotype = StereotypesHelper.getAppliedStereotypeByString(property, "Next");
        if (nextStereotype != null) {
            ObjectParser<Next> parser = new ObjectParser<>(new NextStrategy());
            return parser.parse(property, _class);
        }

        Stereotype foreignKeyStereoType = StereotypesHelper.getAppliedStereotypeByString(property, "ForeignKey");
        if (foreignKeyStereoType != null) {
            ObjectParser<ForeignKey> parser = new ObjectParser<>(new ForeignKeyStrategy());
            return parser.parse(property, _class);
        }

        ObjectParser<FMProperty> parser = new ObjectParser<>(new FMPropertyStrategy());
        return parser.parse(property, _class);

        //throw new IllegalArgumentException("Parser not available to that property");
    }

    private static FMEnumeration getEnumerationData(Enumeration enumeration, String packageName) throws AnalyzeException {
        ObjectParser<FMEnumeration> parser = new ObjectParser<>(new EnumerationStrategy());
        return parser.parse(enumeration, packageName);
    }


}
