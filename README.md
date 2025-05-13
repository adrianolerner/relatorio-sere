
# 🧾 Gerador de Relatórios do SERE (SEED - Secretaria de Estado de Educação do Paraná) via API - Interface Gráfica em Python

Este projeto é uma aplicação gráfica simples, leve e funcional desenvolvida em **Python** com **Tkinter**. Seu objetivo é automatizar a conexão com a API do sistema SERE da SEED (Secretaria de Estado da Educação do Paraná) via token, baixar relatórios em formato **JSON** e convertê-los para **CSV** e **XLSX**, salvando os arquivos em um local especificado pelo usuário.

## 📌 Funcionalidades

- Seleção do ano do relatório (2023 até 2030)
- Escolha do diretório de destino para os arquivos
- Baixa os dados diretamente da API
- Salva o JSON original para auditoria e backup
- Converte os dados em arquivos `.csv` e `.xlsx`
- Interface gráfica amigável e fácil de usar

---

## 🧰 Requisitos

- Python 3.9 ou superior
- Conexão com a internet
- Sistema Operacional: Windows 11 ou Linux

---

## 💻 Instalação do Python

### ✅ Windows

1. Acesse o site oficial: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Baixe o instalador.
3. **Importante**: Marque a opção `Add Python to PATH` durante a instalação.
4. Clique em "Install Now".

### ✅ Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

---

## 📦 Instalação das Bibliotecas (caso já não estejam instaladas)

No terminal (ou Prompt de Comando), execute:

```bash
pip install requests openpyxl pandas tkinter tempfile json
```

---

## ⚙️ Configuração do Script

Abra o arquivo Python principal (`relatorio_gui.py` ou outro nome que tenha salvo) e edite estas duas linhas no início do código:

```python
API_URL = "https://sua.api.com.br/endpoint"
API_TOKEN = "seu_token_aqui"
```

**Substitua**:
- `https://sua.api.com.br/endpoint` pela URL da API.
- `"seu_token_aqui"` pelo seu token pessoal de autenticação.

---

## ▶️ Como Executar

### Via terminal:

```bash
python relatorio_gui.py
```

---

## 📦 Gerando um Executável no Windows

Para criar um executável `.exe`, use o [PyInstaller](https://pyinstaller.org/).

### 1. Instale o PyInstaller:

```bash
pip install pyinstaller
```

### 2. Gere o executável:

```bash
pyinstaller --noconsole --onefile relatorio_gui.py
```

- O arquivo gerado estará na pasta `dist/` com o nome `relatorio_gui.exe`.
- O parâmetro `--noconsole` oculta o terminal (para uso com GUI).
- O parâmetro `--onefile` empacota tudo em um único executável.

---

## 📁 Estrutura de Arquivos

```
projeto-relatorio/
├── relatorio_gui.py
├── parcial.json (opcional para testes)
├── README.md
└── dist/
    └── relatorio_gui.exe (após gerar com PyInstaller)
```

---

## 🛠 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Requests](https://docs.python-requests.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/)
- [PyInstaller](https://pyinstaller.org/)

---

## ✍️ Autor

**Seu Nome Aqui**  
Desenvolvido para automação de geração de relatórios a partir de APIs REST.  

---

## 📝 Licença

Este projeto é de código aberto e está sob a licença [MIT](LICENSE).
