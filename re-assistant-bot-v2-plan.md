# RE Assistant Bot — v2 Build Spec

## Status: PLANNED

## Overview
Add lead capture and follow-up reminder functionality. Bot and Google Sheets stay in sync.

---

## Data Flow

```
Realtor texts bot → "new lead John 403-555-1234"
         ↓
Bot saves to leads.json (local backup)
Bot writes new row to Google Sheet
Bot schedules follow-up reminder
         ↓
Reminder fires 3 days later → Realtor texts back → Bot marks row "followed up" in Sheet
```

---

## Lead Capture

### Fields
- Name
- Phone
- Source (where the lead came from)
- Note (what they're interested in)
- Date Added (auto)
- Follow-up Date (default 3 days out, or custom)
- Status (New | Pending Follow-up | Contacted | Dead)

### Commands
- `/addlead [name] [phone] — [note] [followup_days]` → e.g. `/adlead John 403-555-1234 — interested SW condo 5`
- `/myleads` → shows all leads with status
- `/done [name]` → marks lead as contacted
- `/lead [name]` → shows single lead details

### Text Format
Flexible parser — detects key fields:
```
/adlead John Smith 403-555-1234 interested in SW Calgary condo, 3 days
```
Bot extracts: name, phone, note, follow-up days (defaults to 3 if not specified)

---

## Google Sheets Structure

### Sheet Columns
| Name | Phone | Source | Note | Date Added | Follow-up Date | Status |

### Sheet Name
- Tab name: "Leads"
- Or separate sheet per realtor

### Sync Rules
- Every new lead → new row written
- Every follow-up marked done → row Status updated
- Bot never deletes rows, only updates Status

---

## Follow-Up Reminder

### Trigger
Cron job runs every hour, checks:
- Follow-up date <= today
- Status = "Pending Follow-up"

### Reminder Message
```
Hey, follow up with [Name] — [Phone]
Interested in: [Note]
```

### Mark Done
Realtor replies "done [name]" or "done" (if only one due) → Status updated to "Contacted"

---

## Local Backup
- File: `/root/re_bot/leads.json`
- Mirror of Sheet data — bot reads from this, Sheets client writes to Sheet
- On restart, bot reloads from this file

---

## Priority
HIGH — this is what makes the bot actually useful to a realtor

## Notes
- User (Davy) will gather more RE agent day-to-day info while I build this
- Sheets API key will be provided by user later
- User will start outreach once bot is ready
