USE --Nombre de la base 

IF OBJECT_ID('Usuario', 'U') IS NULL
BEGIN
	CREATE TABLE usuario(
		Idusuario INT PRIMARY KEY IDENTITY(1,1) NOT NULL
		, [Name] NVARCHAR(100) NOT NULL
		, Email NVARCHAR(50) NOT NULL
		, [Password] NVARCHAR(50) NULL)---VER QUE HASH SE UTILIZARA 
END

IF OBJECT_ID('UserData', 'U') IS NULL
BEGIN
	CREATE TABLE UserData(
		Idusuario INT PRIMARY KEY IDENTITY(1,1) NOT NULL
		, Direccion NVARCHAR(100) NOT NULL
		, Telefono INT NOT NULL
		, FechaNaci DATETIME NULL)


END

	ALTER TABLE Usuario
	ADD CONSTRAINT FK_UserData_Usuario
	FOREIGN KEY(Idusuario)
	REFERENCES UserData(Idusuario)
