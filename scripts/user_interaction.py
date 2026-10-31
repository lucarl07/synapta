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

