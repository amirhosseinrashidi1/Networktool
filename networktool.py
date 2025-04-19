import tkinter as tk
import subprocess

# Commands that do not require root
commands = {
    "Ping address": "ping -c 4 {target}",  # Windows: change to -n
    "WHOIS domain info": "whois {target}",
    "DNS lookup (nslookup)": "nslookup {target}",
    "Traceroute": "traceroute {target}",  # Windows: change to tracert
    "Get public IP": "curl ifconfig.me"
}

def run_command():
    selected = listbox.get(listbox.curselection())
    target = entry.get().strip()

    if "{target}" in commands[selected] and not target:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a target (IP address or domain).")
        return

    command_template = commands[selected]
    command = command_template.format(target=target)

    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        result = f"Error:\n{e.output}"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"$ {command}\n\n{result}")

# GUI setup
window = tk.Tk()
window.title("Network Tool")
window.geometry("700x550")

# Input field
tk.Label(window, text="Enter IP address or domain (if required):").pack()
entry = tk.Entry(window, width=50)
entry.pack(pady=5)

# Command selection
listbox = tk.Listbox(window, width=50, height=7)
for cmd in commands:
    listbox.insert(tk.END, cmd)
listbox.pack(pady=10)

# Run button
btn = tk.Button(window, text="Run Command", command=run_command)
btn.pack(pady=5)

# Output area
output_text = tk.Text(window, wrap="word", height=20, width=80)
output_text.pack(padx=10, pady=10)

window.mainloop()
