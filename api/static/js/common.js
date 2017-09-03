function requestBuilder(method, url, body, callback) {
    const request = new XMLHttpRequest();
    request.open(method, url, true);
    request.setRequestHeader('Content-Type', 'application/json');

    request.onreadystatechange = function () {
      const response = request.responseText;
      if (request.readyState === XMLHttpRequest.DONE) {
        callback(response ? JSON.parse(response) : undefined);
      }
    };

    request.send(body ? JSON.stringify(body) : undefined);
}
 
//window.request = {
  //get: requestBuilder("GET"),
  //post: requestBuilder("POST"),
//};
