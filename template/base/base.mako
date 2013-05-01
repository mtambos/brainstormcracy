<html>
<head>
	<link rel="stylesheet" type="text/css" href="/static/style/main.min.css" />
	<link rel="stylesheet" type="text/css" href="/static/style/jHtmlArea.min.css" />
	<link rel="shortcut icon" href="/static/images/favicon.ico" />
	
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script> 
	<script src="http://malsup.github.com/jquery.form.js"></script>
	<script type="text/javascript" src="/static/script/jquery.zclip.min.js"></script>
	<script type="text/javascript" src="/static/script/jHtmlArea-0.7.5.min.js"></script>
	<script type="text/javascript">
    	function setHtmlEditor(){
        	$('textarea').htmlarea({
        	toolbar: [
                ["bold", "italic", "underline",
                 "|", "increasefontsize", "decreasefontsize",
                 "|", "orderedList", "unorderedList",
                 "|", "indent", "outdent",
                 "|", "link", "unlink",
                 ],
            	]
        	});
    	}
	</script>
	
	<title>Brainstormcracy: <%block name="title"/></title>
</head>
<body>
    <div class="header">
        Brainstormcracy <%block name="header"/>
    </div>

    ${next.body(**context.kwargs)}
    
    <div class="footer">
        <%block name="footer" />
    </div>
</body>
</html>
