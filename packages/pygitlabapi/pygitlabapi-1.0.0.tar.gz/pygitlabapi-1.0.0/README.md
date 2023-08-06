# pygitlabapi

pygitlabapi contains some functions to facilitate the usage of gitlab apis inside python modules or in command line.

[The source for this project is available here][src].

---

Example of importing gitlabapi inside a python module :

    import os
    from pygitlabapi import gitlabApi

    iurl = "https://gitlab.com/api/v4"
    ijson = "project.json"
    imethod="POST"
    iapi = "/projects"
    iuser= os.environ.get("GITLAB_USER")
    itoken = os.environ.get("GITLAB_TOKEN")
    message= gitlabApi.rungitlabApi(api=iapi, method=imethod, url=iurl, user=iuser, token=itoken, json=ijson )
    print(message)

---

[packaging guide]: https://packaging.python.org
[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/
[src]: https://github.com/stormalf/pygitlabapi
[rst]: http://docutils.sourceforge.net/rst.html
[md]: https://tools.ietf.org/html/rfc7764#section-3.5 "CommonMark variant"
[md use]: https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
