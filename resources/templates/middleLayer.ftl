"TODO_name"
css="http://bootswatch.com/lumen/bootstrap.min.css"
<#list model.classes as class>
"${class.name}" {
<#list class.properties as property>
  <#if instanceOf(property,Next)>foreignKey "${property.name}" <#rt>
    (<#list property.propertiesKeyValue as keyValue> <#t>
        ${keyValue}<#sep>, </#sep><#t>
    </#list> )<#t>
  <#elseif instanceOf(property,UIProperty)>${property.component} "${property.name}" <#rt>
    (<#list property.propertiesKeyValue as keyValue> <#t>
        ${keyValue}<#sep>, </#sep><#t>
    </#list> ) <#t>
  </#if>

</#list>
}
</#list>
<#list model.classes as class> <#t>
  <#list class.methods as method> <#t>
    "${method.name}"(<#list method.parameters as p><#if p!="">"${p}"</#if><#if p?is_last><#else>,</#if></#list>) <#t>
  </#list> <#t>
</#list> <#t>


