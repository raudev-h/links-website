# Personal Links Website 🌐

Una página web personal estilo Linktree construida con Reflex y Python. Este proyecto muestra mis redes sociales y perfil profesional de una manera elegante y responsive.

## 🚀 Características

- Diseño moderno y minimalista
- Totalmente responsive
- Tema oscuro
- Avatar y perfil personal
- Botones de redes sociales con iconos
- Fuentes personalizadas de Google Fonts
- Footer con copyright dinámico

## 🛠️ Tecnologías

- [Reflex](https://reflex.dev/) - Framework web en Python
- Python 3.12
- Google Fonts (Poppins, Comfortaa)
- Tailwind CSS

## 📦 Estructura del Proyecto

```
web_project/
├── assets/
│   ├── fonts/
│   │   └── fonts.css
│   ├── favicon.ico
│   ├── logo.png
│   └── python.png
├── web_project/
│   ├── components/
│   │   ├── footer.py
│   │   ├── info_text.py
│   │   ├── link_button.py
│   │   ├── link_icon.py
│   │   ├── navbar.py
│   │   └── titles.py
│   ├── styles/
│   │   ├── colors.py
│   │   ├── fonts.py
│   │   └── styles.py
│   ├── views/
│   │   ├── headers/
│   │   │   └── header.py
│   │   └── links/
│   │       └── links.py
│   ├── __init__.py
│   └── web_project.py
├── requirements.txt
└── rxconfig.py
```

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/raudev-h/links-website.git
cd links-website
```

2. Crea un entorno virtual e instala las dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Ejecuta el proyecto:
```bash
reflex run
```

4. Abre http://localhost:3000 en tu navegador

## 🔧 Configuración

1. Edita `web_project/styles/colors.py` para personalizar los colores
2. Modifica `web_project/views/headers/header.py` para actualizar tu información personal
3. Actualiza `web_project/views/links/links.py` para modificar tus enlaces

## 📱 Vista Previa Responsive

El sitio es totalmente responsive y se adapta a todos los tamaños de pantalla:
- Escritorio 🖥️
- Tablet 📱
- Móvil 📱

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para cambios importantes:

1. Haz Fork del proyecto
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para detalles

## 👤 Autor

**Raúl Hechavarria**
- Github: [@raudev-h](https://github.com/raudev-h)
- Instagram: [@rau_05.h](https://www.instagram.com/rau_05.h/)
