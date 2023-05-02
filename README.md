# Stroke Classifier
## Linear Algebra project utilizing linear regressions to create a classifier for information on possible stroke patients

Developers:

* João Lucas de Moraes Barros Cadorniga [JoaoLucasMBC](https://github.com/JoaoLucasMBC)  
* Eduardo Mendes Vaz [EduardoMVaz](https://github.com/EduardoMVAz)

This repository is an implementation of a Classifier which analyzes a data of patients and utilizes linear algebra principles such as linear regressions to try to predict the if the patients will have a stroke based on the information presented. It is an attempt of developing a Stroke Classifier, capable of receiving patient profiles and predicting if they had a stroke.

---
<br/>

## Como Instalar & Utilizar

Para utilizar o projeto <em>"Stroke Classifier"</em>, você deve ter o Python instalado em seu computador e seguir os passos:

1. Clone o repositório na sua máquina na pasta de sua escolha. Utilize o comando:

`git clone https://github.com/JoaoLucasMBC/stroke-classifier.git`

2. Utilizando o terminal / a IDE de sua escolha, crie uma *Virtual Env* de Python e a ative:

`python -m venv env`

`env/Scripts/Activate.ps1` (Windows)

3. Mude para a pasta do <em>"Stroke Classifier"</em> e instale as bibliotecas requeridas:

`cd ./stroke-classifier`

`pip install -r requirements.txt`

4. Após a instalação, visualize as informações e demonstrações no arquivo `demo.ipynb` para ver o programa funcionando e os testes realizados por nós.

---
<br/>

## Modelo Matemático

Detalhes do modelo de cada classificador (tanto linear quanto por árvore de decisão) e do código utilizado se encontram tanto no arquivo `demo.ipynb`, quanto nos arquivos dos próprios classificadores, no diretório `classifiers`.

---
<br/>

## Análise dos dados e conclusões
### Metodologia de Implementação
Implementamos dois classificadores com abordagens diferentes: um linear e um de árvore de decisão. Enquanto o primeiro se baseia no conceito de descida do gradiente, o segundo utiliza de entropia para realizar suas predições¹.

Em ambos, a hipótese nula estudada era o classificador sempre chutar o outcome mais frequente da base de teste, o que determinaria que a acurácia não seria uma boa medida de desempenho. Ao encontramos esse viés no primeiro teste, realizamos uma poda do dataframe, criando um subset com o mesmo número de pacientes que tiveram ou não AVC. Com isso, obtivemos acurácia menor, porém, que representa uma previsão menos enviesada, desprovando a hipótese nula.

Calculamos, então, as 5 características de um paciente que mais corroboram para um AVC. Para isso, realizamos 100 predições com cada classificador, salvando as informações das top 5 importâncias. As características mais frequentes foram: senilidade, idade adulta, obesidade e sobrepeso, hipertensão, e já ter sido casado.

A partir das análises, as conclusões geradas foram que as principais causas do AVC são: idade avançada, obesidade e doenças vasculares. A primeira teve presença acentuada, ficando no topo na maioria das vezes. Os problemas relacionados com obesidade e sobrepeso somam também relevância alta.

### Referências Bibliográficas e Resultados Encontrados

Como uma das principais causas de morte no mundo, seus fatores de risco são extensamente estudados. A descoberta prévia do AVC é fundamental para minimizar sequelas, por exemplo, causadas pela paralisia cerebral. Portanto, comparamos os resultados com estudos sobre AVC, visando validá-las e julgar a eficiência do sistema.

As referências bibliográficas utilizadas foram o artigo no [portal do ministério da saúde brasileiro](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/avc) e a página de causas do AVC da [SBAVC (Sociedade Brasileira de AVC)](https://avc.org.br/pacientes/o-que-causa-um-avc/), onde encontramos os considerados hoje principais fatores de risco:

* Hipertensão, Colesterol Alto, Diabetes, Sedentarismo, Sobrepeso e Obesidade
* Tabagismo, Alcoolismo e uso de Drogas Ilícitas
* Idade Avançada, Histórico Familiar e Sexo Masculino

Analisando-os, verificamos que todas as características no top 5 estão presentes. Entre as que estavam listadas em nossos dados que também foram mencionadas, mas não apareceram nas 5 estão: Tabagismo e Sexo Biológico — o tabagismo por prejudicar o sistema respiratório e o cardiovascular, e o Sexo Masculino por características hereditárias.

Além disso, buscamos questionar a prevalência dos dois principais fatores: idade e obesidade. Uma hipótese possível é que eles não são fatores do AVC em si, mas levam aos reais causadores do acidente, como a hipertensão (citada também em análise). Por exemplo, um indivíduo idoso ou obeso tende a desenvolver esse tipo de doença vascular. Essas, sim, causadoras de acidentes vasculares cerebrais². Portanto, suas amplas presenças estariam ligadas a serem "genéricos". 

Essa análise nos permite confirmar que nossas descobertas refletem o mundo real, já que causas encontradas pelos classificadores estão entre os fatores de risco reconhecidos do AVC. Isso não significa que eles são eficazes e devem ser usados em produção, mas sim que foram capazes de perceber as principais causas na base de dados apresentada, ao realizar as predições.

---

¹Detalhes do modelo matemático no arquivo `demo.ipynb`  
²A correlação entre hipertensão e AVC's já é estudada há muitos anos, o que corrobora a nossa hipótese, em artigos como [este](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6659031/), da **Natural Library of Medicine**.
