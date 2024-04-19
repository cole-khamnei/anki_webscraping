########################################################################################################################
################################## ANKING  CARD  FORMATS   #############################################################

ANKING_QFMT_APPEND = """
<br>
<div class="timer" id="s2"></div>
<script>
    //############## TIMER CONFIGURATION START ##############
    //Set Timer Length
    var minutes = 0
    var seconds = 9
    //############## TIMER CONFIGURATION END ##############
    
    function countdown( elementName, minutes, seconds )
    {
        var element, endTime, hours, mins, msLeft, time;
        function twoDigits( n )
        {
            return (n <= 9 ? "0" + n : n); 
        }
        function updateTimer()
        {
            msLeft = endTime - (+new Date);
    
    //USER CUSTOMIZATION- you can edit color and text of the 'time expired' readout under the element.innerHTML
            if ( msLeft < 1000 ) {
                element.innerHTML = "<span style='color:#CC5B5B'>!<br/>!<br/>!<br/>!<br/>!<br/>!</span>";
            } else {
                time = new Date( msLeft );
                hours = time.getUTCHours();
                mins = time.getUTCMinutes();
                element.innerHTML = (hours ? hours + ':' + twoDigits( mins ) : mins) + ':' + twoDigits( time.getUTCSeconds() );
                setTimeout( updateTimer, time.getUTCMilliseconds() + 500 );
            }
        }
        element = document.getElementById( elementName );
        endTime = (+new Date) + 1000 * (60*minutes + seconds) + 500;
        updateTimer();
    }
    countdown("s2", minutes, seconds ); //2nd value is the minute, 3rd is the seconds
</script>

<script>
    //DONT FADE BETWEEN CARDS
	qFade=0; if (typeof anki !== 'undefined') anki.qFade=qFade;
</script>

{{#Tags}}
    <div id="tags-container">{{clickable::Tags}}</div>
    <script>
        var tagContainer = document.getElementById("tags-container")
        if (tagContainer.childElementCount == 0) {
         var tagList= tagContainer.innerHTML.split(" ");
         var kbdList = [];
         var newTagContent = document.createElement("div");
        
         for (var i = 0; i < tagList.length;  i++) {
          var newTag = document.createElement("kbd");
          newTag.innerHTML = tagList[i];
          newTagContent.append(newTag)
         }
         tagContainer.innerHTML = newTagContent.innerHTML;
         tagContainer.style.cursor = "default";
        }
        if (tagContainer.innerHTML.indexOf("Missed") != -1) {
        tagContainer.style.backgroundColor = "rgba(251,11,11,.2)";
        } else {
        tagContainer.style.display = "none";
        }
    </script>
{{/Tags}}
"""


########################################################################################################################
########################################################################################################################


ANKING_AFMT_APPEND = """
<script>
    // ##############  HINT REVEAL SHORTCUTS  ##############
    // Visit https://keycode.info/ to get the number/letter for the key you want to assign. 
    // The shortcuts are  Alt  +  the number/letter below
    // All shortcuts will also open with "H" if using the Hint Hotkeys add-on 

    var lecturenotes = '49';
    var missedQ = '50';
    var pathoma = '51';
    var bnb = '52';
    var firstaid = '53';
    var sketchy = '54';
    var pixorize = '55';
    var physeo = '56';
    var additional = '57';
    var OpenCloseAll = '222';

	var ScrollToHint = true;
</script>


<!-- ##############  TEXT-TO-SPEECH ##############
replace the arrows/dashes from the statement below with double brackets-->

<!--tts en_US voices=Apple_Samantha speed=1.4:cloze-only:Text-->


<!-- ##############  SHOW HINTS AUTOMATICALLY  ##############
For instructions on how to show a field automatically,  visit www.ankingmed.com/faq and type "show hint" into the search bar -->


<script>
    //HINT REVEALS
    function myFunction(divid, id, divid) {
    var x = document.getElementById(divid), y = document.getElementById(id), z = document.getElementById(divid);
    if (x.style.display == "none")
    {
    x.style.display = "block"; y.style.display = "none"; z.scrollToId;
    }
        else {
          x.style.display = "none"; y.style.display = "inline-block";
        }
    if (ScrollToHint){
	z.scrollIntoView({
      behavior: "smooth", //"auto" for instant scrolling
      block: "start",
      inline: "nearest"
    }); }
      }
      document.addEventListener('keydown', function(evt) {
          if (evt.altKey && evt.keyCode == lecturenotes) {
              myFunction('button-ln', 'hint-ln', 'button-ln')}  
          if (evt.altKey && evt.keyCode == missedQ) {
              myFunction('button-mq', 'hint-mq', 'button-mq')}
          if (evt.altKey && evt.keyCode == pathoma) {
              myFunction('button-pat', 'hint-pat', 'button-pat')}
          if (evt.altKey && evt.keyCode == bnb) {
              myFunction('button-bb', 'hint-bb', 'button-bb')}
          if (evt.altKey && evt.keyCode == firstaid) {
              myFunction('button-fa', 'hint-fa', 'button-fa')}
          if (evt.altKey && evt.keyCode == sketchy) {
              myFunction('button-sketchy', 'hint-sketchy', 'button-sketchy')}
          if (evt.altKey && evt.keyCode == pixorize) {
              myFunction('button-pixorize', 'hint-pixorize', 'button-pixorize')}
          if (evt.altKey && evt.keyCode == physeo) {
              myFunction('button-physeo', 'hint-physeo', 'button-physeo')}
          if (evt.altKey && evt.keyCode == additional) {
              myFunction('button-ar', 'hint-ar', 'button-ar')}
      
          if (evt.keyCode == OpenCloseAll) {
          try{myFunction('button-ar', 'hint-ar', 'button-ar');}
          finally{try{myFunction('button-physeo', 'hint-physeo', 'button-physeo');}
          finally{try{myFunction('button-pixorize', 'hint-pixorize', 'button-pixorize');}
          finally{try{myFunction('button-sketchy', 'hint-sketchy', 'button-sketchy');}
          finally{try{myFunction('button-fa', 'hint-fa', 'button-fa');}
          finally{try{myFunction('button-bb', 'hint-bb', 'button-bb');}
          finally{try{myFunction('button-pat', 'hint-pat', 'button-pat');}
          finally{try{myFunction('button-mq', 'hint-mq', 'button-mq');}
          finally{myFunction('button-ln', 'hint-ln', 'button-ln');}}}}}}}}
          }
      })
</script>


<br>
<br>

<script>
    //ENTER THE TAG TERM WHICH, WHEN PRESENT, WILL TRIGGER A RED BACKGROUND
    var tagID = ""
</script>


{{#Tags}}
    <div id="tags-container">{{clickable::Tags}}</div>
    <script>
        var tagContainer = document.getElementById("tags-container")
        if (tagContainer.childElementCount == 0) {
         var tagList= tagContainer.innerHTML.split(" ");
         var kbdList = [];
         var newTagContent = document.createElement("div");
        
         for (var i = 0; i < tagList.length;  i++) {
          var newTag = document.createElement("kbd");
          newTag.innerHTML = tagList[i];
          newTagContent.append(newTag)
         }
         tagContainer.innerHTML = newTagContent.innerHTML;
         tagContainer.style.cursor = "default";
        }
        if (tagContainer.innerHTML.indexOf(tagID) != -1) {
        tagContainer.style.backgroundColor = "";
        }
        
        function showtags() {
          var xx = document.getElementById("tags-container");
        
            if (xx.style.display 
        === "none") {
            xx.style.display = "block";
          } else {
            xx.style.display = 
          "none";
          }
        } 
        document.addEventListener('keyup', function(e) {
            if(e.key =="c"){
             showtags();
            }
        });
        
        
    </script>
{{/Tags}}


<!-- WIKIPEDIA SEARCHES -->
<div id="popup-container">
    <button id="close-popup-btn" onclick="closePopup(true)">&times;</button>
    <a id="open-wiki-btn" href="">&#8618;</a>
    <div id="tc"></div>
    <div id="fadebottom_v"></div>
    <div id="ic"><img id="popup-image"></div>
</div>
<style>
    #tc {
        color: #222222;
        position: absolute;
        top: 16px;
        margin: 0px;
        left: 15px;
        text-decoration: none;
        height: 320px;
        overflow: hidden;
        overflow-y: scroll;
        white-space: pre-wrap;
        width: 300px;
    }

    #tc p {
        margin: 0px;
    }

    #tc::-webkit-scrollbar {
        display: none;
    }

    #fadebottom_v {
        height: 30px;
        width: 300px;
        background: -webkit-linear-gradient(270deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 1));
        z-index: 111;
        position: absolute;
        bottom: 0px;
        left: 15px;
    }

    #hc {
        color: #666;
        font-weight: bold;
    }

    #ic {
        right: 0px;
        top: 30px;
        position: absolute;
    }

    #ic img {
        width: 160px;
        height: auto;
        object-fit: cover;
        overflow: hidden;
    }

    #popup-image {
        width: 140px;
        height: auto;
    }

    #popup-container {
        background: #fff;
        position: absolute;
        bottom: 30px;
        right: 10px;
        z-index: 110;
        -webkit-box-shadow: 0 30px 90px -20px rgba(0, 0, 0, 0.3), 0 0 1px 1px rgba(0, 0, 0, 0.05);
        box-shadow: 0 30px 90px -20px rgba(0, 0, 0, 0.3), 0 0 1px 1px rgba(0, 0, 0, 0.05);
        padding: 0;
        display: none;
        font-size: 17px;
        line-height: 20px;
        border-radius: 2px;
        width: 480px;
        height: 340px;
        overflow: hidden;
        font-family: Arial;
        text-align: left;
        border: 1px solid #d0d0d0;
        border-radius: 5px;
    }

    #close-popup-btn {
        position: absolute;
        top: 1px;
        right: 5px;
        width: 32px;
        height: 32px;
        background: none;
        border: 0;
        cursor: pointer;
        font-family: 'Josefin Sans', sans-serif;
        font-size: 28px;
        outline: none;
        text-align: right;
        z-index: 112;
    }

    #open-wiki-btn {
        position: absolute;
        top: 10px;
        right: 30px;
        width: 15px;
        height: 32px;
        background: none;
        border: 0;
        cursor: pointer;
        text-decoration: none;
        color: #222222;
        font-family: 'Josefin Sans', sans-serif;
        font-size: 17px;
        outline: none;
        text-align: left;
        z-index: 112;
    }
</style>

<script>
    function getSummaryFor(word) {
      word = word.replace(/^[\.,\/#\!$%\^&\*;:{}=\-_`~()\'\s]+|[\.,\/#\!$%\^&\*;:{}=\-_`~()\'\s]+$/g, "");
           var pc = document.getElementById("popup-container");
         var hc = document.getElementById("hc");
          var tc = document.getElementById("tc");
          var ic = document.getElementById("ic");
          var imgelem = document.getElementById("popup-image");
             imgelem.src = "";
          var shortsum ="";
      fetch("https://en.wikipedia.org/api/rest_v1/page/summary/" + word).then(function(response) {return response.json();}).then(function(response) {
         shortsum = response.description;
       shortsum = shortsum.replace(/(Disambiguation.*)/g, "Disambiguation");
          tc.innerHTML = "<span id='hc'>" +capfl(shortsum) + "</span>" +"\n" +response.extract_html + "\n";
      tc.style.width = "420px";
          if (response.extract_html && !response.extract.endsWith("to:")){
              pc.style.display = "block";
          document.getElementById("open-wiki-btn").href = response.content_urls.desktop.page;
          }else{pc.style.display = "none";}
          if (!response.thumbnail.source || response.type ==="disambiguation"){
               tc.style.width = "420px";
          }else{tc.style.width="300px";imgelem.src = response.thumbnail.source;}
        }).catch(function(error) {console.log(error);});}
        
        function closePopup(deselectAlso=false){
          pcc.style.display = 'none';
          if (deselectAlso){clearSelection();}
        }
        var pcc = document.getElementById("popup-container");
        var prevSel = "";
        document.addEventListener('click', function() {
            var currentSelection = getSelectionText();
            if (currentSelection !==""){prevSel = currentSelection;}
            if (currentSelection && !mustClickW ){
      getSummaryFor(currentSelection);
             }else{closePopup();}
        });
        document.addEventListener('keyup', function(e) {
            if(e.key =="w"){hhh
            if(pcc.style.display ==="block"){closePopup();}else{getSummaryFor(prevSel);}
            }
        });
        function getSelectionText() {
            var text = "";
            if (window.getSelection) {
      text = window.getSelection().toString();
            } else if (document.selection && document.selection.type != "Control") { text = document.selection.createRange().text;}
            return text;
        }
        function capfl(s) {
            return s.charAt(0).toUpperCase() + s.slice(1);
        }
        function clearSelection(){
         if (window.getSelection) {window.getSelection().removeAllRanges();}
         else if (document.selection) {document.selection.empty();}
        }
        
        //CUSTOMIZATION
        //this is a variable controlling whether user must click the "w" key to open the popup.
        //if set to true: user must select text, then click the "w" key to open wikipedia popup. Clicking "w" key again will close the popup. 
        //if set to false: user only needs to select text. popup will open automatically. Clicking "w" is an alternative but not obligatory way of opening/closing the popup in this mode.
        //BELOW SET to true or to false. 
        var mustClickW = true;
        //END CUSTOMIZATION
</script>
"""


########################################################################################################################

ANKING_CSS = """


/*    ANKINGMASTER-v2.1   */

/* The AnKing wishes you the best of luck! Be sure to check out our YouTube channel and Instagram for all things Anki and Med School related (including how to customize this card type and use these decks):  
		www.AnKingMed.com
			@ankingmed    			*/

/*~~~~~~~~USER CUSTOMIZATION START~~~~~~~~~*/
/* You can choose colors at www.htmlcolorcodes.com */

/* TIMER ON/OFF */
.timer { display: block; } /* 'none' or 'block' */
/* TAGS ON/OFF DESKTOP & MOBILE*/
	 #tags-container { display: none; }  /* ‘none’ or ‘block’ */
.mobile #tags-container { display: none; } /* ‘none’ or ‘block’ */
/* MOVE TAGS UP FOR 'NO-DISTRACTIONS' ADD-ON */
#tags-container{ padding-bottom: 0px; } /* 0 normal, 55 to move up */
/* ANKING IMAGE HYPERLINK ON/OFF */
	#pic {display: block; } /* 'none' or 'block' */
/* MNEMONICS CENTER OR LEFT */
.mnemonics { text-align:left; } 

/*FONT SIZE*/
     /* DESKTOP */ html 
	{ font-size: 28px; }
     /* MOBILE */ .mobile
         { font-size: 28px; }
		/* NOTE: anything with 'px' will keep a font that size indefinitely, 'rem' is a fraction of this size above and allows all text to change size with the above setting */

/*IPAD ADJUSTMENTS*/
.ipad .card, .ipad #extra {font-size:18px;}
.ipad .hints {font-size:24px;}
.ipad #firstaid, .ipad #sketchy, .ipad #pixorize, .ipad #physeo, .ipad #additional { font-size: 20px!important; }

/*HINT FONT SIZE*/ .hints 
	{ font-size: .85rem; }
   /*First Aid, Sketchy, Physeo, Additional Resources Font Size*/
	#firstaid, #sketchy, #pixorize, #physeo, #additional { font-size: .6rem !important; } 
   /*First Aid, Sketchy, Physeo, Additional Resources Font Size on Mobile*/
  .mobile #firstaid, .mobile #sketchy, .mobile #pixorize, .mobile #physeo, .mobile #additional { font-size: 20px!important; }

/*FONT STYLE*/	
	.card, kbd { font-family: Arial Greek, Arial; } /*Step exam's font is Arial Greek*/
/*MAX IMAGE HEIGHT*/
	img {max-height: none; }
 /*MAX IMAGE WIDTH*/
		#extra img, #lecture img, #missed img, #pathoma img, #bnb img {max-width: 85%; }
	#firstaid img, #sketchy img, #pixorize img, #physeo img, #additional img {max-width: 60%; }


/* ~~COLORS~~ */
/*DEFAULT TEXT COLOR*/ 
	.card { color: #D7DEE9; }
/*BACKGROUND COLOR*/ 
	.card { background-color: #333B45; }
	#tags-container { background-color: transparent; }
    /*TIMER COUNTDOWN COLOR*/
 	.timer { color: transparent; }
/* CLOZE COLOR */
	.cloze , .cloze b, .cloze u, .cloze i { color: MediumSeaGreen !important; }
/* "EXTRA" FIELD COLOR */
	#extra { color: #D7DEE9; }
/* HINT COLOR*/
	a[href="#"] { color: blue; }
/* HINT REVEAL COLOR */
	.hints { color: #D7DEE9; }
   /* Missed Questions Reveal Color */
	#missed { color: red; }
       #missed a[href="#"] { color: red!important; }
	.nightMode #missed a[href="#"], .night_mode #missed a[href="#"] { color: red!important; }

/* ~~NIGHT MODE COLORS~~ */
/* NM DEFAULT TEXT COLOR*/ 
	.nightMode.card, .night_mode .card
     { color: #FFFAFA !important; }
/* NM BACKGROUND COLOR*/ 
	.nightMode.card, .night_mode .card { background-color: #333B45!important; }
/* NM CLOZE COLOR */
 	.nightMode .cloze, .night_mode .cloze { color: #MediumSeaGreen !important; }
/* NM "EXTRA" FIELD COLOR */
	.nightMode #extra, .night_mode #extra { color: #FFFAFA; }
/* NM HINT COLOR */
	.nightMode a[href="#"], .night_mode a[href="#"] { color: #4297F9!important; }
/* NM HINT REVEAL COLOR */
	.nightMode .hints, .night_mode .hints { color: cyan;}

/* COLOR ACCENTS FOR BOLD-ITALICS-UNDERLINE*/
b { color: #C695C6; }
u { color: #00ffff; } 
i  { color: IndianRed; }

/* ~~~~~~~~END CUSTOMIZATION~~~~~~~~ */

html { min-height: 100%; display: flex; flex-direction: column; }

#qa { margin-top: 15px; padding-bottom: 2rem; }

/* Formatting For Timer */
.timer {
font-size: 28px;
margin: 12em auto auto auto;
}

/* Styling For Whole Card*/
.card {
text-align: center;
font-size: 1rem;
height: 100%;
margin: 2rem;
flex-grow: 1;
padding-bottom: 1em;
}
.mobile .card { padding-bottom: 5em; }

/* Details For IMAGES */
.mobile .card img {max-width: 100%!important; }
.mobile .card {margin: 0ex .3px;}

#extra img { min-width: 30%; }
.mobile #extra img, .mobile #lecture img, .mobile #missed img, .mobile #pathoma img, .mobile #bnb img, .mobile #firstaid img, .mobile #sketchy img, .mobile #pixorize, .mobile #physeo img, .mobile #additional img {max-width: 100%!important; }

/* Classes for individual cards */
.image40 img { width: 40%!important; }
.image50 img { width: 50%!important; }
.image60 img { width: 60%!important; }
.image70 img { width: 70%!important; }
.image80 img { width: 80%!important; }
.image90 img { width: 90%!important; }
.image40 img, .image50 img, .image60 img, .image70 img, .image80 img, .image90 img { display:block; margin-right:auto; margin-left: auto; }
.mobile .image40 img, .mobile .image50 img, .mobile .image60 img, .mobile .image70 img, .mobile .image80 img, .mobile .image90 img {width: auto!important;}

/*Compatibility with Image Style Editor add-on*/
.mobile .card {--w:100%!important;}
.card {--w:0%;}

/*Max image width for resize images in editor add-on */
    .card [class^=ui-] img {max-width: 100%!important; }

/*Compatibility with resize images in editor add-on */
    .resizer {min-width: 0%!important; }
    .mobile .resizer {min-width:100%!important;}

/*Image hover zoom*/
#extra img:active, #lecture img:active, #missed img:active, #pathoma img:active, #bnb img:active { transform:scale(1.2); }
#firstaid img:active, #sketchy img:active, #pixorize img:active, #physeo img:active, #additional img:active { transform:scale(1.5); }
.mobile #extra img:active, .mobile #lecture img:active, .mobile #missed img:active, .mobile #pathoma img:active, .mobile #bnb img:active, .mobile #firstaid img:active, .mobile #sketchy img:active, .mobile #pixorize img:active, .mobile #physeo img:active, .mobile #additional img:active { transform:scale(1.0); }

/* Cloze format */
.cloze { font-weight: bold; }

/* Adjustments For Cloze Edit In Review On Mobile */
.clozefield, .mobile .editcloze { display: none; }
.editcloze, .mobile .clozefield { display:  block; }

/* BEGIN HINT FIELDS */

/* Hint Link */
a[href="#"] {
 font-style: italic;
 padding: 0 !important;
text-decoration: underline; 
}

/* Text When Hint Is Shown*/
.hints { font-style: italic; }

/* Put Bottom Hints Lower */
/* #firstaid { padding-top: 40px!important; }
#extra { padding-bottom: 40px!important; } */


.hints + #extra { margin-top: 1rem; } /*add spacing between hints and extra field*/
/* END HINT FIELDS  */

/* EXTRA FIELD */
#extra { font-style: italic; font-size: 1rem;}


/* Fix to make pop-up dictionary images the right size */
.qtip img {
   max-width: 95% !important;
   max-height: 95% !important;
}

/* Details for AnKing hyperlink image */
#pic { opacity: 0.0; font-size: 16px; font-color: #F2E48E; font-family:Comic Sans!important; font-style:bold;}
#pic:hover { opacity: 1; transition: opacity 0.2s ease; }
.mobile #pic { display: none; }

/* TAGS */
/* Container To Fix Tags At Bottom Of Screen */
#tags-container{
position: fixed;
bottom: .5px;
width: 100%;
line-height: .45rem;
margin-left: -15px;
}

/* Clickable Tags (need to download the add-on) */
kbd {
 display: inline-block;
 letter-spacing: .1px;
 font-weight: bold;
 font-size: 10px !important;
 text-shadow: none !important;
 padding: 0.05rem 0.1rem !important;
 margin: 1px -3px !important;
 border-radius: 4px;
 border-width: 1.5px !important;
 border-style: solid;
 background-color: transparent !important;
 box-shadow: none !important;
 opacity: 0.5;
 vertical-align: middle !important;
 line-height: auto!important;
 height: auto!important;
}

/* Tag Becomes More Visible On Hover */
kbd:hover { opacity: 1; transition: opacity 0.2s ease; }

/* Tag Colors */
kbd:nth-of-type(1n+0) { border-color: #F44336; color: #F44336!important; }
kbd:nth-of-type(2n+0) { border-color: #9C27B0; color: #9C27B0!important; }
kbd:nth-of-type(3n+0) { border-color: #3F51B5; color: #3F51B5!important; }
kbd:nth-of-type(4n+0) { border-color: #03A9F4; color: #03A9F4!important; }
kbd:nth-of-type(5n+0) { border-color: #009688; color: #009688!important; }
kbd:nth-of-type(6n+0) { border-color: #C0CA33; color: #C0CA33!important; }
kbd:nth-of-type(7n+0) { border-color: #FF9800; color: #FF9800!important;}
kbd:nth-of-type(8n+0) { border-color: #FF5722; color: #FF5722!important; }
kbd:nth-of-type(9n+0) { border-color: #9E9E9E; color: #9E9E9E!important; }
kbd:nth-of-type(10n+0) { border-color: #607D8B; color: #607D8B!important; }

/* Tag Mobile Adjustments */
.mobile kbd { opacity: .9; margin: 1px !important; display: inline-block; font-size: 10px !important; }
.mobile #tags-container {line-height:0.6rem; margin-left: 0px; }

/* MNEMONICS CENTER OR LEFT */
.mnemonics { display: inline-block; } 
.centerbox {text-align:center;}

/*AMBOSS UNDERLINE
.amboss-mark { border-bottom: 2px solid rgba(72,74,74,0.2) !important; padding-bottom: .2px; text-decoration: none !important; }

.amboss-mark:hover { border-bottom: rgba(72,74,74,.8) !important; background-color: grey; }*/

/*~~~BUTTON LAYOUT ~~~*/

.button-ln {
  outline: 0;
  background-color: #424242; 
  border-radius: 0.12em; 
  border: 1px solid #525253 !important;
  color: #AFAFAF !important;
  padding: 5px 5px;
  text-align: center;
  display: inline-block;
  font-size: 9.5px;
  %box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
.button-ln:hover {
  background-color: #E9E9E9 !important;
  color: #363638 !important;
  cursor: default;
  }


.button-mq {
  outline: 0;
  background-color: #424242; 
  border-radius: 0.12em; 
  border: 1px solid #525253 !important;
  color: #c26165 !important;
  padding: 5px 5px;
  text-align: center;
  display: inline-block;
  font-size: 9.5px;
  %box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
.button-mq:hover {
  background-color: #FA8072 !important;
  color: #363638 !important;
  cursor: default;
  }


.button-pat {
  outline: 0;
  background-color: #424242; 
  border-radius: 0.12em; 
  border: 1px solid #525253 !important;
  color: #AFAFAF !important;
  padding: 5px 5px;
  text-align: center;
  display: inline-block;
  font-size: 9.5px;
  %box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
.button-pat:hover {
  background-color: #EABCE4 !important;
  color: #363638 !important;
  cursor: default;
  }


.button-bb {
  outline: 0;
  background-color: #424242; 
  border-radius: 0.12em; 
  border: 1px solid #525253 !important;
  color: #AFAFAF !important;
  padding: 5px 5px;
  text-align: center;
  display: inline-block;
  font-size: 9.5px;
  %box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
.button-bb:hover {
  background-color: #47C3F3 !important;
  color: #363638 !important;
  cursor: default;
  }


.button-fa {
  outline: 0;
  background-color: #424242; 
  border-radius: 0.12em; 
  border: 1px solid #525253 !important;
  color: #AFAFAF !important;
  padding: 5px 5px;
  text-align: center;
  display: inline-block;
  font-size: 9.5px;
  %box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
.button-fa:hover {
  background-color: #FFF1B8 !important;
  color: #363638 !important;
  cursor: default;
  }


.button-sketchy {
  outline: 0;
  background-color: #424242; 
  border-radius: 0.12em; 
  border: 1px solid #525253 !important;
  color: #AFAFAF !important;
  padding: 5px 5px;
  text-align: center;
  display: inline-block;
  font-size: 9.5px;
  %box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
.button-sketchy:hover {
  background-color: #7EDEC0 !important;
  color: #363638 !important;
  cursor: default;
  }


.button-pixorize {
  outline: 0;
  background-color: #424242; 
  border-radius: 0.12em; 
  border: 1px solid #525253 !important;
  color: #AFAFAF !important;
  padding: 5px 5px;
  text-align: center;
  display: inline-block;
  font-size: 9.5px;
  %box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
.button-pixorize:hover {
  background-color: #ea8eed !important;
  color: #363638 !important;
  cursor: default;
  }

.button-physeo {
  outline: 0;
  background-color: #424242; 
  border-radius: 0.12em; 
  border: 1px solid #525253 !important;
  color: #AFAFAF !important;
  padding: 5px 5px;
  text-align: center;
  display: inline-block;
  font-size: 9.5px;
  %box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
.button-physeo:hover {
  background-color: #A1C0C6 !important;
  color: #363638 !important;
  cursor: default;
  }


.button-ar {
  outline: 0;
  background-color: #424242; 
  border-radius: 0.12em; 
  border: 1px solid #525253 !important;
  color: #AFAFAF !important;
  padding: 5px 5px;
  text-align: center;
  display: inline-block;
  font-size: 9.5px;
  %box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
.button-ar:hover {
  background-color: #E9E9E9 !important;
  color: #363638 !important;
  cursor: default;
  }


.mobile .button-ln,  .mobile .button-mq,  .mobile .button-pat,  .mobile .button-bb,  .mobile .button-fa,  .mobile .button-sketchy,  .mobile .button-pixorize,  .mobile .button-physeo,  .mobile .button-ar { font-size: 28px; padding: 9px 7px; }
/*Start of style added by resize image add-on. Don't edit directly or the edition will be lost. Edit via the add-on configuration */
.mobile .card img {height:unset  !important; width:unset  !important;}
/*End of style added by resize image add-on*/
"""