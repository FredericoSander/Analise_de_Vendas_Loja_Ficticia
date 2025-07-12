# Projeto de ETL em Python

## Sumário

1. [Visão Geral](#visão-geral)
2. [Arquitetura do Projeto](#arquitetura-do-projeto)
3. [Instalação e Configuração](#instalação-e-configuração)
4. [Estrutura de Pastas](#estrutura-de-pastas)
5. [Módulos do Sistema](#módulos-do-sistema)
6. [Fluxo de Execução](#fluxo-de-execução)
7. [Testes](#testes)
8. [Comandos Disponíveis](#comandos-disponíveis)
9. [Troubleshooting](#troubleshooting)
10. [Contribuição](#contribuição)

---

## Visão Geral

O **Projeto de ETL em Python** é um sistema de ETL (Extract, Transform, Load) desenvolvido em Python para processar e consolidar dados de vendas armazenados em múltiplos arquivos Excel. O projeto pode ser replicado em diversos processos que necessite de consolidação de dados de fontes com a mesma estrutura.

### Objetivo Principal
Automatizar o processo de consolidação de dados de vendas, transformando múltiplos arquivos Excel em um único arquivo processado para análise posterior.

### Tecnologias Utilizadas
- **Python 3.12+**: Linguagem principal
- **Pandas**: Manipulação e análise de dados
- **NumPy**: Operações numéricas
- **OpenPyXL**: Leitura e escrita de arquivos Excel
- **Poetry**: Gerenciamento de dependências
- **Pytest**: Framework de testes
- **MkDocs**: Geração de documentação (Em desenvolvimento)

---

## Arquitetura do Projeto

O projeto segue o padrão **ETL (Extract, Transform, Load)** com separação clara de responsabilidades:

```
Pipeline ETL
├── Extract (Extração)
│   └── Leitura de arquivos Excel da pasta raw
├── Transform (Transformação)
│   └── Concatenação dos DataFrames
└── Load (Carregamento)
    └── Salvamento do arquivo consolidado
```

### Princípios de Design Aplicados
- **Separação de Responsabilidades**: Cada módulo tem uma função específica
- **Modularidade**: Código organizado em módulos independentes
- **Reutilização**: Funções podem ser reutilizadas em outros contextos
- **Testabilidade**: Estrutura permite testes unitários eficazes

---

## Instalação e Configuração

### Pré-requisitos
- Python 3.12 ou superior
- Poetry (gerenciador de dependências)

### Passos de Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/FredericoSander/Projeto_de_ETL_em_Python
cd analise-vendas-loja-ficticia
```

2. **Configure a verssão correta do python com pyenv:**
```bash
Pyenv install 3.12.1
pyenv local 3.12.1
```

3. **Instalar o poerty configurar para o Python version 3.12.1 e ativar o ambiente virtual:**
```bash
pip install poetry
poetry env use 3.12.1
poetry shell
```

4. **Configurar as dependencias do projeto:**
```bash
poetry install
```

5. **Configure o pre-commit (opcional):**
```bash
pre-commit install
```

6. **Execute os teste para garantir que tudo esta funcionando como esperado:**
```bash
task test
```

7. **Execute o comando de execução da pipeline para realizar a ETL:**
```bash
task run
```

8. **Verifique na pasta data/processed se o arquivo foi gerado corretamente.**

---

## Estrutura de Pastas

```
analise-vendas-loja-ficticia/
├── src/
│   └── app/
│       ├── pipeline/
│       │   ├── extract.py      # Módulo de extração
│       │   ├── transform.py    # Módulo de transformação
│       │   └── load.py         # Módulo de carregamento
│       └── main.py             # Script principal
├── tests/
│   └── test_pipeline.py        # Testes unitários
├── data/
│   ├── raw/                    # Arquivos Excel originais
│   └── processed/              # Arquivos processados
├── docs/                       # Documentação
├── pyproject.toml              # Configurações do projeto
└── README.md                   # Documentação básica
```

---

## Módulos do Sistema

### 1. Módulo Extract (`extract.py`)

**Responsabilidade**: Extrair dados de arquivos Excel de um diretório específico.

**Função Principal**: `extract_from_excel(path: str) -> List[pd.DataFrame]`

**Funcionalidades**:
- Validação de existência do caminho
- Verificação se é um diretório válido
- Busca por arquivos .xlsx no diretório
- Leitura de cada arquivo Excel
- Tratamento de erros durante a leitura

**Exemplo de Uso**:
```python
from pipeline.extract import extract_from_excel

# Extrai dados de todos os arquivos Excel na pasta
dataframes = extract_from_excel("data/raw")
```

### 2. Módulo Transform (`transform.py`)

**Responsabilidade**: Transformar e consolidar os dados extraídos.

**Função Principal**: `concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame`

**Funcionalidades**:
- Concatenação de múltiplos DataFrames
- Reindexação automática para evitar conflitos
- Preservação da estrutura original dos dados

**Exemplo de Uso**:
```python
from pipeline.transform import concat_data_frames

# Concatena lista de DataFrames em um único DataFrame
df_consolidado = concat_data_frames(lista_dataframes)
```

### 3. Módulo Load (`load.py`)

**Responsabilidade**: Salvar os dados processados em arquivo Excel.

**Função Principal**: `load_excel(data_frame: pd.DataFrame, processed_path: str, file_name: str) -> str`

**Funcionalidades**:
- Criação automática de diretórios se não existirem
- Salvamento em formato Excel (.xlsx)
- Remoção do índice do DataFrame no arquivo final
- Confirmação de salvamento bem-sucedido

**Exemplo de Uso**:
```python
from pipeline.load import load_excel

# Salva DataFrame em arquivo Excel
resultado = load_excel(df, "data/processed", "vendas_consolidadas")
```

### 4. Script Principal (`main.py`)

**Responsabilidade**: Orquestrar todo o processo ETL.

**Fluxo de Execução**:
1. Extração dos dados da pasta `data/raw`
2. Transformação (concatenação) dos DataFrames
3. Carregamento do resultado na pasta `data/processed`

---

## Fluxo de Execução

### Execução Manual

```bash
# Usando Poetry
poetry run python src/app/main.py

# Ou usando o taskipy
poetry run task run
```

### Fluxo Detalhado

1. **Inicialização**: O script `main.py` é executado
2. **Extração**:
   - Verifica a pasta `data/raw`
   - Lê todos os arquivos .xlsx encontrados
   - Retorna lista de DataFrames
3. **Transformação**:
   - Recebe a lista de DataFrames
   - Concatena todos em um único DataFrame
   - Reindexiza para evitar conflitos
4. **Carregamento**:
   - Cria pasta `data/processed` se não existir
   - Salva o DataFrame consolidado como `vendas_consolidadas.xlsx`

---

## Testes

### Estrutura de Testes

O projeto utiliza **pytest** para testes unitários, seguindo o padrão **AAA (Arrange, Act, Assert)**:

```python
def testar_a_concatenação_da_lista_de_dataframe():
    # Arrange: Preparação dos dados de teste
    arrange = pd.concat([df_1, df_2, df_3], ignore_index=True)

    # Act: Execução da função a ser testada
    act = concat_data_frames([df_1, df_2, df_3])

    # Assert: Verificação do resultado
    assert arrange.equals(act)
```

### Executando os Testes

```bash
# Executa todos os testes
poetry run pytest -v

# Ou usando taskipy
poetry run task test
```

---

## Comandos Disponíveis

O projeto utiliza **taskipy** para automatizar tarefas comuns:

```bash
# Formatação de código
poetry run task format

# Execução de testes
poetry run task test

# Execução da aplicação
poetry run task run

# Encerrar processos na porta 8000
poetry run task kill
```

---

## Troubleshooting

### Problemas Comuns

#### 1. Erro: "FileNotFoundError"
**Causa**: Pasta `data/raw` não existe ou está vazia.
**Solução**: Crie a pasta e adicione arquivos .xlsx para processar.

#### 2. Erro: "No module named 'app'"
**Causa**: Ambiente virtual não está ativado.
**Solução**: Execute `poetry shell` antes de rodar o script.

#### 3. Erro na leitura de arquivos Excel
**Causa**: Arquivo corrompido ou em formato incompatível.
**Solução**: Verifique se os arquivos estão no formato .xlsx válido.

### Logs de Erro

O sistema exibe mensagens informativas para ajudar na identificação de problemas:

```python
# Exemplo de tratamento de erro
try:
    df = pd.read_excel(file)
except Exception as e:
    print(f"Erro ao ler o arquivo {file}: {e}")
```
---

## Contribuição

### Padrões de Código

O projeto segue as seguintes convenções:

- **PEP 8**: Padrão de estilo Python
- **Type Hints**: Tipagem estática para melhor legibilidade
- **Docstrings**: Documentação de funções em formato Google Style
- **Formatação**: Black e isort para formatação automática

### Processo de Contribuição

1. **Fork** o repositório
2. **Crie** uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. **Push** para a branch (`git push origin feature/nova-funcionalidade`)
5. **Abra** um Pull Request

### Qualidade de Código

Antes de submeter código, execute:

```bash
# Formatação
poetry run task format

# Testes
poetry run task test

# Linting
poetry run flake8 src/
```

---

## Notas Técnicas

### Dependências Principais

- **pandas**: Manipulação eficiente de dados tabulares
- **openpyxl**: Engine para leitura/escrita de arquivos Excel
- **numpy**: Operações numéricas otimizadas

### Dependências de Desenvolvimento

- **pytest**: Framework de testes
- **black**: Formatador de código
- **isort**: Organizador de imports
- **flake8**: Linter para verificação de código
- **mkdocs**: Geração de documentação

---

## Suporte

Para dúvidas ou problemas:

1. Verifique a seção [Troubleshooting](#troubleshooting)
2. Consulte os logs de erro
3. Abra uma issue no repositório
4. Entre em contato: sanderfn@hotmail.com

---

## Autor
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/136928502?s=96&v=4" width=115><br><sub>Frederico Sander</sub>](https://github.com/FredericoSander)
| :---: |

*Documentação gerada para o projeto Análise de Vendas Loja Fictícia - Versão 0.1.0*
