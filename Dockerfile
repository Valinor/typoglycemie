# -------------------------------------------------------
# Étape 1 : builder sous Alpine pour produire un binaire musl
# -------------------------------------------------------
FROM python:3.11-alpine AS builder

# Installer les dépendances de compilation & pyinstaller
RUN apk add --no-cache gcc musl-dev make \
    && pip install --no-cache-dir pyinstaller

WORKDIR /src

# Copier le script Python (inchangé)
COPY typoglycemie.py .

# Générer un exécutable musl‐compatible
# --onefile → binaire unique ; --strip enlève les symboles pour réduire la taille.
# Note : sous Alpine, PyInstaller s’appuie sur musl‐dev/gcc.
RUN pyinstaller --noconfirm --onefile --strip --name typoglycemie-bin typoglycemie.py

# -------------------------------------------------------
# Étape 2 : runtime minimal sur Alpine
# -------------------------------------------------------
FROM alpine:latest

WORKDIR /app

# Copier seulement le binaire produit précédemment
COPY --from=builder /src/dist/typoglycemie-bin .

# S’assurer qu’il est exécutable
RUN chmod +x typoglycemie-bin

# Point d’entrée : on exécute toujours ./typoglycemie-bin avec l’argument passé à docker run
ENTRYPOINT ["./typoglycemie-bin"]
