<!DOCTYPE html>
<html lang="es">
<head>
	<title>Adivina el numero</title>
	<meta charset="utf-8" />
</head>
<body>
	<header>
		<h1>Adivina el numero</h1>
		<p>El numero es : {{numeroAdivinar}}</p>
		<p>El numero enviado es: {{num}}</p>
		<h1>Has fallado!! El numero es mas pequeño!</h1>		
	</header>
	<article>
		<form action='' method='get'>
			<input type='number' name='numeroEnviado'/>
			<input type='submit' value='Enviar'>
		</form>
	</article>	
</body>
</html>
