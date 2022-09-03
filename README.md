# Projeto exemplo para testes unitários em PYTHON com PYTEST

## Versões das principais dependências

- pytest-cov 3.0.0
- pytest 7.1.3
- python 3.10.1

Para ver a lista completa de depedências que foram adicionadas visite o arquivo 
https://github.com/izabelrodrigues/tests-python/blob/main/requirements.txt

## Comandos úteis

- pytest customizado no arquivo pytest.ini
```
pytest 
```
![image](https://user-images.githubusercontent.com/3687713/188285303-73f940c6-8885-4e42-b261-e100f2a2a233.png)

- pytest com report html em diretório customizado no arquivo .coveragerc
```
pytest --cov --cov-report html
```
#### Estrutura onde foi criado o diretório do report
![image](https://user-images.githubusercontent.com/3687713/188285387-bc46d0eb-d2b0-43f5-9a8c-8399a54c1f10.png)

#### Relatório HTML
![image](https://user-images.githubusercontent.com/3687713/188285448-dfe92eb7-7344-40b6-83e8-afdf5e9f8e65.png)

#### Linhas perdidas na cobertura
![Linhas perdidas na cobertura](https://user-images.githubusercontent.com/3687713/188285478-ded57165-769a-492e-b5d5-0edbd45e47a9.png)

## Outros tipos de relatórios

- Relatório padrão junitXML
```
pytest --junitxml report.xml
```
#### Estrutura e resultado: Gerado um arquivo chamado report.xml na raiz
![image](https://user-images.githubusercontent.com/3687713/188286731-3bfca30e-08df-4701-9f06-cd180c5b7289.png)
#### Relatório xml aberto via ide no browser ( open in -> browser )
![image](https://user-images.githubusercontent.com/3687713/188286743-d8ce9844-4e85-4f60-9ac4-4376298b874c.png)

- Relatório coverage xml
```
pytest --cov-report xml
```
#### Estrutura e resultado: Gerado um arquivo chamado coverage.xml na raiz
![image](https://user-images.githubusercontent.com/3687713/188286900-7b985cc9-3707-4598-af02-90e14ee084c2.png)
#### Relatório xml aberto via ide no browser ( open in -> browser )
![image](https://user-images.githubusercontent.com/3687713/188286934-c19b8728-d16a-457b-9c80-0eb6d200df79.png)


## Documentações de referência

- Marks pytest: https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark
- Configure options pytest.ini: https://docs.pytest.org/en/7.1.x/reference/reference.html#ini-options-ref
- Pytest-cov: https://pypi.org/project/pytest-cov/
- Lista de plugins para pytest: https://docs.pytest.org/en/7.1.x/reference/plugin_list.html
