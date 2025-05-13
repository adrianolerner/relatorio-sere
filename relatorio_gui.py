import requests
import tempfile
import json
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime

# === CONFIGURAÇÕES DA API ===
API_URL = "https://www.sere.pr.gov.br/sere/service/alunos/buscaPost/busca_exporta_dados_escola_json_castro/1"  # <-- Substitua pela URL da API (caso ela mude)
TOKEN = "seu_token_aqui"

# === BAIXAR O RELATÓRIO ===
def baixar_relatorio(ano):
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "token": TOKEN,
        "ano": ano
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()

        temp_dir = tempfile.gettempdir()
        temp_json_path = os.path.join(temp_dir, "relatorio.json")

        with open(temp_json_path, "w", encoding="utf-16") as f:
            f.write(response.text)

        return temp_json_path, response.text
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro de Conexão", f"Erro ao baixar o relatório:\n\n{str(e)}")
        return None, None

# === CONVERTER PARA CSV E XLSX ===
def converter_relatorio(json_path, destino_path, raw_json):
    try:
        with open(json_path, encoding='utf-16') as f:
            dados = json.load(f)

        if not isinstance(dados, list):
            raise ValueError("O relatório não está no formato esperado (lista de escolas).")

        campos_desejados = [
            "numchamada", "nummatricula", "cgmaluno", "datamatricula", "nomealuno", "datanasc",
            "indsexo", "descrracacor", "codracacor", "nomemae", "nomepai", "nomeresponsavel",
            "cpfaluno", "cpfpai", "cpfmae", "cpfresponsavel", "rgaluno", "ufrgaluno",
            "siglaorgaoemissor", "dataexpedicaorg", "numrgestrangeiro", "codigonis",
            "codtiponacionalidade", "zonaresaluno", "descrtiponacionalidade", "codnacionalidade",
            "descrnacionalidade", "codnaturalidade", "rgmae", "ufrgmae", "rgpai", "ufrgpai",
            "numcertidaonasc", "numfolhacertidaonasc", "numlivrocertidaonasc", "dataemissaocertidao",
            "matriculacertnasc", "fonecelaluno", "fonecelpai", "fonecelmae", "fonecelresponsavel",
            "indutilizatransporte", "bolsafamilia", "nomeNaturalidade", "ufNaturalidade",
            "codlocalidade", "nomelocalidade", "nomebairro", "nomelogradouro", "numend",
            "numcep", "complementoend", "ufendereco", "descrtipoidentgeo", "numidentgeo",
            "descrseriacaomultisseriado", "codseriacaoprincmultisseriado", "codseriacaosecmultisseriado",
            "codsituacaomatricula", "descrsituacaomatricula", "resultado", "codresultado",
            "codtipomovimentacao", "descrtipomovimentacao", "descrmotivomovimentacao",
            "codmotivomovimentacao", "datamovimentacao", "ultimaAtualizacaoMatricula", "ultimaAtualizacaoAluno"
        ]

        dados_extraidos = []
        for escola in dados:
            for turma in escola.get("turmas", []):
                matriculas = turma.get("matricula")
                if isinstance(matriculas, list):
                    for aluno in matriculas:
                        registro = {campo: aluno.get(campo) for campo in campos_desejados}
                        dados_extraidos.append(registro)

        if not dados_extraidos:
            raise ValueError("O relatório está vazio ou sem dados de alunos.")

        df = pd.DataFrame(dados_extraidos)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = f"relatorio_{timestamp}"

        csv_path = os.path.join(destino_path, f"{base_name}.csv")
        xlsx_path = os.path.join(destino_path, f"{base_name}.xlsx")
        json_path_final = os.path.join(destino_path, f"{base_name}.json")

        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        df.to_excel(xlsx_path, index=False)

        with open(json_path_final, "w", encoding="utf-16") as f:
            f.write(raw_json)

        return csv_path, xlsx_path, json_path_final

    except Exception as e:
        messagebox.showerror("Erro de Conversão", f"Erro ao converter o relatório:\n\n{str(e)}")
        return None, None, None

# === INICIAR PROCESSO ===
def iniciar_processo():
    ano = ano_var.get()
    destino = destino_var.get()

    if not destino:
        messagebox.showwarning("Destino Não Selecionado", "Por favor, selecione a pasta de destino.")
        return

    temp_json_path, raw_json = baixar_relatorio(ano)
    if temp_json_path and raw_json:
        csv, xlsx, json_final = converter_relatorio(temp_json_path, destino, raw_json)
        if csv and xlsx:
            messagebox.showinfo("Sucesso", f"Arquivos gerados com sucesso!\n\nCSV: {csv}\nXLSX: {xlsx}\nJSON: {json_final}")

# === SELECIONAR PASTA ===
def selecionar_destino():
    pasta = filedialog.askdirectory()
    if pasta:
        destino_var.set(pasta)

# === INTERFACE TKINTER ===
root = tk.Tk()
root.title("Gerador de Relatório Escolar")
root.geometry("500x250")
root.resizable(False, False)

ano_var = tk.StringVar(value="2023")
destino_var = tk.StringVar()

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

tk.Label(frame, text="Selecione o ano do relatório:").grid(row=0, column=0, sticky="w")
anos = [str(a) for a in range(2023, 2031)]
ttk.Combobox(frame, textvariable=ano_var, values=anos, state="readonly").grid(row=0, column=1, pady=10)

tk.Label(frame, text="Selecione a pasta de destino:").grid(row=1, column=0, sticky="w")
tk.Entry(frame, textvariable=destino_var, width=30).grid(row=1, column=1, pady=10, sticky="w")
tk.Button(frame, text="Procurar...", command=selecionar_destino).grid(row=1, column=2, padx=5)

tk.Button(frame, text="Gerar Relatório", command=iniciar_processo,
          bg="#4CAF50", fg="white", padx=10, pady=5).grid(row=3, column=0, columnspan=3, pady=20)

root.mainloop()
