Lesson 010: Cryptography Fundamentals

Overview

Cryptography protects information by using mathematical techniques.

The main goals are:

Confidentiality

Integrity

Authentication

Non-repudiation

Different cryptographic tools solve different problems.

Encryption, hashing, and digital signatures are related, but they are not interchangeable.

Confidentiality

Confidentiality means preventing unauthorized people from reading information.

Encryption provides confidentiality by converting readable data into unreadable ciphertext.

Example:

Plaintext → Encryption → Ciphertext

Someone with the correct key can decrypt the ciphertext and recover the original plaintext.

Symmetric Encryption

Symmetric encryption uses the same secret key to encrypt and decrypt data.

Simplified flow:

Plaintext + Secret Key → Ciphertext
Ciphertext + Secret Key → Plaintext

Common symmetric algorithms include:

AES

ChaCha20

Symmetric encryption is generally fast and efficient.

It is commonly used for:

Full-disk encryption

File encryption

VPN traffic

Database encryption

Web-session data

Symmetric Encryption Challenge

Both parties need access to the same secret key.

This creates a key-distribution problem.

If the key is intercepted, an attacker may be able to decrypt the protected data.

The security of the encryption depends heavily on protecting the key.

Asymmetric Encryption

Asymmetric cryptography uses a key pair:

Public key

Private key

The public key can be shared.

The private key must remain secret.

Data encrypted with the public key can be decrypted with the corresponding private key.

Simplified flow:

Plaintext + Public Key → Ciphertext
Ciphertext + Private Key → Plaintext

Common asymmetric systems include:

RSA

Elliptic-curve cryptography

Asymmetric cryptography is slower than symmetric encryption, so it is usually not used to encrypt large amounts of data directly.

Hybrid Encryption

Many secure systems combine symmetric and asymmetric cryptography.

A common pattern is:

Asymmetric cryptography establishes or protects a temporary session key.

Symmetric encryption protects the actual data.

The temporary key is discarded or rotated after the session.

This combines:

The key-sharing advantages of asymmetric cryptography

The speed of symmetric encryption

HTTPS and many VPN systems use this general approach.

Hashing

A hash function converts input data into a fixed-size output called a hash or digest.

Example:

Input Data → Hash Function → Digest

Hashing is designed to be one-way.

You do not decrypt a hash to recover the original data.

Common hash functions include:

SHA-256

SHA-3

Older algorithms such as MD5 and SHA-1 should not be trusted for collision-resistant security.

Hash Properties

A secure cryptographic hash function should provide:

Deterministic Output

The same input should always produce the same hash.

Fixed-Length Output

A short file and a large file produce hashes of the same length when using the same algorithm.

Avalanche Effect

A small change in the input should create a dramatically different hash.

Preimage Resistance

Given a hash, it should be impractical to determine the original input.

Collision Resistance

It should be impractical to find two different inputs that produce the same hash.

Integrity Checking

Hashes can detect whether data has changed.

Example:

Calculate the hash of a file.

Transfer or store the file.

Calculate the hash again.

Compare the two hashes.

If the hashes differ, the file changed.

However, a plain hash does not prove who created the file.

An attacker who changes the file may also replace the published hash.

Password Hashing

Passwords should generally be stored as password hashes rather than plaintext.

Secure password-storage systems use specialized algorithms such as:

Argon2

bcrypt

scrypt

PBKDF2

These algorithms are intentionally slower than ordinary hashing functions.

That makes large-scale password guessing more expensive.

Salting Passwords

A salt is a random value added to a password before hashing.

Simplified example:

Password + Random Salt → Password Hash

Salts help prevent:

Identical passwords from producing identical stored hashes

Efficient use of precomputed rainbow tables

Immediate identification of users who share the same password

A salt does not need to be secret.

It should be unique and unpredictable.

Keyed Hashing

A keyed hash combines data with a secret key.

A common construction is an HMAC.

HMAC can provide:

Integrity

Authentication

It helps prove that the message came from someone who possessed the shared secret key and that the message was not altered.

Digital Signatures

Digital signatures use asymmetric cryptography.

The signer uses a private key.

The verifier uses the corresponding public key.

A simplified signing process is:

Hash the message.

Sign the hash using the private key.

Send the message and signature.

Verify the signature using the public key.

Digital signatures can provide:

Integrity

Authentication

Non-repudiation

They do not automatically provide confidentiality.

A digitally signed message may still be readable by anyone unless it is also encrypted.

Encryption Versus Hashing

Encryption is reversible with the proper key.

Hashing is intended to be one-way.

Use encryption when the original data must later be recovered.

Use hashing when you need to verify integrity, compare values, or protect passwords through a specialized password-hashing 
process.

Encryption Versus Encoding

Encoding changes the representation of data so another system can store or transmit it.

Examples include:

Base64

URL encoding

ASCII

UTF-8

Encoding is not encryption.

Base64 can be reversed without a secret key.

It should not be used to protect sensitive information.

Certificates

A digital certificate links a public key to an identity.

A certificate may identify:

A website

A person

A company

A server

A device

Certificates are commonly issued and signed by certificate authorities.

A certificate helps a user or system determine whether a public key belongs to the expected entity.

Public Key Infrastructure

Public key infrastructure, or PKI, manages:

Certificates

Certificate authorities

Public and private keys

Certificate validation

Certificate expiration

Certificate revocation

Trust relationships

PKI is used in:

HTTPS

Secure email

VPN authentication

Device authentication

Code signing

Enterprise identity systems

Key Management

Strong algorithms can fail if keys are managed poorly.

Key-management responsibilities include:

Secure generation

Secure storage

Access control

Rotation

Backup

Recovery

Revocation

Destruction

Private keys should not be stored in source-code repositories or sent through unsecured messages.

Common Cryptographic Failures

Examples include:

Hard-coded keys

Weak passwords used as keys

Reused initialization values

Expired certificates

Disabled certificate validation

Weak random-number generation

Outdated algorithms

Improper key storage

Keys exposed in logs

Encryption without integrity protection

Security+ Connection

These concepts relate to:

Data at rest

Data in transit

Data in use

Symmetric encryption

Asymmetric encryption

Hashing

Salting

Digital signatures

Certificates

Public key infrastructure

Key management

Non-repudiation

Authentication

Integrity

Confidentiality

Key Takeaway

Use the correct cryptographic tool for the correct purpose.

Encryption protects confidentiality.

Hashing helps verify integrity.

Password hashing protects stored passwords.

HMAC provides integrity and shared-secret authentication.

Digital signatures provide integrity and identity verification.

Certificates connect public keys to trusted identities.

Key management determines whether the entire system remains secure.
