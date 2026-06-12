# CI / CD con GitHub Actions

Este repositorio incluye workflows básicos para CI en backend y frontend, y un pipeline opcional para construir y publicar una imagen Docker.

- `backend-ci.yml` (ruta: .github/workflows/backend-ci.yml): ejecuta tests de Python con `pytest` cuando hay cambios en `hoopflex-backend/`.
- `frontend-ci.yml` (ruta: .github/workflows/frontend-ci.yml): instala dependencias y ejecuta `yarn validate` en `HoopFlex/` (lint + checks). La app usa Yarn en lugar de npm.
- `docker-build.yml` (ruta: .github/workflows/docker-build.yml): construye y publica una imagen Docker a Docker Hub al pushear en `main` (requiere secretos).

Qué hace cada workflow:
- Backend CI: instala Python 3.11, instala `requirements.txt` y ejecuta `pytest -q`.
- Frontend CI: usa Node.js 18, ejecuta `yarn install --frozen-lockfile` y `yarn validate`.
- Docker: usa las acciones oficiales de Docker para buildx y push; necesita `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN` en Secrets.

Ejecución manual:
- Desde la pestaña **Actions** en GitHub puedes seleccionar cualquiera de los workflows y usar **Run workflow** (gracias a `workflow_dispatch`). Esto te permite ver cómo se ejecuta el pipeline sin hacer un push.

Caching:
- El workflow frontend usa caché para Yarn (`~/.cache/yarn` y `HoopFlex/node_modules`) y el backend cachea `~/.cache/pip` para acelerar instalaciones.

Dónde ver logs:
- Abre la ejecución en **Actions** y selecciona el job; los pasos se muestran en orden con output y código de salida.

Cómo habilitar despliegue (opcional):
1. En GitHub repo > Settings > Secrets > Actions, crear `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN`.
2. Personalizar la etiqueta (`tags`) en `.github/workflows/docker-build.yml` si usas otro registry.

Notas y siguientes pasos sugeridos:
- Si quieres desplegar a un servicio (AWS/GCP/Azure), puedo añadir una job de despliegue que use sus acciones y secretos.
- Si prefieres build de imagen en PRs para validación, lo puedo añadir.
