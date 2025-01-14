# RSA Calculator

Dieses Programm implementiert den RSA-Verschlüsselungs- und Entschlüsselungsalgorithmus. Es bietet Funktionen zum Berechnen des größten gemeinsamen Teilers (GGT), des erweiterten GGT, des modularen Inversen, der schnellen Exponentiation und zum Berechnen der Eulerschen Phi-Funktion.

## Disclaimer
Wurde KI-Generiert. Keine Ahnung


## Voraussetzungen

- Python 3.x

## Verwendung

1. Führen Sie das Programm aus.
2. Geben Sie die Werte für `m`, `e` und `w` ein, wenn Sie dazu aufgefordert werden.
3. Das Programm zeigt die berechneten Werte und Zwischenschritte an.

## Funktionen

### `normal_gcd(a, b)`

Diese Funktion berechnet den GGT von zwei Zahlen `a` und `b` mit dem normalen euklidischen Algorithmus. Sie gibt auch die Schritte des Algorithmus aus.

### `extended_gcd(a, b)`

Diese Funktion berechnet den erweiterten GGT von zwei Zahlen `a` und `b` mit dem erweiterten euklidischen Algorithmus. Sie gibt den GGT sowie die Koeffizienten `x` und `y` zurück, sodass `ggT = x * a + y * b`. Sie gibt auch die Schritte des Algorithmus aus.

### `mod_inverse(a, m)`

Diese Funktion berechnet das modulare Inverse von `a` modulo `m` mit dem erweiterten euklidischen Algorithmus. Sie gibt `None` zurück, wenn das modulare Inverse nicht existiert.

### `fast_exp(base, exp, mod, rev = False)`

Diese Funktion führt eine schnelle Exponentiation von `base` hoch `exp` modulo `mod` durch. Sie gibt das Ergebnis zurück und gibt auch die binäre Darstellung von `exp`, alle Zwischenschritte und die verwendeten Schritte in der Berechnung aus.

### `calculate_phi(m)`

Diese Funktion berechnet die Eulersche Phi-Funktion (phi) von `m`, die die Anzahl der positiven ganzen Zahlen kleiner als `m` darstellt, die zu `m` teilerfremd sind.

### `main()`

Dies ist die Hauptfunktion des Programms. Sie fordert den Benutzer auf, Werte für `m`, `e` und `w` einzugeben, und führt dann den RSA-Verschlüsselungs- und Entschlüsselungsprozess durch.

## Beispiel

```
Gib m: 101
Gib e: 21
Gib w: 8

Gegeben:
m = 101
e = 21
w = 8


Lösung:
φ(m) = φ(101) = 100


EA:
100 = 4 * 21 + 16
21 = 1 * 16 + 5
16 = 3 * 5 + 1
5 = 5 * 1 + 0


EA rückwärts:
1 = 1 * 1 + 0 * 5
1 = -3 * 5 + 1 * 16
1 = 4 * 16 + -3 * 21
1 = -19 * 21 + 4 * 100


⇒ 1 = e * d ≡ 21 * -19 (mod 100)
⇒ d ≡ -19 ≡ 81 (mod 100)


Verschlüsselungm des Wortes w = 8:
Binärdarstellung von e = 21 = 10101
8 exp 1 ≡ 8 (mod 101)
8 exp 2 ≡ 64 (mod 101)
8 exp 4 ≡ 56 (mod 101)
8 exp 8 ≡ 5 (mod 101)
8 exp 16 ≡ 25 (mod 101)
⇒ c = 8 ∙ 56 ∙ 25 ≡ 90 (mod 101)


Entschlüsselung des Chiffrats c = 90:
Binärdarstellung von d = 81 = 1010001
90 exp 1 ≡ 90 (mod 101)
90 exp 2 ≡ 20 (mod 101)
90 exp 4 ≡ 97 (mod 101)
90 exp 8 ≡ 16 (mod 101)
90 exp 16 ≡ 54 (mod 101)
90 exp 32 ≡ 88 (mod 101)
90 exp 64 ≡ 68 (mod 101)
⇒ w' = 90 ∙ 54 ∙ 68 ≡ 8 (mod 101)
```

