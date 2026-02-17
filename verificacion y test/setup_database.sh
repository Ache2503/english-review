#!/bin/bash
set -e  # Salir si hay error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Directorio del script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Banner
echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║                                                                      ║"
echo "║   🗄️  DATABASE SETUP - English Learning Platform                     ║"
echo "║                                                                      ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo -e "${BLUE}📅 Fecha:${NC} $(date '+%Y-%m-%d %H:%M:%S')"
echo -e "${BLUE}📁 Directorio:${NC} $SCRIPT_DIR"
echo ""

# Verificar argumentos
CHECK_ONLY=false
RESET_MODE=false
BACKUP_FIRST=false
SKIP_SEEDS=false

for arg in "$@"; do
    case $arg in
        --check)
            CHECK_ONLY=true
            ;;
        --reset)
            RESET_MODE=true
            ;;
        --backup)
            BACKUP_FIRST=true
            ;;
        --skip-seeds)
            SKIP_SEEDS=true
            ;;
        --help|-h)
            echo "Uso: $0 [opciones]"
            echo ""
            echo "Opciones:"
            echo "  --check       Solo verificar (no modificar)"
            echo "  --reset       Resetear base de datos (¡ELIMINA DATOS!)"
            echo "  --backup      Crear backup antes de cambios"
            echo "  --skip-seeds  No ejecutar seeds"
            echo "  --help        Mostrar esta ayuda"
            exit 0
            ;;
    esac
done

# =============================================================================
# PASO 1: Verificar entorno virtual
# =============================================================================
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${PURPLE}📦 PASO 1: Verificando entorno virtual${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [ -d ".venv" ]; then
    echo -e "${GREEN}✅ Entorno virtual encontrado${NC}"
    source .venv/bin/activate
    echo -e "${GREEN}✅ Entorno virtual activado${NC}"
else
    echo -e "${YELLOW}⚠️  Entorno virtual no encontrado. Creando...${NC}"
    python3 -m venv .venv
    source .venv/bin/activate
    echo -e "${GREEN}✅ Entorno virtual creado y activado${NC}"
fi

# Verificar Python
PYTHON_VERSION=$(python --version 2>&1)
echo -e "${BLUE}🐍 Python:${NC} $PYTHON_VERSION"

# =============================================================================
# PASO 2: Verificar dependencias
# =============================================================================
echo ""
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${PURPLE}📦 PASO 2: Verificando dependencias${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [ -f "requirements.txt" ]; then
    echo -e "${BLUE}📋 Instalando/verificando dependencias...${NC}"
    pip install -r requirements.txt -q
    echo -e "${GREEN}✅ Dependencias verificadas${NC}"
else
    echo -e "${RED}❌ requirements.txt no encontrado${NC}"
    exit 1
fi

# =============================================================================
# PASO 3: Verificar archivo .env
# =============================================================================
echo ""
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${PURPLE}🔐 PASO 3: Verificando configuración${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [ -f ".env" ]; then
    echo -e "${GREEN}✅ Archivo .env encontrado${NC}"
    # Verificar DATABASE_URL
    if grep -q "DATABASE_URL" .env; then
        echo -e "${GREEN}✅ DATABASE_URL configurada${NC}"
    else
        echo -e "${RED}❌ DATABASE_URL no encontrada en .env${NC}"
        echo -e "${YELLOW}💡 Tip: Copia .env.example a .env y configura la base de datos${NC}"
        exit 1
    fi
else
    if [ -f ".env.example" ]; then
        echo -e "${YELLOW}⚠️  .env no encontrado. Copiando desde .env.example...${NC}"
        cp .env.example .env
        echo -e "${YELLOW}⚠️  Por favor, edita .env con tus credenciales de base de datos${NC}"
        exit 1
    else
        echo -e "${RED}❌ No se encontró .env ni .env.example${NC}"
        exit 1
    fi
fi

# =============================================================================
# PASO 4: Verificar conexión a PostgreSQL
# =============================================================================
echo ""
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${PURPLE}🐘 PASO 4: Verificando conexión a PostgreSQL${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

python -c "
from app import create_app
from app.extensions import db
app = create_app()
with app.app_context():
    try:
        db.session.execute(db.text('SELECT 1'))
        print('✅ Conexión a PostgreSQL exitosa')
    except Exception as e:
        print(f'❌ Error de conexión: {e}')
        exit(1)
"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ No se pudo conectar a PostgreSQL${NC}"
    echo -e "${YELLOW}💡 Verifica que PostgreSQL esté corriendo y las credenciales sean correctas${NC}"
    exit 1
fi

# =============================================================================
# PASO 5: Backup (si se solicita)
# =============================================================================
if [ "$BACKUP_FIRST" = true ]; then
    echo ""
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${PURPLE}💾 PASO 5: Creando backup${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    BACKUP_FILE="backup_$(date +%Y%m%d_%H%M%S).sql"
    
    # Obtener credenciales del .env
    source .env 2>/dev/null || true
    
    if command -v pg_dump &> /dev/null; then
        # Extraer partes de DATABASE_URL
        if [[ $DATABASE_URL =~ postgresql://([^:]+):([^@]+)@([^:]+):([^/]+)/(.+) ]]; then
            DB_USER="${BASH_REMATCH[1]}"
            DB_PASS="${BASH_REMATCH[2]}"
            DB_HOST="${BASH_REMATCH[3]}"
            DB_PORT="${BASH_REMATCH[4]}"
            DB_NAME="${BASH_REMATCH[5]}"
            
            PGPASSWORD="$DB_PASS" pg_dump -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -f "$BACKUP_FILE" 2>/dev/null
            
            if [ $? -eq 0 ]; then
                echo -e "${GREEN}✅ Backup creado: $BACKUP_FILE${NC}"
            else
                echo -e "${YELLOW}⚠️  No se pudo crear backup automático${NC}"
            fi
        fi
    else
        echo -e "${YELLOW}⚠️  pg_dump no disponible, saltando backup${NC}"
    fi
fi

# =============================================================================
# PASO 6: Verificar/Actualizar estructura de tablas
# =============================================================================
echo ""
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${PURPLE}🗄️  PASO 6: Verificando estructura de base de datos${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [ "$RESET_MODE" = true ]; then
    echo -e "${RED}⚠️  MODO RESET - Se eliminarán todos los datos${NC}"
    read -p "¿Estás seguro? (escribe 'SI'): " confirm
    if [ "$confirm" = "SI" ]; then
        python db_manager.py --reset
    else
        echo -e "${YELLOW}Operación cancelada${NC}"
        exit 0
    fi
elif [ "$CHECK_ONLY" = true ]; then
    python db_manager.py --check
else
    python db_manager.py
fi

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error en la verificación de base de datos${NC}"
    exit 1
fi

# =============================================================================
# PASO 7: Ejecutar seeds
# =============================================================================
if [ "$SKIP_SEEDS" = false ] && [ "$CHECK_ONLY" = false ]; then
    echo ""
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${PURPLE}🌱 PASO 7: Ejecutando seeds${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    python seed_runner.py --force
    
    if [ $? -ne 0 ]; then
        echo -e "${YELLOW}⚠️  Algunos seeds tuvieron errores${NC}"
    fi
fi

# =============================================================================
# PASO 8: Verificar estado final
# =============================================================================
echo ""
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${PURPLE}📊 PASO 8: Estado final${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

python seed_runner.py --status

# =============================================================================
# RESUMEN FINAL
# =============================================================================
echo ""
echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║                                                                      ║"
echo "║   ✅ CONFIGURACIÓN COMPLETADA                                        ║"
echo "║                                                                      ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${GREEN}Para iniciar el servidor:${NC}"
echo -e "   ${BLUE}python run.py${NC}"
echo ""
echo -e "${GREEN}Acceso:${NC}"
echo -e "   ${BLUE}http://localhost:5000${NC}"
echo ""
echo -e "${GREEN}Usuario administrador:${NC}"
echo -e "   ${BLUE}Usuario: admin${NC}"
echo -e "   ${BLUE}Password: admin123${NC}"
echo ""
