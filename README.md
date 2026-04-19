# OpenClaw Multi-Agent Team Configuration

Acest repository conține configurarea completă pentru echipa de 8 agenți AI specializați în dezvoltarea proiectului QuickDelivery, configurată pentru OpenClaw + Multica.

## 🏛️ Structura Echipei (8 Agenți)

### 🎯 Product-Architect (Orchestrator)
**Rol:** Product Owner + Orchestrator  
**Responsabilități:**
- Definește cerințele și specificațiile
- Prioritizează backlog-ul
- Assign task-uri către ceilalți 7 agenți (via scripturi `.sh`)
- Coordonează comunicarea între agenți

### Arhitecți
| Agent | Rol | Descriere |
|-------|-----|-----------|
| **Frontend-Architect** | UI/UX Lead | Design system, UI patterns, experiență utilizator |
| **Backend-Architect** | API/DB Lead | Arhitectură API, database, infrastructură backend |

### Builders
| Agent | Rol | Descriere |
|-------|-----|-----------|
| **Builder-Modules** | Web Developer | Toate modulele web (customer, admin, rider, store) |
| **Builder-Mobile** | Mobile Developer | Aplicații iOS și Android |

### Quality & Operations
| Agent | Rol | Descriere |
|-------|-----|-----------|
| **Reviewer-All** | Code Reviewer | Review cod, security audit, best practices |
| **Operations-All** | DevOps | CI/CD, deploy, infrastructură, monitoring |
| **Specialists-All** | Research/BA | Cercetare, business analysis, documentație |

## 📁 Structura Repository-ului

```
openclaw-multiagents-team/
├── README.md                          # Acest fișier
├── start-taskboard-api.sh             # 🆕 Script pornire backend API
├── product-architect/                 # 🎯 Orchestrator + Product Owner
│   ├── SOUL.md                        # Identitate: Product-Architect + Orchestrator
│   ├── IDENTITY.md                    # Nume, creature, vibe, emoji
│   ├── USER.md                        # Informații despre Andrei
│   ├── AGENTS.md                      # Reguli generale pentru agenți
│   ├── BOOTSTRAP.md                   # Ghid de pornire
│   ├── HEARTBEAT.md                   # Task-uri periodice
│   ├── TOOLS.md                       # Note locale despre setup
│   ├── assign-to-backend-architect.sh # Script assign către Backend-Architect
│   ├── assign-to-builder-modules.sh   # Script assign către Builder-Modules
│   ├── assign-to-builder-mobile.sh    # Script assign către Builder-Mobile
│   ├── assign-to-frontend-architect.sh# Script assign către Frontend-Architect
│   ├── assign-to-operations-all.sh    # Script assign către Operations-All
│   ├── assign-to-reviewer-all.sh      # Script assign către Reviewer-All
│   ├── assign-to-specialists-all.sh   # Script assign către Specialists-All
│   └── assign-to-builder.sh           # Script assign legacy
├── taskboard/                         # 📊 Taskboard v2.0 + Backend API
│   ├── taskboard.html                 # UI interactiv
│   ├── data.json                      # Config agenți și proiecte
│   ├── api.py                         # 🆕 Flask Backend API
│   └── start-taskboard-api.sh         # 🆕 Script pornire API
├── backend-architect/                 # ⚙️ Backend-Architect config
│   ├── SOUL.md
│   ├── IDENTITY.md
│   ├── USER.md
│   ├── AGENTS.md
│   ├── BOOTSTRAP.md
│   ├── HEARTBEAT.md
│   └── TOOLS.md
├── builder-modules/                   # 🛠️ Builder-Modules config
│   ├── SOUL.md
│   ├── IDENTITY.md
│   ├── USER.md
│   ├── AGENTS.md
│   ├── BOOTSTRAP.md
│   ├── HEARTBEAT.md
│   └── TOOLS.md
├── builders/
│   └── mobile/                        # 📱 Builder-Mobile config
│       ├── SOUL.md
│       ├── IDENTITY.md
│       ├── USER.md
│       ├── AGENTS.md
│       ├── BOOTSTRAP.md
│       ├── HEARTBEAT.md
│       └── TOOLS.md
├── frontend-architect/                # 🎨 Frontend-Architect config
│   ├── SOUL.md
│   ├── IDENTITY.md
│   ├── USER.md
│   ├── AGENTS.md
│   ├── BOOTSTRAP.md
│   ├── HEARTBEAT.md
│   └── TOOLS.md
├── operations-all/                    # 🚀 Operations-All config
│   ├── SOUL.md
│   ├── IDENTITY.md
│   ├── USER.md
│   ├── AGENTS.md
│   ├── BOOTSTRAP.md
│   ├── HEARTBEAT.md
│   └── TOOLS.md
├── reviewer-all/                      # 👁️ Reviewer-All config
│   ├── SOUL.md
│   ├── IDENTITY.md
│   ├── USER.md
│   ├── AGENTS.md
│   ├── BOOTSTRAP.md
│   ├── HEARTBEAT.md
│   └── TOOLS.md
└── specialists-all/                   # 🔬 Specialists-All config
    ├── SOUL.md
    ├── IDENTITY.md
    ├── USER.md
    ├── AGENTS.md
    ├── BOOTSTRAP.md
    ├── HEARTBEAT.md
    └── TOOLS.md
```

## 📄 Fișiere de Configurare (per agent)

Fiecare agent are următoarele fișiere standard:

| Fișier | Scop |
|--------|------|
| **SOUL.md** | Identitate, rol și responsabilități |
| **IDENTITY.md** | Nume, creatură, vibe, emoji |
| **USER.md** | Informații despre owner (Andrei) |
| **AGENTS.md** | Reguli generale pentru workspace |
| **BOOTSTRAP.md** | Ghid pentru prima conversație |
| **HEARTBEAT.md** | Task-uri periodice |
| **TOOLS.md** | Note locale despre setup |

## 🔧 Scripturi de Assign (Product-Architect)

Product-Architect are 8 scripturi shell pentru a assigna task-uri către fiecare agent:

```bash
# Assign task către Backend-Architect
./product-architect/assign-to-backend-architect.sh

# Assign task către Builder-Modules  
./product-architect/assign-to-builder-modules.sh

# Assign task către Builder-Mobile
./product-architect/assign-to-builder-mobile.sh

# Assign task către Frontend-Architect
./product-architect/assign-to-frontend-architect.sh

# Assign task către Operations-All
./product-architect/assign-to-operations-all.sh

# Assign task către Reviewer-All
./product-architect/assign-to-reviewer-all.sh

# Assign task către Specialists-All
./product-architect/assign-to-specialists-all.sh
```

## 📊 Taskboard v2.0

Taskboard interactiv cu backend API real pentru managementul task-urilor echipei.

### 🎯 Features
- **8 Agenți** configurați cu emoji și culori
- **Multi-proiect** support
- **Persistență reală** via Flask API + JSON file
- **Auto-backup** înainte de fiecare save
- **Dependințe** între task-uri cu blocare automată
- **Drag & drop** Kanban board (5 coloane)
- **Stats live** (total, active, completed, blocked)
- **Backup restore** functionality

### 📁 Fișiere Taskboard
```
taskboard/
├── taskboard.html          # UI complet (32KB)
├── data.json               # Config agenți și proiecte
├── api.py                  # 🆕 Flask Backend API
└── start-taskboard-api.sh  # 🆕 Script pornire API
```

### 🚀 Utilizare Taskboard

**1. Instalează dependințele:**
```bash
pip install flask flask-cors
```

**2. Pornește backend API:**
```bash
./start-taskboard-api.sh
# sau
cd taskboard && python3 api.py
```

**3. Deschide în browser:**
```
http://localhost:5000
```

### 🔌 API Endpoints

| Method | Endpoint | Descriere |
|--------|----------|-----------|
| GET | `/api/data` | Get all data |
| POST | `/api/data` | Save all data (cu backup auto) |
| GET | `/api/tasks` | Get tasks (filtrat by project) |
| POST | `/api/tasks` | Create task |
| PUT | `/api/tasks/<id>` | Update task |
| DELETE | `/api/tasks/<id>` | Delete task |
| GET | `/api/projects` | Get projects |
| POST | `/api/projects` | Create project |
| GET | `/api/agents` | Get agents |
| GET | `/api/stats` | Get statistics |
| GET | `/api/backups` | List backups |
| POST | `/api/backups/<file>` | Restore backup |

### 🎨 Agenți în Taskboard

| Agent | Emoji | Rol | Culoare |
|-------|-------|-----|---------|
| Product-Architect | 🎯 | Product Owner + Orchestrator | #e94560 |
| Backend-Architect | ⚙️ | API/DB Architect | #4ecdc4 |
| Frontend-Architect | 🎨 | UI/UX Architect | #ff6b6b |
| Builder-Modules | 🛠️ | Web Developer | #95e1d3 |
| Builder-Mobile | 📱 | Mobile Developer | #ffd93d |
| Reviewer-All | 👁️ | Code Reviewer | #a8d8ea |
| Operations-All | 🚀 | DevOps Engineer | #6c5ce7 |
| Specialists-All | 🔬 | Research/BA | #fd79a8 |

## 🚀 Stack Tehnologic

- **OpenClaw** - Gateway pentru agenți AI (port 18789)
- **Multica** - Platformă pentru gestionarea agenților
- **Telegram Bots** - Interfață de comunicare pentru fiecare agent
- **Flask** - Backend API pentru taskboard
- **PostgreSQL** - Database pentru persistență
- **Docker** - Containerizare servicii

## 📅 Istoric

| Data | Eveniment |
|------|-----------|
| **19 Aprilie 2026** | Configurare inițială a echipei de 8 agenți AI |
| **19 Aprilie 2026** | Setup Product-Architect ca Orchestrator + scripturi de assign |
| **19 Aprilie 2026** | Taskboard v2.0 cu multi-project și persistență reală |
| **19 Aprilie 2026** | Backend API Flask cu auto-backup și restore |

## 👤 Owner

**Andrei** (@david3366) - Ownerul proiectului, definește direcția și prioritățile.

---

*Notă: Această configurare este specifică pentru proiectul QuickDelivery și OpenClaw. Nu ar trebui folosită în alte contexte fără adaptare.*
