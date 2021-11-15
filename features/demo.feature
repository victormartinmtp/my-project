Feature: AnimeFLV

 Scenario: el 'ultimo episodeo es el 999
   Given chrome is up
   When the user get animeflv page
   And  the user clics one piece
   Then the las episode is the 999