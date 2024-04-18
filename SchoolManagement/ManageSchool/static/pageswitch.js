// Function to switch to Page 1
const switchToPage1 = () => {
  // Replace the URL below with the actual URL of Page 1
  const page1Url = "/studentlogin/";
  window.location.href = page1Url;
};

// Function to switch to Page 2
const switchToPage2 = () => {
  // Replace the URL below with the actual URL of Page 2
  const page2Url = "/stafflogin/";
  window.location.href = page2Url;
};

// Function to switch to Page 3
const switchToPage3 = () => {
  // Replace the URL below with the actual URL of Page 3
  const page3Url = "schoollogin";
  window.location.href = page3Url;
};

// Attach these functions to your buttons
const button1 = document.getElementById("parent");
button1.addEventListener("click", switchToPage1);

const button2 = document.getElementById("staff");
button2.addEventListener("click", switchToPage2);

const button3 = document.getElementById("admin");
button3.addEventListener("click", switchToPage3);