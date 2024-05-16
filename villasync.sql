go

create table Agente_imobiliario (
    pnome varchar(20),
    unome varchar(20),
    nif int,
    salario int,
    num_emp int,
    PRIMARY KEY (num_emp)
);

create table Cliente(
    pnome varchar(20),
    unome varchar(20),
    nif int,
    num_cliente int,
    PRIMARY KEY (num_cliente)
);

create table Propriedade(
    id int,
    localizacao varchar(30),
    num_empregado int,
    m_quadrados int,
    n_pisos int,
    n_quartos int,
    n_wc int,
    cert_energ varchar(20),
    garagem int,
    PRIMARY KEY (id),
    foreign key (num_empregado) references Agente_imobiliario(num_emp)
);

create table Visita(
    id int,
    data date,
    id_propriedade int,
    num_cliente int,
    PRIMARY KEY (id),
    foreign key (id_propriedade) references Propriedade(id),
    foreign key (num_cliente) references Cliente(num_cliente)
);

create table Contrato(
    id int,
    num_cliente int,
    valor_propriedade int,
    --assinatura,
    id_propriedade int,
    id_visita int,
    PRIMARY KEY (id),
    foreign key (id_propriedade) references Propriedade(id),
    foreign key (num_cliente) references Cliente(num_cliente)
); 

create table Anuncio(
    id int,
    titulo varchar(50),
    descricao varchar(50),
    id_contrato int,
    PRIMARY KEY (id),
    foreign key (id_contrato) references Contrato(id)
);

create table Avaliacao_imobiliaria(
    id_visita int,
    valor_apos_avaliacao int,
    PRIMARY KEY (id_visita),
    foreign key (id_visita) references Visita(id)
);

create table Apresentacao_imovel(
    id_visita int,
    PRIMARY KEY (id_visita),
    foreign key (id_visita) references Visita(id)
);

create table Moradia(
    id_propriedade int,
    area_exterior int,
    PRIMARY KEY (id_propriedade),
    foreign key (id_propriedade) references Propriedade(id)
);

create table Apartamento(
    id_propriedade int,
    andar int,
    elevador int,
    PRIMARY KEY (id_propriedade),
    foreign key (id_propriedade) references Propriedade(id)
);

create table Oferta(
    id int,
    estado varchar(20),
    valor int,
    id_anuncio int,
    num_cliente int,
    PRIMARY KEY (id),
    foreign key (id_anuncio) references Anuncio(id),
    foreign key (num_cliente) references Cliente(num_cliente)
);

INSERT INTO Agente_imobiliario (pnome, unome, nif, salario, num_emp, password)
VALUES ('John', 'Doe', 123456789, 50000, 1, 'agente');

-- Inserting data into Cliente
INSERT INTO Cliente (pnome, unome, nif, num_cliente, password)
VALUES ('Jane', 'Doe', 987654321, 1, 'cliente');

-- Inserting data into Propriedade
INSERT INTO Propriedade (id, localizacao, num_empregado, m_quadrados, n_pisos, n_quartos, n_wc, cert_energ, garagem)
VALUES (1, 'Lisbon', 1, 100, 2, 3, 2, 'A', 1);

-- Inserting data into Visita
INSERT INTO Visita (id, data, id_propriedade, num_cliente)
VALUES (1, '2022-01-01', 1, 1);

-- Inserting data into Contrato
INSERT INTO Contrato (id, num_cliente, valor_propriedade, id_propriedade, id_visita)
VALUES (1, 1, 200000, 1, 1);

-- Inserting data into Anuncio
INSERT INTO Anuncio (id, titulo, descricao, id_contrato)
VALUES (1, 'Great house in Lisbon', '3 bedroom house in Lisbon with great views', 1);

-- Inserting data into Avaliacao_imobiliaria
INSERT INTO Avaliacao_imobiliaria (id_visita, valor_apos_avaliacao)
VALUES (1, 210000);

-- Inserting data into Apresentacao_imovel
INSERT INTO Apresentacao_imovel (id_visita)
VALUES (1);

-- Inserting data into Moradia
INSERT INTO Moradia (id_propriedade, area_exterior)
VALUES (1, 50);

-- Inserting data into Apartamento
INSERT INTO Apartamento (id_propriedade, andar, elevador)
VALUES (1, 2, 1);

-- Inserting data into Oferta
INSERT INTO Oferta (id, estado, valor, id_anuncio, num_cliente)
VALUES (1, 'pending', 190000, 1, 1);