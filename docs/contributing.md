---
layout: default
title: Contributing Guidelines
nav_order: 7
description: 'Guidelines and instructions for contributing to the Ebook Generator project'
permalink: /contributing
---

# Contributing to Ebook Generator

{: .no_toc }

Thank you for considering contributing to the Ebook Generator project! This document provides guidelines and instructions for contributing.
{: .fs-6 .fw-300 }

## Table of Contents

{: .no_toc .text-delta }

1. TOC
   {:toc}

---

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone. Please be considerate of differing viewpoints and experiences, and focus on what is best for the community.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment
4. Create a new branch for your feature or bugfix
5. Make your changes
6. Submit a pull request

## Development Environment

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup

1. Clone your fork of the repository:

   ```bash
   git clone https://github.com/your-username/novelforge-ai.git
   cd novelforge-ai
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up your `.env` file with your Gemini API key(s)

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use 4 spaces for indentation (no tabs)
- Maximum line length of 100 characters
- Use meaningful variable and function names
- Write docstrings for all functions, classes, and modules

### Documentation

- Update documentation when changing code functionality
- Document all new features
- Keep the README.md up to date

### Testing

- Write tests for new features
- Ensure all tests pass before submitting a pull request
- Maintain or improve test coverage

## Pull Request Process

1. Create a new branch for your feature or bugfix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

   or

   ```bash
   git checkout -b fix/issue-you-are-fixing
   ```

2. Make your changes and commit them with clear, descriptive commit messages:

   ```bash
   git commit -m "Add feature: description of the feature"
   ```

3. Push your branch to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

4. Submit a pull request to the main repository

5. Update the README.md or documentation with details of changes if appropriate

6. The pull request will be reviewed by maintainers who may request changes or improvements

7. Once approved, your pull request will be merged

## Feature Requests

If you have an idea for a new feature:

1. Check if the feature has already been suggested in the Issues section
2. If not, create a new issue with the label "enhancement"
3. Clearly describe the feature and its potential benefits
4. Discuss the feature with maintainers and the community

## Bug Reports

When reporting bugs:

1. Check if the bug has already been reported
2. Create a new issue with the label "bug"
3. Include:
   - A clear title and description
   - Steps to reproduce the bug
   - Expected behavior
   - Actual behavior
   - Screenshots if applicable
   - Your environment (OS, Python version, etc.)

## Development Workflow

1. **Choose an Issue**: Start by selecting an open issue to work on
2. **Discuss Approach**: Comment on the issue to discuss your planned approach
3. **Create Branch**: Create a branch with a descriptive name
4. **Implement Changes**: Make your code changes following the coding standards
5. **Write Tests**: Add tests for your changes
6. **Update Documentation**: Update relevant documentation
7. **Submit PR**: Create a pull request with a clear description of changes
8. **Address Feedback**: Respond to review comments and make necessary adjustments
9. **Merge**: Once approved, your PR will be merged

## Project Structure

Understanding the project structure will help you contribute effectively:

```
novelforge-ai/
├── docs/                       # Documentation
├── src/                        # Source code
│   ├── core/                   # Core functionality
│   ├── formatters/             # Output formatting
│   ├── ui/                     # User interface
│   └── utils/                  # Utilities
├── tests/                      # Test suite
├── .env.example                # Example environment file
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Project Maintainer

**Mosaddiq** - _Creator & Lead Developer_

- GitHub: [@mosadd1X](https://github.com/mosadd1X)
- Project: [NovelForge AI](https://github.com/mosadd1X/novelforge-ai)

For questions about contributing or project direction, feel free to open an issue or start a discussion on GitHub.

## Related Documentation

- [Development Setup](./development-setup.html): Detailed setup instructions
- [Code Style Guide](./code-style.html): Specific code style requirements
- [API Documentation](./api.html): Reference for the project's API

Thank you for contributing to the NovelForge AI project!
