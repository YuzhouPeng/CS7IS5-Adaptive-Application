var pageCounter = 1;
// var animalContainer = document.getElementById("animal-info");
var btn = document.getElementById("btn");



// btn.addEventListener("click", demonstrateLinks);


function demonstrateLinks(){
    var ourRequest = new XMLHttpRequest();
        ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-' + pageCounter + '.json');
        ourRequest.onload = function () {
            if (ourRequest.status >= 200 && ourRequest.status < 400) {
                var ourData = JSON.parse(ourRequest.responseText);
                renderHTML(ourData);
            } else {
                console.log("We connected to the server, but it returned an error.");
            }

        };

        ourRequest.onerror = function () {
            console.log("Connection error");
        };

        ourRequest.send();
        pageCounter++;
        if (pageCounter > 3) {
            btn.classList.add("hide-me");
        }
}

function renderHTML(data) {
  var htmlString = "";

  for (i = 0; i < data.length; i++) {
    htmlString += "<p><input type=\"checkbox\" name=\"link\" value=\"link"+i+"\"/>" + data[i].name + " is a " + data[i].species + " that likes to eat ";

    for (ii = 0; ii < data[i].foods.likes.length; ii++) {
      if (ii == 0) {
        htmlString += data[i].foods.likes[ii];
      } else {
        htmlString += " and " + data[i].foods.likes[ii];
      }
    }

    htmlString += ' and dislikes ';

    for (ii = 0; ii < data[i].foods.dislikes.length; ii++) {
      if (ii == 0) {
        htmlString += data[i].foods.dislikes[ii];
      } else {
        htmlString += " and " + data[i].foods.dislikes[ii];
      }
    }

    htmlString += '.</p>';

  }

  animalContainer.insertAdjacentHTML('beforeend', htmlString);


}



function init() {
    var myPage = page;
    var contentContainer = document.getElementById("content");
    console.log("");
    contentText = myPage['content'].replace(/\n/g, "<br/>");

    var headingNode = document.createElement("h2");
    headingNode.innerText = myPage['page_name'];
    // var heading ="<h3>" + myPage['page_name'] + "</h3>";

    document.body.appendChild(headingNode);
    var content = document.createElement("div");
    content.innerHTML = contentText;
    document.body.appendChild(content)
    // contentContainer.innerHTML = content;
}

window.addEventListener('load', init());

