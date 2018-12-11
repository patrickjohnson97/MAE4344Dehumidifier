'use strict';

// =================================================================================
// App Configuration
// =================================================================================

const {App} = require('jovo-framework');


var admin = require("firebase-admin");
var modeRef;
var serviceAccount = require("./firebase-admin.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://mae4344-5859b.firebaseio.com"
  });

var database = admin.firestore();
const config = {
    logging: true,
};

const app = new App(config);


// =================================================================================
// App Logic
// =================================================================================

app.setHandler({
    'LAUNCH': function() {
        this.toIntent('hotWaterIntent');
    },

    'hotWaterIntent': function() {

        this.tell('Engaging hot water mode');

        modeRef = database.collection('modes').doc('mode');

        modeRef.set({
            value: 2
        }, {merge: true}).then(function() {
    console.log("Document successfully written!");
    });
    },
});

module.exports.app = app;
