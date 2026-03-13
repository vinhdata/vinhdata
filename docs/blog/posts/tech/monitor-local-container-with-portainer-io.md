---
date: 2026-02-02
categories:
  - Tech
tags:
  - docker
  - portainer
  - monitoring
  - containers
---

# Monitor Local Docker Containers with Portainer

Portainer is a lightweight web UI for Docker that makes it easy to view container status, check logs, and manage images/volumes without memorizing commands.

<!-- more -->

## Prerequisites

- Docker installed and running
- Permission to access the Docker socket (usually being in the `docker` group, or using `sudo`)

## Step 1: Create a persistent volume

This stores Portainer data (users, settings) so it survives restarts.

```bash
docker volume create portainer_data
```

## Step 2: Run Portainer

```bash
docker run -d --name portainer --restart=unless-stopped \
  -p 9443:9443 -p 9000:9000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest
```

**What this does:**
- Exposes the UI on **9443 (HTTPS)** and **9000 (HTTP)**.
- Mounts the Docker socket so Portainer can manage your local Docker engine.
- Persists configuration in the `portainer_data` volume.

## Step 3: Open the UI

- HTTPS (recommended): `https://localhost:9443`
- HTTP (optional): `http://localhost:9000`

On first launch, Portainer will ask you to create an admin user, then choose an environment.

Pick **Local** (Docker) since we mounted `/var/run/docker.sock`.

## What to use Portainer for (quick wins)

- **Container list**: status, CPU/memory graphs, restart count
- **Logs**: open a container → *Logs*
- **Exec shell**: open a container → *Console*
- **Inspect config**: open a container → *Inspect* (env vars, mounts, network)
- **Volumes**: see what’s consuming space and which containers use them

## Upgrading Portainer

Portainer is just a container, so upgrading is a pull + recreate:

```bash
docker pull portainer/portainer-ce:latest
docker rm -f portainer
docker run -d --name portainer --restart=unless-stopped \
  -p 9443:9443 -p 9000:9000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest
```

## Removing Portainer (optional)

Remove the container:

```bash
docker rm -f portainer
```

Remove stored data too (this deletes Portainer settings):

```bash
docker volume rm portainer_data
```

## Notes on security

Mounting `/var/run/docker.sock` effectively gives Portainer **admin-level control** over your Docker host. Keep it local-only, or put it behind authentication and trusted networking if you expose it.

