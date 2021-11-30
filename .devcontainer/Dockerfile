# syntax=docker/dockerfile:labs
# escape=\

# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.194.3/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# avoid reinstalling extensions on container rebuild
RUN mkdir -p /home/vscode/.vscode-server/extensions && chown -R vscode /home/vscode/.vscode-server

# assets
ENV DEBIAN_FRONTEND=noninteractive
COPY ./.devcontainer/assets/apt_pkglist apt_pkglist
RUN apt-get update -y && apt-get install -y --no-install-recommends $(cat apt_pkglist) && rm apt_pkglist
RUN pip3 --disable-pip-version-check --no-cache-dir install --upgrade pip
COPY ./.devcontainer/assets/requirements.txt requirements.txt
RUN pip3 --disable-pip-version-check --no-cache-dir install --requirement requirements.txt && rm requirements.txt
USER vscode
COPY ./.devcontainer/assets/.bash_aliases /home/vscode/.bash_aliases
COPY ./.devcontainer/assets/.bashrc /home/vscode/.bashrc.addon
RUN cat /home/vscode/.bashrc.addon >> /home/vscode/.bashrc && rm /home/vscode/.bashrc.addon
