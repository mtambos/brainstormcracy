<%!
    from google.appengine.ext.db import DateTimeProperty, ReferenceProperty, ListProperty, StringListProperty
    from helpers.config import datetime_format
    import inspect
%>
<form action='./' method='POST'>
    <input type='hidden' name="key" value='${session.key() | h}' />
    <div class="list">
        <h2>session.name</h2>
        <table>
            <thead>
                <tr>
                    <td>
                        Ideas
                    </td>
                    % for item in voters:
                    <td>
                        ${item.name | h}
                    </td>
                    % endfor
                    <td>
                        <input type="text" name="new_voter" id="new_voter" />
                    </td>
                </tr>
            </thead>
            <tbody>
            % for item in session.ideas:
                <tr>
                    <td>
                        <div>
                            ${item.name | h}
                            <br />
                            ${item.short_description | h}
                        </div>
                        <div>
                            ${item.description | h}
                        </div>
                    </td>
                    % for vote in item.votes:
                    <td>
                        ${vote.yes_no}
                    </td>
                    % endfor
                    <td>
                        <input type="radio" name="vote_yes_no" id="vote_yes_no" value="Yes"/>
                        | <input type="radio" name="vote_yes_no" id="vote_yes_no"  value="No"/>
                    </td>
                </tr>
            % endfor
            </tbody>
        </table>
    </div>
    <input type='submit' value='Save' />
</form>
<a href="/">Home</a><br />
