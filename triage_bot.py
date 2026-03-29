def display_header():
    print("+" + "-"*48 + "+")
    print("|        VIRTUAL MEDICAL TRIAGE ASSISTANT        |")
    print("|          Powered by Logic-Based AI             |")
    print("+" + "-"*48 + "+")
    print("\nINSTRUCTIONS: Please answer 'yes' or 'no' to help the")
    print("agent determine the urgency of the case.\n")

def get_input(prompt):
    while True:
        val = input(prompt).lower().strip()
        if val in ['yes', 'no', 'y', 'n']:
            return 'yes' if val in ['yes', 'y'] else 'no'
        print("Invalid input. Please type 'yes' or 'no'.")

def triage_agent():
    display_header()

    breath = get_input("Q1: Is there severe shortness of breath? ")
    chest  = get_input("Q2: Is the patient feeling heavy chest pain? ")
    fever  = get_input("Q3: Is the body temperature above 102°F (High)? ")
    cough  = get_input("Q4: Is there a persistent dry cough? ")
    fatigue = get_input("Q5: Is the patient experiencing extreme fatigue? ")

    if breath == 'yes' or chest == 'yes':
        # Critical priority - Life-threatening
        status = "CRITICAL (EMERGENCY)"
        action = "Dispatch Ambulance / Move to ICU immediately."
        priority_code = "RED"
    elif fever == 'yes' and fatigue == 'yes':
        # Urgent priority - Needs medical intervention
        status = "URGENT (ACUTE CARE)"
        action = "Schedule General Physician consultation within 4 hours."
        priority_code = "ORANGE"
    elif cough == 'yes' or fever == 'yes':
        # Standard priority - Monitoring required
        status = "NON-URGENT (OBSERVATION)"
        action = "Recommend home isolation and paracetamol. Re-check in 24h."
        priority_code = "YELLOW"
    else:
        # Lowest priority - Minor or no issues
        status = "STABLE (ROUTINE)"
        action = "No immediate threat. Continue standard hydration and rest."
        priority_code = "GREEN"

    print("\n" + "="*50)
    print(f" FINAL DIAGNOSIS: {status}")
    print(f" PRIORITY COLOR : {priority_code}")
    print(f" DIRECTIVE     : {action}")
    print("="*50)
    print("\nDISCLAIMER: This is an AI simulation and not a substitute")
    print("for professional medical advice.")

if __name__ == "__main__":
    triage_agent()
