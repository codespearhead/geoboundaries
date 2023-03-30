<h1 align="center"><a href="https://github.com/Paguiar735/geoboundaries">Geoboundaries</a></h1>

<p align="center">
    <br>
  <a href="https://pixabay.com/pt/vectors/brasil-geografia-mapa-estados-153881/">
    <img src="https://cdn.pixabay.com/photo/2013/07/12/18/47/brazil-153881_960_720.png" width="200px" height="200px"/>
  </a>
  <br><br>
    Download the vector file of the boundaries of administrative divisions anywhere in the world
  <br>
</p>

<br>

## Project Goal

Enable developers to generate updated vectors of boundaries of administrative divisions from OpenStreetMap via ready-to-go code snippets.

## Introduction

> **Note**: For other countries, pick a more appropriate tag you can find by looking through the tags of the desired administrative division in your country, which can by found by looking up some of said divisions on [OpenStreetMap](https://openstreetmap.org/).

TODO: Explain what OpenStreetMap and the Overpass API are

All examples can be run online via [Overpass Turbo](https://overpass-turbo.eu/).

TODO: Explain [ISO3166-2](https://pt.wikipedia.org/wiki/ISO_3166-2:BR)


## Extracted Cities

<br>

<details>
<summary>Click me</summary>
<br>

| Cidade | Assessor Responsável | Bairros Catalogados | Mapa Catalogado | Mapa Nomeado | Finished |
|---|---|---|---|---|---|
| Americana - SP | David | ✅ | ✅ | ✅ | ✅ |
| Barbacena - MG | Odair Ferreira | ✅ | ✅ | ✅ | ✅ |
| Belém - PA | Matheus Cavalcante | ✅ | ✅ | ✅ | ✅ |
| Boa Vista - RR | Naira Rodrigues | ✅ | ✅ | ✅ | ✅ |
| Botelhos - MG | Marcus Lima | ✅ | ✅ | ✅ | ✅ |
| Brasília - DF | Paula Belmonte | ✅ | ✅ | ✅ | ✅ |
| Campo Grande - MS | Beto Pereira | ✅ | ✅ | ✅ | ✅ |
| Caruaru - PE | Vitinho Maia | ✅ | ✅ | ✅ | ✅ |
| Caucaia - CE | Ícaro Bonfim | ✅ | ✅| ✅ | ✅ |
| Cuiabá - MT | Abilio Moumer | ❌ | ❌ | ❌ | ❌ |
| Itamaraju - BA | Miguel Xavier | ✅ | ✅ | ✅ | ✅ |
| Itapema - SC | Adriano Pivotto | ✅ | ✅ | ✅ | ✅ |
| Maracás - BA | Jamon | ❌ | ❌ | ❌ | ❌ |
| Natal - RN | Paulo Ovídio | ✅ | ✅ | ✅ | ✅ |
| Paraíso do Tocantins - TO | Renan Aires | ✅ | ✅ | ✅ | ✅ |
| Presidente Figueiredo - AM | ? | ✅ | ✅ | ✅ | ✅ |
| Rio Claro - SP | Andrey Sepulveda | ❌ | ❌ | ❌ | ❌ |
| São Carlos - SP | Gabriel Mesquita | ✅ | ✅ | ✅ | ✅ |
| São Paulo - SP | ? | ✅ | ✅ | ✅ | ✅ |
| Salinas - MG | Arthur Bastos | ✅ | ✅ | ✅ | ✅ |
| Silvânia - GO | Matheus Brito | ✅ | ✅ | ✅ | ✅ |
| Vitória da Conquista - BH | Wesley Brito | ✅ | ✅ | ✅ | ✅ |

<br>
</details>

<br>

## Code Snippets

1. Get all Brazilian territories / borders

```
[out:json];
rel["ISO3166-1"="BR"];
out geom;
```

2. Get all Brazilian Geographic Regions

```
[out:json];
area["ISO3166-1"="BR"];
relation["admin_level"="3"](area);
out geom;
```

3. Get all Brazilian States

```
[out:json];
area["ISO3166-1"="BR"];
relation["admin_level"="5"](area);
out geom;
```

4. Get a specific Brazilian State

```
[out:json];
area["ISO3166-1"="BR"]->.searchArea;
relation["ISO3166-2"="BR-AM"](area.searchArea);
out geom;
```

5. Get a specific Brazilian City

```
[out:json];
area["ISO3166-1"="BR"]->.searchArea;
relation["is_in:state"="Amazonas"]["name"="Manaus"](area.searchArea);
out geom;
```

6. Get all official neighborhoods in a Brazilian city (might be outdated)

```
[out:json];
area["ISO3166-1"="BR"]->.searchArea;
area["is_in:state"="Amazonas"]->.searchArea;
relation["admin_level"~"10"]["border_type"!="district"](area.searchArea);
out geom;
```