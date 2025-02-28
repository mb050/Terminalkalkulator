# Terminalkalkulator

En enkel kalkulator som er ment å kunne brukes fra en terminal. laget i python 3.8, og bruker
standard libraries. 

Når koden kjøres vil brukeren bli spurt om hvilken matematisk operasjon som skal brukes. 
disse vil komme opp i terminalen, og må bli skrevet slikt det blir spurt om. Man kan 
skrive inn 'help', for å få opp en mer detaljert beskrivelse av hva de ulike operastorene 
gjør, og hvordan de brukes. 

operator som kan velges:
	- valid operators:
	- sub --> subtraction
	- add --> addition
	- mul --> multiplication
	- div --> division
	- sqrt --> square root of first number
	- perc --> percentage:
	  - example: x% of y --> 5% of 100 = 5
	- sin --> sine of x, x is given in radians
	- cos --> cosine of x, x is given in radians
	- tan --> tangent of x, x is given in radians
	- log --> base e logarithm of x
	- log10 --> base 10 logarithm of x
	- fact --> the factorial of x, or simply x!

Deretter blir man spurt om å legge til verdiene som skal brukes under kalkulasjonen, og
resultatet blir printet ut i terminalen.




kalkulatoren aksepterer bruk av brøk, slik som 2/4. Alt på venstre side
av brøkstreken blir ansett som teller, og alt på høyre blir ansett som nevner. Den aksepterer $\pi$, skrevet
som pi, i kombinasjon med andre verdier.

Eksempel med bruk av pi og hvordan det blir tolket: 
  - pi $\Rightarrow$ $\pi$
  - 2*pi $\Rightarrow$ $2 \cdot \pi$
  - 2pi $\Rightarrow$ $2 \cdot \pi$ 
  - (2pi) $\Rightarrow$ $2 \cdot \pi$

Eksempel på bruk av brøk og pi: 
  - 5pi/3 $\Rightarrow$ $\frac{5\cdot \pi}{3}$
  - 2 * pi/3 $\Rightarrow$ $\frac{2\cdot \pi}{3}$
  - (4 * 5*pi)/(3 * 7) $\Rightarrow \frac{(4 \cdot 5 \cdot \pi)}{(3\cdot7)}$


