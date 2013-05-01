<%!
    _section = "section"
%>

<%inherit file="../base/base.mako"/>
<%block name="title">${self.attr._section.capitalize()}</%block>
<%block name="header">
    ${parent.header()}
    <h2>${self.attr._section.capitalize()}</h2>
</%block>
${next.body(**context.kwargs)}