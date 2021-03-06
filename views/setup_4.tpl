<html>
	<head>
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
		<title>HvsI Initial Configuration</title>
	</head>
	<body>
		<h3>Database Connection</h3>
		<form action="4" method="post">
			Infrastructure: <input type="radio" name="infra" value="aws">Amazon Web Services</input>
							<input type="radio" name="infra" value="af">AppFog</input>
							<input type="radio" name="infra" value="custom" checked="true">Custom</input>
			<br/><br/>
			Protocol: <select class="c" name="dbproto">
					  %if has_mysql:
						<option value="mysql">MySQL</option>
					  %end
						<option value="postgres">Postgres</option>
						<option value="sqlite">SQLite</option>
					  </select><br/><br/>
			Hostname (filepath for SQLite): <input class="c" type="text" name="dbhost" /><br/><br/>
			Port (empty for protocol default): <input class="c" type="text" name="dbport" /><br/><br/>
			Username: <input class="c" type="text" name="dbuser" /><br/><br/>
			Password: <input class="c" type="text" name="dbpass" /><br/><br/>
			Database (filename for SQLite): <input class="c" type="text" name="dbdb" /><br/><br/>
			<input type="submit" value="Next" />
		</form>
		<script type="text/javascript">
			$('input:radio').change(function(evt) {
				if (this.value == "custom") {
					$('input.c').prop('disabled', false);
				} else {
					$('input.c').prop('disabled', true);
				}
			});
		</script>
	</body>
</html>