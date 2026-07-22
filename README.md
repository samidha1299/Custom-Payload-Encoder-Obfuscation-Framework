# Custom-Payload-Encoder-Obfuscation-Framework
Windows Payload Encoder & Obfuscation Framework

Automated Static Signature Evasion & Structural Mutation Toolkit

📌 Project Overview

The Custom Payload Encoder & Obfuscation Framework is a modular security utility designed to evaluate static signature detection mechanisms against mutated operational payloads. Operating as a Static Evasion Simulator, it accepts command-line payloads—including real-world execution scripts generated via msfvenom—applies multi-scheme encoding and structural string transformations, and tests them against a simulated static signature engine.

📌 Core Features

Multi-Scheme Encoding: Applies Base64, ROT13, and single-byte XOR (0x5A) encryption.
Structural Obfuscation: Mutates strings using character splitting, reversal, and junk delimiter insertion.
Simulated Evasion Engine: Tests transformed payloads against a database of flagged operational keywords.
Forensic Archiving: Calculates aggregate bypass rates and dumps execution reports to `Obfuscation_Report.txt`.

📌 Tested Transformation Modules

The system transforms raw inputs across six distinct obfuscation pipelines:
Base64 Encoding (Binary-to-text transformation).
ROT13 Substitution Cipher (Alphabetical rotation scheme).
Single-Byte XOR Encryption (Bitwise key masking using key 0x5A).
String Splitting & Concatenation (Fragmenting string literals).
Payload Reversal (Inverting string character sequence).
Junk Character Insertion (Interspersing non-functional `@` delimiters).

📌 Tech Stack

Language: Python 3.x
Standard Libraries: base64, datetime, os
Payload Generation Utility: msfvenom (Metasploit Framework on Kali Linux)
Verification Environments: Windows PowerShell, Command Prompt, Kali Linux Terminal.

📌 How To Run, Test, and Validate

1. Launch the Framework

cd D:\Project\Project_4
python payload_framework.py

2. Test Custom msfvenom Payload

Generate a sample payload in Kali Linux:
msfvenom -p windows/exec CMD=calc.exe -e cmd/powershell_base64 -f psh

Run the script in PowerShell and paste the single-line payload string when prompted.

3. Verify Forensic Output

Open `Obfuscation_Report.txt` to review execution timestamps, baseline detection status, transformed string samples, and the 100% bypass rate summary.
