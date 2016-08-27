"TODO_name"
css="http://bootswatch.com/lumen/bootstrap.min.css"
<#list model.classes as class>
"${class.name}" {
<#list class.properties as property>
  <#if instanceOf(property,Next)>${property.type} "${property.name}"<#rt>
  <#elseif instanceOf(property,FMProperty)>${property.type} "${property.name}"<#rt>
  <#elseif instanceOf(property,UIProperty)>${property.component} "${property.name}"</#if>
</#list>
}

</#list>
