-- Création des bases de données 

CREATE DATABASE ForestAI_DWH;
CREATE DATABASE ForestAI_Client_DM;
CREATE DATABASE ModelPerformance_DATAMART;



-- Création de la table DimDate
CREATE TABLE DimDate (
    DateKey INT PRIMARY KEY,
    FullDate DATE,
    Year INT,
    Quarter INT,
    Month INT,
    Day INT
);

-- Création de la table DimRegion
CREATE TABLE DimRegion (
    RegionKey INT PRIMARY KEY,
    RegionName VARCHAR(100),
    RegionDescription VARCHAR(255)
);

-- Création de la table DimSpecies
CREATE TABLE DimSpecies (
    SpeciesKey INT PRIMARY KEY,
    SpeciesName VARCHAR(100),
    SpeciesDescription VARCHAR(255)
);

-- Création de la table DimModelVersion
CREATE TABLE DimModelVersion (
    ModelVersionKey INT PRIMARY KEY,
    ModelVersion VARCHAR(50),
    ModelDescription VARCHAR(255),
    CreationDate DATE
);

-- Création de la table DimDataSource
CREATE TABLE DimDataSource (
    DataSourceKey INT PRIMARY KEY,
    DataSourceName VARCHAR(100),
    DataSourceDescription VARCHAR(255)
);

-- Création de la table DimClient
CREATE TABLE DimClient (
    ClientID INT PRIMARY KEY,
    ClientName VARCHAR(100),
    Industry VARCHAR(100),
    Region VARCHAR(100)
);

-- Création de la table FactModelPerformance
CREATE TABLE FactModelPerformance (
    DateKey INT,
    RegionKey INT,
    SpeciesKey INT,
    ModelVersionKey INT,
    DataSourceKey INT,
    PredictedVolume FLOAT,
    PredictedHeight FLOAT,
    PredictedDiameter FLOAT,
    ErrorMetric FLOAT,
    ClientEstimate FLOAT,
    GroundTruth FLOAT,
    FOREIGN KEY (DateKey) REFERENCES DimDate(DateKey),
    FOREIGN KEY (RegionKey) REFERENCES DimRegion(RegionKey),
    FOREIGN KEY (SpeciesKey) REFERENCES DimSpecies(SpeciesKey),
    FOREIGN KEY (ModelVersionKey) REFERENCES DimModelVersion(ModelVersionKey),
    FOREIGN KEY (DataSourceKey) REFERENCES DimDataSource(DataSourceKey)
);

-- Création de la table FactClientComparison
CREATE TABLE FactClientComparison (
    ClientID INT,
    ModelVersionKey INT,
    PredictionDate DATE,
    SpeciesKey INT,
    PredictedVolume FLOAT,
    ClientEstimatedVolume FLOAT,
    ErrorMetric FLOAT,
    FOREIGN KEY (ClientID) REFERENCES DimClient(ClientID),
    FOREIGN KEY (ModelVersionKey) REFERENCES DimModelVersion(ModelVersionKey),
    FOREIGN KEY (SpeciesKey) REFERENCES DimSpecies(SpeciesKey)
);