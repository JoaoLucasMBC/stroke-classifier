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

Para evitar o problema da hipótese nula (classificador sempre chutar o outcome mais frequente), realizamos uma poda do dataframe, criando um subset dele que tivesse o mesmo número de pacientes que tiveram ou não AVC. Com essa resalva, obtivemos uma acurácia menor, porém que representa uma previsão muito menos enviesada, e que se aplicada em dados que não se comportassem como os dados que temos seria mais ideal.

Calculamos então quais são as 5 características de um paciente que mais corroboram para um AVC. Para isso, realizamos 100 predições com cada classificador, salvando as informações do top 5 das características que mais apareceram em pacientes que tiveram AVC. Após as predições, as características que mais apareceram nesse top 5 foram: Ser idoso, ser adulto, obesidade e sobrepeso, hipertensão, e já ter sido casado.

A partir das análises, as conclusões geradas foram de que as principais causas do AVC são a idade avançada e problemas relacionados a obesidade. A característica de ser idoso teve uma presença extremamente acentuada, ficando no topo na grande maioria das vezes. Os problemas relacionados com obesidade e sobrepeso somam para ter uma relevância alta também. 

### Referências Bibliográficas e Resultados Encontrados

Por ser uma das principais causas de morte súbita no mundo, o AVC é extensamente estudado para definir suas principais causas. A descoberta prévia do AVC é fundamental para minimizar os danos, como por exemplo sequelas causadas pela paralisia cerebral. Portanto, comparamos as descobertas feitas por nós com o classificador com estudos sobre o AVC, para validá-las e para julgar a eficiência do classificador.

As referências bibliográficas utilizadas foram o artigo no [portal do ministério da saúde brasileiro](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/avc) sobre o AVC, e a página de causas do AVC da [SBAVC (Sociedade Brasileira de AVC)](https://avc.org.br/pacientes/o-que-causa-um-avc/), onde encontramos os principais fatores de risco do AVC, sendo estes:

* Hipertensão, Colesterol Alto, Diabetes, Sedentarismo, Sobrepeso e Obesidade
* Tabagismo, Alcoolismo e uso de Drogas Ilícitas
* Idade Avançada, Histórico Familiar e Sexo Masculino

Analisando esses fatores de risco, podemos verificar que todas as características no nosso top 5 estão presentes nessa lista. Entre as características que estavamam listadas em nossos dados que também foram mencionadas mas não apareceram no top 5 estão: Tabagismo e Sexo Biológico, o tabagismo por prejudicar o sistema respiratório e o cardiovascular, e o Sexo Masculino por características hereditárias.

Essa análise nos permite confirmar que nossas descobertas refletem o mundo real, já que causas encontradas pelo nosso classificador estão todas entre os fatores de risco reconhecidos do AVC. Isso não significa que o classificador é eficaz e deve ser usado em situações reais, mas sim que ele foi capaz de perceber as principais causas do AVC, ao tentar realizar as predições.
