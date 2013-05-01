from model.brainstorming_session import BrainstormingSession as Model
from model.idea import Idea
from model.vote import Vote
from model.user import User
from model.user_by_session import UserBySession
from helpers.templates import serve_template

from HTMLParser import HTMLParser
from cherrypy import tools, HTTPRedirect
from datetime import datetime

import logging


class BrainstormingSession(object):
    exposed = True
    request_timestamp = datetime.utcnow()

    def __init__(self):
        self.model_class = Model
        self.template_path = "%s/" % self.model_class.__name__

    def default(self, *args, **kwargs):
        path = "/" + "/".join(args)
        method = cherrypy.request.method
        return "Request for path: %s with method: %s and args: %s!" % (path, method, kwargs)

    def GET(self, key=None):
        if key is None:
            return serve_template(self.template_path + "index.mako", collection=[])
        else:
            props = sorted(self.model_class.properties().items(), key=lambda (k, v): v.creation_counter)
            if key == "0":
                return serve_template(self.template_path + "create.mako",
                                      model=self.model_class,
                                      props=props)
            else:
                session = self.model_class.get(key)
                users = set(u.user for u in session.users)
                users = sorted(users, key=lambda u: u.doe)
                ideas = set(idea for idea in session.ideas)
                ideas = sorted(ideas, key=self._order_ideas, reverse=True)
                return serve_template(self.template_path + "edit.mako",
                                      model=session,
                                      ideas=ideas,
                                      users=users,
                                      props=props)

    def POST(self, key=None, **kwargs):
        session = self._process_session(key, **kwargs)
        (new_user, modified_voters) = self._process_users(session, **kwargs)
        self._process_ideas(session, **kwargs)
        self._process_votes(session, new_user, modified_voters, **kwargs)

        raise HTTPRedirect(str(session.key()))

    def _process_session(self, key, **kwargs):
        if not key:
            session = Model(name=kwargs["session_name"])
            session.put()
        else:
            session = Model.get(key)
        return session

    def _process_ideas(self, session, **kwargs):
        idea_keys = kwargs["idea_keys"] if "idea_keys" in kwargs else []
        idea_names = kwargs["idea_names"] if "idea_names" in kwargs else []
        idea_s_descriptions = kwargs["idea_s_descriptions"] if "idea_s_descriptions" in kwargs else []
        idea_descriptions = kwargs["idea_descriptions"] if "idea_descriptions" in kwargs else []

        idea_keys = [idea_keys] if not isinstance(idea_keys, list) else idea_keys
        idea_names = [idea_names] if not isinstance(idea_names, list) else idea_names
        idea_s_descriptions = [idea_s_descriptions] if not isinstance(idea_s_descriptions, list) else idea_s_descriptions
        idea_descriptions = [idea_descriptions] if not isinstance(idea_descriptions, list) else idea_descriptions

        for i in range(len(idea_names)):
            if idea_names[i] != "":
                if i < len(idea_keys) and idea_keys[i]:
                    idea = Idea.get(idea_keys[i])
                    idea.name = idea_names[i]
                    idea.short_description = idea_s_descriptions[i]
                    idea.description = idea_descriptions[i]
                else:
                    idea = Idea(name=idea_names[i],
                                    short_description=idea_s_descriptions[i],
                                    description=idea_descriptions[i],
                                    session=session)
                idea.put()

    def _process_users(self, session, **kwargs):
        modified_voters = set()
        new_user = None
        if "new_voter" in kwargs and kwargs["new_voter"]:
            new_user = User(name=kwargs["new_voter"])
            new_user.put()

            user_by_session = UserBySession(user=new_user, session=session)
            user_by_session.put()

        voter_keys = []
        if "voter_key" in kwargs:
            voter_keys = [kwargs["voter_key"]]
            if isinstance(kwargs["voter_key"], list):
                voter_keys = voter_keys[0]

            if "voter_name" in kwargs and not isinstance(kwargs["voter_name"], list):
                kwargs["voter_name"] = [kwargs["voter_name"]]

            for i in range(len(voter_keys)):
                voter = User.get(voter_keys[i])
                voter.name = kwargs["voter_name"][i]
                voter.put()
                modified_voters.add(voter)

        return (new_user, modified_voters)

    def _process_votes(self, session, new_user, modified_voters, **kwargs):
        for idea in session.ideas:
            for user in modified_voters:
                vote_id = ("vote_" + str(idea.key()) + "_" + str(user.key()))
                vote = idea.votes.filter("user =", user).get()
                if not vote:
                    vote = Vote(user=user, idea=idea)
                if vote_id in kwargs:
                    vote.yes_no = kwargs[vote_id]
                vote.put()

            if new_user:
                new_vote = Vote(user=new_user, idea=idea, yes_no="No")
                if ("new_vote_" + str(idea.key())) in kwargs:
                    new_vote.yes_no = kwargs["new_vote_" + str(idea.key())]
                new_vote.put()

    def _order_ideas(self, idea):
        yes_votes = idea.votes.filter("yes_no =", "Yes").count()
        no_votes = idea.votes.filter("yes_no =", "No").count()
        nil_votes = idea.votes.filter("yes_no =", None).count()

        return (yes_votes - no_votes - nil_votes, datetime.utcnow() - idea.doe)

