package myplugin;

import com.nomagic.magicdraw.actions.MDAction;
import com.nomagic.magicdraw.core.Application;
import com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels.Model;
import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import myplugin.analyzer.AnalyzeException;
import myplugin.analyzer.ModelAnalyzer;
import myplugin.generator.EJBGenerator;
import myplugin.generator.fmmodel.FMModel;
import myplugin.generator.options.GeneratorOptions;
import myplugin.generator.options.ProjectOptions;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.io.*;

/**
 * Action that activate code generation
 */
class GenerateAction extends MDAction {


    public GenerateAction(String name) {
        super("", name, null, null);
    }

    public void actionPerformed(ActionEvent evt) {

        if (Application.getInstance().getProject() == null) return;
        Model root = Application.getInstance().getProject().getModel();
        if (root == null) return;

        FMModel fmModel = new FMModel();
        ModelAnalyzer analyzer = new ModelAnalyzer(root, "ejb", fmModel);

        try {
            analyzer.prepareModel();
            GeneratorOptions go = ProjectOptions.getProjectOptions().getGeneratorOptions().get("EJBGenerator");
            EJBGenerator generator = new EJBGenerator(go);
            generator.generate(fmModel);
            JOptionPane.showMessageDialog(null, "Code is successfully generated! Generated code is in folder: " + go.getOutputPath() +
                    "package: " + go.getFilePackage());
            exportToXml(fmModel);
        } catch (AnalyzeException e) {
            JOptionPane.showMessageDialog(null, e.getMessage());
        }
    }

    private void exportToXml(FMModel fmModel) {
        if (JOptionPane.showConfirmDialog(null, "Do you want to extract model metadata?") ==
                JOptionPane.OK_OPTION) {
            JFileChooser jfc = new JFileChooser();
            if (jfc.showSaveDialog(null) == JFileChooser.APPROVE_OPTION) {
                String fileName = jfc.getSelectedFile().getAbsolutePath();

                XStream xstream = new XStream(new DomDriver());
                BufferedWriter out;
                try {
                    out = new BufferedWriter(new OutputStreamWriter(
                            new FileOutputStream(fileName), "UTF8"));
                    xstream.toXML(fmModel.getClasses(), out);
                    xstream.toXML(fmModel.getEnumerations(), out);
                    JOptionPane.showMessageDialog(null, "Metadata successfully extracted!");

                } catch (UnsupportedEncodingException e) {
                    JOptionPane.showMessageDialog(null, e.getMessage());
                } catch (FileNotFoundException e) {
                    JOptionPane.showMessageDialog(null, e.getMessage());
                }
            }
        }
    }

}