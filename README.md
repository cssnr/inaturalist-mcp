[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/inaturalist-mcp?logo=github)](https://github.com/cssnr/inaturalist-mcp/releases/latest)
[![PyPI Version](https://img.shields.io/pypi/v/inaturalist-mcp?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/inaturalist-mcp/)
[![Image Latest](https://badges.cssnr.com/ghcr/tags/cssnr/inaturalist-mcp/latest)](https://github.com/cssnr/inaturalist-mcp/pkgs/container/inaturalist-mcp)
[![Image Size](https://badges.cssnr.com/ghcr/size/cssnr/inaturalist-mcp)](https://github.com/cssnr/inaturalist-mcp/pkgs/container/inaturalist-mcp)
[![Deployment PyPi](https://img.shields.io/github/deployments/cssnr/inaturalist-mcp/pypi?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/inaturalist-mcp/)
[![Workflow Build](https://img.shields.io/github/actions/workflow/status/cssnr/inaturalist-mcp/build.yaml?logo=norton&logoColor=white&label=build)](https://github.com/cssnr/inaturalist-mcp/actions/workflows/build.yaml)
[![Workflow Deploy](https://img.shields.io/github/actions/workflow/status/cssnr/inaturalist-mcp/deploy.yaml?logo=norton&logoColor=white&label=deploy)](https://github.com/cssnr/inaturalist-mcp/actions/workflows/deploy.yaml)
[![Workflow Release](https://img.shields.io/github/actions/workflow/status/cssnr/inaturalist-mcp/release.yaml?logo=norton&logoColor=white&label=release)](https://github.com/cssnr/inaturalist-mcp/actions/workflows/release.yaml)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/inaturalist-mcp?logo=listenhub&label=updated)](https://github.com/cssnr/inaturalist-mcp/pulse)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/cssnr/inaturalist-mcp?logo=buffer&label=repo%20size)](https://github.com/cssnr/inaturalist-mcp?tab=readme-ov-file#readme)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/inaturalist-mcp?logo=devbox)](https://github.com/cssnr/inaturalist-mcp?tab=readme-ov-file#readme)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/cssnr/inaturalist-mcp?logo=southwestairlines)](https://github.com/cssnr/inaturalist-mcp/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/inaturalist-mcp?logo=codeforces&logoColor=white)](https://github.com/cssnr/inaturalist-mcp/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/inaturalist-mcp?logo=theconversation)](https://github.com/cssnr/inaturalist-mcp/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/inaturalist-mcp?style=flat&logo=forgejo&logoColor=white)](https://github.com/cssnr/inaturalist-mcp/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/inaturalist-mcp?style=flat&logo=gleam&logoColor=white)](https://github.com/cssnr/inaturalist-mcp/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=apachespark&logoColor=white&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

# iNaturalist MCP

<a title="iNaturalist MCP" href="https://github.com/cssnr/inaturalist-mcp?tab=readme-ov-file#readme" target="_blank">
<img alt="iNaturalist MCP" align="right" width="128" height="auto" src="https://raw.githubusercontent.com/cssnr/inaturalist-mcp/refs/heads/master/.github/assets/logo.svg"></a>

- [Setup](#setup)
  - [Local](#local)
  - [Remote](#remote)
- [Development](#development)
- [Building](#building)
- [Support](#support)
- [Contributing](#contributing)

iNaturalist MCP server that provides access to the [iNaturalist](https://www.inaturalist.org) API via the Model Context Protocol.

Exposes a `search_taxa` tool that searches for organisms by common or scientific name and returns taxonomic details, common names, photos, and Wikipedia links.

## Setup<a id="setup"></a>

This can be run in [Local](#local) CLI mode or [Remote](#remote) server mode.

### Local<a id="local"></a>

In CLI mode using `uv`.

<details open><summary>View Config - Local uv</summary>

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "inaturalist": {
      "type": "local",
      "command": ["uvx", "inaturalist-mcp"],
      "enabled": true
    }
  }
}
```

</details>

In CLI mode using Python pip.

```shell
pip install inaturalist-mcp
```

<details><summary>View Config - Local Python</summary>

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "inaturalist": {
      "type": "local",
      "command": ["inaturalist-mcp"],
      "enabled": true
    }
  }
}
```

</details>

### Remote<a id="remote"></a>

With Docker run.

```shell
docker run --rm -p 80:8000 ghcr.io/cssnr/inaturalist-mcp:latest
```

With Docker Compose.

```yaml
services:
  app:
    image: ghcr.io/cssnr/inaturalist-mcp:latest
    ports:
      - '80:8000'
```

With Python from source.

```shell
uv sync
uv run uvicorn inaturalist_mcp.server:app --app-dir src --host 0.0.0.0 --port 8000
```

<details open><summary>View Config - Remote</summary>

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "inaturalist": {
      "type": "remote",
      "url": "http://localhost/mcp",
      "enabled": true
    }
  }
}
```

Note: Set the `url` to the host you are running the server on.

</details>

[![Deploy to Render](https://img.shields.io/badge/Deploy_to_Render-4351E8?style=for-the-badge&logo=render)](https://render.com/deploy?repo=https://github.com/cssnr/inaturalist-mcp)

For a Docker Swarm + Traefik example see the [docker-compose-swarm.yaml](https://github.com/cssnr/inaturalist-mcp/blob/master/docker-compose-swarm.yaml).

For a Portainer Deploy workflow see the [.github/workflows/deploy.yaml](https://github.com/cssnr/inaturalist-mcp/blob/master/.github/workflows/deploy.yaml).

## Development<a id="development"></a>

Sync project.

```shell
uv sync
```

Run local server.

```shell
run cli
```

Run remote server (live reload).

```shell
run dev
```

Point your client to: http://localhost:8000/mcp

Run remote Docker Compose (live reload).

```shell
run compose
```

Point your client to: http://localhost/mcp

You can set the `PORT` environment variable.

## Building<a id="building"></a>

### Docker Image

To build and test the docker image run.

```shell
bash build.sh
docker compose up
```

Point your client to: http://localhost/mcp

### Python Package

This builds the bdist and wheel, if you have a use for it...

```shell
run build
```

## Support<a id="support"></a>

If you run into any issues or need help getting started, please do one of the following:

- Report an Issue: <https://github.com/cssnr/inaturalist-mcp/issues>
- Q&A Discussion: <https://github.com/cssnr/inaturalist-mcp/discussions/categories/q-a>
- Request a Feature: <https://github.com/cssnr/inaturalist-mcp/issues/new?template=1-feature.yaml>
- Chat with us on Discord: <https://discord.gg/wXy6m2X8wY>

[![Features](https://img.shields.io/badge/features-brightgreen?style=for-the-badge&logo=rocket&logoColor=white)](https://github.com/cssnr/inaturalist-mcp/issues/new?template=1-feature.yaml)
[![Issues](https://img.shields.io/badge/issues-red?style=for-the-badge&logo=southwestairlines&logoColor=white)](https://github.com/cssnr/inaturalist-mcp/issues)
[![Discussions](https://img.shields.io/badge/discussions-blue?style=for-the-badge&logo=livechat&logoColor=white)](https://github.com/cssnr/inaturalist-mcp/discussions)
[![Discord](https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/wXy6m2X8wY)

## Contributing<a id="contributing"></a>

Please consider making a donation to support the development of this project
and [additional](https://cssnr.com/) open source projects.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cssnr)

For a full list of current projects visit: [https://cssnr.github.io/](https://cssnr.github.io/)

<a href="https://github.com/cssnr/inaturalist-mcp/stargazers">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=cssnr/inaturalist-mcp&type=date&legend=bottom-right&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=cssnr/inaturalist-mcp&type=date&legend=bottom-right" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=cssnr/inaturalist-mcp&type=date&legend=bottom-right" />
 </picture>
</a>
