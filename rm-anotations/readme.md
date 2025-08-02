# setup

Clean before start new test.

1. Esperar a que termine el agente actual:
```bash
# Verificar si ya terminó
docker compose ps

# Si sigue corriendo, esperar a que termine
docker compose logs -f agents
```

2. Limpieza completa de Docker:
```bash
# Detener todos los contenedores
docker compose down -v

# Limpiar todo Docker
docker system prune -a -f

# Limpiar redes
docker network prune -f

# Limpiar volúmenes
docker volume prune -f

# Limpiar imágenes no utilizadas
docker image prune -a -f
```

3. Verificar que esté todo limpio:
```bash
# Verificar que no haya contenedores
docker ps -a

# Verificar que no haya redes
docker network ls

# Verificar que no haya volúmenes
docker volume ls
```

4. Preparar para el fork:
```bash
# Navegar a tu fork
cd /d/APPs/compose-for-agents-fork

# Crear rama de trabajo
git checkout -b feature/crew-ai-improvements

# Verificar que esté limpio
docker compose ps
```