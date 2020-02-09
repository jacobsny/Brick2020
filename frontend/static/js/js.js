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
      console.log(http.responseText);
      var json = JSON.parse(http.responseText);
      callback(json)
      return;
    }

  }
}
