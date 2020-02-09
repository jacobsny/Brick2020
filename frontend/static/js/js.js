function post(endpt, args, takesArgs, callback) {
  const http = new XMLHttpRequest();
  const url = endpt;
  if (takesArgs) {
    const data = new FormData();
    for (let k in args) {
      data.append(k, args[k]);
    }
    http.open("POST", url);
    http.send(data)
  } else {
    http.open("POST", url);
    http.send();
  }

  http.onreadystatechange = function() {
    if (http.readyState === 4 && http.status === 200) {
      var response = http.responseText;
      console.log(response);
      var json = JSON.parse(http.response);
      callback(json);
    }

  }
}

function get(endpt, callback) {
  const http = new XMLHttpRequest();
  const url = endpt;

  http.open("GET", url);
  http.send();

  http.onreadystatechange = function() {
    if (http.readyState === 4 && http.status === 200) {
      var response = http.responseText;
      console.log(response);
      var json = JSON.parse(http.response);
      callback(json);
    }

  }
}
