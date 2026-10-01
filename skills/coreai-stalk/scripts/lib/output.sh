#!/usr/bin/env bash
# coreai-stalk/scripts/lib/output.sh
# Padroniza paths de output em <raiz>/businesses/<slug>/outputs/inteligencia/{tipo}/{item}/
# A raiz do Context OS chega por --root/--context-root (exportada pelo stalk.sh) ou pela
# variável CONTEXT_OS_ROOT; o negócio chega por --client <slug>, CONTEXT_OS_BUSINESS ou
# default_client do config. Sem raiz ou sem negócio, falha: não existe default relativo.
# Todo destino passa antes por coreai-shared/scripts/gate.py (precisa devolver READY).

set -euo pipefail

STALK_SKILL_DIR="${STALK_SKILL_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
STALK_CONFIG_FILE="${STALK_CONFIG_FILE:-$STALK_SKILL_DIR/config.yaml}"
STALK_GATE="${STALK_GATE:-$STALK_SKILL_DIR/../coreai-shared/scripts/gate.py}"

# Lê valor de chave do config.yaml. Args: $1=chave
stalk_config_get() {
  local key="$1"
  local default="${2:-}"
  if [[ -f "$STALK_CONFIG_FILE" ]]; then
    local val
    val=$(grep -E "^${key}:" "$STALK_CONFIG_FILE" 2>/dev/null | head -1 | sed -E "s/^${key}:[[:space:]]*//" | tr -d '"' | tr -d "'")
    [[ -n "$val" ]] && echo "$val" && return
  fi
  echo "$default"
}

stalk_config_set() {
  local key="$1"
  local value="$2"

  mkdir -p "$(dirname "$STALK_CONFIG_FILE")"
  touch "$STALK_CONFIG_FILE"

  if grep -qE "^${key}:" "$STALK_CONFIG_FILE" 2>/dev/null; then
    sed -i '' "s|^${key}:.*|${key}: \"${value}\"|" "$STALK_CONFIG_FILE"
  else
    echo "${key}: \"${value}\"" >> "$STALK_CONFIG_FILE"
  fi
}

# Slugifica string para nome de pasta
stalk_slugify() {
  echo "$1" \
    | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g' \
    | sed -E 's/^-+|-+$//g' \
    | head -c 60
}

# Gera path de output. Args: $1=tipo (profile/search/dossie/comments/compare), $2=slug, $3=cliente (opcional)
stalk_output_dir() {
  local tipo="$1"
  local slug="$2"
  local cliente="${3:-${CONTEXT_OS_BUSINESS:-$(stalk_config_get default_client '')}}"
  local root="${CONTEXT_OS_ROOT:-}"

  if [[ -z "$root" ]]; then
    echo "❌ Raiz do Context OS não informada. Use --root <raiz> (ou exporte CONTEXT_OS_ROOT)." >&2
    return 1
  fi
  if [[ "$root" != /* && ! "$root" =~ ^[A-Za-z]:[\/] ]]; then
    echo "❌ A raiz do Context OS precisa ser um caminho absoluto: $root" >&2
    return 1
  fi
  if [[ -z "$cliente" ]]; then
    echo "❌ Negócio não informado. Use --client <slug> (ou /stalk config default_client <slug>)." >&2
    return 1
  fi

  local base="${STALK_OUTPUT_BASE:-$root/businesses/$cliente/outputs/inteligencia}"
  local dir="$base/$tipo/$slug"

  if [[ ! -f "$STALK_GATE" ]]; then
    echo "❌ Gate não encontrado: $STALK_GATE (instale coreai-shared ao lado desta skill)." >&2
    return 1
  fi
  local py
  py="$(command -v python3 || command -v python || true)"
  if [[ -z "$py" ]]; then
    echo "❌ Python não encontrado; o gate de saída é obrigatório." >&2
    return 1
  fi
  local verdict
  if ! verdict="$("$py" "$STALK_GATE" --root "$root" --business "$cliente" --output "$dir")"; then
    echo "❌ Gate bloqueou o destino $dir: $verdict" >&2
    return 1
  fi

  mkdir -p "$dir"
  echo "$dir"
}

# Helper: imprime cabeçalho de output
stalk_print_header() {
  local titulo="$1"
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "  $titulo"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
}
