 # CompleteHoopFlex — Monorepo (Frontend + Backend)

 ## 📁 Estructura del Proyecto

 ```
 CompleteHoopFlex/
 ├── HoopFlex/              # React Native Frontend (Expo)
 ├── hoopflex-backend/      # FastAPI Backend
 ├── docker-compose.yml     # Orquestación de servicios
 ├── .github/
 │   └── workflows/         # Workflows: backend-ci.yml, frontend-ci.yml
 └── Makefile               # Comandos útiles
 ```

 ## 🚀 Quick Start

 ### Frontend (React Native — Yarn)

 ```bash
 cd HoopFlex
 yarn install --frozen-lockfile
 yarn start
 ```

 ### Backend (FastAPI)

 ```bash
 cd hoopflex-backend
 pip install -r requirements.txt
 python -m uvicorn main:app --reload
 ```

 ### Con Docker Compose (Ambos)

 ```bash
 docker-compose up --build
 ```

 - Frontend (web): http://localhost:3000
 - Backend: http://localhost:8000
 - API Docs: http://localhost:8000/docs

 ## 🧪 Testing

 ### Frontend

 ```bash
 cd HoopFlex
 yarn validate        # lint + format check
 yarn lint            # eslint
 yarn lint:fix        # fix eslint
 yarn format          # prettier
 ```

 ### Backend

 ```bash
 cd hoopflex-backend
 pytest -q                        # Run tests
 pytest --cov                     # With coverage
 black .                          # Format
 flake8 .                         # Lint
 bandit -r .                      # Security check
 ```

 ## 🔄 CI/CD (GitHub Actions)

 He añadido workflows básicos en `.github/workflows/`:
 - `frontend-ci.yml` — valida Yarn (lint/format) cuando se tocan archivos en `HoopFlex/`.
 - `backend-ci.yml` — ejecuta `pytest` cuando se tocan archivos en `hoopflex-backend/`.

 Todos los workflows soportan ejecución manual (`workflow_dispatch`) y usan caché de dependencias para acelerar runs.

 ### Triggers
 - `push` y `pull_request` sobre paths relevantes.
 - `workflow_dispatch` para ejecutar manualmente desde la pestaña Actions.

 ### Cómo ejecutar manualmente
 1. Ve a la pestaña **Actions** en GitHub.
 2. Selecciona el workflow (`Backend CI` o `Frontend CI`).
 3. Pulsa **Run workflow**.

 ## 📝 Crear el repo en GitHub (opcional)

 Si quieres crear el repo público `CompleteHoopFlex` desde tu máquina con GitHub CLI (`gh`) y empujar el contenido actual:

 ```powershell
 cd C:\Users\Ale23\CompleteHoopFlex
 git add .
 git commit -m "chore: setup CI/CD workflows"
 gh repo create CompleteHoopFlex --public --source=. --remote=origin --confirm
 git push -u origin HEAD
 ```

 Si no usas `gh`, crea el repo en github.com y luego:

 ```bash
 git remote add origin git@github.com:TU_USUARIO/CompleteHoopFlex.git
 git push -u origin HEAD
 ```

 ## 📚 Recursos y logs
 - Los logs y detalles de cada ejecución están disponibles en la pestaña **Actions** → seleccionar run → ver steps.
 - `CI_CD.md` contiene instrucciones específicas sobre los workflows.

 ## 🛠️ Troubleshooting (rápido)

 - MongoDB no conecta:
 ```bash
 docker-compose down -v
 docker-compose up -d mongodb
 ```

 - Puerto 8000 en uso:
 ```bash
 lsof -i :8000
 kill -9 <PID>
 ```

 - Limpiar caché frontend/backend:
 ```bash
 cd HoopFlex && yarn cache clean && yarn install --frozen-lockfile
 cd hoopflex-backend && rm -rf __pycache__ .pytest_cache
 ```

 ---

 Si quieres, puedo ejecutar por ti los comandos para crear el repo y empujar los cambios (necesito que `gh` esté instalado y autenticado), o generarte un script para ejecutarlo localmente.
