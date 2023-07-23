document.addEventListener("DOMContentLoaded", function(event) { 

  // --------------------------ON REFRESH DELETE HASH IF EXISTS AND RELOAD--------------------------
  if (performance.getEntriesByType('navigation')[0].type != 'navigate') {
    if(window.location.hash){
      history.pushState("", document.title, window.location.pathname);
      window.location = history.state;
      sessionStorage.setItem('pageHasBeenLoaded', 'true');
    }
  }

    if (window.location.pathname=='/') {
  
      // --------------------------ADD EVENT LISTENER FOR BOTTOM TO TOP BUTTON ON INDEX PAGE--------------------------
      //Get the button
      let mybutton = document.getElementById("btn-back-to-top");
      // When the user clicks on the button, scroll to the top of the document
      mybutton.addEventListener("click", backToTop);
      function backToTop() {
        history.pushState("", document.title, window.location.pathname);
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
      }
  
    }

    // Manage the display of favorite forms to ensure users can only add meals to their 'favorites' once //

    if (window.location.pathname.includes('/menu/')) {
      const mealIdList = document.getElementsByClassName('mealId')
      const mealList = document.getElementsByClassName('meal')
  
      //add value of meal id to favourite form field
      for(input of mealIdList){
        input.value = input.previousElementSibling.value
      }
  
      //display favourite forms depending on p hidden element value that is generated only if favourite exists for user and specific meal
      for(meal of mealList){
        console.log(meal)
        const favouriteExists = meal.getElementsByClassName('favourite-exists')[0]
        const addFavouriteForm = meal.getElementsByClassName('add-favourite-form')[0]
        const removeFavouriteForm = meal.getElementsByClassName('remove-favourite-form')[0]
  
        if(favouriteExists){
          addFavouriteForm.style.display = 'none'
        }
  
      }
  
  
    }