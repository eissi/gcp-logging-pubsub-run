#!/bin/sh
kubectl delete -f pubsub-pull.yaml
kubectl apply -f pubsub-pull.yaml
