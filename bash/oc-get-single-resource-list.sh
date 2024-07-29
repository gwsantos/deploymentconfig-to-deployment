#!/usr/bin/env bash

#Returns list of all kubernetes resources of a given kind in text format from the current openshift namespace.
#User must be logged in and authenticated to an openshift cluster and be at the desired namespace/project to execute the script.

KIND=$(echo "$1" | awk '{print tolower($0)}')

oc get "${KIND}" -o template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}' > ../temp-files/"${KIND}"_list