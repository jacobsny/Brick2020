function post(endpt, args, takesArgs) {
  const http = new XMLHttpRequest();
  const url= "localhost:8080/" + endpt;
  if(takesArgs){
    const data = new FormData();
    for(let k in args){
        data.append(k, args[k]);
    }
    http.open("POST", url);
    http.send(data)
  }
  else {
    http.open("POST", url);
    http.send();
  }

  http.onreadystatechange = (e) => {
    return http.responseText
  }
}
