# Implementation Plan: Rappjdeutsch Website Prototype

## Objective
Build a simple, static, modern-looking website prototype for "Rappjdeutsch," a private German school in Rapperswil-Jona taught by Maria Bernardina Milano. The site will default to English with a toggle for simple German, focusing on her unique value proposition (improving German for job opportunities) and approachability.

## Key Files & Context
*   **Tech Stack:** React, Vite, Vanilla CSS.
*   **Assets:** Teacher's photo (`materials/20260522 Lehrerin.jpg`), Logo (`materials/Rappjdeutsch logo.png`), provided course list from Excel.
*   **Contact Info:** Name: Maria Bernardina Milano, Phone/WhatsApp: +41 76 649 11 55, Address: Placeholder in Jona (e.g., Molkereistrasse 1, 8645 Jona). No email.
*   **Inspiration:** GoGerman.ch (modern, clear pricing, conversational tone, emphasis on practical goals).

## Implementation Steps
1.  **Project Setup:**
    *   Initialize a React + Vite (TypeScript) project.
    *   Set up a simple localization mechanism (a context or state hook) to toggle between English and German.
2.  **Layout & Design:**
    *   **Color Palette:** Professional deep blue/charcoal paired with warm, friendly accents (e.g., soft green or Swiss red) and plenty of whitespace.
    *   **Typography:** Clean, highly legible sans-serif.
3.  **Core Components:**
    *   **Header:** Logo (placeholder until generated), Navigation, and Language Toggle (EN/DE).
    *   **Hero Section:** Headline ("Better German - Better Job!" / "Besseres Deutsch - Besseren Job!"), welcoming subtext, and a prominent CTA for a Free Trial / WhatsApp contact.
    *   **About Me:** Friendly introduction using Maria's photo, highlighting her experience and approachable teaching style.
    *   **Courses/Packages:** Clean display of the course offerings derived from the Excel sheet:
        *   Beginner (A1.1 - A2.2)
        *   Intermediate (B1.1 - B1.2)
        *   Specialized Focus: Job-Coaching & RAV-Support (unique selling point).
    *   **Contact/Action Section:** Emphasize reaching out via WhatsApp (since email is not preferred) and display the placeholder address in Jona.

## Verification & Testing
*   Ensure the language toggle correctly swaps all textual content.
*   Verify the design is fully responsive (mobile, tablet, desktop).
*   Check that the provided image is optimized and displays correctly.