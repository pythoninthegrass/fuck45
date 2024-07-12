# fuck45

**Table of Contents**
* [fuck45](#fuck45)
  * [Setup](#setup)
    * [Minimum requirements](#minimum-requirements)
    * [Recommended requirements](#recommended-requirements)
  * [Development](#development)
    * [Devbox](#devbox)
  * [TODO](#todo)

## Setup

### Minimum requirements
* [Python 3.11+](https://www.python.org/downloads/)

### Recommended requirements

* [devbox](https://www.jetpack.io/devbox/docs/quickstart/)
* [task](https://taskfile.dev/#/installation)

## Development

### Devbox

```bash
# enter dev environment
devbox shell

# run server (dev)
fastapi run backend/main.py --port 8000

# run server (prod)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend.main:app --bind 0.0.0.0:8000

# exit dev environment
exit

# run tests
devbox run test
```

## TODO
* [Open Issues](https://github.com/pythoninthegrass/fuck45/issues)
* `docker-compose.yml` volume appears to be clobbering `frontend/public/build`
  * may not be an issue, just have to test without volume
* Server
  * 405 errors
  * gunicorn/uvicorn
* UI
  * fix css
    * move h1 to center and slightly below navbar
    * center submission form
    * github footer should be invertocat and at bottom of viewport
  * remove placeholders
    * "Article Viewer"
* Pages
  * create about page
* Auth
  * Either implement rate limiting/bans or OAuth
* Testing
  * create content for articles, submissions, and users
  * unit test all endpoints
* Update docs
