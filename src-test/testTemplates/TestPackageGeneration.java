package testTemplates;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import myplugin.generator.EJBGenerator;
import myplugin.generator.fmmodel.FMClass;
import myplugin.generator.fmmodel.FMModel;
import myplugin.generator.fmmodel.FMProperty;
import myplugin.generator.options.GeneratorOptions;
import myplugin.generator.options.ProjectOptions;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.List;

/**
 * TestPackageGeneration: Class for package generation testing
 *
 * @ToDo: Create another test class that loads metadata saved by MagicDraw plugin
 * ( @see myplugin.GenerateAction#exportToXml() ) and activate code generation.
 * This is the way to perform code generation testing without
 * need to restart MagicDraw
 */

public class TestPackageGeneration {

    private FMModel fmModel = new FMModel();

    public TestPackageGeneration() {

    }

    private void initModel() {


        List<FMClass> classes = fmModel.getClasses();

        classes.clear();

        FMClass cl = new FMClass("Preduzece", "ejb.orgsema", "public");
        cl.addProperty(new FMProperty("sifraPreduzeca", "String", "private", 1, 1));
        cl.addProperty(new FMProperty("nazivPreduzeca", "String", "private", 1, 1));

        classes.add(cl);

        cl = new FMClass("Materijal", "ejb.magacin", "public");
        cl.addProperty(new FMProperty("sifraMaterijala", "String", "private", 1, 1));
        cl.addProperty(new FMProperty("nazivMaterijala", "String", "private", 1, 1));
        cl.addProperty(new FMProperty("slozen", "Boolean", "private", 1, 1));

        classes.add(cl);

        cl = new FMClass("Odeljenje", "ejb.orgsema", "public");
        cl.addProperty(new FMProperty("sifra", "String", "private", 1, 1));
        cl.addProperty(new FMProperty("naziv", "String", "private", 1, 1));

        classes.add(cl);

        cl = new FMClass("Osoba", "ejb", "public");
        cl.addProperty(new FMProperty("prezime", "String", "private", 1, 1));
        cl.addProperty(new FMProperty("ime", "String", "private", 1, 1));
        cl.addProperty(new FMProperty("datumRodjenja", "Date", "private", 0, 1));
        cl.addProperty(new FMProperty("clanoviPorodice", "Osoba", "private", 0, -1));
        cl.addProperty(new FMProperty("vestina", "String", "private", 1, 3));

        classes.add(cl);

        cl = new FMClass("Kartica", "ejb.magacin.kartica", "public");
        cl.addProperty(new FMProperty("sifraKartice", "String", "private", 1, 1));
        cl.addProperty(new FMProperty("nazivKartice", "String", "private", 1, 1));

        classes.add(cl);
    }

    public FMModel importFromXml(String absolutePath) {

        FileReader fileReader = null;  // load our xml file
        try {
            fileReader = new FileReader(absolutePath);

            XStream xstream = new XStream(new DomDriver());     // init XStream
            // define root alias so XStream knows which element and which class are equivalent
            xstream.alias("myplugin.generator.fmmodel.FMModel", FMModel.class);
            FMModel loadedModel = (FMModel) xstream.fromXML(fileReader);
            return loadedModel;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void testGenerator() {
        //initModel();
        fmModel = importFromXml("C:\\Users\\Jozef\\Documents\\GitHub\\mbrs\\src-test\\MagicDrawModelExport.xml");
        GeneratorOptions go = ProjectOptions.getProjectOptions().getGeneratorOptions().get("EJBGenerator");
        EJBGenerator g = new EJBGenerator(go);
        g.generate(fmModel);
    }

    public static void main(String[] args) {
        TestPackageGeneration tg = new TestPackageGeneration();
        /** @Todo: load project options from xml file */

        //for test purpose only:  "./resources/templates/"
        GeneratorOptions ejbOptions = new GeneratorOptions("c:/temp", "middleLayer", "./resources/templates/", "{0}.txt", true, "JDS");
        ProjectOptions.getProjectOptions().getGeneratorOptions().put("EJBGenerator", ejbOptions);

        tg.testGenerator();
    }


}
