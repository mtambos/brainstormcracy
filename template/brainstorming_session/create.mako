<%!
    _section = "brainstorming sessions"
%>
<%inherit file="../crud/base.mako" />
<%block name="header">
    ${parent.header()}
    <h3>Create<h3>
</%block>
<script type="text/javascript">
    var ideas_count = 4;
    function add_more_ideas(){
        $('<div class="row blue">'
            + '<div class="cell">Name:<br />Short Description:<br />Description:</div>'
            + '<div class="cell">'
                + '<input type="text" name="idea_names" id="idea_names_' + ideas_count + '" size="50"/>'
                + '<br />'
                + '<input type="text" name="idea_s_descriptions" id="idea_s_descriptions_' + ideas_count + '" size="50"/>'
                + '<br />'
                + '<textarea name="idea_descriptions" id="idea_descriptions_' + ideas_count + '" cols="43" rows="5"></textarea>'
            + '</div>'
        + '</div>').appendTo('#ideas_container');
        ideas_count++;
        setHtmlEditor();
    }
    $(document).ready(function(){
        setHtmlEditor();
    });
</script>
<form action='./' method='POST'>
    <div>
        Session Name: <input type="text" name="session_name" id="session_name" />
    </div>
    <div class="table">
        <div class="header">
            <div class="row">
                <div class="cell">
                    <h3>Ideas</h3>
                </div>
            </div>
        </div>
        <div id="ideas_container" class="ideas_container footer">
            <div class="row blue">
                <div class="cell">
                    Name:
                    <br />
                    Short Description:
                    <br />
                    Description:
                </div>
                <div class="cell">
                    <input type='text' name="idea_names" id="idea_names_0" size="50"/>
                    <br />
                    <input type='text' name="idea_s_descriptions" id="idea_s_descriptions_0" size="50"/>
                    <br />
                    <textarea type='text' name="idea_descriptions" id="idea_descriptions_0" cols="43" rows="5"></textarea>
                </div>
            </div>
            <div class="row blue">
                <div class="cell">
                    Name:
                    <br />
                    Short Description:
                    <br />
                    Description:
                </div>
                <div class="cell">
                    <input type='text' name="idea_names" id="idea_names_1" size="50"/>
                    <br />
                    <input type='text' name="idea_s_descriptions" id="idea_s_descriptions_1" size="50"/>
                    <br />
                    <textarea type='text' name="idea_descriptions" id="idea_descriptions_1" cols="43" rows="5"></textarea>
                </div>
            </div>
            <div class="row blue">
                <div class="cell">
                    Name:
                    <br />
                    Short Description:
                    <br />
                    Description:
                </div>
                <div class="cell">
                    <input type='text' name="idea_names" id="idea_names_2" size="50"/>
                    <br />
                    <input type='text' name="idea_s_descriptions" id="idea_s_descriptions_2" size="50"/>
                    <br />
                    <textarea type='text' name="idea_descriptions" id="idea_descriptions_2" cols="43" rows="5"></textarea>
                </div>
            </div>
            <div class="row blue">
                <div class="cell">
                    Name:
                    <br />
                    Short Description:
                    <br />
                    Description:
                </div>
                <div class="cell">
                    <input type='text' name="idea_names" id="idea_names_3" size="50"/>
                    <br />
                    <input type='text' name="idea_s_descriptions" id="idea_s_descriptions_3" size="50"/>
                    <br />
                    <textarea type='text' name="idea_descriptions" id="idea_descriptions_3" cols="43" rows="5"></textarea>
                </div>
            </div>
        </div>
    </div>
    <div>
        <a href="javascript:add_more_ideas();">Add more Ideas</a>
    </div>
    <input type='submit' value='Save' />
</form>
<div>
    <a href="/">Home</a>
</div>
