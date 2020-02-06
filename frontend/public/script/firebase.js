import { firebase } from "@firebase/app";
import "@firebase/firestore";

//UPDATE WITH YOUR CONFIG

const firebaseApp = firebase.initializeApp({
  apiKey: "AIzaSyDMFDTw4rQ02n0SBq-N-rJbdpPD9CA-IDc",
  authDomain: "farmaciadaw.firebaseapp.com",
  databaseURL: "https://farmaciadaw.firebaseio.com",
  projectId: "farmaciadaw",
  storageBucket: "farmaciadaw.appspot.com",
  messagingSenderId: "462836711908",
  appId: "1:462836711908:web:467a9bd41b788e63f087f1",
  measurementId: "G-LNL6JCN92T"
});

export const db = firebaseApp.firestore();