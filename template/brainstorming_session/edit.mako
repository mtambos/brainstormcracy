<%!
    from config import template_config
    _section = "brainstorming sessions"
%>
<%inherit file="../crud/base.mako" />
<%block name="header">
    ${parent.header()}
    <h3>Vote<h3>
</%block>
<script type="text/javascript">
    var ideas_count = ${len(ideas)};
    function add_more_ideas(){
        $('<div class="row blue">'
            + '<div class="cell">Name:<br />Short Description:<br />Description:</div>'
            + '<div class="cell">'
                + '<input type="hidden" name="idea_keys" id="idea_keys_' + ideas_count + '" value=""/>'
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
    
    function edit_vote(id){
        var voter_div = $(".voter_"+id);
        var voter_key = $(".voter_"+id).attr("id");
        voter_div.children("a").remove();
        voter_div.children("p").remove();

        voter_div.children("input#voter_name_" + id)
                .detach()
                .attr('type', 'text')
                .appendTo(voter_div);

        var vote_divs = $(".vote_"+id);
        for(i=0; i < vote_divs.length; i++){
            var vote_div = $(vote_divs[i]);
            var idea_key = vote_div.parent().attr("id");
            var vote_value = vote_div.children("img").attr("alt").trim();
            var new_div = '<input type="checkbox" ';
            new_div += ' name="vote_chkbx"';
            new_div += ' value="' + idea_key + '_' + voter_key + '" ';
            new_div += ((vote_value=="Yes")?'checked="true"':'') + ' />';
            new_div += '<input type="hidden" name="vote_' + idea_key + '_' + voter_key + '"';
            new_div += 'id="vote_' + idea_key + '_' + voter_key + '"';
            new_div += ' value="' + ((vote_value=="Yes")?'Yes':'No') + '" />';
            vote_div.html(new_div);
            $('#edit_form :checkbox').click(vote);
        }
    }

    function vote() {
        var $this = $(this);
        var chkbx = null;
        if ($this.attr("name").indexOf("new_vote_") >= 0){
            chkbx = $('#new_vote_' + $this.val());
        }else{
            chkbx = $('#vote_' + $this.val());
        }
        if ($this.is(':checked')) {
            chkbx.val("Yes");
        } else {
            chkbx.val("No");
        }
    }

    $(document).ready(function(){
        $('a#copy-link').zclip({
            path:'/static/script/ZeroClipboard.swf',
            copy:'${template_config.domain}' + '/session/' + '${str(model.key()) | u}'
        });

        $('#edit_form :checkbox').click(vote);
        
        setHtmlEditor();
    });
</script>
<form action='./' method='POST' id="edit_form">
    <div>
        <input type="hidden" name="key" id="key" value="${model.key() | u}"/>
        Session Name: <label name="session_name" id="session_name">${model.name | h}</label>
        <br />
        You can copy the session's link by clicking <a id="copy-link" href="#">here</a>.
    </div>
    <div class="table">
        <div class="header">
            <div class="row">
                <div class="cell">
                    <h3>Ideas</h3>
                </div>
                <div class="cell">&nbsp;</div>
                <div class="cell">
                    <h3>Votes</h3>
                </div>
            </div>
            <div class="row">
                <div class="cell blue">&nbsp;</div>
                <div class="cell blue">&nbsp;</div>
                <%
                    i = 0
                %>
                %for user in users:
                    <div class="cell yellow voter_${i}" id="${user.key() | h}">
                        <input type="hidden" name="voter_key" id="voter_key_${i}" value="${user.key() | h}">
                        <input type="hidden" name="voter_name" id="voter_name_${i}" value="${user.name | h}">
                        <p>${user.name | h}</p>
                        <a href="javascript:edit_vote(${i});">edit</a>
                    </div>
                    <% i += 1 %>
                % endfor
                <div class="cell yellow">
                    <input type="text" name="new_voter" id="new_voter" />
                </div>
            </div>
        </div>
        <div id="ideas_container" class="ideas_container footer">
            % for idea in ideas:
                <div class="row blue" id="${idea.key() | h}">
                    <div class="cell">
                        Name:
                        <br />
                        Short Description:
                        <br />
                        Description:
                    </div>
                    <div class="cell">
                        <input type='hidden' name="idea_keys" id="idea_keys_${loop.index}" value="${idea.key() | h}"/>
                        <input type='text' name="idea_names" id="idea_names_${loop.index}" value="${idea.name | h}" size="50"/>
                        <br />
                        <input type='text' name="idea_s_descriptions" id="idea_s_descriptions_${loop.index}" value="${idea.short_description | h}" size="50"/>
                        <br />
                        <textarea type='text' name="idea_descriptions" id="idea_descriptions_${loop.index}" cols="43" rows="5">${idea.description | h}</textarea>
                    </div>
                    <%
                        i = 0
                    %>
                    %for user in users:
                        <%
                            vote = user.votes.filter('idea =', idea).get()
                        %>
                        <div class="cell ${vote.yes_no if vote and vote.yes_no else "NoVote"} vote_${i} all-centered">
                        % if vote:
                            % if vote.yes_no == "Yes":
                                <img title="Yes" alt="Yes" src="/static/images/plus.png" />
                            % elif vote.yes_no == "No":
                                <img title="No" alt="No" src="/static/images/minus.png" />
                            % else:
                                <img title="Not voted" alt="Not voted" src="/static/images/no-vote.png" />
                            % endif
                        % else:
                            <img title="Not voted" alt="Not voted" src="/static/images/no-vote.png" />
                        % endif
                        </div>
                        <% i += 1 %>
                    % endfor
                    <div class="cell yellow all-centered">
                        <input type="checkbox" name="new_vote_chkbx" value="${idea.key() | h}"/>
                        <input type="hidden" name="new_vote_${idea.key() | h}" id="new_vote_${idea.key() | h}" value="No"/>
                    </div>
                </div>
            % endfor
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
