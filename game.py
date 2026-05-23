#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import os
import sys
import time

# --- ANSI Colors for Terminal ---
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# Text Colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright/Bold Text Colors
B_RED = "\033[91m"
B_GREEN = "\033[92m"
B_YELLOW = "\033[93m"
B_BLUE = "\033[94m"
B_MAGENTA = "\033[95m"
B_CYAN = "\033[96m"

# Backgrounds
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"

# --- Game Translations & Localisation Data ---
CURRENT_LANG = 'sk'  # Default to Slovak as requested!

LOCALES = {
    'en': {
        'rules_title': "TRADITIONAL RULES of OČKO (Slovak 21):",
        'rule_1': "Goal: Reach exactly 21 points (or as close as possible) without exceeding it.",
        'rule_2': "Card Deck: 32 German/Mariáš cards (7, 8, 9, 10, J, Q, K, A).",
        'rule_3': "Card Values:",
        'rule_4': "Special Payout: Kráľovské Oko (Royal Eye) 👑\n   * If you get exactly TWO ACES as your first two cards (value 22), you win instantly! (Pays out 2:1)",
        'rule_5': "Dealer's Rule:\n   * The banker must draw another card if their score is under 15.\n   * The banker must stand if their score is 15 or more.",
        'press_enter': "Press [ENTER] to return to the main menu...",
        'wallet': "Your Current Chips",
        'enter_bet': "Enter your bet (min $1, max ${max_bet}): ",
        'invalid_bet': "Invalid amount. You can bet between $1 and ${max_bet}.",
        'valid_number': "Please enter a valid whole number.",
        'dealer_hand': "DEALER'S HAND",
        'your_hand': "YOUR HAND",
        'score': "Score",
        'active_bet': "Active Bet",
        'royal_eye_msg': "👑 KRÁĽOVSKÉ OKO (Royal Eye)! Two Aces! 👑",
        'exactly_21': "Exactly 21! Standing automatically.",
        'busted_msg': "💥 BUSTED! You went over 21! ({score} points)",
        'hit_stand_prompt': "Do you want to [{g}H{r}]it (Daj) or [{y}S{r}]tand (Dosť)? ",
        'drawing_card': "Drawing card...",
        'dealer_royal': "Dealer got KRÁĽOVSKÉ OKO (Royal Eye)!",
        'dealer_busted': "💥 Dealer BUSTED! ({score} points)",
        'dealer_stands': "Dealer stands on {score} points.",
        'dealer_draws': "Dealer has under 15 ({score}). Dealer draws card...",
        'final_hands': "FINAL HANDS",
        'res_royal': "🎉 RESULT: WINNER! You won with Kráľovské Oko! (2:1 Payout)",
        'res_bust': "😭 RESULT: BUST! You went over 21. You lose your bet.",
        'res_dealer_royal': "😭 RESULT: DEALER WINNER! Dealer hit Kráľovské Oko!",
        'res_dealer_bust': "🎉 RESULT: WINNER! Dealer busted!",
        'res_win': "🎉 RESULT: WINNER! Your {p_score} beat Dealer's {d_score}.",
        'res_lose': "😭 RESULT: LOSE! Dealer's {d_score} beat your {p_score}.",
        'res_tie': "🤝 RESULT: TIE! (Remíza) You both got {p_score} points. Your bet is returned.",
        'press_continue': "Press [ENTER] to continue to next round...",
        'welcome': "Welcome to Očko, the authentic Slovak Twenty-One Game!",
        'menu_play': "Play Game",
        'menu_rules': "Read Rules & Card Values",
        'menu_lang': "Change Language / Zmeniť jazyk",
        'menu_quit': "Quit Game",
        'bankrupt': "💀 GAME OVER! You went bankrupt.",
        'resetting': "You are out of chips! Resetting wallet to $100...",
        'play_again': "Do you want to play another round? (y/n): ",
        'quit_msg': "Thank you for playing Očko! Dovidenia! 👋",
        'invalid_opt': "Invalid option. Please try again.",
        'card_names': {
            '7': 'Seven (7)',
            '8': 'Eight (8)',
            '9': 'Nine (9)',
            '10': 'Ten (10)',
            'J': 'Jack (Spodok)',
            'Q': 'Queen (Zvršok)',
            'K': 'King (Kráľ)',
            'A': 'Ace (Eso)'
        },
        'suit_names': {
            '♥': 'Hearts (Červene)',
            '♦': 'Bells (Gule)',
            '♣': 'Leaves (Zelene)',
            '♠': 'Acorns (Žalude)'
        }
    },
    'sk': {
        'rules_title': "TRADIČNÉ PRAVIDLÁ OČKA (Slovenská 21):",
        'rule_1': "Cieľ: Dosiahnuť presne 21 bodov (alebo čo najbližšie) a neprekročiť túto hodnotu.",
        'rule_2': "Hrací balík: 32 nemeckých/mariášových kariet (7, 8, 9, 10, Spodok, Zvršok, Kráľ, Eso).",
        'rule_3': "Hodnoty kariet:",
        'rule_4': "Špeciálna kombinácia: Kráľovské Oko 👑\n   * Ak dostaneš presne DVE ESÁ ako prvé dve karty (hodnota 22), vyhrávaš okamžite! (Výplata 2:1)",
        'rule_5': "Pravidlo pre bankára:\n   * Bankár si musí ťahať ďalšiu kartu, ak má menej ako 15 bodov.\n   * Bankár musí stáť (nebrať viac), ak má 15 alebo viac bodov.",
        'press_enter': "Stlač [ENTER] pre návrat do hlavného menu...",
        'wallet': "Tvoje žetóny",
        'enter_bet': "Zadaj svoju stávku (min $1, max ${max_bet}): ",
        'invalid_bet': "Neplatná suma. Môžeš staviť medzi $1 a ${max_bet}.",
        'valid_number': "Prosím, zadaj platné celé číslo.",
        'dealer_hand': "BANKÁROVA RUKA (DEALER)",
        'your_hand': "TVOJA RUKA",
        'score': "Skóre",
        'active_bet': "Aktívna stávka",
        'royal_eye_msg': "👑 KRÁĽOVSKÉ OKO! Dve esá! 👑",
        'exactly_21': "Presne 21! Stojíš automaticky.",
        'busted_msg': "💥 PRASKOL SI! Prekročil si 21! ({score} bodov)",
        'hit_stand_prompt': "Chceš [{g}D{r}]ať kartu (Hit) alebo ti [{y}S{r}]tačí (Stand)? ",
        'drawing_card': "Ťahám kartu...",
        'dealer_royal': "Bankár dosiahol KRÁĽOVSKÉ OKO!",
        'dealer_busted': "💥 Bankár PRASKOL! ({score} bodov)",
        'dealer_stands': "Bankár stojí s {score} bodmi.",
        'dealer_draws': "Bankár má menej ako 15 ({score}). Ťahá kartu...",
        'final_hands': "KONEČNÉ KARTY",
        'res_royal': "🎉 VÝSLEDOK: VÝHRA! Vyhral si s Kráľovským Okom! (Výplata 2:1)",
        'res_bust': "😭 VÝSLEDOK: PREHRA! Prekročil si 21 bodov a strácaš stávku.",
        'res_dealer_royal': "😭 VÝSLEDOK: PREHRA! Bankár dosiahol Kráľovské Oko!",
        'res_dealer_bust': "🎉 VÝSLEDOK: VÝHRA! Bankár praskol!",
        'res_win': "🎉 VÝSLEDOK: VÝHRA! Tvojich {p_score} bodov porazilo bankárových {d_score} bodov.",
        'res_lose': "😭 VÝSLEDOK: PREHRA! Bankárových {d_score} bodov porazilo tvojich {p_score} bodov.",
        'res_tie': "🤝 VÝSLEDOK: REMÍZA! Obaja máte {p_score} bodov. Stávka sa ti vracia.",
        'press_continue': "Stlač [ENTER] pre pokračovanie do ďalšieho kola...",
        'welcome': "Vitaj v Očku, tradičnej slovenskej kartovej hre 21!",
        'menu_play': "Hrať hru",
        'menu_rules': "Zobraziť pravidlá a hodnoty kariet",
        'menu_lang': "Zmeniť jazyk / Change Language",
        'menu_quit': "Ukončiť hru",
        'bankrupt': "💀 KONIEC HRY! Zbankrotoval si.",
        'resetting': "Nemáš žiadne žetóny! Obnovujem peňaženku na $100...",
        'play_again': "Chceš hrať ďalšie kolo? (a/n): ",
        'quit_msg': "Ďakujeme za hranie Očka! Dovidenia! 👋",
        'invalid_opt': "Neplatná voľba. Skús to znova.",
        'card_names': {
            '7': 'Sedem (7)',
            '8': 'Osem (8)',
            '9': 'Deväť (9)',
            '10': 'Desať (10)',
            'J': 'Spodok (Jack)',
            'Q': 'Zvršok (Queen)',
            'K': 'Kráľ (King)',
            'A': 'Eso (Ace)'
        },
        'suit_names': {
            '♥': 'Červene (Hearts)',
            '♦': 'Gule (Bells)',
            '♣': 'Zelene (Leaves)',
            '♠': 'Žalude (Acorns)'
        }
    }
}

SUITS_COLORS = {
    '♥': B_RED,
    '♦': B_YELLOW,
    '♣': B_GREEN,
    '♠': B_BLUE
}

VALUES = {
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 2,
    'Q': 3,
    'K': 4,
    'A': 11
}


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = VALUES[rank]

    def get_localized_name(self):
        rank_name = LOCALES[CURRENT_LANG]['card_names'][self.rank]
        suit_name = LOCALES[CURRENT_LANG]['suit_names'][self.suit]
        color = SUITS_COLORS[self.suit]
        return f"{color}{rank_name} ({suit_name}) {self.suit}{RESET}"

    def to_ascii_lines(self, hidden=False):
        """Renders an ASCII playing card."""
        if hidden:
            return [
                "┌─────────┐",
                "│░░░░░░░░░│",
                "│░░░ O ░░░│",
                "│░░░ Č ░░░│",
                "│░░░ K ░░░│",
                "│░░░ O ░░░│",
                "└─────────┘"
            ]

        color = SUITS_COLORS[self.suit]
        rank_str = self.rank
        r_space_left = f"{rank_str} " if len(rank_str) == 1 else rank_str
        r_space_right = f" {rank_str}" if len(rank_str) == 1 else rank_str

        return [
            f"┌─────────┐",
            f"│ {color}{r_space_left}{RESET}      │",
            f"│         │",
            f"│    {color}{self.suit}{RESET}    │",
            f"│         │",
            f"│      {color}{r_space_right}{RESET} │",
            f"└─────────┘"
        ]


class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        # 32 Mariáš cards
        self.cards = [Card(rank, suit) for suit in SUITS_COLORS.keys() for rank in VALUES.keys()]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            self.reset()
            self.shuffle()
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_score(self):
        # Kráľovské oko (Royal Eye): exactly 2 Aces = 22 points
        if len(self.cards) == 2 and all(c.rank == 'A' for c in self.cards):
            return 22
        return sum(card.value for card in self.cards)

    def is_royal_eye(self):
        return len(self.cards) == 2 and all(c.rank == 'A' for c in self.cards)

    def is_bust(self):
        if self.is_royal_eye():
            return False
        return self.get_score() > 21

    def render(self, hide_first=False):
        if not self.cards:
            return ""
        
        card_lines = []
        for i, card in enumerate(self.cards):
            if i == 0 and hide_first:
                card_lines.append(card.to_ascii_lines(hidden=True))
            else:
                card_lines.append(card.to_ascii_lines(hidden=False))

        joined_lines = []
        for line_idx in range(7):
            joined_lines.append("  ".join(lines[line_idx] for lines in card_lines))
        
        return "\n".join(joined_lines)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner():
    banner = f"""
{B_YELLOW}████████████████████████████████████████████████████████████████{RESET}
{B_RED}             ▀▄ ▄▀{RESET}
{B_RED}   ██████╗  ██████╗██╗  ██╗ ██████╗     {B_YELLOW}╔════╗╔════╗╔════╗╔════╗{RESET}
{B_RED}  ██╔═══██╗██╔════╝██║ ██╔╝██╔═══██╗    {B_YELLOW}║ 7  ║║ J  ║║ Q  ║║ A  ║{RESET}
{B_RED}  ██║   ██║██║     █████╔╝ ██║   ██║    {B_YELLOW}║  ♥ ║║  ♦ ║║  ♣ ║║  ♠ ║{RESET}
{B_RED}  ██║   ██║██║     ██╔═██╗ ██║   ██║    {B_YELLOW}║  7 ║║  J ║║  Q ║║  A ║{RESET}
{B_RED}  ╚██████╔╝╚██████╗██║  ██╗╚██████╔╝    {B_YELLOW}╚════╝╚════╝╚════╝╚════╝{RESET}
{B_RED}   ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝     {B_CYAN}Slovak Twenty-One Card Game{RESET}
{B_YELLOW}████████████████████████████████████████████████████████████████{RESET}
"""
    print(banner)


def show_rules():
    clear_screen()
    print_banner()
    
    loc = LOCALES[CURRENT_LANG]
    rules = f"""
{BOLD}{UNDERLINE}{loc['rules_title']}{RESET}

1. {loc['rule_1']}
2. {loc['rule_2']}
3. {BOLD}{loc['rule_3']}{RESET}
   * {B_CYAN}{loc['card_names']['A']}{RESET}  = {BOLD}11 bodov/points{RESET}
   * {B_CYAN}{loc['card_names']['10']}{RESET} = {BOLD}10 bodov/points{RESET}
   * {B_CYAN}{loc['card_names']['K']}{RESET}  = {BOLD}4 body/points{RESET}
   * {B_CYAN}{loc['card_names']['Q']}{RESET}  = {BOLD}3 body/points{RESET}
   * {B_CYAN}{loc['card_names']['J']}{RESET}  = {BOLD}2 body/points{RESET}
   * {B_CYAN}7, 8, 9{RESET}           = Face value (7, 8, 9 bodov/points)
   
4. {BOLD}{loc['rule_4']}{RESET}
     
5. {BOLD}{loc['rule_5']}{RESET}

{loc['press_enter']}"""
    print(rules)
    input()


def select_language():
    global CURRENT_LANG
    while True:
        clear_screen()
        print_banner()
        print("Select Game Language / Vyberte jazyk hry:\n")
        print(f" 1. {B_CYAN}English{RESET}")
        print(f" 2. {B_YELLOW}Slovenčina{RESET}")
        
        choice = input("\nChoice / Voľba (1-2): ").strip()
        if choice == '1':
            CURRENT_LANG = 'en'
            break
        elif choice == '2':
            CURRENT_LANG = 'sk'
            break


def play_round(deck, player_chips):
    loc = LOCALES[CURRENT_LANG]
    clear_screen()
    print_banner()
    
    print(f"💰 {loc['wallet']}: {B_GREEN}${player_chips}{RESET}")
    
    # --- Place Bet ---
    while True:
        try:
            bet_prompt = loc['enter_bet'].replace('${max_bet}', str(player_chips))
            bet_input = input(bet_prompt).strip()
            if not bet_input:
                continue
            bet = int(bet_input)
            if 1 <= bet <= player_chips:
                break
            else:
                invalid_msg = loc['invalid_bet'].replace('${max_bet}', str(player_chips))
                print(f"{B_RED}{invalid_msg}{RESET}")
        except ValueError:
            print(f"{B_RED}{loc['valid_number']}{RESET}")

    # Initialize Hands
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal initial cards (1 to player, 1 to dealer)
    player_hand.add_card(deck.draw())
    dealer_hand.add_card(deck.draw())

    player_bust = False
    player_royal_eye = False
    
    # --- Player's Turn ---
    while True:
        clear_screen()
        print_banner()
        
        # Display Current Hands
        print(f"💰 {loc['active_bet']}: {B_GREEN}${bet}{RESET}\n")
        
        print(f"=== {B_BLUE}{loc['dealer_hand']}{RESET} ===")
        print(dealer_hand.render())
        print(f"{loc['score']}: {B_CYAN}{dealer_hand.get_score()}{RESET}\n")

        print(f"=== {B_GREEN}{loc['your_hand']}{RESET} ===")
        print(player_hand.render())
        print(f"{loc['score']}: {B_YELLOW}{player_hand.get_score()}{RESET}")
        
        # Check immediate win conditions
        if player_hand.is_royal_eye():
            player_royal_eye = True
            print(f"\n{loc['royal_eye_msg']}")
            time.sleep(2)
            break
            
        if player_hand.get_score() == 21:
            print(f"\n✨ {loc['exactly_21']} ✨")
            time.sleep(1.5)
            break
            
        if player_hand.is_bust():
            player_bust = True
            print(f"\n{loc['busted_msg'].format(score=player_hand.get_score())}")
            time.sleep(2.5)
            break

        # Ask Player for action
        action_prompt = loc['hit_stand_prompt'].format(g=B_GREEN, y=B_YELLOW, r=RESET)
        action = input(action_prompt).strip().lower()
        # English and Slovak hit/stand commands
        if action in ['h', 'hit', 'd', 'daj', 'k', 'kartu']:
            print(f"\n{loc['drawing_card']}")
            time.sleep(0.8)
            player_hand.add_card(deck.draw())
        elif action in ['s', 'stand', 'dost', 'dosť', 'stoj']:
            break
        else:
            print(f"{B_RED}{loc['invalid_opt']}{RESET}")
            time.sleep(1)

    # --- Dealer's Turn ---
    dealer_bust = False
    dealer_royal_eye = False
    
    if not player_bust and not player_royal_eye:
        while True:
            clear_screen()
            print_banner()
            
            print(f"=== {B_BLUE}{loc['dealer_hand']}{RESET} ===")
            print(dealer_hand.render())
            dealer_score = dealer_hand.get_score()
            print(f"{loc['score']}: {B_CYAN}{dealer_score}{RESET}\n")

            print(f"=== {B_GREEN}{loc['your_hand']}{RESET} ===")
            print(player_hand.render())
            print(f"{loc['score']}: {B_YELLOW}{player_hand.get_score()}{RESET}\n")

            if dealer_hand.is_royal_eye():
                dealer_royal_eye = True
                print(loc['dealer_royal'])
                time.sleep(2)
                break

            if dealer_score > 21:
                dealer_bust = True
                print(loc['dealer_busted'].format(score=dealer_score))
                time.sleep(2)
                break

            if dealer_score >= 15:
                print(loc['dealer_stands'].format(score=dealer_score))
                time.sleep(1.5)
                break
            
            print(loc['dealer_draws'].format(score=dealer_score))
            time.sleep(1.5)
            dealer_hand.add_card(deck.draw())

    # --- Round Outcome / Payout ---
    clear_screen()
    print_banner()
    
    print(f"=== {B_BLUE}{loc['final_hands']}{RESET} ===\n")
    print(f"{loc['dealer_hand']} ({loc['score']}: {B_CYAN}{dealer_hand.get_score()}{RESET}):")
    print(dealer_hand.render())
    print()
    print(f"{loc['your_hand']} ({loc['score']}: {B_YELLOW}{player_hand.get_score()}{RESET}):")
    print(player_hand.render())
    print("\n" + "=" * 40 + "\n")

    p_score = player_hand.get_score()
    d_score = dealer_hand.get_score()

    if player_royal_eye:
        winnings = bet * 2
        print(loc['res_royal'])
        print(f"+${winnings}")
        player_chips += winnings
    elif player_bust:
        print(loc['res_bust'])
        print(f"-${bet}")
        player_chips -= bet
    elif dealer_royal_eye:
        print(loc['res_dealer_royal'])
        print(f"-${bet}")
        player_chips -= bet
    elif dealer_bust:
        print(loc['res_dealer_bust'])
        print(f"+${bet}")
        player_chips += bet
    elif p_score > d_score:
        print(loc['res_win'].format(p_score=p_score, d_score=d_score))
        print(f"+${bet}")
        player_chips += bet
    elif p_score < d_score:
        print(loc['res_lose'].format(p_score=p_score, d_score=d_score))
        print(f"-${bet}")
        player_chips -= bet
    else:
        print(loc['res_tie'].format(p_score=p_score))

    print("\n" + "=" * 40 + "\n")
    input(loc['press_continue'])
    return player_chips


def main():
    global CURRENT_LANG
    player_chips = 100
    deck = Deck()
    
    # Prompt language selection right at startup
    select_language()
    
    while True:
        loc = LOCALES[CURRENT_LANG]
        clear_screen()
        print_banner()
        print(loc['welcome'])
        print(f"💰 {loc['wallet']}: {B_GREEN}${player_chips}{RESET} in chips.\n")
        print(f"1. {loc['menu_play']}")
        print(f"2. {loc['menu_rules']}")
        print(f"3. {loc['menu_lang']}")
        print(f"4. {loc['menu_quit']}")
        
        choice = input("\nSelect / Vyberte (1-4): ").strip()
        if choice == '1':
            if player_chips <= 0:
                print(f"\n{B_RED}{loc['resetting']}{RESET}")
                player_chips = 100
                time.sleep(2)
            
            while player_chips > 0:
                deck.reset()
                deck.shuffle()
                player_chips = play_round(deck, player_chips)
                
                if player_chips <= 0:
                    clear_screen()
                    print_banner()
                    print(loc['bankrupt'])
                    time.sleep(3)
                    break
                
                clear_screen()
                print_banner()
                print(f"💰 {loc['wallet']}: {B_GREEN}${player_chips}{RESET}")
                again = input(loc['play_again']).strip().lower()
                # Accept both slovak 'a' (áno) and english 'y' (yes)
                if again not in ['a', 'ano', 'y', 'yes', '']:
                    break
        elif choice == '2':
            show_rules()
        elif choice == '3':
            select_language()
        elif choice == '4':
            print(f"\n{loc['quit_msg']}")
            break
        else:
            print(f"{B_RED}{loc['invalid_opt']}{RESET}")
            time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        loc = LOCALES[CURRENT_LANG]
        print(f"\n\nGame aborted. {loc['quit_msg']}")
        sys.exit(0)
