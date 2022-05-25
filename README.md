# Clash of Castles

Project for python class.

The game circles around popular clash of clans.

### Features

Въпреки че играта не е съвсем готова, основната и идея
е, че играчите могат да си направят база, която се запазва във база
и се използва за т.нар raid-ове, при които човек може да печели 
ресурси, за да продължава да разширява кралството си.

С добавена поддръжка на база данни играчите могат да имат запазена
база всеки път, когато влезнат в играта. Атаките са обновени, като
сега вкючват епична музика, която обаче не продължава дълго, тъй като
за да победиш в атаката, трябва да избягваш смъртоносните снайперисти, които
само чакат да останеш на едно място и те приключват. Но освен тях, трябва да
внимаваш да не се приближаваш прекалено много до оръдието, което те следи като
stalker и е напълно готово всеки миг да пусне гюлето и да удариш топа.

Играта стана забавна и ако бъде продължена може да се получи
наистина добра. Надявам се да съм показал потенциала си с кода,
който написах и да не съм допуснал много грешки, въпреки Unittest
библиотеката. Както и да е....

    Пожелавам Ви приятна игра!

### Todo
- [X] Reorganize project

- [X] Make HUD

- [X] Attacking
    - [X] Attacking base generation 
    - [X] Attacking HUD
    - [X] Attacking path-finding alg
    - [X] Attacking troops
    - [X] Manual routing
    - [ ] Fight
    
- [X] Building
    - [X] Buildings
    - [X] GUI
    - [x] Prices
    - [ ] Health of different buildings
    - [ ] Fighting
    
- [x] Resources
    - [x] Elixir
    - [x] Gold coins  
    - [ ] Maybe gems

- [X] Database
    - [X] Code
    - [X] Saving
    - [X] Loading
    - [X] Attacks

### Dependencies

`Pygame`

`Python 3.10.2`

`Time module`

`Mysql connector module`

`pymediainfo module` `os module`

`random module`

`MYSQL or MariaDB configuration in config.py`
`CONFIG FILE`
https://pastebin.com/RdabZPQL
