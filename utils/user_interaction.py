# ==:== Interação com o Usuário ==:==

def ask_yes_no(prompt: str, default: bool = True) -> bool:
    while True:
        answer = input(prompt).strip().lower()
        if answer == "":
            return default
        if answer in ("s", "sim"):
            return True
        if answer in ("n", "não", "nao"):
            return False
        print("Resposta inválida. Tente novamente.")

def print_section(title: str | None, content: str):
    if not title:
        print(content, end="\n\n")
    else:
        print(f"|==== {title.upper()} ====|", content, sep="\n", end="\n\n")
