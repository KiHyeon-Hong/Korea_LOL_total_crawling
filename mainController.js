const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const cookieParser = require('cookie-parser');
const session = require('express-session');
const request = require('request');

const app = express();


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(cookieParser());


app.use(express.static('view'));


const index = require(__dirname + '/controller/index.js');


app.use('/', index);


app.listen(65001, () => {
	request.get(
		{url:'https://api.ipify.org'},
		function(err, response, body) {
				fs.writeFileSync(__dirname + '/files/webPage.txt', body + ':65001', 'utf8')
				console.log('server running at ' + body + ':65001');
		}
	);
});
