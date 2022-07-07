#!/bin/sh
kubectl delete -f logger-deployment.yaml
kubectl apply -f logger-deployment.yaml
