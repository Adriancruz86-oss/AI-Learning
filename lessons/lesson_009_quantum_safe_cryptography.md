Lesson 009: Quantum-Safe Cryptography

Overview

Quantum-safe cryptography, also called post-quantum cryptography, is designed to protect data against attacks from future quantum 
computers.

The goal is not to make encryption impossible to break.

The goal is to use mathematical problems that remain impractical to solve, even with quantum computing.

Why Quantum Computing Matters

Modern computers process information using bits.

A bit is either:

0 or 1

Quantum computers use quantum bits, called qubits.

Qubits can represent combinations of states and can be used by certain algorithms to solve specific problems much faster than 
traditional computers.

Quantum computers are not automatically faster at every task.

Their advantage applies mainly to certain mathematical problems.

Current Public-Key Cryptography

Much of modern internet security relies on public-key cryptography.

Common examples include:

RSA

Diffie-Hellman

Elliptic-curve cryptography

These systems rely on mathematical problems that are extremely difficult for traditional computers to reverse.

Examples include:

Factoring very large numbers

Solving discrete logarithm problems

Shor’s Algorithm

Shor’s algorithm is a quantum algorithm that could efficiently solve some of the mathematical problems used by current public-key 
cryptography.

A sufficiently powerful quantum computer could threaten:

RSA encryption

RSA digital signatures

Diffie-Hellman key exchange

Elliptic-curve cryptography

This does not mean all encryption would immediately become useless.

Symmetric encryption and hashing are affected differently.

Symmetric Encryption

Symmetric encryption uses the same secret key for encryption and decryption.

Examples include:

AES-128

AES-256

Quantum computers may reduce the effective security strength of symmetric keys through Grover’s algorithm.

A simplified view is:

AES-128 may offer roughly 64-bit resistance against an ideal quantum search.
AES-256 may offer roughly 128-bit resistance.

This is one reason AES-256 is commonly considered a strong option for long-term protection.

Hashing

Hash functions create fixed-size outputs from data.

Examples include:

SHA-256

SHA-3

Quantum search may reduce the effective resistance of some hash functions, but it does not completely break them in the same way 
Shor’s algorithm threatens RSA.

Longer hash outputs can provide additional protection.

Post-Quantum Cryptography

Post-quantum cryptography uses algorithms designed to run on normal computers while resisting both classical and quantum attacks.

Major approaches include:

Lattice-based cryptography

Hash-based cryptography

Code-based cryptography

Multivariate cryptography

Isogeny-based cryptography

Not every proposed approach has proven secure.

Some candidates have been broken during public research and testing.

Lattice-Based Cryptography

Lattice-based cryptography relies on difficult mathematical problems involving points in high-dimensional spaces.

These problems are believed to be hard for both traditional and quantum computers.

Lattice-based methods are commonly used for:

Key establishment

Encryption

Digital signatures

Hash-Based Signatures

Hash-based signatures rely primarily on secure hash functions.

They are considered well understood and conservative from a security standpoint.

Their limitations may include:

Larger signature sizes

Larger keys

State-management requirements in some designs

Cryptographic Migration

Organizations cannot wait until a powerful quantum computer exists before beginning migration.

Cryptographic systems are deeply embedded in:

Operating systems

Applications

Certificates

VPNs

Cloud platforms

Network devices

Embedded systems

Long-lived hardware

Replacing cryptography across a large organization may take years.

Harvest Now, Decrypt Later

An attacker may collect encrypted data today and store it.

The attacker may attempt to decrypt it later when better tools or quantum computers become available.

This matters for data that must remain confidential for many years, such as:

Government information

Medical records

Financial records

Intellectual property

Authentication secrets

Crypto Agility

Crypto agility is the ability to replace cryptographic algorithms without rebuilding an entire system.

A crypto-agile system should make it easier to:

Change algorithms

Replace certificates

Increase key sizes

Rotate keys

Update protocols

Disable weak cryptography

Hard-coding one algorithm throughout an application makes future migration more difficult.

Hybrid Cryptography

Hybrid cryptography combines a traditional algorithm with a post-quantum algorithm.

For example, a system may derive a shared secret using both:

A traditional elliptic-curve method

A post-quantum key-establishment method

The combined system may remain secure if at least one of the methods remains secure.

Hybrid deployment can reduce migration risk while new standards mature.

Implementation Risks

A mathematically secure algorithm can still be implemented badly.

Possible failures include:

Weak random-number generation

Incorrect key storage

Poor certificate validation

Side-channel leaks

Reused keys

Software bugs

Incorrect parameter choices

Downgrade attacks

Cryptography is only one part of a secure system.

Security+ Connection

These concepts relate to:

Symmetric encryption

Asymmetric encryption

Hashing

Key exchange

Digital signatures

Certificates

Public key infrastructure

Cryptographic attacks

Key management

Data confidentiality

Crypto agility

Key Takeaway

Quantum computers do not make all cryptography useless.

They create serious risks for some widely used public-key systems.

The practical defense is to:

Identify where cryptography is used.

Protect long-lived sensitive data.

Build crypto-agile systems.

Follow post-quantum standards.

Test migration before quantum attacks become practical.
