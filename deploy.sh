#!/bin/bash
set -e

echo "🚀 Iniciando despliegue de English Review..."

if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ docker-compose no está instalado."
    exit 1
fi

echo "📋 Configuración: Puerto 5100, Dominio: ingles.jaripeo.online"

docker-compose down || true
docker image prune -af --filter "until=24h" || true
docker-compose build
docker-compose up -d

sleep 10

if docker ps | grep -q english-review-production; then
    echo "✅ Contenedor ejecutándose correctamente"
else
    echo "❌ Error: El contenedor no se inició correctamente"
    docker-compose logs
    exit 1
fi

echo "📊 Logs iniciales:"
docker-compose logs --tail=20

echo ""
echo "✨ Despliegue completado exitosamente"
echo ""
echo "📌 Siguientes pasos:"
echo "   1. Configurar Nginx:"
echo "      sudo cp nginx-config.conf /etc/nginx/sites-available/english-review"
echo "      sudo ln -sf /etc/nginx/sites-available/english-review /etc/nginx/sites-enabled/"
echo "   2. Verificar y reiniciar Nginx:"
echo "      sudo nginx -t"
echo "      sudo systemctl restart nginx"
echo "   3. Verificar en: http://ingles.jaripeo.online"
