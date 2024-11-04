# API Security Testing and Evaluation Using SoapUI

| Course       | Course Name            | Professor    | Semester  |
| ------------ | ---------------------- | ------------ | --------- |
| CPSC 542     | Verification & Validation | Neeraj Gupta | Fall 2024 |

## Developers:
| Name                         | Email                          |
| ---------------------------- | ------------------------------ |
| Erwin Medina                 | erwinmedina@csu.fullerton.edu  |
| Angel Santoyo                | asantoyo@csu.fullerton.edu |
| Kaayva Varshitha Raman Shantha | {insert} |

## About This Project
This project aims to demonstrate and refine API security testing techniques using SoapUI, an open-source testing tool. By integrating SoapUI into our testing workflow, we focus on identifying and mitigating security vulnerabilities in web applications that utilize JSON Web Tokens (JWT) for authentication. The project encompasses creating a series of automated tests that evaluate the security, reliability, and robustness of a Flask-based web service designed to handle secure authentication and data handling.

## Objectives
- **Security Testing**: Leverage SoapUI to conduct thorough security assessments, including testing for common vulnerabilities outlined by the OWASP Top 10, such as SQL injection, XSS, and improper authentication handling.
- **Functional Testing**: Validate that all API endpoints perform expected functions under various conditions and handle errors gracefully.
- **Load and Performance Testing**: Analyze how the application performs under stress, using SoapUI to simulate high traffic and data load.
- **Mocking and Service Virtualization**: Implement mocks for external services to test the API in isolation, ensuring functionality is preserved even when external dependencies are not available.

## Languages / Frameworks Used
- Python
- Flask
- JWT (JSON Web Tokens)
- SoapUI 

## Key Documents
- [Progress Report](https://docs.google.com/document/d/19PD9qQ1MrDe3q04viIqkm0AUrVoqBNzupTVlvp7JMy8/edit?tab=t.0)
- [Presentation Slide Deck](https://docs.google.com/presentation/d/1BOiDA0U-Q0WbjOpwfiXQamYEvvKAoWZNx4SG4HT7_sE/edit?usp=sharing)
- [Final Report]()
- [pyJWT GitHub Repository](https://github.com/jpadilla/pyjwt)

## Getting Started
To get started with this project, clone the repository and ensure all dependencies listed in `requirements.txt` are installed. Follow the setup instructions in instructions.md 

## Usage
Details on how to run tests using SoapUI are available in `TESTING.md`. This includes step-by-step instructions for setting up test suites, cases, and security scenarios within SoapUI.

## Contribution
We welcome contributions from the community. Please refer to `CONTRIBUTING.md` for guidelines on how to submit issues, feature requests, and patches.

## License
This project is open-sourced under the MIT license. See [LICENSE](LICENSE.md) for more details.
