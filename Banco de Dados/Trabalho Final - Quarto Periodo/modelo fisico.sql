/* logico_Imobiliaria: */

CREATE TABLE Imoveis (
    id_imovel INTEGER PRIMARY KEY,
    valor_comissao FLOAT,
    estatus VARCHAR(50),
    categoria VARCHAR(50),
    data_construcao DATE,
    data_cadastro DATE,
    endereco VARCHAR(255),
    bairro VARCHAR(100),
    id_cliente_proprietario INTEGER,
    id_cliente_usuario INTEGER,
    id_funcionario INTEGER,
    data_aluguel_venda DATE,
    valor_sugerido FLOAT,
    valor_real FLOAT
);

CREATE TABLE Fotos_imovel (
    id_foto INTEGER PRIMARY KEY,
    id_imovel INTEGER,
    nome_arquivo VARCHAR(255)
);

CREATE TABLE Casas (
    id_imovel INTEGER PRIMARY KEY,
    qtd_quartos INTEGER,
    qtd_suites INTEGER,
    qtd_salas_estar INTEGER,
    qtd_salas_jantar INTEGER,
    nmr_vagas_garagem INTEGER,
    area_metros_quadrados INTEGER,
    possui_armario_embutido BOOLEAN,
    descricao VARCHAR(255)
);

CREATE TABLE Apartamentos (
    id_imovel INTEGER PRIMARY KEY,
    andar INTEGER,
    valor_condominio INTEGER,
    qtd_quartos INTEGER,
    portaria_24hrs BOOLEAN,
    qtd_salas_estar INTEGER,
    qtd_salas_jantar INTEGER,
    nmr_vagas_garagem INTEGER,
    area_metros_quadrados FLOAT,
    possui_armario_embutido BOOLEAN,
    descricao VARCHAR(255)
);

CREATE TABLE Salas_Comerciais (
    id_imovel INTEGER PRIMARY KEY,
    area_metros_quadrados FLOAT,
    qtd_banheiros INTEGER,
    qtd_comodos INTEGER
);

CREATE TABLE Terrenos (
    id_imovel INTEGER PRIMARY KEY,
    area_metros_quadrados FLOAT,
    largura FLOAT,
    comprimento FLOAT,
    aclive_declive VARCHAR(50)
);

CREATE TABLE Historico_Atualizacao (
    id_historico INTEGER PRIMARY KEY,
    id_imovel INTEGER,
    tipo_atualizacao VARCHAR(50),
    data_atualizacao DATE,
    detalhes VARCHAR(255)
);

CREATE TABLE Avaliacoes_Imoveis (
    id_avaliacao INTEGER,
    id_imovel INTEGER,
    id_cliente INTEGER,
    data_avaliacao DATE,
    nota FLOAT,
    comentario VARCHAR(255)
);

CREATE TABLE Funcionarios (
    id_funcionario INTEGER PRIMARY KEY,
    id_cargo INTEGER,
    usuario VARCHAR(50),
    nome VARCHAR(100),
    senha VARCHAR(50),
    telefone INTEGER,
    cpf INTEGER,
    endereco VARCHAR(255),
    telefone_contato VARCHAR(20),
    telefone_celular VARCHAR(20),
    data_ingresso DATE
);

CREATE TABLE Transacoes (
    id_transacao INTEGER PRIMARY KEY,
    id_imovel INTEGER,
    id_cliente INTEGER,
    id_funcionario INTEGER,
    data_transacao DATE,
    nro_contato INTEGER,
    id_forma_pag INTEGER
);

CREATE TABLE Formas_Pagamento (
    id_forma_pag INTEGER PRIMARY KEY,
    nome_forma_pag VARCHAR(50)
);

CREATE TABLE Clientes (
    id_clientes INTEGER PRIMARY KEY,
    profissao VARCHAR(50),
    cpf INTEGER,
    nome VARCHAR(100),
    endereco VARCHAR(255),
    telefones INTEGER,
    email VARCHAR(100),
    sexo VARCHAR(10),
    estado_civil VARCHAR(20)
);

CREATE TABLE Clientes_Indicados (
    id_clientes INTEGER,
    nome VARCHAR(100),
    cpf FLOAT
);

CREATE TABLE Clientes_Fiadores (
    id_cliente INTEGER,
    nome VARCHAR(100),
    cpf FLOAT
);

CREATE TABLE Cargos (
    id_cargo INTEGER PRIMARY KEY,
    nome_cargo VARCHAR(50),
    salario_base FLOAT
);

-- Adicionando chaves estrangeiras

ALTER TABLE Imoveis ADD CONSTRAINT FK_Imoveis_1
    FOREIGN KEY (id_cliente_proprietario)
    REFERENCES Clientes (id_clientes);

ALTER TABLE Imoveis ADD CONSTRAINT FK_Imoveis_2
    FOREIGN KEY (id_cliente_usuario)
    REFERENCES Clientes (id_clientes);

ALTER TABLE Imoveis ADD CONSTRAINT FK_Imoveis_3
    FOREIGN KEY (id_funcionario)
    REFERENCES Funcionarios (id_funcionario);

ALTER TABLE Fotos_imovel ADD CONSTRAINT FK_Fotos_imovel_1
    FOREIGN KEY (id_imovel)
    REFERENCES Imoveis (id_imovel);

ALTER TABLE Casas ADD CONSTRAINT FK_Casas_1
    FOREIGN KEY (id_imovel)
    REFERENCES Imoveis (id_imovel);

ALTER TABLE Apartamentos ADD CONSTRAINT FK_Apartamentos_1
    FOREIGN KEY (id_imovel)
    REFERENCES Imoveis (id_imovel);

ALTER TABLE Salas_Comerciais ADD CONSTRAINT FK_Salas_Comerciais_1
    FOREIGN KEY (id_imovel)
    REFERENCES Imoveis (id_imovel);

ALTER TABLE Terrenos ADD CONSTRAINT FK_Terrenos_1
    FOREIGN KEY (id_imovel)
    REFERENCES Imoveis (id_imovel);

ALTER TABLE Historico_Atualizacao ADD CONSTRAINT FK_Historico_Atualizacao_1
    FOREIGN KEY (id_imovel)
    REFERENCES Imoveis (id_imovel);

ALTER TABLE Avaliacoes_Imoveis ADD CONSTRAINT FK_Avaliacoes_Imoveis_1
    FOREIGN KEY (id_imovel)
    REFERENCES Imoveis (id_imovel);

ALTER TABLE Avaliacoes_Imoveis ADD CONSTRAINT FK_Avaliacoes_Imoveis_2
    FOREIGN KEY (id_cliente)
    REFERENCES Clientes (id_clientes);

ALTER TABLE Funcionarios ADD CONSTRAINT FK_Funcionarios_1
    FOREIGN KEY (id_cargo)
    REFERENCES Cargos (id_cargo);

ALTER TABLE Transacoes ADD CONSTRAINT FK_Transacoes_1
    FOREIGN KEY (id_imovel)
    REFERENCES Imoveis (id_imovel);

ALTER TABLE Transacoes ADD CONSTRAINT FK_Transacoes_2
    FOREIGN KEY (id_cliente)
    REFERENCES Clientes (id_clientes);

ALTER TABLE Transacoes ADD CONSTRAINT FK_Transacoes_3
    FOREIGN KEY (id_funcionario)
    REFERENCES Funcionarios (id_funcionario);

ALTER TABLE Transacoes ADD CONSTRAINT FK_Transacoes_4
    FOREIGN KEY (id_forma_pag)
    REFERENCES Formas_Pagamento (id_forma_pag);

ALTER TABLE Clientes_Indicados ADD CONSTRAINT FK_Clientes_Indicados_1
    FOREIGN KEY (id_clientes)
    REFERENCES Clientes (id_clientes);

ALTER TABLE Clientes_Fiadores ADD CONSTRAINT FK_Clientes_Fiadores_1
    FOREIGN KEY (id_cliente)
    REFERENCES Clientes (id_clientes);
