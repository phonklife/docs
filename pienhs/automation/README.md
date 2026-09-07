# PIENHS CULT OS — Automation

Moduł automatyzacji dla `THE_GRINDING_WHEEL`.

## Flow

```text
IDEA → SESSION → ABLETON/SUNO TEST → REVIEW → DECISION → COMMIT → VALIDATION → MILESTONE → RELEASE GATE
```

## Start lokalny

```bash
cd pienhs/automation
python scripts/validate_project.py
python scripts/create_session.py --focus core-loop
python scripts/build_dashboard.py
```

## Zasada

Repo i vault automatyzują dokumentację, status, review i release gate. Ableton/Suno pozostają handoffem do czasu podłączenia wspieranego API/mostu lokalnego.
