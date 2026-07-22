import base64
import os
from datetime import datetime

# ==========================================
# 1. ENCODING MODULES
# ==========================================

def encode_base64(payload: str) -> str:
    """Encodes string to Base64."""
    encoded_bytes = base64.b64encode(payload.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def encode_xor(payload: str, key: int = 0x5A) -> str:
    """Encodes string using a single-byte XOR key."""
    xor_chars = [chr(ord(c) ^ key) for c in payload]
    return "".join(xor_chars)

def encode_rot13(payload: str) -> str:
    """Encodes string using ROT13 substitution cipher."""
    chars = []
    for c in payload:
        if 'a' <= c <= 'z':
            chars.append(chr((ord(c) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= c <= 'Z':
            chars.append(chr((ord(c) - ord('A') + 13) % 26 + ord('A')))
        else:
            chars.append(c)
    return "".join(chars)

# ==========================================
# 2. OBFUSCATION MODULES
# ==========================================

def obfuscate_split(payload: str) -> str:
    """Splits string into concatenated chunks."""
    return " + ".join([f"'{char}'" for char in payload])

def obfuscate_reverse(payload: str) -> str:
    """Reverses the string payload."""
    return payload[::-1]

def obfuscate_junk_insertion(payload: str, delimiter: str = "@") -> str:
    """Inserts a non-functional delimiter between characters."""
    return delimiter.join(list(payload))

# ==========================================
# 3. SIMULATED EVASION DETECTION ENGINE
# ==========================================

SIGNATURE_DATABASE = [
    "powershell", 
    "cmd.exe", 
    "exec", 
    "system", 
    "downloadstring", 
    "invoke-expression",
    "bypass",
    "virtualalloc",
    "kernel32",
    "add-type"
]

def simulate_detection(payload: str) -> bool:
    """
    Simulates signature-based detection rule.
    Returns True if detected (signature matched), False if bypassed.
    """
    lowered_payload = payload.lower()
    for signature in SIGNATURE_DATABASE:
        if signature in lowered_payload:
            return True
    return False

# ==========================================
# 4. MAIN EXECUTION & REPORTING ENGINE
# ==========================================

def run_framework():
    print("==================================================")
    print(" CUSTOM PAYLOAD ENCODER & OBFUSCATION FRAMEWORK  ")
    print("==================================================")
    
    default_payload = "powershell.exe -ExecutionPolicy Bypass -Command Write-Host Hello"
    print(f"\nDefault Payload: {default_payload}")
    user_input = input("Enter custom payload (or press Enter to use default): ").strip()
    
    test_payload = user_input if user_input else default_payload

    print(f"\n[*] Target Payload: {test_payload[:80]}...")
    initial_detection = simulate_detection(test_payload)
    print(f"[*] Baseline Signature Status: {'[DETECTED]' if initial_detection else '[CLEAN]'}\n")

    # Generate obfuscation variations
    transformations = {
        "Base64 Encoding": encode_base64(test_payload),
        "ROT13 Encoding": encode_rot13(test_payload),
        "XOR Encoding (Key=0x5A)": encode_xor(test_payload, 0x5A),
        "String Splitting": obfuscate_split(test_payload),
        "Payload Reversal": obfuscate_reverse(test_payload),
        "Junk Character Insertion": obfuscate_junk_insertion(test_payload, "@")
    }

    report_lines = []
    report_lines.append("=" * 60)
    report_lines.append(" PAYLOAD ENCODING & OBFUSCATION AUDIT REPORT")
    report_lines.append(f" Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 60 + "\n")
    report_lines.append(f"Original Payload: {test_payload}")
    report_lines.append(f"Initial Status  : {'DETECTED' if initial_detection else 'CLEAN'}\n")
    report_lines.append("-" * 60)

    print("[+] Applying Transformations & Running Static Evasion Test:\n")
    
    bypassed_count = 0
    total_count = len(transformations)

    for name, result in transformations.items():
        is_detected = simulate_detection(result)
        status = "DETECTED" if is_detected else "BYPASSED"
        
        if not is_detected:
            bypassed_count += 1
            
        print(f"  [{status}] {name}")
        print(f"    └─ Transformed: {result[:60]}...\n")
        
        report_lines.append(f"Technique  : {name}")
        report_lines.append(f"Output     : {result}")
        report_lines.append(f"Detection  : {status}\n")

    bypass_rate = (bypassed_count / total_count) * 100
    summary = f"Summary: {bypassed_count}/{total_count} techniques successfully bypassed detection ({bypass_rate:.1f}% Bypass Rate)."
    
    print("-" * 50)
    print(f"[+] {summary}")

    report_lines.append("-" * 60)
    report_lines.append(summary)

    # Save to report file
    report_filename = "Obfuscation_Report.txt"
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"[+] Audit log saved to '{report_filename}'.")

if __name__ == "__main__":
    run_framework()