def format_update(text):
    lines = [x.strip() for x in text.split(".") if x.strip()]

    completed = []
    current = []
    blockers = []

    for line in lines:
        low = line.lower()

        if any(k in low for k in ["completed", "finished", "done"]):
            completed.append(line)

        elif any(k in low for k in ["blocked", "waiting", "pending"]):
            blockers.append(line)

        else:
            current.append(line)

    output = "Progress Update\n\n"

    if completed:
        output += "Completed:\n"
        output += "\n".join([f"- {x}" for x in completed])
        output += "\n\n"

    if current:
        output += "Current Work:\n"
        output += "\n".join([f"- {x}" for x in current])
        output += "\n\n"

    if blockers:
        output += "Blockers:\n"
        output += "\n".join([f"- {x}" for x in blockers])

    return output
