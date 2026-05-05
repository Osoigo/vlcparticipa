#!/usr/bin/env bash

# Script para instalar git hooks
# Copia los hooks de scripts/hooks/ a .git/hooks/

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
GIT_HOOKS_DIR="$REPO_ROOT/.git/hooks"

echo "📦 Instalando git hooks..."

# Crear directorio de hooks si no existe
mkdir -p "$GIT_HOOKS_DIR"

# Copiar y dar permisos a los hooks
for hook in "$SCRIPT_DIR/hooks"/*; do
    if [ -f "$hook" ]; then
        hook_name=$(basename "$hook")
        cp "$hook" "$GIT_HOOKS_DIR/$hook_name"
        chmod +x "$GIT_HOOKS_DIR/$hook_name"
        echo "✅ Instalado: $hook_name"
    fi
done

echo "✨ Git hooks instalados correctamente"
