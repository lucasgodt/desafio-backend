const http = require('http');
const port = process.env.PORT || 3000;

module.exports = http.createServer(function (req, res) {
    res.writeHead(404, { 'Content-Type': 'text/plain' });

    if (req.url.indexOf('/suggestions') === 0) {
        res.end(JSON.stringify({
            suggestions: []
        }));
    } else {
        res.end();
    }
}).listen(port, '127.0.0.1');

console.log('Server running at http://127.0.0.1:%d/suggestions', port);
