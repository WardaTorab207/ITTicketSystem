# IT Ticket System

A Django-based IT support ticket management system for tracking, assigning, and resolving support requests within an organization.

---

## Features

### For Employees
- **Login/Logout** – Role-based authentication
- **Dashboard** – Personal home page
- **My Tickets** – View all tickets assigned to you
- **Create Ticket** – Submit new support requests with type, urgency, and project
- **Profile Management** – Update personal information

### For Admins/Managers
- **Admin Dashboard** – Separate dashboard with full oversight
- **All Tickets** – View, approve, reject, and manage all tickets
- **All Employees** – View and manage employee list
- **Add Employee** – Register new employees with department, designation, and role
- **Add Ticket** – Create tickets on behalf of employees
- **Ticket Actions** – Approve, reject, mark complete, or delete tickets
- **Employee Management** – Delete employees

<img width="682" height="725" alt="Screenshot 2026-02-01 145341" src="https://github.com/user-attachments/assets/504a45d2-0bd7-47ca-bb5f-5b7631e5156b" />
<img width="1913" height="812" alt="Screenshot 2026-02-01 145413" src="https://github.com/user-attachments/assets/060989fb-b38f-40e4-85d8-0b6bb03a2423" />
<img width="1914" height="886" alt="Screenshot 2026-02-01 145435" src="https://github.com/user-attachments/assets/e86312a2-88a5-4358-89a6-5cb57d986210" />
<img width="1897" height="848" alt="Screenshot 2026-02-01 145713" src="https://github.com/user-attachments/assets/96ecf609-ff26-459c-8125-445d19041984" />
<img width="1915" height="872" alt="Screenshot 2026-02-01 150225" src="https://github.com/user-attachments/assets/ae22d5d9-2eee-49b8-a314-b07b21e97af5" />
<img width="1918" height="884" alt="Screenshot 2026-02-01 150303" src="https://github.com/user-attachments/assets/d49b4eb2-057e-4c90-9240-aea9ed0e25a2" />
<img width="1910" height="828" alt="Screenshot 2026-02-01 150317" src="https://github.com/user-attachments/assets/33404347-f945-41d6-81fd-15247117874b" />
<img width="1893" height="856" alt="Screenshot 2026-02-01 150325" src="https://github.com/user-attachments/assets/791bd6c1-1c60-4643-8d1f-03821c0bd691" />


### Projects Supported
5S System, Automations, Bar Stock Inventory Audit, Calibration, Costing, Dashboard - Main, Time Clock, HR - Human Resources, Toolcrib, Surveillance, SetupSheet, StockRoom, Quality, Production, Metrics, Maintenance


## Tech Stack

- **Backend:** Django 4.2
- **Database:** SQLite
- **Frontend:** HTML, CSS (SCSS), JavaScript
- **Python:** 3.11 or 3.12 (recommended)

---

## Prerequisites

- Python 3.11 or 3.12
- pip

> ⚠️ **Note:** Django does not yet support Python 3.14. Use Python 3.11 or 3.12.

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ITTicketSystem-main
```

### 2. Create virtual environment

```bash
# Windows
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1

# Linux/Mac
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

---

## Default Credentials

### Admin / Manager Login (Employee Dashboard)
| Username      | Password  |
|---------------|-----------|
| Warda Mirza   | 11112222  |


### Django Admin (`/admin/`)
Create a superuser for database management:

```bash
python manage.py createsuperuser
```

---

## Project Structure

```
ITTicketSystem-main/
├── home/                 # Main app
│   ├── models.py         # Employee, Ticket, Department models
│   ├── views.py          # All views (employee + admin)
│   ├── urls.py           # URL routing
│   └── admin.py          # Django admin config
├── loginSystem/          # Django project config
│   ├── settings.py
│   └── urls.py
├── templates/            # HTML templates
│   ├── admin/            # Admin-specific templates
│   ├── index.html
│   ├── loginForm.html
│   ├── addTicket.html
│   ├── emp_tickets.html
│   └── profile.html
├── static/               # CSS, JS, images
├── db.sqlite3            # SQLite database
├── manage.py
├── requirements.txt
└── README.md
```

---

## URL Routes

| Route | Description |
|-------|-------------|
| `/` | Employee dashboard |
| `/login/` | Login page |
| `/logout/` | Logout |
| `/emp_tickets/` | My assigned tickets |
| `/add-ticket/` | Create new ticket |
| `/profile/` | Employee profile |
| `/admin-desboard/` | Admin dashboard |
| `/admin-allTickets/` | All tickets |
| `/admin-allEmployees/` | All employees |
| `/admin-addEmployee/` | Add new employee |
| `/admin-addTicket/` | Admin add ticket |
| `/admin/` | Django admin |

---

## User Roles

| Role | IsManager | Access |
|------|-----------|--------|
| **Manager/Admin** | `True` | Full access to admin dashboard and all features |
| **Employee** | `False` | Personal dashboard, own tickets, add tickets, profile |

---

## License

This project is available for educational and internal use.
