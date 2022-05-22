# Clash of Castles

Project for python class.

The game circles around popular clash of clans.

### Todo
- [X] Reorganize project

- [X] Make HUD

- [ ] Attacking
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

- [ ] Database
    - [X] Code
    - [ ] Saving
    - [ ] Loading
    - [ ] Attacks
 
### Features

Въпреки че играта не е съвсем готова, основната и идея
е, че играчите могат да си направят база, която се запазва във база
и се използва за т.нар raid-ове, при които човек може да печели 
ресурси, за да продължава да разширява кралството си.

Готовите неща са показани отгоре, като крайния продукт би трябвало да
съдържа всичките характеристика на напълно завършена и забавна игра.

Нещата, които не съм успял да направя, ще мога да довърша до максимум
1 месец време, тъй като за повечето няма никакъв код в интернет и 
трябва да се четат документации.

Извинявам се за невключването на unit-test-ове, но всичко е тествано,
освен A*star pathfinding алгоритъма, който се смята за най-добър, но
всъщност има сравнително много проблеми, които не зависят от моя код. 

### Dependencies

`Pygame`

`Python 3.10.2`

`Time module`

`Mysql connector module`(Not used because of not enough time)

`pymediainfo module` `os module`