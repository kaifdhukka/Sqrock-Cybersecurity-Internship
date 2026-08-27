def generate_se_script(target_company, attacker_role, pretext, scenario_type):
    if scenario_type == "IT":
        script = f"""
==================================================
  VISHING AWARENESS SIMULATION SCRIPT: IT SUPPORT
==================================================
Caller Role  : {attacker_role}
Target Org   : {target_company}
Pretext      : {pretext}

[OPENER]
"Hi, this is Alex from {target_company} IT Support. We detected unusual security alerts on your employee account."

[HOOK / URGENCY]
"We are resetting compromised tokens right now. Can you quickly confirm your employee ID and your current active password?"

[RED FLAGS FOR AWARENESS]
-> Legitimate IT will NEVER ask for plain-text passwords over the phone.
-> Triggers Used: Authority (IT Dept) + Scarcity/Urgency (Immediate lockout risk).
--------------------------------------------------"""

    elif scenario_type == "BANK":
        script = f"""
==================================================
  VISHING AWARENESS SIMULATION SCRIPT: BANK FRAUD
==================================================
Caller Role  : {attacker_role}
Target Org   : {target_company}
Pretext      : {pretext}

[OPENER]
"Good day, I am calling from the Fraud Prevention Division at {target_company}."

[HOOK / FEAR]
"An unauthorized transaction of $1,250 was just attempted from your account in another location. To block this payment immediately, please read out the 6-digit OTP sent to your phone."

[RED FLAGS FOR AWARENESS]
-> Banks never ask for OTPs or PINs to cancel transactions.
-> Triggers Used: Fear (Financial loss) + Urgency (Preventing transfer).
--------------------------------------------------"""

    elif scenario_type == "GOV":
        script = f"""
==================================================
  SMISHING/VISHING SCRIPT: GOV / TAX AUTHORITIES
==================================================
Caller Role  : {attacker_role}
Target Org   : {target_company}
Pretext      : {pretext}

[OPENER]
"[ALERT] {target_company} Legal Notice: Immediate action required regarding unpaid tax audit penalties."

[HOOK / AUTHORITY]
"Failure to verify your identity and settle overdue compliance charges within 2 hours will result in legal escalation and account freeze."

[RED FLAGS FOR AWARENESS]
-> Government agencies do not demand immediate phone payments or secret credential verification via SMS/calls.
-> Triggers Used: Extreme Authority + Fear of Legal Penalties.
--------------------------------------------------"""

    return script


# Generating 3 unique scripts for awareness training
scenarios = [
    ("Sqrock Corp", "IT Helpdesk Specialist", "Password Expiry Audit", "IT"),
    ("Global Bank", "Fraud Prevention Officer", "Unauthorized Wire Transfer", "BANK"),
    (
        "Internal Revenue Dept",
        "Tax Compliance Officer",
        "Overdue Audit Fine",
        "GOV",
    ),
]

for company, role, pretext, s_type in scenarios:
    print(generate_se_script(company, role, pretext, s_type))