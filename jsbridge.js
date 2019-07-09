var app = require("express")();

var http = require('http').Server(app);
var bodyParser = require('body-parser');
app.use(bodyParser.json())

const Counter = require('./Counter')
var counter = new Counter()
// for demonstration, not required for implementation
app.post('/',function(req,res){
	var msg=req.body.msg;
	console.log("python: " + msg);
	res.json({ 'msg': msg })
});

app.post('/counter/set',function(req,res){
	var msg=req.body.msg;
	console.log("jsbridge setting counter to: " + msg);
	try {
		var count = counter.set_counter(msg)
	} catch (error) {
		console.log("Caught error "+error)
		return res.status(500).json({"error": error})
	}
	if (isNaN(count)){
		console.log("Invalid input sent "+ msg)
		return res.status(500).json({"error": 'NaN'})
	}
	console.log("counter is now " + count)
	res.json({ 'msg': count })
});

app.post('/counter/increment',function(req,res){
	console.log("jsbridge incrementing counter..");
	try {
		count = counter.increment_counter()
	} catch (error) {
		console.log("Caught error "+error)
		return res.status(500).json({"error": error})
	}
	console.log("counter is now " + count)
	res.json({ 'msg': count })
});

app.get('/counter', async function(req,res){
	value = counter.get_count()
	console.log("returning counter value of "+ value);
	res.json({'msg': value})
});

app.post('/stop',async function(req,res){
	console.log("stoping jsbridge");
	res.status(200).send()
	process.exit()
});

http.listen(3000, function(){
	console.log('jsbridge listening...'); 
});
