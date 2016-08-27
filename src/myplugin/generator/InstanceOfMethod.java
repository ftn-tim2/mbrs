package myplugin.generator;

import freemarker.ext.util.WrapperTemplateModel;
import freemarker.template.TemplateMethodModelEx;
import freemarker.template.TemplateModelException;

import java.util.List;

/**
 * Created by Jozef on 8/27/2016.
 */
public class InstanceOfMethod implements TemplateMethodModelEx {

    @Override
    public Object exec(List list) throws TemplateModelException
    {
        if (list.size() != 2) {
            throw new TemplateModelException("Wrong arguments for method 'instanceOf'. Method has two required parameters: object and class");
        } else {
            Object object = ((WrapperTemplateModel) list.get(0)).getWrappedObject();
            Object p2 = ((WrapperTemplateModel) list.get(1)).getWrappedObject();
            if (!(p2 instanceof Class)) {
                throw new TemplateModelException("Wrong type of the second parameter. It should be Class. Found: " + p2.getClass());
            } else {
                Class c = (Class) p2;
                return c == object.getClass();
            }
        }
    }
}
