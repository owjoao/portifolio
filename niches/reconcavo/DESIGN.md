---
name: Recôncavo Culinária
description: Editorial gastronomic restaurant system with Bahian warmth, saffron accents and deep root-green surfaces.
colors:
  cream: "#f7f0e4"
  cream-soft: "#f0e6d5"
  paper: "#fffaf1"
  forest: "#173d2d"
  forest-deep: "#102c21"
  forest-mid: "#2b5a43"
  saffron: "#e5a21b"
  saffron-light: "#f2c75b"
  terracotta: "#b95635"
  ink: "#2b211a"
  ink-soft: "#6f6256"
typography:
  display:
    fontFamily: "DM Serif Display, Georgia, serif"
    fontSize: "clamp(3rem, 6vw, 7.2rem)"
    fontWeight: 400
    lineHeight: 0.91
    letterSpacing: "-0.045em"
  body:
    fontFamily: "Manrope, Segoe UI, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Manrope, Segoe UI, sans-serif"
    fontSize: "11px"
    fontWeight: 800
    letterSpacing: "0.15em"
rounded:
  control: "2px"
  image-arch: "0 130px 0 130px"
  seal: "50%"
spacing:
  xs: "8px"
  sm: "16px"
  md: "24px"
  lg: "48px"
  section: "clamp(6rem, 11vw, 10rem)"
components:
  button-primary:
    backgroundColor: "{colors.saffron}"
    textColor: "{colors.forest-deep}"
    rounded: "{rounded.control}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.forest}"
    border: "1px solid rgba(23, 61, 45, 0.36)"
  navigation:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    height: "86px"
---

# Design System: Recôncavo Culinária

## Creative North Star

**“O sabor como memória.”**

A premium Brazilian restaurant identity that feels rooted in the Recôncavo without becoming a tourist cliché. The page should feel like a carefully edited menu book: warm paper, a deep living green, saffron light, terracotta accents, generous space and images that carry the atmosphere.

## Visitor promise

The visitor should understand three things quickly:

1. This is a contemporary Bahian restaurant experience.
2. The existing digital menu is the clearest next action.
3. The house is in Barra, Salvador, and can be reached by WhatsApp or phone.

## Narrative sequence

1. **Hero** — the name, the promise “Sabores que nascem do Recôncavo” and a large editorial food/table composition.
2. **Nossa identidade** — the idea that memory, origin and hospitality live in the plate.
3. **Cardápio** — a clear link to the official Strelo menu plus a transparent list of publicly listed highlights, without invented prices.
4. **Experiência** — bead curtain, music, table, culture and the feeling of being received.
5. **Galeria** — a visual rhythm of real supplied photography.
6. **Visite** — address, hours, WhatsApp, map and public information links.
7. **CTA final** — invite the visitor to open the menu and bring the flavor home.

## Visual language

### Color

- **Forest green** is the grounding surface: restaurant room, night, foliage and institutional confidence.
- **Saffron** is the signal color: logo relationship, menu CTA, highlights and small moments of joy.
- **Terracotta** gives warmth to editorial emphasis and action labels.
- **Cream and paper** provide breathing room and make photography feel tactile.
- Blue and extra colors stay absent unless they already exist in a supplied photograph.

### Typography

- **DM Serif Display** is reserved for statements, section titles, menu item names and the final invitation.
- **Manrope** handles navigation, body copy, labels, ingredients, practical information and buttons.
- Do not use all caps for long copy. Uppercase is limited to navigation labels, section numbers and small metadata.

### Form

The signature is the **arched editorial frame**: a rounded image corner or a complete arch appears in the identity image, menu board, experience banner, map and CTA. It gives the system a recognizable silhouette without copying the reference site.

The secondary signature is the **saffron line and numbered editorial index**. Numbers and short rules help the long page feel intentional rather than crowded.

## Photography

The page uses the supplied photographs and existing local presentation compositions. Images are framed, cropped and layered with CSS; no image is presented as synthetic factual photography. The menu list names dishes identified in public menu references, but the official Strelo link remains the source for current prices and availability.

## Motion

Motion is restrained and purposeful:

- content rises gently into view;
- images shift by a few pixels on scroll;
- buttons lift by 3px on hover;
- mobile navigation uses a clipped reveal;
- all motion is disabled or reduced when `prefers-reduced-motion` is active.

## Responsive rules

- Desktop uses a two-column hero, a split identity section, a three-column menu list and an editorial gallery.
- Mobile uses a single column, stacked CTAs, full-width menu items, a two-column gallery and a simplified map card.
- Tap targets remain at least 44px high.
- Decorative circles and rings are clipped by their section or visual frame so they cannot create horizontal scrolling.

## Content integrity

- Do not invent prices, ratings, reviews, awards, hours or menu items.
- Do not add a numeric Google rating without a current confirmed value.
- Do not describe a generated or edited composition as an official photograph.
- Keep the official menu, WhatsApp, phone, Instagram, address and map links easy to find.
