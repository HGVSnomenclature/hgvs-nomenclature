import logging

import git
import pytz

import mkdocs.plugins

_logger = logging.getLogger()

@mkdocs.plugins.event_priority(-100)
def on_env(env, config, files):
    r = git.Repo(".")
    tag = r.git.describe(tags=True)
    hc = r.head.commit
    commit_datetime_utc = r.head.commit.committed_datetime.astimezone(pytz.timezone("UTC"))
    env.globals["git"] = {
        # intended to be consistent with mkdocs-macros-plugin git info:
        "author": hc.author.author,
        "author_email": hc.author.email,
        "commit": hc.hexsha,
        "committer": hc.committer.name,
        "committer_email": hc.committer.email,
        "date": hc.committed_date,
        "message": hc.message,
        "short_commit": hc.hexsha[:7],
        "tag": tag,

        # bonus:
        "datetime_utc": commit_datetime_utc,
        }
    _logger.info(f"Entering on_env hook; added {tag}")
    return env

# @mkdocs.plugins.event_priority(-100)
# def on_page_context(context, *, page, config, nav):
#     context["flubber"] = {"bar": "baz"}


# git info from macros_info():

# Variable	Type	Content
# status	bool	True
# author	str	'Reece Hart'
# author_email	str	'reecehart@gmail.com'
# commit	str	'e96724beebe7070710b0b946e98d4e04483c20c9'
# committer	str	'Reece Hart'
# committer_email	str	'reecehart@gmail.com'
# date	datetime	datetime.datetime(2023, 11, 27, 15, 44, 42, tzinfo=tzoffset(None, -28800))
# date_ISO	str	'Mon Nov 27 15:44:42 2023 -0800'
# message	str	'update versioning text'
# raw	str	'commit e96724beebe7070710b0b946e98d4e04483c20c9\nAuthor: Reece Hart \nDate: Mon Nov 27 15:44:42 2023 -0800\n\n update versioning text'
# root_dir	str	'/home/reece/projects/HGVSnomenclature/hgvs-nomenclature'
# short_commit	str	'e96724b'
# short_tag	str	'24.1.0rc1'
# tag	str	'24.1.0rc1-68-ge96724b'
