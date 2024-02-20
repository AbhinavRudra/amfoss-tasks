// popup.js
const apiKey = "659c6005f3e1c8f8e9b21966cd95dd79";
const searchButton = document.getElementById('searchButton');
searchButton.addEventListener('click', getWeatherDetails);

//function capitalizeFirstLetter(string) {
    //   return string.charAt(0).toUpperCase() + string.slice(1);
    //}
    
    
// Add this function to capitalize the first letter of the each word
function capitalizeFirstLetter(string) {
    return string
      .split(" ")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(" ");
  }

async function getWeatherDetails() {
    const cityname = document.getElementById("cityInput").value;
    const tempElement = document.getElementById("temp");
    const cityElement = document.getElementById("cityName");
    const descElement = document.getElementById("description");
    const imgElement = document.getElementById("weatherImage");
  
    if (!cityname) {
      if (cityElement) {
        cityElement.innerHTML = "City not found! Try again";
      }
  
      if (tempElement) {
        tempElement.innerHTML = "Unavailable!";
      }
  
      if (descElement) {
        descElement.innerHTML = "Unavailable!";
      }
      return;
    }
  
    try {
      const stateResponse = await fetch(
        `https://api.openweathermap.org/geo/1.0/direct?q=${cityname}&appid=${apiKey}`
      );
      const stateData = await stateResponse.json();
  
      if (stateData.length === 0) {
        if (cityElement) {
          cityElement.innerHTML = "City not found! Try again";
        }
  
        if (tempElement) {
          tempElement.innerHTML = "Unavailable!";
        }
  
        if (descElement) {
          descElement.innerHTML = "Unavailable!";
        }
        return;
      }
  
      const lat = stateData[0].lat;
      const lon = stateData[0].lon;
  
      const weatherResponse = await fetch(
        `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${apiKey}`
      );
      const weatherData = await weatherResponse.json();
  
      if (cityElement) {
        cityElement.innerHTML = capitalizeFirstLetter(cityname);
      }
  
      if (descElement) {
        descElement.innerHTML = capitalizeFirstLetter(
            weatherData.weather[0].description
          );
      }
  
      if (tempElement) {
        tempElement.innerHTML = `${weatherData.main.temp} °C`;
      }
  
      if (imgElement) {
        // Extract the icon property from the weather array
        const icon = weatherData.weather[0].icon;
  
        // Construct the URL for the image
        const imageUrl = `https://openweathermap.org/img/wn/${icon}.png`;
  
        // Set the src attribute of the img element to the image URL
        imgElement.src = imageUrl;
      }
  
    } catch (error) {
      console.log(error);
      if (cityElement) {
        cityElement.innerHTML = "City not found! Try again";
      }
  
      if (tempElement) {
        tempElement.innerHTML = "Unavailable!";
      }
  
      if (descElement) {
        descElement.innerHTML = "Unavailable!";
      }
    }
  }