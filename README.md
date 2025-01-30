# WIP - Web Browser
A simple web browser made by following the book [Web Browser Engineering](https://browser.engineering/index.html)

## Exercises:
### Chapter 1 - Downloading Web Pages:
- [x] 1.1 - HTTP/1.1. Along with Host, Send the Connection and User-Agent headers
- [ ] 1.2 - File URLs. Add support for the file scheme, which allows the browser to open local files, e.g. file:///path/goes/here.
- [ ] 1.3 - Data URLs. Add support for the data scheme. e.g. data:text/html,Hello world!
- [ ] 1.4 - Entities. Implement support for the less-than (&lt;) and greater-than (&gt;) entities. These should be printed as < and >, respectively. 
- [ ] 1.5 - view-source. Add support for the view-source scheme; Your browser should print the entire HTML file as if it was text.
- [ ] 1.6 - Keep-alive. Implement Exercise 1-1; however, do not send the Connection: close header (send Connection: keep-alive instead). When reading the body from the socket, only read as many bytes as given in the Content-Length header and don’t close the socket afterward, save it to reuse later when requesting to the same server
- [ ] 1.7 - Redirects. Error codes in the 300 range request a redirect. When your browser encounters one, it should make a new request to the URL given in the Location header.
- [ ] 1.8 - Implement caching for any 200 reponse.Servers control caches using the Cache-Control header. Add support for this header, specifically for the no-store and max-age values.
- [ ] 1.9 - Compression. Add support for HTTP compression. Your browser must send the Accept-Encoding header with the value gzip. If the server supports compression, its response will have a Content-Encoding header with value gzip. 

### Chapter 2 - Drawing to the Screen
- [ ] 2.1 - Line breaks. Change layout to end the current line and start a new one when it sees a newline character
- [x] 2.2 - Mouse wheel. Add support for scrolling up when you hit the up arrow. 
- [ ] 2.3 - Resizing. Make the browser resizable. 
- [ ] 2.4 - Scrollbar. At the right edge of the screen, draw a blue, rectangular scrollbar.
- [ ] 2.5 - Emoji. Add support for emoji to your browser 😀.
- [ ] 2.6 - about:blank. Add support for the special about:blank URL, which should just render a blank page, and cause malformed URLs to automatically render as if they were about:blank.
- [ ] 2.7 - Alternate text direction. Implement basic support for this with a command-line flag to your browser.