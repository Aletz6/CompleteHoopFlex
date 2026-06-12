# CI / CD con GitHub Actions

Este repositorio incluye workflows básicos para CI en backend y frontend.

- `backend-ci.yml` (ruta: .github/workflows/backend-ci.yml): ejecuta tests de Python con `pytest` cuando hay cambios en `hoopflex-backend/`.
- `frontend-ci.yml` (ruta: .github/workflows/frontend-ci.yml): instala dependencias y ejecuta `yarn validate` en `HoopFlex/` (lint + checks). La app usa Yarn en lugar de npm.

Qué hace cada workflow:
- Backend CI: instala Python 3.11, instala `requirements.txt` y ejecuta `pytest -q`.
- Frontend CI: usa Node.js 18, ejecuta `yarn install --frozen-lockfile` y `yarn validate`.

Ejecución manual:
- Desde la pestaña **Actions** en GitHub puedes seleccionar cualquiera de los workflows y usar **Run workflow** (gracias a `workflow_dispatch`). Esto te permite ver cómo se ejecuta el pipeline sin hacer un push.

Caching:
- El workflow frontend usa caché para Yarn (`~/.cache/yarn` y `HoopFlex/node_modules`) y el backend cachea `~/.cache/pip` para acelerar instalaciones.

Dónde ver logs:
- Abre la ejecución en **Actions** y selecciona el job; los pasos se muestran en orden con output y código de salida.
