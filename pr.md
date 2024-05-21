## Exercicio 1

### Classes

- Animal
- Cachorro
- Fazenda
- Localidade
- Pessoa
- Produto
- TrabalhadorTemporario
- Trator

#### Queries

1.

PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT (COUNT(DISTINCT ?class) AS ?numClasses) WHERE {
  ?class a owl:Class.
}


2.

PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT (COUNT(DISTINCT ?property) AS ?numObjectProperties) WHERE {
  ?property a owl:ObjectProperty.
}

3.

PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT (COUNT(DISTINCT ?individual) AS ?numIndividuals) WHERE {
  ?individual a owl:NamedIndividual.
}

4.

PREFIX : <http://rpcw.di.uminho.pt/2024/historia/>
SELECT ?nome WHERE {
  ?tomate a :Produto ;
    :nomeProduto "Tomate" .
  ?fazenda a :Fazenda ;
   :cultiva ?tomate .
  ?pessoa a :Pessoa ;
    :nomePessoa ?nome ;
    :temFazenda ?fazenda .
}


5.

PREFIX : <http://rpcw.di.uminho.pt/2024/historia/>
SELECT ?nome WHERE {
  ?trabalhador a :TrabalhadorTemporario .
  ?fazenda a :Fazenda ;
   :contrata ?trabalhador .
  ?pessoa a :Pessoa ;
    :nomePessoa ?nome ;
    :temFazenda ?fazenda .
}


## Exercicio 2

11.

PREFIX : <http://www.example.org/disease-ontology#>
SELECT (COUNT(?doenca) AS ?numDoencas) WHERE {
  ?doenca a :Disease .
}


PREFIX : <http://www.example.org/disease-ontology#>
SELECT ?doenca WHERE {
  ?doenca a :Disease ;
          :hasSymptom :yellowish_skin .
}


PREFIX : <http://www.example.org/disease-ontology#>
SELECT ?doenca WHERE {
  ?doenca a :Disease ;
          :hasTreatment :exercise .
}


PREFIX : <http://www.example.org/disease-ontology#>
SELECT ?nome
WHERE {
  ?doente a :Patient ;
     :name ?nome
    
}
ORDER BY ?nome


12.

PREFIX : <http://www.example.org/med_doentes#>

CONSTRUCT {
  ?patient :hasDisease ?disease .
}
WHERE {
  ?patient a :Patient ;
           :exhibitsSymptom ?symptom .
  ?disease a :Disease ;
           :hasSymptom ?symptom .
}

13.

PREFIX : <http://www.example.org/disease-ontology#>

SELECT ?disease (COUNT(?patient) AS ?numPatients) WHERE {
  ?patient a :Patient ;
           :hasDisease ?disease .
}
GROUP BY ?disease
ORDER BY DESC(?numPatients)

14.


PREFIX : <http://www.example.org/med_doentes#>

SELECT ?symptom (COUNT(?disease) AS ?numDiseases) WHERE {
  ?disease a :Disease ;
           :hasSymptom ?symptom .
}
GROUP BY ?symptom ORDER BY DESC(?numDiseases)


------------------------------------


PREFIX : <http://www.example.org/med_doentes#>

SELECT ?treatment (COUNT(?disease) AS ?numDiseases) WHERE {
  ?disease a :Disease ;
           :hasTreatment ?treatment .
}
GROUP BY ?treatment ORDER BY DESC(?numDiseases)


