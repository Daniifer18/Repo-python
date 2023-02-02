<!DOCTYPE html>
<html>
<head>
	<title>Formulario de inicio de sesión con recordar usuario</title>
	<style>
		form {
			width: 300px;
			margin: 50px auto;
			padding: 20px;
			border: 1px solid #ddd;
			border-radius: 10px;
			box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
		}
		label {
			display: block;
			margin-bottom: 10px;
			font-weight: bold;
		}
		input[type="text"],
		input[type="password"] {
			width: 100%;
			padding: 10px;
			margin-bottom: 20px;
			border: 1px solid #ddd;
			border-radius: 5px;
			box-sizing: border-box;
		}
		input[type="submit"] {
			width: 100%;
			padding: 10px;
			background-color: #4CAF50;
			color: white;
			border: none;
			border-radius: 5px;
			cursor: pointer;
		}
		input[type="checkbox"] {
			margin-bottom: 20px;
		}
		label[for="remember"] {
			display: inline-block;
			margin-left: 10px;
			font-weight: normal;
		}
	</style>
</head>
<body>
	<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
		<label for="username">Usuario:</label>
		<input type="text" id="username" name="username" value="<?php echo isset($_COOKIE['username']) ? $_COOKIE['username'] : ''; ?>">

		<label for="password">Contraseña:</label>
		<input type="password" id="password" name="password">

		<input type="checkbox" id="remember" name="remember">
		<label for="remember">Recuerdame</label>

		<input type="submit" value="Iniciar sesión">
	</form>
</body>
</html>
