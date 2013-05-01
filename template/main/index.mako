<%
#display_column = lambda x: "%s %s" % (x.first_name, x.last_name)
%>
<%inherit file="../base/base.mako"/>

<%block name="title">Home</%block>

<script type="text/javascript">
$(document).ready(function() { 
    var options = { 
            type: 'POST',        // 'get' or 'post', override for form's 'method' attribute 
            success: function(){
                location.replace($('#upload_form').attr('action'));
            }  // post-submit callback 
        }; 
    // bind form using 'ajaxForm' 
    $('#upload_form').ajaxForm(options); 
}); 
</script>
<h1>${self.title()}</h1>
<br />
<a href="session/0">Create New Session</a>