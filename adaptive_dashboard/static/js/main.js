var pageCounter = 1;
// var animalContainer = document.getElementById("animal-info");
var btn = document.getElementById("btn");
var btn1 = document.getElementById("btn1");
var btn2 = document.getElementById("btn2");
var close = document.getElementsByClassName('close');
var popup = document.getElementById('popup');
var popupButton = document.getElementsByClassName('popup');
var bodyobj = document.body;

btn1.addEventListener("click", CheckPageId());

var wiky = require('wiky.js');

function CheckPageId() {
    var pageCounter = pageId.valueOf();
    if (pageCounter <= 1) {
        btn1.classList.add("hide-me");
    }
    if (pageCounter >= 10) {
        btn2.classList.add("hide-me");

    }
    // if (pageCounter > 1 && pageCounter <= 9) {
    //     $.ajax({
    //         url: "/ajax/",
    //         type: "POST",
    //         data: newPageId,
    //         cache: false,
    //         dataType: "json",
    //         success: function (resp) {
    //             alert("resp: " + resp.name);
    //         }
    //     });
    // }
}



function init(updatedPage) {
    if (!updatedPage) {
        updatedPage = page
    }
    var myPage = updatedPage;
    var myKeywords = keywords;
    var contentContainer = document.getElementById("content");
    var keywordnameContainer = document.getElementById("name");
    contentText = myPage['content'];

    var offset = 0;
    var last_end_index = -1;
    for (keyword of keywords) {
        if (!keyword['start_index']) {
            continue;
        }

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
    // content.innerHTML = contentText.replace(/\n/g, "<br/>");

    content.innerHTML = wiky.process(contentText, {'link-image': false});

    document.body.appendChild(content);
    // contentContainer.innerHTML = content;

    var modal = document.getElementById('myModal');
    var showNum = document.getElementById('show-num');
    showNum.innerHTML = showLen + " / "  + totalLen;
    var btns = document.getElementsByClassName("highlight");
    var span = document.getElementsByClassName("close")[0];

    for (btn of btns) {
        btn.onclick = function (e) {
            var myId = e.currentTarget.id;
            wikiContentCont = document.getElementById("wiki-content");

            var myContent = keywords.filter(function (keyword) {
                return keyword['name'] === myId;
            });

            wikiContentCont.innerText = myContent[0]['summary'];
            modal.style.display = "block";
            $.get('/model-update', {'topic': page['topics'], 'page': pageId}, function(data) {
                console.log(data);
            });

        }
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    };

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}


// function highlight(text) {
//     inputText = document.getElementById("content");
//     var innerHTML = inputText.innerHTML;
//     var index = innerHTML.indexOf(text);
//     if (index >= 0) {
//         innerHTML = innerHTML.substring(0, index) + "<span class='highlight'>" + innerHTML.substring(index, index + text.length) + "</span>" + innerHTML.substring(index + text.length);
//         inputText.innerHTML = innerHTML;
//     }
//
// }


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

$("#btn1").click(function(event){
    $.get('/page-change', {'last-page':pageId, 'topic': page['topics']}, function(data) {
        console.log(data);
    });
    window.location.href = "../" + (pageId-1);
});

$("#btn2").click(function(event){
    $.get('/page-change', {'last-page':pageId, 'topic': page['topics']}, function(data) {
        console.log(data);
    });
    window.location.href = "../"+(pageId+1);
});

// close[0].addEventListener("click", function () {
//     hide(popup)
// }, false);
// popupButton[0].addEventListener("click", function () {
//     show(popup)
// }, false);

window.addEventListener('load', init(null));