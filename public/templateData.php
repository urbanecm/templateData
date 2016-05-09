<!DOCTYPE html>
<html lang="cs-cz">
	<head>
		<meta charset="utf-8" />
		<title>Titulek</title>
	</head>
	<body>
		<?php
		$cmd = "/data/project/urbanecmbot/templateData/run_not.sh";
		$result = shell_exec($cmd);
		echo("<h1>Bez template data</h1>");
		echo("<ol>");
		echo($result);
		echo("</ol>");
		$cmd = "/data/project/urbanecmbot/templateData/run_yes.sh";
		$result = shell_exec($cmd);
		echo("<h1>S template data</h1>");
		echo($result);
		?>		
	</body>
</html>
