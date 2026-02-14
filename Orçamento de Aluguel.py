import csv


class Orcamento:
    def __init__(self):
        # Valores fixos conforme o roteiro
        self.taxa_contrato = 2000.00
        self.valor_aluguel = 0.0
        self.tipo_imovel = ""
        self.qtd_quartos = 1

    # =============================
    # CÁLCULO DO VALOR BASE
    # =============================
    def calcular_aluguel(self, tipo, quartos):
        self.tipo_imovel = tipo
        self.qtd_quartos = quartos

        # Apartamento
        if tipo == "Apartamento":
            self.valor_aluguel = 700.00
            if quartos == 2:
                self.valor_aluguel += 200.00  # CORRETO (era 300)

        # Casa
        elif tipo == "Casa":
            self.valor_aluguel = 900.00
            if quartos == 2:
                self.valor_aluguel += 250.00  # CORRETO (era 450)

        # Estúdio
        elif tipo == "Estúdio":
            self.valor_aluguel = 1200.00

    # =============================
    # ADICIONAIS
    # =============================
    def adicionar_garagem(self):
        self.valor_aluguel += 300.00

    def adicionar_vagas_estudio(self, vagas):
        if vagas >= 2:
            self.valor_aluguel += 250.00
            extras = vagas - 2
            if extras > 0:
                self.valor_aluguel += extras * 60.00

    def aplicar_desconto(self):
        self.valor_aluguel *= 0.95  # 5%

    # =============================
    # GERAR CSV
    # =============================
    def gerar_csv(self):
        with open("orcamento.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Mês", "Valor do Aluguel"])

            for mes in range(1, 13):
                writer.writerow([mes, f"{self.valor_aluguel:.2f}"])

    # =============================
    # RESUMO FINAL
    # =============================
    def exibir_resumo(self, parcelas, valor_parcela):
        print("\n" + "=" * 30)
        print("      ORÇAMENTO R.M      ")
        print("=" * 30)
        print(f"Imóvel: {self.tipo_imovel}")
        print(f"Quartos: {self.qtd_quartos}")
        print(f"Aluguel Mensal: R$ {self.valor_aluguel:.2f}")
        print("-" * 30)
        print(f"Taxa de Contrato: R$ {self.taxa_contrato:.2f}")
        print(f"Parcelamento da Taxa: {parcelas}x de R$ {valor_parcela:.2f}")
        print("-" * 30)

        total_primeiro_mes = self.valor_aluguel + valor_parcela
        print(f"TOTAL NO 1º MÊS: R$ {total_primeiro_mes:.2f}")
        print("=" * 30)
        print("Arquivo CSV gerado com 12 parcelas!")


# ==================================================
# INTERAÇÃO COM O USUÁRIO
# ==================================================

meu_orcamento = Orcamento()

print("--- Bem-vindo à Imobiliária R.M ---")

tipo = input("Escolha o tipo (Apartamento, Casa ou Estúdio): ").capitalize()

quartos = 1
if tipo != "Estúdio":
    quartos = int(input("Quantidade de quartos (1 ou 2): "))

meu_orcamento.calcular_aluguel(tipo, quartos)


# =============================
# GARAGEM OU VAGAS
# =============================
if tipo in ["Apartamento", "Casa"]:
    garagem = input("Deseja garagem? (s/n): ").lower()
    if garagem == "s":
        meu_orcamento.adicionar_garagem()

elif tipo == "Estúdio":
    vagas = int(input("Quantidade de vagas de estacionamento: "))
    meu_orcamento.adicionar_vagas_estudio(vagas)


# =============================
# DESCONTO APARTAMENTO
# =============================
if tipo == "Apartamento":
    criancas = input("Possui crianças? (s/n): ").lower()
    if criancas == "n":
        meu_orcamento.aplicar_desconto()


# =============================
# TAXA DE CONTRATO
# =============================
parcelas = int(input("Em quantas vezes pagar a taxa (máximo 5): "))

if parcelas > 5:
    parcelas = 5
    print("Limite de 5 vezes aplicado.")

valor_parcela = meu_orcamento.taxa_contrato / parcelas


# =============================
# GERAR CSV + EXIBIR
# =============================
meu_orcamento.gerar_csv()
meu_orcamento.exibir_resumo(parcelas, valor_parcela)



