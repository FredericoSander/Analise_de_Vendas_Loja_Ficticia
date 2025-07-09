# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


flowchart LR<font></font>
    A[Start: Problem - Car won't start] --> B{Is the battery dead?}<font></font>
    B -- Yes --> C[Replace battery]<font></font>
    B -- No --> D{Is the fuel tank empty?}<font></font>
    D -- Yes --> E[Refill fuel tank]<font></font>
    D -- No --> F{Is the engine oil level low?}<font></font>
    F -- Yes --> G[Refill engine oil]<font></font>
    F -- No --> H[Consult a mechanic]<font></font>
    C --> I[End: Problem Solved]<font></font>
    E --> I<font></font>
    G --> I<font></font>
    H --> I



# Função de Extração de Dados

### ::: app.pipeline.extract.extract_from_excel

# Função de transformação de Dados

### ::: app.pipeline.transform.concat_data_frames

# Função de leitura dos dados

### ::: app.pipeline.load.load_excel
