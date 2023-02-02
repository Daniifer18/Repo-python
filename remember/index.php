<?php
if (isset($_POST['username']) && isset($_POST['password'])) {
	// Aquí verificarías las credenciales del usuario y autenticarías su sesión.

	if ($_POST['remember']) {
		setcookie('username', $_POST['username'], time() + (30 * 24 * 60 * 60));
	} else {
		setcookie('username', '', time() - 3600);
	}
}
?>

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
	<h1>Formulario de inicio de sesión</h1>
	<form action="login.php" method="post">
		<label for="username">Nombre de usuario:</label>
		<input type="text" name="username" id="username" value="<?php echo isset($_COOKIE['username']) ? $_COOKIE['username'] : ''; ?>">
		<br>
		<label for="password">Contraseña:</label>
		<input type="password" name="password" id="password">
		<br>
		<input type="checkbox" name="remember" id="remember" <?php echo isset($_COOKIE['username']) ? 'checked' : ''; ?>>
		<label for="remember">Recordar usuario</label>
		<br>
		<input type="submit" value="Iniciar sesión">
	</form>
</body>
</html>
