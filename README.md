# 🚗 Smart Mechanic

**Smart Mechanic** is a project built with FastAPI that aims to manage car repair appointments and provide users with real-time information about their vehicles. 🛠️

---

## 🔹 Overview

The project allows two main types of users:

1. **👤 Regular Users**: 
   - 📝 Can register and log in to the system.
   - 📅 Can view available appointment slots for different mechanics.
   - ✅ Can book an appointment for car repair.
   - 🔧 Can track the status of their car during the repair process.

2. **🧰 Mechanics**:
   - 📝 Can register by providing a verified mechanic ID.
   - 🛠️ Can manage appointments and update the repair status of cars.

---

## 🔹 Features (Planned / Basic)

- 🗝️ User registration and login system.
- 🧾 Mechanic verification via a unique mechanic ID.
- 📅 Appointment booking system for car repairs.
- 🔧 Track car repair status.
- 🖥️ Simple dashboard for users to view their appointments.
- 🖥️ Dashboard for mechanics to see assigned appointments.

---

## 🔹 Technologies

- ⚡ **Backend:** FastAPI
- 🗄️ **Database:** SQLAlchemy with SQLite (for development)
- 🧪 **Testing:** Pytest
- 🔐 **Authentication:** JWT / OAuth (planned)
- 🐳 **Dockerized:** The project runs in Docker using Docker Compose for easy development and deployment.

---

## 🔹 Project Status

🚧 This is an early-stage project. Currently, it focuses on core functionalities such as:

- **User management:** The `accounts` app is fully implemented with user models, registration, and authentication.  
- **Appointment management:** Booking and tracking repair appointments.  
- **Docker support:** The project can be started with Docker Compose for a consistent development environment.  

More advanced features like messaging between mechanics and users or advanced notifications will be considered in the future.

---

## 🔹 Quick Start with Docker Compose

This project is fully **dockerized** and can be run easily using Docker Compose.

### 1️⃣ Build and start the containers
From the root of the project, run:

```bash
docker-compose up -d --build
