function login(){
    user_email=document.getElementById('email').value
    user_password=document.getElementById('password').value
    window.alert(user_email+" "+user_password)
}
  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyAsyoSoEWizlaMig1JOnldJTejCdVK1B-c",
    authDomain: "login-991f1.firebaseapp.com",
    databaseURL: "https://login-991f1.firebaseio.com",
    projectId: "login-991f1",
    storageBucket: "login-991f1.appspot.com",
    messagingSenderId: "437852254376",
    appId: "1:437852254376:web:13d0fcbad908e2e883129d",
    measurementId: "G-828G7SM6L2"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();