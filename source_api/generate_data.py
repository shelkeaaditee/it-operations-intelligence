
import random
import csv
from datetime import datetime, timedelta
priorities = [
    "P1 - Critical",
    "P2 - High",
    "P3 - Medium",
    "P4 - Low"
]

statuses = [
    "New",
    "In Progress",
    "On Hold",
    "Resolved",
    "Closed"
]


categories = [
    "Network",
    "Security",
    "Software/App",
    "Infrastructure",
    "Login/Access",
    "Cloud"
]

support_groups = {
    "Network": "Network Team",
    "Security": "Security Team",
    "Software/App": "Application Support",
    "Infrastructure": "Infrastructure Team",
    "Login/Access": "AD/Entra Team",
    "Cloud": "Cloud Team"
}

descriptions = {
    "Network": [
        "Intermittent network connectivity",
        "VPN connection failure",
        "Slow network response"
    ],
    "Security": [
        "Suspicious login activity",
        "Access permission issue",
        "Security alert investigation"
    ],
    "Software/App": [
        "Application login failure",
        "Application response is slow",
        "Error while processing a request"
    ],
    "Infrastructure": [
        "Server performance degradation",
        "Disk space running low",
        "Server availability issue"
    ],
    "Login/Access": [
        "Unable to log in to corporate account",
        "AD account locked",
        "Entra ID authentication failure",
        "Multi-factor authentication issue",
        "User access provisioning request"
    ],
    "Cloud": [
        "Cloud service unavailable",
        "Cloud resource access denied",
        "Virtual machine performance issue",
        "Cloud deployment failure"
    ]
}


incidents = []

for number in range(1, 50001):
    category = random.choice(categories)

    
    current_time = datetime.now()

    priority = random.choice(priorities)
    status = random.choice(statuses)

    # Define an SLA target based on priority
    sla_hours = {
        "P1 - Critical": 4,
        "P2 - High": 8,
        "P3 - Medium": 24,
        "P4 - Low": 72
    }

    # Generate creation times based on incident status
    if status in ["Resolved", "Closed"]:
        # Completed incidents can be older
        created_at = current_time - timedelta(
            days=random.randint(1, 180),
            hours=random.randint(0, 23)
        )
    else:
        # Unresolved incidents range from recent to 5 days old
        created_at = current_time - timedelta(
            hours=random.randint(0, 120)
        )

    # Calculate the SLA deadline
    sla_due_at = created_at + timedelta(
        hours=sla_hours[priority]
    )

    # Generate a valid resolution time for completed incidents
    if status in ["Resolved", "Closed"]:
        elapsed_hours = int(
            (current_time - created_at).total_seconds() / 3600
        )

        resolution_hours = random.randint(
            1,
            min(96, elapsed_hours)
        )

        resolved_at = created_at + timedelta(
            hours=resolution_hours
        )
    else:
        resolved_at = None


    incident = {
        "incident_id": f"INC{100000 + number}",
        "short_description": random.choice(descriptions[category]),
        "priority": priority,
        "category": category,
        "status": status,
        "support_group": support_groups[category],
        "created_at": created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "resolved_at": (
            resolved_at.strftime("%Y-%m-%d %H:%M:%S")
            if resolved_at else ""
        ),
        "sla_due_at": sla_due_at.strftime("%Y-%m-%d %H:%M:%S")
    }

    

    incidents.append(incident)

with open("data/incidents.csv","w",newline="") as file:
    fieldnames = [
        "incident_id",
        "short_description",
        "priority",
        "category",
        "status",
        "support_group",
        "created_at",
        "resolved_at",
        "sla_due_at"
    ]
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(incidents)
print("Incidents data saved to incident.csv")

with open("data/incidents.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    rows = list(reader)

print("Total incident records:", len(rows))
print("First incident:", rows[0])

# Data quality checks

incident_ids = [row["incident_id"] for row in rows]

required_fields = [
    "incident_id",
    "short_description",
    "priority",
    "category",
    "status",
    "support_group"
]

missing_values = 0

for row in rows:
    for field in required_fields:
        if not row[field].strip():
            missing_values += 1

print("Total records:", len(rows))
print("Unique incident IDs:", len(set(incident_ids)))
print("Missing required values:", missing_values)