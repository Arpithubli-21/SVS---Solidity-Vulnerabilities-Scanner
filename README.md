# SVS---Solidity-Vulnerabilities-Scanner
A Solidity Vulnerability Scanner is a web-based security tool that analyzes Solidity smart contracts to detect vulnerabilities using 37 SWC-based rules. It scans uploaded or pasted code, identifies security issues, classifies them by severity, and provides recommendations to help developers secure smart contracts before deployment.


🚀 Project Overview

Smart contracts are immutable once deployed to a blockchain. Any vulnerability in the contract logic can lead to loss of funds, exploits, or contract takeover.

This project provides an automated vulnerability detection system that analyzes Solidity source code and identifies common smart contract security issues using rule-based pattern matching.

The scanner processes the contract code, detects vulnerable patterns, classifies them based on severity, and generates a structured security report including:

Vulnerability type

SWC ID

Severity level

Line numbers where the vulnerability occurs

Recommended mitigation steps

This tool helps developers identify and fix security flaws early in the development process.


🖥️ User Interface

The project provides a modern web interface designed for easy interaction and quick security analysis.

Landing Page

The homepage introduces the Solidity Vulnerability Scanner and highlights its capabilities.

Key information displayed:

37 vulnerability detection rules

SWC registry coverage

Three severity levels (High, Medium, Low)

This gives users a quick understanding of the tool's detection capability.


Smart Contract Analysis

Users can analyze Solidity code in two ways:

1️⃣ Upload a Solidity File

Users can upload a .sol file directly from their system.

Features include:

Drag and drop support

File browser selection

Maximum file size limit of 10 MB

Once the file is uploaded, the scanner processes the contract and runs vulnerability detection.

2️⃣ Paste Solidity Code

Developers can also paste Solidity code directly into the editor.

The interface provides:

Syntax-styled code input area

Character counter

Clear button for quick reset

After pasting the code, users can click Scan Pasted Code to start the analysis.

🔎 Vulnerability Detection Engine

The backend scanner analyzes the Solidity source code using pattern-based static analysis.

The scanning engine performs the following steps:

Reads the Solidity source code line by line.

Compares each line against predefined vulnerability rules.

Detects matching patterns using regular expressions.

Records the line number and vulnerable code snippet.

Categorizes the vulnerability by severity.

The system currently supports 37 SWC vulnerability rules, covering the range:

SWC-100 → SWC-136

These vulnerabilities are categorized into three severity levels.

🔴 High Severity Vulnerabilities

High severity vulnerabilities represent critical security risks that could allow attackers to steal funds or gain full control over the contract.

Examples detected by the scanner include:

Integer Overflow / Underflow

Unprotected Ether Withdrawal

Unprotected Self-Destruct

Reentrancy

Uninitialized Storage Pointer

Delegatecall to Untrusted Callee

tx.origin Authentication

Incorrect Constructor Name

Weak Randomness

Signature Replay Attack

Arbitrary Storage Write

Arbitrary Jump via Function Variable

RLO Hidden Character Attack

Private Data Stored On-Chain

🟡 Medium Severity Vulnerabilities

Medium severity vulnerabilities can cause unexpected behavior, denial of service, or security weaknesses if exploited.

Examples include:

Function Default Visibility

Outdated Compiler Version

Unchecked Call Return Value

Assert Violation

DoS with Failed Call

Transaction Order Dependence

Block Timestamp Dependence

Signature Malleability

Shadowing State Variables

Improper Signature Verification

Requirement Violation

Incorrect Inheritance Order

Insufficient Gas Griefing

DoS with Block Gas Limit

Unexpected Ether Balance

Hash Collision using encodePacked

Hardcoded Gas Amount

🟢 Low Severity Issues

Low severity findings generally represent best practice violations or code quality issues.

Examples include:

Floating Pragma

State Variable Default Visibility

Deprecated Solidity Functions

Typographical Errors

Unused Variables

Code With No Effects

🛠️ Technologies Used


Backend - Python

Web Framework - Flask

Vulnerability Detection - Regex-based rule engine

Frontend - HTML

Styling - CSS

Security Standard - SWC Registry
