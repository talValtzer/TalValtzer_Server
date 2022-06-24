const activePage = window.location.pathname;
console.log(window);
console.log(window.location);
console.log(activePage);

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/ 
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});


const loadDiv = document.getElementById("loading");

const Jordan=document.getElementById("Jordan");
const Alps=document.getElementById("Alps");
const NZ=document.getElementById("NewZealand");
const Israel=document.getElementById("Israel");
const InfoDiv = document.getElementById("Info");
Jordan.addEventListener("mouseover", openTextJ);
Jordan.addEventListener("mouseout", CloseTextJ);

Alps.addEventListener("mouseover", openTextA);
Alps.addEventListener("mouseout", CloseTextA);

NZ.addEventListener("mouseover", openTextN);
NZ.addEventListener("mouseout", CloseTextN);
Israel.addEventListener("mouseover", openTextI);
Israel.addEventListener("mouseout", CloseTextI);

function openTextJ(){
  InfoDiv.style.borderColor="rgba(181, 152, 103, 0.2)";
  InfoDiv.style.background="rgba(181, 152, 103, 0.477)";
  InfoDiv.style.visibility="visible";

}
function CloseTextJ(){

  InfoDiv.style.visibility="hidden";
}


function openTextA(){
  InfoDiv.style.borderColor="rgba(165, 196, 202, 0.9)";
  InfoDiv.style.background="rgba(165, 196, 202, 0.2)";
  InfoDiv.style.visibility="visible";

}
function CloseTextA(){

  InfoDiv.style.visibility="hidden";
}

function openTextN(){
  InfoDiv.style.borderColor="rgba(125, 157, 137, 0.9)";
  InfoDiv.style.background="rgba(125, 157, 137, 0.2)";
  InfoDiv.style.visibility="visible";

}
function CloseTextN(){

  InfoDiv.style.visibility="hidden";
}
function openTextI(){
  InfoDiv.style.borderColor="rgba(194, 146, 184, 0.9)";
  InfoDiv.style.background="rgba(194, 146, 184, 0.2)";
  InfoDiv.style.visibility="visible";

}
function CloseTextI(){

  InfoDiv.style.visibility="hidden";
}


function btn1Click(){
 
  loadDiv.style.display = "block";
  setTimeout(function(){loadDiv.style.display = "none"; } ,5000);
   setTimeout(myFunction,5000);
   
}


function myFunction() {
  var x = document.getElementById("snackbar");
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);

}