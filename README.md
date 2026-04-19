# OpenClaw Multi-Agent Team Configuration

Acest repository conține configurarea completă pentru echipa de 8 agenți AI specializați în dezvoltarea proiectului QuickDelivery, configurată pentru OpenClaw + Multica.

## 🏛️ Structura Echipei (8 Agenți)

### 🎯 Product-Architect (Orchestrator)
**Rol:** Product Owner + Orchestrator  
**Responsabilități:**
- Definește cerințele și specificațiile
- Prioritizează backlog-ul
- Assign task-uri către ceilalți 8 agenți (via scripturi `.sh`)
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
├── taskboard/                         # 📊 Taskboard v2.0
│   ├── taskboard.html                 # UI interactiv
│   ├── data.json                      # Config agenți și proiecte
│   └── start-taskboard.sh             # Script pornire
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

## 🚀 Stack Tehnologic

- **OpenClaw** - Gateway pentru agenți AI (port 18789)
- **Multica** - Platformă pentru gestionarea agenților
- **Telegram Bots** - Interfață de comunicare pentru fiecare agent
- **PostgreSQL** - Database pentru persistență
- **Docker** - Containerizare servicii

## 📅 Istoric

| Data | Eveniment |
|------|-----------|
| **19 Aprilie 2026** | Configurare inițială a echipei de 8 agenți AI |
| **19 Aprilie 2026** | Setup Product-Architect ca Orchestrator + scripturi de assign |
| **19 Aprilie 2026** | Taskboard v2.0 cu multi-project și persistență |

## 👤 Owner

**Andrei** (@david3366) - Ownerul proiectului, definește direcția și prioritățile.

---

*Notă: Această configurare este specifică pentru proiectul QuickDelivery și OpenClaw. Nu ar trebui folosită în alte contexte fără adaptare.*

---

## 📊 Taskboard v2.0

Taskboard interactiv pentru managementul task-urilor echipei:

### 🎯 Features
- **8 Agenți** configurați cu emoji și culori
- **Multi-proiect** support
- **Persistență** (JSON + localStorage backup)
- **Dependințe** între task-uri cu blocare automată
- **Drag & drop** Kanban board (5 coloane)
- **Stats live** (total, active, completed, blocked)
- **Auto-save** la fiecare 30 secunde

### 📁 Fișiere Taskboard
```
taskboard/
├── taskboard.html          # UI complet (32KB)
├── data.json               # Config agenți și proiecte
└── start-taskboard.sh      # Script pornire server
```

### 🚀 Utilizare
```bash
# Pornește serverul
cd /workspace/shared
./start-taskboard.sh

# Deschide în browser
http://localhost:8080/taskboard.html
```

### 🎨 Agenți în Taskboard
| Agent | Emoji | Rol |
|-------|-------|-----|
| Product-Architect | 🎯 | Product Owner + Orchestrator |
| Backend-Architect | ⚙️ | API/DB Architect |
| Frontend-Architect | 🎨 | UI/UX Architect |
| Builder-Modules | 🛠️ | Web Developer |
| Builder-Mobile | 📱 | Mobile Developer |
| Reviewer-All | 👁️ | Code Reviewer |
| Operations-All | 🚀 | DevOps Engineer |
| Specialists-All | 🔬 | Research/BA |
