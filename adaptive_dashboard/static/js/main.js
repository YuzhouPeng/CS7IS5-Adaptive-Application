var pageCounter = 1;
// var animalContainer = document.getElementById("animal-info");
var btn = document.getElementById("btn");
var close = document.getElementsByClassName('close');
var popup = document.getElementById('popup');
var popupButton = document.getElementsByClassName('popup');
var bodyobj = document.body;

// btn.addEventListener("click", demonstrateLinks);


function demonstrateLinks() {
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
        htmlString += "<p><input type=\"checkbox\" name=\"link\" value=\"link" + i + "\"/>" + data[i].name + " is a " + data[i].species + " that likes to eat ";

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
    var myKeywords = keywords;
    var contentContainer = document.getElementById("content");
    var keywordnameContainer = document.getElementById("name");
    contentText = myPage['content'];

    var offset = 0;
    var last_end_index = -1;
    for (keyword of keywords) {
        var spanStart = "<span id='" + keyword['name'] + "' class='highlight'>";
        var spanEnd = "</span>";

        var spanStartLen = spanStart.length;
        var spanEndLen = spanEnd.length;


        if (last_end_index > -1 && last_end_index > keyword['start_index']) {
            continue;
        }
        contentText = contentText.slice(0, keyword['start_index'] + offset)
            + spanStart
            + contentText.slice(keyword['start_index'] + offset);
        offset += spanStartLen;
        end_index = keyword['end_index'] + offset;

        // temp_start_index = keyword['start_index'] + offset;
        // var temp_string = contentText.substring(temp_start_index, end_index);
        // console.log(keyword['name'] + " " + keyword['start_index'] + " " + keyword["end_index"] + ": " + temp_string);

        contentText = contentText.slice(0, end_index) + spanEnd + contentText.slice(end_index);
        offset += spanEndLen;
        last_end_index = keyword['end_index'];
    }

    // keywordsText = myKeywords['name'];
    var headingNode = document.createElement("h2");
    headingNode.innerText = myPage['page_name'];
    // var heading ="<h3>" + myPage['page_name'] + "</h3>";
    // highlight(keywordsText);
    document.body.appendChild(headingNode);
    var content = document.createElement("div");
    content.innerHTML = contentText.replace(/\n/g, "<br/>");
    document.body.appendChild(content);
    // contentContainer.innerHTML = content;

    var modal = document.getElementById('myModal');
    var btns = document.getElementsByClassName("highlight");
    var span = document.getElementsByClassName("close")[0];

    for (btn of btns) {
        btn.onclick = function(e) {
            var myId = e.currentTarget.id;
            wikiContentCont = document.getElementById("wiki-content");

            var myContent = keywords.filter(function(keyword){
                return keyword['name'] === myId;
            });

            wikiContentCont.innerText = myContent[0]['summary'];
            modal.style.display = "block";
        }
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    };

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}


function highlight(text) {
    inputText = document.getElementById("content");
    var innerHTML = inputText.innerHTML;
    var index = innerHTML.indexOf(text);
    if (index >= 0) {
        innerHTML = innerHTML.substring(0, index) + "<span class='highlight'>" + innerHTML.substring(index, index + text.length) + "</span>" + innerHTML.substring(index + text.length);
        inputText.innerHTML = innerHTML;
    }

}


window.addEventListener('load', init());




function show(obj) {
    var top = (document.documentElement.clientHeight - 250) / 2 - 150;
    var left = (document.documentElement.clientWidth - 300) / 2;
    obj.style.display = 'block';
    obj.style.left = left + 'px';
    obj.style.top = top + 'px';

}

function hide(obj) {
    obj.style.display = 'none';
    screen.style.display = 'none';
}

close[0].addEventListener("click", function () {
    hide(popup)
}, false);
popupButton[0].addEventListener("click", function () {
    show(popup)
}, false);

