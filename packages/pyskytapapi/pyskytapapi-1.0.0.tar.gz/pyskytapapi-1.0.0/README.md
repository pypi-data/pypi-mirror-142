# pyskytapapi

pyskytapapi contains some functions to facilitate the usage of skytap apis inside python modules or in command line.

[The source for this project is available here][src].

---

Example of importing skytapapi inside a python module :

    import os
    from pyskytapapi import skytapApi

    iurl = "https://cloud.skytap.com"
    ijson = "configurations.json"
    imethod="POST"
    iapi = "/configurations.json"
    iuser= os.environ.get("SKYTAP_USER")
    itoken = os.environ.get("SKYTAP_TOKEN")
    message= skytapApi.runskytapApi(api=iapi, method=imethod, url=iurl, user=iuser, token=itoken, json=ijson )
    print(message)

---

[packaging guide]: https://packaging.python.org
[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/
[src]: https://github.com/stormalf/pyskytapapi
[rst]: http://docutils.sourceforge.net/rst.html
[md]: https://tools.ietf.org/html/rfc7764#section-3.5 "CommonMark variant"
[md use]: https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
