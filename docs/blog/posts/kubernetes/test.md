---
date: 2026-01-29
categories:
  - Kubernetes
tags:
  - kubernetes
  - k8s
  - kubectl
  - cheatsheet
---

# kubectl Cheat Sheet (Kubernetes CLI)

A practical `kubectl` cheat sheet for day-to-day debugging and operations.

<!-- more -->

## Setup & context

Show current context and switch clusters:

```bash
kubectl config current-context
kubectl config get-contexts
kubectl config use-context <context-name>
```

Set a default namespace for the current context:

```bash
kubectl config set-context --current --namespace=<ns>
```

## Quick “what’s running?”

```bash
kubectl get nodes -o wide
kubectl get ns
kubectl get pods -A
kubectl get pods -n <ns> -o wide
kubectl get deploy,rs,svc,ing -n <ns>
```

Watch changes:

```bash
kubectl get pods -n <ns> -w
```

## Describe & events (first stop for debugging)

```bash
kubectl describe pod <pod> -n <ns>
kubectl describe deploy <deploy> -n <ns>
kubectl get events -n <ns> --sort-by=.metadata.creationTimestamp
```

## Logs

Single container:

```bash
kubectl logs <pod> -n <ns>
kubectl logs <pod> -n <ns> -f
```

Specific container in a multi-container pod:

```bash
kubectl logs <pod> -n <ns> -c <container>
```

Previous crash:

```bash
kubectl logs <pod> -n <ns> --previous
```

## Exec / shell in a container

```bash
kubectl exec -n <ns> -it <pod> -- sh
kubectl exec -n <ns> -it <pod> -c <container> -- bash
```

## Port-forward

Pod:

```bash
kubectl port-forward -n <ns> pod/<pod> 8080:8080
```

Service:

```bash
kubectl port-forward -n <ns> svc/<service> 8080:80
```

## Apply / rollout

Apply manifests:

```bash
kubectl apply -f k8s/
kubectl apply -f app.yaml -n <ns>
```

Deployment rollout status:

```bash
kubectl rollout status deploy/<deploy> -n <ns>
kubectl rollout history deploy/<deploy> -n <ns>
```

Rollback:

```bash
kubectl rollout undo deploy/<deploy> -n <ns>
```

## Scale & restart

Scale replicas:

```bash
kubectl scale deploy/<deploy> -n <ns> --replicas=3
```

Restart a deployment (forces new ReplicaSet):

```bash
kubectl rollout restart deploy/<deploy> -n <ns>
```

## Delete safely

Delete one resource:

```bash
kubectl delete pod/<pod> -n <ns>
kubectl delete -f app.yaml -n <ns>
```

Delete a namespace (careful):

```bash
kubectl delete ns <ns>
```

## YAML/JSON output + common JSONPath

Get full YAML:

```bash
kubectl get deploy/<deploy> -n <ns> -o yaml
```

Common JSONPath snippets:

```bash
# Image(s) used by a deployment
kubectl get deploy/<deploy> -n <ns> -o jsonpath='{.spec.template.spec.containers[*].image}{"\n"}'

# Pod phase + node
kubectl get pod/<pod> -n <ns> -o jsonpath='{.status.phase}{" on "}{.spec.nodeName}{"\n"}'
```

## Troubleshooting patterns

Pod stuck Pending:
- Check node capacity / taints / tolerations / PVC binding.

```bash
kubectl describe pod <pod> -n <ns>
kubectl get pvc -n <ns>
kubectl get nodes
```

CrashLoopBackOff:
- Check logs + `--previous`, then events.

```bash
kubectl logs <pod> -n <ns> --previous
kubectl describe pod <pod> -n <ns>
```

ImagePullBackOff:
- Check image name/tag and registry credentials.

```bash
kubectl describe pod <pod> -n <ns>
kubectl get secret -n <ns>
```

- Placeholder content for validating category + tags rendering.
