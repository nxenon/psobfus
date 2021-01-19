# PSobfus
[![Tool Category](https://badgen.net/badge/Tool/Obfuscator/black)](https://github.com/nxenon/psobfus)
[![Python Version](https://badgen.net/badge/Python/3.x/blue)](https://www.python.org/download/releases/3.0/)
[![License](https://badgen.net/badge/License/GPLv2/purple)](https://github.com/nxenon/psobfus/blob/master/LICENSE)

**PSobfus** is a tool for obfuscating Powershell codes with Base64 encoding method.
 
Installation
----

    git clone https://github.com/nxenon/psobfus.git
    cd psobfus

Usage
----

    python3 psobfus.py --file your_ps_script.ps1

- Then it creates a new file ---> **your_ps_script_obfuscated.ps1**
  

- Then you can run new script by executing : `powershell .\your_ps_script_obfuscated.ps1`