# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Proyecto

Landing page estática de **JNM Abogados** (estudio jurídico argentino especializado en accidentes de tránsito, accidentes de trabajo y derecho sucesorio). Sitio de una sola página con navegación por anclas; todo el contenido está en español argentino (voseo).

Stack: [Astro](https://docs.astro.build) 6 sin frameworks de UI ni TypeScript de aplicación (solo `.astro` + CSS plano). El build genera un sitio estático en `dist/`.

## Comandos

```sh
npm install      # instala dependencias (requiere Node >= 22.12.0, ver "engines" en package.json)
npm run dev      # servidor de desarrollo en http://localhost:4321
npm run build    # build de producción a ./dist/
npm run preview  # sirve el build localmente
```

No hay tests ni linter configurados.

## Arquitectura

- `src/pages/index.astro` — única página; compone las secciones en orden: `Header`, `Hero`, `AreasPractica`, `Experiencia`, `Contacto`, `Footer`, `WhatsAppButton`.
- `src/layouts/Layout.astro` — shell HTML: SEO/Open Graph, JSON-LD (`LegalService` + `FAQPage`), fuentes de Google (Inter/Outfit) y el JS global inline (scroll-reveal con IntersectionObserver sobre `.reveal`, contadores animados sobre `[data-counter]` con `data-target`/`data-prefix`/`data-suffix`). Toda página nueva debe usarlo.
- `src/components/*.astro` — un componente por sección, cada uno con su `<style>` scoped de Astro. Los IDs de ancla son `#inicio`, `#areas`, `#experiencia`, `#contacto`; el nav del Header (desktop y móvil) apunta a ellos. `Header.astro` trae su propio script inline (efecto scroll del header y toggle del menú móvil).
- `src/styles/global.css` — design system en CSS custom properties: colores de marca (`--primary`, `--accent`, neutros), escala tipográfica fluida con `clamp()`, spacing, sombras, transiciones, keyframes y utilities (`.container`, `.section`, `.btn--*`, `.heading-*`, `.reveal`). Antes de agregar estilos nuevos, reutilizar los tokens/utilities existentes.
- `public/` — assets estáticos servidos tal cual: logos (`logo_cropped.png` es el que usa el Header), favicon, `og-image.jpg`, `robots.txt`.
- `astro.config.mjs` — `site: https://www.jnmabogados.com.ar` con integración `@astrojs/sitemap` (genera el sitemap en el build; `robots.txt` ya lo referencia).
- `crop_logo.py` y `make_transparent.py` — scripts únicos (Pillow) que generaron las variantes de logo en `public/`. No forman parte del build.

## Datos de contacto del sitio

WhatsApp (`5491151345587`) e Instagram (`@jnmabogados`) están hardcodeados en tres lugares: `WhatsAppButton.astro`, `Contacto.astro` y el JSON-LD de `Layout.astro`. Si cambian, actualizar en los tres.

## Notas

- El formulario de `Contacto.astro` (`#contact-form`) no tiene handler de submit: no envía datos a ningún lado; los leads llegan por los links de WhatsApp. Pendiente conectarlo a un backend cuando se contrate Google Workspaces.
- No hay CI/deploy configurado dentro del repo; el hosting se sirve del build de `dist/`.
