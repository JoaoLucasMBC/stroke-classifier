# Stroke Classifier
## Linear Algebra project utilizing linear regressions to create a classifier for information on possible stroke patients

Developers:

* João Lucas de Moraes Barros Cadorniga [JoaoLucasMBC](https://github.com/JoaoLucasMBC)  
* Eduardo Mendes Vaz [EduardoMVaz](https://github.com/EduardoMVAz)

This repository is an implementation of a Classifier which analyzes a data of patients and utilizes linear algebra principles such as linear regressions to try to predict the if the patients will have a stroke based on the information presented. It is an attempt of developing a Stroke Classifier, capable of receiving patient profiles and predicting if they will have a stroke.

---
<br/>

## Como Instalar

Para utilizar o projeto <em>"Stroke Classifier"</em>, você deve ter o Python instalado em seu computador e seguir os passos:

1. Clone o repositório na sua máquina na pasta de sua escolha. Utilize o comando:

`git clone https://github.com/JoaoLucasMBC/stroke-classifier.git`

2. Utilizando o terminal / a IDE de sua escolha, crie uma *Virtual Env* de Python e a ative:

`python -m venv env`

`env/Scripts/Activate.ps1` (Windows)

3. Mude para a pasta do <em>"Stroke Classifier"</em> e instale as bibliotecas requeridas:

`cd ./stroke-classifier`

`pip install -r requirements.txt`

4. Após a instalação, visualize as informações e demonstrações no arquivo *demo.ipynb* para ver o programa funcionando e os testes realizados por nós.

---
<br/>

## Como Utilizar


---
<br/>

## Modelo Matemático

---
<br/>

## Análise dos dados e conclusões
### Metodologia de Implementação
Implementamos dois classificadores com abordagens diferentes: Um classificador linear e um classificador de árvore de decisão.

Diversos testes durante a implementação e o desenvolvimento nos levaram a perceber que a perspectiva fornecida pela hipótese nula é extremamente pertinente, visto que a situação descrita se repetiu durante o desenvolvimento. Basicamente, os dados compreendiam aproximadamente 90% de patientes cujo status de AVC era negativo. Dessa forma, somente implementando o classificador, ele seguia o caminho da hipótese nula e "chutava" sempre que não haveria AVC, e alcançava uma acurácia de 95.36%.

Para evitar esse problema, realizamos uma poda do dataframe, criando um subset do dataframe que tivesse o mesmo número de pacientes que tiveram e que não tiveram AVC, com 498 pacientes ao todo. Implementando o classificador com essa resalva, obtivemos uma acurácia de 72.32% com o classificador linear e 66.07% com o classificador de árvore de decisão, que apesar de ser muito menor do que a acurácia encontrada sem a poda do dataframe, representa uma previsão muito menos enviesada, e que se aplicada em dados que não se comportassem como os dados que temos (distribuição mais uniforme, ou com proeminência de AVCs) seria mais ideal.

Após resolver esse impasse, calculamos quais são as 5 características de um paciente que mais corroboram para um AVC. Para realizar esse cálculo, realizamos 100 predições com cada classificador, salvando as informações do top 5 das características que mais apareceram em pacientes que tiveram AVC, e atribuíndo pontos para essas características. Toda vez que uma característica aparecia nesse top 5, ela ganhava "pontos" baseado na sua posição no rank (5 para a primeira, e diminuíndo progressivamente até a quinta, que recebia 1 ponto). Após as predições, as características que mais apareceram nesse top 5 foram: Ser idoso, ser adulto, obesidade, hipertensão, e um empate entre já ter sido casado e sobrepeso.

A partir dessa análise, as conclusões geradas foram de que as principais causas do AVC, segundo nossos dados, são a idade avançada e problemas relacionados a obesidade. Durante a contagem de pontos do top 5, a característica de ser idoso teve uma presença extremamente acentuada, ficando no topo na grande maioria das vezes. Os problemas relacionados com obesidade e sobrepeso somam para ter uma relevância alta também. 

Para chegar numa conclusão mais próxima da realidade e validar se nossas descobertas são pertinentes, comparamos essas descobertas com referências bibliográficas sobre o AVC.

### Referências Bibliográficas e Resultados Encontrados

Por ser uma das principais causas de morte súbita no mundo (mais de 150 mil casos por ano no Brasil), o AVC é extensamente estudado para definir suas principais causas. A descoberta prévia do AVC é fundamental para minimizar os danos, como por exemplo sequelas causadas pela paralisia cerebral do AVC. Portanto, comparar as descobertas feitas por nós com o classificador com estudos sobre o AVC é fundamental, tanto para validá-las, quanto para verificar se o classificador seria eficiente em um cenário real.

A primeira referência bibliográfica utilizada foi o artigo no [portal do ministério da saúde brasileiro](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/avc) sobre o AVC, onde a doença está definido e explicado, e também há uma lista das principais fatores de risco do AVC, sendo estes:

* Hipertensão, Colesterol Alto, Diabetes, Sedentarismo, Sobrepeso e Obesidade
* Tabagismo, Alcoolismo e uso de Drogas Ilícitas
* Idade Avançada, Histórico Familiar e Sexo Masculino

Analisando esses fatores de risco, podemos verificar que todas as características no nosso top 5 estão presentes nessa lista. Entre as características que estavamam listadas em nossos dados que também foram mencionadas mas não apareceram no top 5 estão: Tabagismo e Sexo Biológico. Esses dois são fatores de risco, o tabagismo por prejudicar o sistema respiratório e por consequência o cardiovascular, e o Sexo Masculino por características hereditárias.

O segundo material consultado foi a página de causas do AVC da [SBAVC (Sociedade Brasileira de AVC)](https://avc.org.br/pacientes/o-que-causa-um-avc/), onde as informações encontradas foram novamente reforçadas, numa lista de ações para combater o AVC:

* Que conheçam seus fatores de risco: hipertensão arterial, diabetes, colesterol alto ou fibrilação atrial
* Que sejam fisicamente ativas e exercitem-se regularmente.
* Que se evite o ganho de peso e a obesidade, mantendo uma dieta saudável.
* Que se limite o consumo de álcool.
* Que evitem o uso do cigarro.
* Que todos aprendam a reconhecer os sinais de alerta de um AVC.ao 

Novamente, os mesmos fatores de risco são mencionados: Obesidade, Tabagismo, Alcoolismo, Hipertensão, etc. 

Essa análise, tanto do ministério da saúde, quanto da SBAVC, nos permite confirmar que nossas descobertas refletem o mundo real, já que causas encontradas pelo nosso classificador estão todas entre os fatores de risco reconhecidos do AVC, mesmo que nem todas as causas mais importantes (Tabagismo por exemplo, que estava nos dados mas não ficou muito pronunciado no ranking) tenham sido definidas, provavelmente por enviesamento dos nossos dados.

Isso não significa que o classificador é eficaz e deve ser usado em situações reais, mas sim que ele foi capaz de perceber as principais causas do AVC, ao tentar realizar as predições.
