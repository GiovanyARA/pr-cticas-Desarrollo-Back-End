# Backend Unidad 1 (Django + DRF)

Este repositorio contiene las prácticas de la Unidad 1 (Opción B: Django REST Framework).

## Requisitos
- Python 3.11+
- Git
- Visual Studio Code

## Cómo ejecutar (resumen; se detallará por práctica)
1. Crear y activar entorno virtual.
2. Instalar dependencias.
3. Ejecutar el servidor.

> Requisitos rápidos
>
> ```cmd
> .\.venv\Scripts\activate
> python manage.py migrate
> python manage.py runserver 127.0.0.1:8000
> ```
> Endpoints base: `http://127.0.0.1:8000/api/productos/`  
> (Si usas otro puerto, ajusta las URLs)

---

### 1) Usando la interfaz navegable (DRF Browsable API)

1. Abre `http://127.0.0.1:8000/api/productos/`.
2. **Crear (POST)** desde el formulario (o pestaña *Raw data* con `application/json`):
   ```json
   {
     "nombre": "Mouse Gamer",
     "descripcion": "RGB, 6 botones",
     "precio": 499.99,
     "stock": 25,
     "activo": true
   }
