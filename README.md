# E-mail signature generator

## Pre-requirements

Docker or Docker toolbox (https://docs.docker.com/toolbox/)

## Make targets

```
deploy-pipeline      -  deploys the CI/CD pipeline
delete-pipeline      -  deletes the CI/CD pipeline
deploy-app           -  deploys the application
delete-app           -  deletes the application
update-image         -  updates the image reference in the deployment
build                -  builds a new version of your container image
snapshot             -  builds a new version of your container image, and pushes it to the registry
showver              -  shows the current release tag based on the workspace
showimage            -  shows the container image name based on the workspace
tag-patch-release    -  increments the patch release level and create the tag without build
tag-minor-release    -  increments the minor release level and create the tag without build
tag-major-release    -  increments the major release level and create the tag without build
patch-release        -  increments the patch release level, build and push to registry
minor-release        -  increments the minor release level, build and push to registry
major-release        -  increments the major release level, build and push to registry
check-status         -  checks whether there are outstanding changes
check-release        -  checks whether the workspace matches the tagged release in git
help                 -  show this help.

```


## Run from CLI

```shell
docker build -txebia-signature .
docker run -it --rm --entrypoint xebia-signature-cli xebia-signature
```

## Run as service locally

```shell
docker build -txebia-signature .
docker run -d -p 8080:8080 --rm xebia-signature
open http://localhost:8080
```

Fill in the fields and press the button!

