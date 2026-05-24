# Očko (Slovak Twenty-One) - Terminal Game

A terminal-based implementation of the traditional Slovak/Czech card game Očko (similar to Blackjack), written in pure Python 3. The game uses a standard 32-card German deck (Mariáš) and features a basic AI banker, a virtual chips betting system, and a bilingual interface.

### Features / Vlastnosti
* **Deck / Balík:** 32-card German deck (7, 8, 9, 10, Jack/Spodok, Queen/Zvršok, King/Kráľ, Ace/Eso).
* **Visuals / Grafika:** ASCII art cards rendered side-by-side using Unicode and ANSI escape codes.
* **Bilingual / Dvojjazyčné:** Full English and Slovak support, selectable at startup.
* **Banker AI / AI Bankár:** Automated banker logic (draws on < 15, stands on 15+).

### Rules / Pravidlá hry

**Goal / Cieľ:**
Get a hand value as close to 21 points as possible without going over.
*Dosiahnuť celkové skóre čo najbližšie k 21 bodom a neprekročiť túto hodnotu.*

**Card Values / Hodnoty kariet:**
* Ace / Eso = 11
* Ten / Desiatka = 10
* King / Kráľ = 4
* Queen / Zvršok = 3
* Jack / Spodok = 2
* 7, 8, 9 = Face value / Hodnota na karte

**Special Rules / Špeciálne pravidlá:**
* **Kráľovské Oko:** Getting exactly two Aces as your first two cards (value 22) is an instant win with a 2:1 payout. *(Dve Esá ako prvé dve karty znamenajú okamžitú výhru s výplatou 2:1).*
* **Banker / Bankár:** The banker must draw if their score is under 15, and must stand if their score is 15 or more. *(Bankár musí ťahať kartu, ak má menej ako 15 bodov. Ak má 15 a viac, musí stáť).*

### How to Run / Ako hrať

Requires Python 3.x and a terminal with Unicode/ANSI color support (standard on Linux/macOS, Windows Terminal, or WSL). Zero external dependencies.

```bash
git clone <your-repository-url>
cd ocko
chmod +x game.py
./game.py
```

### License / Licencia
MIT License. See the LICENSE file for details.
