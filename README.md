# Očko (Slovak Twenty-One / Slovenská 21) 🃏

A highly polished, interactive terminal-based implementation of the traditional Slovak/Czech card game **Očko** (similar to Blackjack or Twenty-One), written in Python 3. The game features beautiful, colorized ASCII art cards, a chips betting system, authentic Slovak rules (like the instant-win *Kráľovské oko*), and full bilingual support (Slovak/English).

---

## 🎨 Features / Vlastnosti

* **Traditional Mariáš Deck / Tradičný Mariášový Balík**: Played with a 32-card German deck (7, 8, 9, 10, Jack/Spodok, Queen/Zvršok, King/Kráľ, Ace/Eso).
* **Kráľovské Oko (Royal Eye) 👑**: Instant-win combination of two Aces (22 points) right at the start of a hand, paying out 2:1!
* **ASCII Art Visuals / ASCII Grafika**: Cards are beautifully drawn side-by-side in your terminal, with Unicode suits colorized using ANSI escape codes.
* **Fully Bilingual / Plne dvojjazyčné**: Prompts you to select either **Slovenčina** or **English** at startup. All rules, cards, prompts, and actions are translated.
* **Betting & AI Dealer / Stávkovanie a AI Bankár**: Play against the banker's AI (which stands on 15+ and draws on anything under 15) using a virtual chips wallet.

---

## 📜 Rules of the Game (English)

1. **Goal**: Get a hand value as close to **21 points** as possible without going over.
2. **Card Values**:
   - **Ace (Eso)** = 11 points
   - **Ten (Desiatka)** = 10 points
   - **King (Kráľ)** = 4 points
   - **Queen (Zvršok)** = 3 points
   - **Jack (Spodok)** = 2 points
   - **7, 8, 9** = Face value
3. **Kráľovské Oko**: If you get exactly **two Aces** as your first two cards (value 22), you win instantly with a **2:1 payout**!
4. **Banker's Rule**: The banker must draw another card if their score is **under 15**, and must stand if their score is **15 or more**.

---

## 📜 Pravidlá hry (Slovensky)

1. **Cieľ**: Dosiahnuť celkové skóre kariet čo najbližšie k **21 bodom** a neprekročiť túto hodnotu.
2. **Hodnoty kariet**:
   - **Eso** = 11 bodov
   - **Desať** = 10 bodov
   - **Kráľ** = 4 body
   - **Zvršok** = 3 body
   - **Spodok** = 2 body
   - **7, 8, 9** = Hodnota na karte (7, 8, 9 bodov)
3. **Kráľovské Oko**: Ak získaš presne **dve Esá** ako prvé dve karty (hodnota 22), vyhrávaš okamžite s **výplatou 2:1**!
4. **Pravidlo bankára**: Bankár si musí ťahať ďalšiu kartu, ak má menej ako **15 bodov**. Ak má **15 alebo viac**, musí stáť.

---

## 🚀 How to Run / Ako hrať

1. Open your terminal.
2. Clone this repository and navigate to the directory:
   ```bash
   git clone <your-repository-url>
   cd ocko
   ```
3. Make the script executable:
   ```bash
   chmod +x game.py
   ```
4. Start the game:
   ```bash
   ./game.py
   ```

---

## 🛠 Requirements / Požiadavky

* **Python 3.x**
* A modern terminal emulator that supports **Unicode character set** and **ANSI escape color codes** (standard on Linux/macOS).
