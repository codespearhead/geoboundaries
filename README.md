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

| Cidade | Estado | Cargo | Gabinete | Assessor Responsável | Observação |Bairros Catalogados | Mapa Catalogado | Mapa Nomeado | Etapa 1 Finalizada |
|---|---|---|---|---|---|---|---|---|---|
| Americana | SP | - | - | David | Jornalista, Ex-assessor parlamentar | ✅ | ✅ | ✅ | ✅ |
| Barbacena | MG | Vereador | Odair Ferreira | Tamara Bruno | - |✅ | ✅ | ✅ | ✅ |
| Bela Vista | MS | Senador | Tereza Cristina | Gabriel Boccia | Atualmente não exerce função pública. É advogado, atual presidente do Rotary Club de Bela Vista. Já foi vice-prefeito (2017-2020), e na última eleição foi candidato a prefeito, a qual por pouco não ganhou. Pretende concorrer a prefeito novamente. | ❌ | ❌ | ❌ | ❌ |
| Belém | PA | Vereador | Matheus Cavalcante | O próprio | - | ✅ | ✅ | ✅ | ✅ |
| Boa Vista | RR | Vereador | Ruan Kenobby | Naira Rodrigues | - | ✅ | ✅ | ✅ | ✅ |
| Botelhos | MG | Vereador | Marcus Vinicius | O próprio | - | ✅ | ✅ | ✅ | ✅ |
| Brasília | DF | Deputado Distrital | Paula Belmonte | O próprio | - | ✅ | ✅ | ✅ | ✅ |
| Campo Grande | MS | Deputado Federal | Beto Pereira | O próprio | - | ✅ | ✅ | ✅ | ✅ |
| Caruaru | PE | - | - | Vitinho Maia | Candidato a Deputado Federal | ✅ | ✅ | ✅ | ✅ |
| Caucaia | CE | - | - | Ícaro Bonfim | Ex-assessor parlamentar de Vereador, de Deputado Estadual e de Vice-Prefeito | ✅ | ✅| ✅ | ✅ |
| Criciúma | SC | Vereador | Daniel Antunes | Cristyane Limas | - | ❌ | ❌ | ❌ | ❌ |
| Cuiabá | MT | Deputado Federal | Abilio Moumer | O próprio | - | ✅ | ✅ | ✅ | ✅ |
| Itamaraju | BA | - | - | Miguel Xavier | Liderança de Grupo Político | ✅ | ✅ | ✅ | ✅ |
| Itapema | SC | Vereador | Adriano Pivotto | Áxion Tridapalli | - | ✅ | ✅ | ✅ | ✅ |
| Maracás | BA | - | - | Jamon Soares | Afirma trabalhar no setor de Comunicação | ❌ | ❌ | ❌ | ❌ |
| Natal | RN | - | - | Paulo Ovídio | Candidato a Vereador | ✅ | ✅ | ✅ | ✅ |
| Paraíso do Tocantins | TO | Deputado Estadual | Nilton Franco | Renan Aires | - | ✅ | ✅ | ✅ | ✅ |
| Presidente Figueiredo | AM | - | - | Felipe Gonçalves | Assessor do Próprio GdA. Responsável a pedido do Deputado Federal Amom Mandel | ✅ | ✅ | ✅ | ✅ |
| Rio Claro | SP | Vereador | Carol Gomes | Andrey Sepulveda | - | ❌ | ❌ | ❌ | ❌ |
| São Carlos | SP | Vereador | Elton Carvalho | Gabriel Mesquita | - | ✅ | ✅ | ✅ | ✅ |
| São Paulo | SP | Deputado Federal | Tabata Amaral | Felipe Gonçalves | Assessor do Próprio GdA. Responsável a pedido do Deputado Federal Amom Mandel | ✅ | ✅ | ✅ | ✅ |
| Salinas | MG | Vereador | Arthur Bastos | O próprio | - | ✅ | ✅ | ✅ | ✅ |
| Silvânia | GO | Vereador | Matheus Brito | O próprio | - | ✅ | ✅ | ✅ | ✅ |
| Vitória da Conquista | BA | - | - | Wesley Brito | Candidato a Deputado Estadual | ✅ | ✅ | ✅ | ✅ |

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