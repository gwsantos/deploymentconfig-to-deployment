#!/usr/bin/env bash

#Returns list of all kubernetes resources of a given kind in text format from the current openshift namespace.
#User must be logged in and authenticated to an openshift cluster and be at the desired namespace/project to execute the script.
#Resource kind should be passed IN PLURAL as the first argument - i.e. "routes", "deployments", "services" etc

KIND=$(echo "$1" | awk '{print tolower($0)}')

oc get "$KIND" --no-headers | oc get "$1" -o template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}' > ../temp-files/"$KIND"_list