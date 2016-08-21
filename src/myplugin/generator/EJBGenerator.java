package myplugin.generator;

import freemarker.template.TemplateException;
import myplugin.generator.fmmodel.FMClass;
import myplugin.generator.fmmodel.FMModel;
import myplugin.generator.options.GeneratorOptions;

import javax.swing.*;
import java.io.IOException;
import java.io.Writer;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/** EJB generator that now generates incomplete ejb classes based on MagicDraw 
 * class model 
 * @ToDo: enhance resources/templates/ejbclass.ftl template and intermediate data structure
 *  (@see myplugin.generator.fmmodel) in order to generate complete ejb classes 
 */

public class EJBGenerator extends BasicGenerator {	
	
	public EJBGenerator(GeneratorOptions generatorOptions) {			
		super(generatorOptions);			
	}

	public void generate(FMModel model) {
		
		try {
			super.generate();
		} catch (IOException e) {		
			JOptionPane.showMessageDialog(null, e.getMessage());
		}

		List<FMClass> classes = model.getClasses();
		for (int i = 0; i < classes.size(); i++) {
			FMClass cl = classes.get(i);			
				Writer out;
				Map<String, Object> context = new HashMap<>();
				try {
					out = getWriter(cl.getName(), cl.getTypePackage());
					if (out != null) {
						context.clear();
						context.put("class", cl);
						context.put("properties", cl.getProperties());					
						context.put("importedPackages", cl.getImportedPackages());					
						getTemplate().process(context, out);
						out.flush();
					}
				} catch (TemplateException e) {	
					JOptionPane.showMessageDialog(null, e.getMessage());
				}	
				catch (IOException e) {
					JOptionPane.showMessageDialog(null, e.getMessage());
				}	
			}			
		}
	}


