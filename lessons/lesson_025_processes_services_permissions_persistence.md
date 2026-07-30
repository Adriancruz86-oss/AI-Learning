# Lesson 025: Processes, Services, Permissions, and Persistence

## Overview

This lesson connects basic operating-system behavior to common cybersecurity risks.

The main concepts are:

- Processes and services
- Privileges and least privilege
- Service accounts
- Weak service permissions
- Unquoted service paths
- Persistence and lateral movement
- Evidence versus inference during an investigation

## Programs and Processes

A program is code stored on disk.

A process is a running instance of that program in memory.

One program may create several processes. Each process can have its own:

- Process ID
- Memory space
- Permissions
- Open files
- Network connections
- Parent and child processes

Security teams examine processes because malicious behavior must execute somewhere.

## Services

A service is a process designed to perform background work, usually without direct user interaction.

Examples include:

- Antivirus services
- Backup services
- Print services
- Web servers
- Update services

All services are processes, but not all processes are services.

Services are especially important in security because they may:

- Start automatically
- Run even when no user is signed in
- Operate with elevated privileges
- Provide persistence after a reboot

## Privilege and Kernel Access

A service running as `SYSTEM` on Windows or `root` on Linux may have extensive authority.

It may be able to:

- Modify protected files
- Change system settings
- Access other users' data
- Start or stop services
- Install software
- Create accounts

High privilege does not automatically mean direct kernel access. Most privileged services still operate in user mode and ask the operating system to perform authorized actions.

Kernel-level access normally involves drivers, kernel modules, or exploitation of a kernel vulnerability.

## Least Privilege

Least privilege means giving a user, process, or service only the access required for its assigned task.

A service that only checks printer status should not run with full control of the computer.

Excessive privilege increases the damage caused by:

- A software bug
- A stolen credential
- A vulnerable service
- Malicious code running through the service

The goal is:

```text
Required task: Check printer status
Granted access: Printer-related resources only
```

## Service Accounts

A service account is an identity created for software or background services rather than for a person.

Examples include accounts used by:

- Backup software
- Databases
- Web servers
- Monitoring systems

Common risks include:

- Excessive permissions
- Shared credentials
- Passwords that rarely change
- Interactive login rights
- Reuse across many servers

A service account should normally be restricted to its required function. It should not be used for email, web browsing, workstation sign-in, or unrelated administration.

## Credential Reuse and Lateral Movement

Using the same service-account credential across many servers increases the blast radius of a compromise.

If one server exposes the credential, an attacker may use it to access other servers.

```text
One stolen credential
        ↓
Authentication to several systems
        ↓
Lateral movement across the network
```

Safer designs use unique or managed service identities and restrict where each account may authenticate.

## Weak Service Permissions

A service may be legitimate while its surrounding permissions are insecure.

Example:

- A backup service runs as `SYSTEM`.
- A regular user can replace its executable file.
- An attacker compromises that user account.
- The attacker replaces the executable with malicious code.
- The service restarts and launches the replacement as `SYSTEM`.

This creates a privilege-escalation path because a low-privilege user can modify something that a high-privilege service trusts and executes.

Defenders should check who can modify:

- The service executable
- The executable's folder
- The service configuration
- The account under which the service runs

## Unquoted Service Paths

A file path is the complete location of a file.

Example:

```text
C:\Program Files\Backup Tools\backup service.exe
```

Because the path contains spaces, the full path should be placed inside quotation marks:

```text
"C:\Program Files\Backup Tools\backup service.exe"
```

Without quotes, Windows may test shorter possible executable names while interpreting the path.

An attacker who can place a malicious executable in one of those earlier locations may cause the privileged service to launch the wrong file.

This risk requires more than spaces alone. The dangerous combination is:

```text
Privileged service + unquoted path + attacker-writable location
```

## Services as Persistence

An attacker may create or modify a service so malicious code starts automatically.

Possible warning signs include:

- A recently created service
- A legitimate-looking but unfamiliar name
- An executable stored in a user-writable folder
- Automatic startup
- Execution as `SYSTEM` or `root`
- Unexpected network connections
- Unusual child processes

A convincing name does not prove a service is legitimate.

Defenders should examine:

- Full executable path
- Digital signature and publisher
- Creation and modification times
- Service account
- Startup type
- Process behavior
- Network activity
- Whether the service exists in the approved baseline

## Investigate Before Removing

An unfamiliar service should not automatically be deleted.

It may be:

- A critical operating-system component
- Required business software
- Part of authentication, backups, or monitoring
- Evidence needed for incident analysis

A safer response sequence is:

1. Identify the service and its properties.
2. Validate it against known-good records and expected behavior.
3. Contain the threat if it is actively dangerous.
4. Preserve relevant evidence.
5. Eradicate confirmed malicious components.
6. Recover and verify normal operation.

Containment limits damage. Eradication removes the threat. Recovery restores normal operations.

## Evidence Versus Inference

An analyst must separate what the evidence proves from what it merely suggests.

For example, an unfamiliar process that connects to the internet and launches commands may suggest command-and-control activity or data theft.

It does not prove exfiltration without supporting evidence such as:

- Sensitive files being accessed
- Archives being created
- Large or unusual outbound transfers
- Commands that upload data
- Confirmed transfer records

A strong investigation tells the story by asking:

```text
What is it?
Why is it here?
Who created or changed it?
What permissions does it have?
What has it done?
Is that behavior expected?
```

## Example Attack Chain

1. An attacker compromises a normal user or workstation.
2. The attacker obtains a reused service-account credential.
3. The credential works on several servers.
4. The attacker uses it for lateral movement.
5. A weak permission or vulnerable service on one server allows privilege escalation.
6. The attacker creates a fake automatic service running as `SYSTEM`.
7. The service provides persistence after reboot.
8. A legitimate-looking name helps the service avoid casual attention.

## Security+ Connections

This lesson reinforces:

- Least privilege
- Account management
- Credential security
- Privilege escalation
- Persistence
- Lateral movement
- Misconfiguration
- Indicators of compromise
- Incident response
- Containment, eradication, and recovery

## Key Takeaway

A service is not suspicious merely because it runs in the background, and it is not safe merely because its name or path looks legitimate.

Security comes from examining the complete story:

- What runs
- Where it runs from
- Which identity runs it
- What that identity can access
- Who can modify it
- How it starts
- What behavior it produces

One indicator creates a question. Multiple related indicators create an evidence-backed attack narrative.
