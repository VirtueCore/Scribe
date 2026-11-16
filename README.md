# 🔎 Scribe — Domain WHOIS Lookup

[![Python 3](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![GPL-3.0 License](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![WHOIS](https://img.shields.io/badge/WHOIS-Domain%20Lookup-8A2BE2.svg)

Scribe is a Python-based terminal tool for retrieving domain registration information using the WHOIS library. It allows users to enter a domain name and displays the returned WHOIS information directly in the terminal.

## ✨ Features

- 🔎 **Domain Lookup:** Retrieve WHOIS information for an entered domain.
- 🔡 **Automatic Lowercase Conversion:** Converts domain input to lowercase before searching.
- 📋 **Formatted Output:** Displays returned WHOIS information as organized key-value pairs.
- 🎨 **Colored Terminal Output:** Uses ANSI escape sequences to distinguish information and messages.
- ⚠️ **Error Handling:** Handles WHOIS lookup errors and keyboard interruptions (`CTRL+C`).
- 🌐 **Lookup Reference:** Provides a link to [Whois.com](https://www.whois.com/) for additional domain information.

## 🛠️ Requirements

- Python 3
- Git
- `python-whois` library
- pip or [uv](https://docs.astral.sh/uv/)

## 📥 Installation

### 1. Clone the Repository

Choose the instructions for your operating system.

**🐧 Linux**

Open a terminal and execute:

```bash
git clone https://github.com/VirtueCore/Scribe.git
cd Scribe
```

**🪟 Windows**

Open Command Prompt or PowerShell and execute:

```powershell
git clone https://github.com/VirtueCore/Scribe.git
cd Scribe
```

**🍎 macOS**

Open Terminal and execute:

```bash
git clone https://github.com/VirtueCore/Scribe.git
cd Scribe
```

### 2. Install Dependencies

Install the required Python library using either pip or uv.

**Using pip:**

```bash
pip install python-whois
```

**Using uv:**

```bash
uv add python-whois
```

## 🚀 Usage

Run Scribe from the cloned repository directory.

**Using Python:**

```bash
python scribe.py
```

**Using uv:**

```bash
uv run scribe.py
```

Enter the domain name when prompted:

```text
Domain 💪: google.com
```

Scribe retrieves the WHOIS information and displays the returned fields in the terminal.

## 📸 Example Output

```text
Domain Name: google.com 📢

Registrar: Example Registrar 📢

Creation Date: 1997-09-15 📢

Expiration Date: 2028-09-14 📢
```

*Actual output depends on the WHOIS information returned for the queried domain.*

## ⚠️ Error Handling

| Condition | Behavior |
|---|---|
| WHOIS lookup error | Displays a message asking the user to enter a valid domain. |
| Keyboard interruption (`CTRL+C`) | Displays a termination message before exiting. |

## ❓ FAQ

**1. What is Scribe used for?**

Scribe retrieves publicly available domain registration information through WHOIS lookups.

**2. What information does Scribe retrieve?**

It displays the information returned by the WHOIS library, which can include domain registration details such as registrar, creation date, and expiration date.

**3. Do I need to install anything before running Scribe?**

Yes. You need Python 3, Git, and the `python-whois` library. You can install the library using either pip or uv.

**4. Can I use Scribe on different operating systems?**

Scribe is a Python terminal script and can be run on Linux, Windows, and macOS. Terminal support for ANSI colors may vary depending on the environment.

**5. Where can I find additional domain information?**

Visit [Whois.com](https://www.whois.com/) for additional information about a queried domain.

## 📜 License

Scribe is distributed under the **GNU General Public License v3.0 (GPL-3.0)**.

See the [GNU GPL v3.0](https://github.com/VirtueCore/Scribe/blob/main/LICENSE) for license details.
