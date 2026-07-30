# Lesson 006: Security Attack Lifecycle

## Overview

This lesson covers three major stages commonly discussed in cybersecurity:

- Payload
- Persistence
- Lateral movement

These concepts help explain what an attacker may do after gaining initial access to a system.

## Payload

A payload is the part of an attack that performs the intended action.

Examples include:

- Opening a remote shell
- Encrypting files
- Stealing credentials
- Downloading additional malware
- Creating a new user account

The exploit gets the attacker through the door. The payload performs the action after entry.

## Persistence

Persistence is how an attacker maintains access after a reboot, logout, password change, or temporary interruption.

Common persistence methods include:

- Startup programs
- Scheduled tasks
- Services
- Registry changes
- New administrator accounts
- Modified login scripts
- Malicious browser extensions

Defenders should investigate how access was maintained, not only how the attacker entered.

## Lateral Movement

Lateral movement occurs when an attacker moves from one system or account to another inside a network.

Examples include:

- Using stolen credentials
- Connecting through Remote Desktop
- Accessing shared folders
- Exploiting another internal computer
- Using administrative tools such as PowerShell
- Moving from a user workstation to a server

The attacker’s first compromised machine may only be a stepping stone toward more valuable systems.

## Example Attack Flow

1. An attacker sends a phishing email.
2. The victim opens a malicious attachment.
3. The payload creates a remote connection.
4. The attacker creates persistence with a scheduled task.
5. Credentials are stolen from the compromised computer.
6. The attacker uses those credentials to access another machine.
7. The attacker eventually reaches a valuable server.

## Security+ Connection

These concepts relate to:

- Indicators of compromise
- Malware behavior
- Incident response
- Credential attacks
- Privilege escalation
- Network segmentation
- Endpoint detection and response
- Least privilege

## Key Takeaway

Initial access is only the beginning of an attack.

A complete investigation should determine:

- How the attacker entered
- What the payload did
- How access was maintained
- Whether other systems were reached
- What data or resources were affected
