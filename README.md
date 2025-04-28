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

-   [x] Reorganize project

-   [x] Make HUD

-   [x] Attacking
    -   [x] Attacking base generation
    -   [x] Attacking HUD
    -   [x] Attacking path-finding alg
    -   [x] Attacking troops
    -   [x] Manual routing
    -   [ ] Fight
-   [x] Building
    -   [x] Buildings
    -   [x] GUI
    -   [x] Prices
    -   [ ] Health of different buildings
    -   [ ] Fighting
-   [x] Resources

    -   [x] Elixir
    -   [x] Gold coins
    -   [ ] Maybe gems

-   [x] Database
    -   [x] Code
    -   [x] Saving
    -   [x] Loading
    -   [x] Attacks

### Dependencies

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

### RUN DOCKERFILE

`docker build -t clashofcastles-db .`

`docker run -d -p 3306:3306 --name clashofcastles-db-container clashofcastles-db`
